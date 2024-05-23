#!/bin/bash

# Prompt for inputs
read -p "Enter the unit: " UNIT
read -p "Enter the version (e.g., 2.1 or 3.0): " VERSION
read -p "Enter the base URL: " BASE_URL
read -p "Enter the starting identifier: " START_ID
read -p "Enter the desired number of valid manifests: " DESIRED_COUNT

SERVER_URL="http://localhost:8080/validate"
OUTPUT_JSONL="lux-iiif-results.jsonl"

# Ensure the output file is empty before writing new results
> "$OUTPUT_JSONL"

# Initialize counter for progress tracking and valid manifests
counter=0
valid_count=0
current_id=$START_ID

# Function to log messages with timestamps
log_message() {
    echo "[$(date)] $1"
}

while [ $valid_count -lt $DESIRED_COUNT ]; do
    url="${BASE_URL}${current_id}"
    log_message "Processing Unit: $UNIT, Version: $VERSION, URL: $url"

    # Validate the URL
    response=$(curl -s -o /dev/null -w "%{http_code}" "${SERVER_URL}?version=${VERSION}&url=${url}")

    if [ "$response" -eq 404 ]; then
        log_message "URL $url returned 404, skipping."
        current_id=$((current_id + 1))
        continue
    fi

    response=$(curl -s "${SERVER_URL}?version=${VERSION}&url=${url}")

    if [ -z "$response" ]; then
        response=$(jq -n --arg url "$url" --arg version "$VERSION" --arg unit "$UNIT" '{"okay": 0, "warnings": ["Failed to fetch or invalid response"], "error": "Empty response", "errorList": [], "url": $url, "version": $version, "unit": $unit}')
    else
        response=$(echo "$response" | jq --arg version "$VERSION" --arg unit "$UNIT" '. + {version: $version, unit: $unit}' | jq -c .)
    fi

    log_message "Processed response for URL $url: $response"

    echo "$response" >> "$OUTPUT_JSONL"

    log_message "Written response for URL $url to $OUTPUT_JSONL"

    valid_count=$((valid_count + 1))

    # Calculate progress percentage
    counter=$((counter + 1))
    progress=$((counter * 100 / DESIRED_COUNT))
    log_message "Progress: $progress%"

    # Increment the current identifier
    current_id=$((current_id + 1))
done

log_message "Validation complete, results saved to $OUTPUT_JSONL"

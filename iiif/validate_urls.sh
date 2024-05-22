#!/bin/bash

CSV_FILE="lux-iiif.csv"
TEMP_CSV_FILE="temp_$CSV_FILE"
SERVER_URL="http://localhost:8080/validate"
OUTPUT_JSONL="lux-iiif-results.jsonl"

# Ensure the output file is empty before writing new results
> "$OUTPUT_JSONL"

# Add a newline character to the end of the CSV file to ensure the last line is processed
cp "$CSV_FILE" "$TEMP_CSV_FILE"
echo "" >> "$TEMP_CSV_FILE"

# Read the CSV file line by line, including the header
{
    read
    while IFS=, read -r unit version url
    do
        if [ -n "$unit" ] && [ -n "$version" ] && [ -n "$url" ]; then
            # Trim any trailing carriage return or newline characters from the URL
            url=$(echo "$url" | tr -d '\r\n')

            echo "Processing Unit: $unit, Version: $version, URL: $url"  # Debug statement

            # Validate the URL
            response=$(curl -s "${SERVER_URL}?version=${version}&url=${url}")

            # Debugging statement to show raw response
            echo "Raw response for URL $url: $response"

            # Check if response is empty
            if [ -z "$response" ]; then
                response=$(jq -n --arg url "$url" --arg version "$version" --arg unit "$unit" '{"okay": 0, "warnings": ["Failed to fetch or invalid response"], "error": "Empty response", "errorList": [], "url": $url, "version": $version, "unit": $unit}')
            else
                # Remove all newlines and extra spaces from the JSON response to make it a single line
                response=$(echo "$response" | jq --arg version "$version" --arg unit "$unit" '. + {version: $version, unit: $unit}' | jq -c .)
            fi

            # Debugging statement to show processed response
            echo "Processed response for URL $url: $response"

            # Write the response to the JSONL file (without pretty-printing)
            echo "$response" >> "$OUTPUT_JSONL"

            # Debugging statement to confirm write
            echo "Written response for URL $url to $OUTPUT_JSONL"
        fi
    done
} < "$TEMP_CSV_FILE"

# Remove the temporary CSV file
rm "$TEMP_CSV_FILE"

echo "Validation complete, results saved to $OUTPUT_JSONL"

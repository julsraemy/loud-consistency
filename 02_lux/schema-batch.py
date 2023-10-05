import os
import json
import argparse
import requests
import warnings
import csv
from referencing import Registry, Resource
from jsonschema import validate, Draft202012Validator
from jsonschema.exceptions import ValidationError
from jsonschema._utils import find_additional_properties

def load_json_from_file(file_path):
    with open(file_path) as file:
        return json.load(file)

def merge_schemas(*schemas):
    merged_schema = {}
    for schema in schemas:
        merged_schema.update(schema)
    return merged_schema

def validate_json(json_data, schema):
    return list(Draft202012Validator(schema).iter_errors(json_data))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Validate JSON data against a schema.")
    parser.add_argument("-f", "--file", type=str, required=True, help="Path to the file containing URLs to validate")
    
    args = parser.parse_args()

    # Load the core schema and resolve references
    schema_dir = "schema"

    # Read URLs from the file
    with open(args.file, 'r') as file:
        urls = file.readlines()

    # Initialize a dictionary to store validation results
    validation_results = []

    # Dictionary to store schema validation counts
    schema_validation_counts = {}

    # Process each URL
    for url in urls:
        url = url.strip()
        schema_name = url.split('/')[-2]  # Extract schema name from URL

        # Load the specified schema
        schema_file_path = os.path.join(schema_dir, f"{schema_name}.json")
        specified_schema_contents = load_json_from_file(schema_file_path)

        # Merge the core and specified schemas
        merged_schema = merge_schemas(specified_schema_contents)

        # Load the instance data
        instance = url
        resp = requests.get(instance)
        data = resp.json()

        # Validate the instance against the schema
        with warnings.catch_warnings():
            warnings.filterwarnings("ignore", category=DeprecationWarning)
            errs = validate_json(data, merged_schema)

        # Collect validation results
        validation_result = {
            "url": url,
            "schema": schema_name,
            "validation_errors": [] if not errs else [str(err) for err in errs]
        }
        validation_results.append(validation_result)

        # Update schema validation counts
        schema_validation_counts[schema_name] = schema_validation_counts.get(schema_name, 0) + 1 if not errs else schema_validation_counts.get(schema_name, 0)

    # Write validation results to a JSONL file
    with open("validation_results.jsonl", "w") as jsonl_file:
        for result in validation_results:
            jsonl_file.write(json.dumps(result) + '\n')

    # Write schema validation counts to a CSV file
    with open("validation_summary.csv", "w", newline='') as csvfile:
        fieldnames = ['schema', 'validated', 'non_validated']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for schema_name, count in schema_validation_counts.items():
            writer.writerow({'schema': schema_name, 'validated': count, 'non_validated': len(urls) - count})

    print("Validation completed. Results saved to validation_results.jsonl and validation_summary.csv.")

import os
import json
import argparse
import requests
import warnings
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
    parser.add_argument("-i", "--instance", type=str, required=True, help="Instance URL for validation")
    parser.add_argument("-s", "--schema", type=str, required=True, choices=["core", "concept", "digital", "event", "group", "image", "object", "place", "person", "provenance", "set", "text"], help="Schema to validate against")
    
    args = parser.parse_args()

    # Load the core schema and resolve references
    schema_dir = "schema"
    core_schema_contents = load_json_from_file(os.path.join(schema_dir, "core.json"))
    core_schema = Resource.from_contents(core_schema_contents)
    core_registry = Registry().with_resources([
        ("https://linked.art/api/1.0/schema/core.json", core_schema),
        ("core.json", core_schema)
    ])

    schema_file_mapping = {
        "core": "core.json",
        "concept": "concept.json",
        "digital": "digital.json",
        "event": "event.json",
        "group": "group.json",
        "image": "image.json",
        "object": "object.json",
        "place": "place.json",
        "person": "person.json",
        "provenance": "provenance.json",
        "set": "set.json",
        "text": "text.json"
    }

    if args.schema not in schema_file_mapping:
        print("Invalid schema specified.")
        exit(1)

    specified_schema_contents = load_json_from_file(os.path.join(schema_dir, schema_file_mapping[args.schema]))
    specified_schema = Resource.from_contents(specified_schema_contents)

    # Merge the core and specified schemas
    merged_schema = merge_schemas(core_schema_contents, specified_schema_contents)

    # Load the instance data
    instance = args.instance
    resp = requests.get(instance)
    data = resp.json()

    print("-"*120)
    print("Processing: %s" % instance)
    
    with warnings.catch_warnings():
        warnings.filterwarnings("ignore", category=DeprecationWarning)
        errs = validate_json(data, merged_schema)

    for error in errs:
        if error.validator == 'additionalProperties':
            aps = []
            for ap in find_additional_properties(error.instance, error.schema):
                if ap[0] != '_':
                    aps.append(ap)
            if not aps:
                continue
        print(f"  /{'/'.join([str(x) for x in error.absolute_path])} --> {error.message}")

    if not errs:
        print("  Validated!")

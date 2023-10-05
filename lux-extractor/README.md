# LUX JSONL Data Extractor

This script processes a JSONL file and creates output files based on the specified parameters. It can extract a specified number of lines, a specified line range, or all lines from a JSONL file and save the main `id`, i.e. the LUX URI pointing to a given Linked Art object, in txt files (each 10,000 entries a new file is generated). Additionally, it can save entries as individual JSON(-LD) files.

## Usage

```bash
python3 lux_jsonl_extractor.py [options]
```

## Options

- `-i, --input_file <file_path>`: Path to the input JSONL file (required).
- `-r, --line_range <start-end>`: Range of lines to process (start-end) or a single line (e.g., `240-800` or `259`). Use `-r` to process from a specific line until the end of the file.
- `-n, --num_lines <num>`: Number of lines to process. Default is to process all available lines.
- `-j, --json_output`: Save entries as JSON files.

Please note that `-r` and `-n` can't be used together.

## Examples

1. To process the entire JSONL file and save entries as JSON files:

```bash
python3 lux_jsonl_extractor.py -i export_full_0.jsonl -j
```

2. To process from a specific line until the end and save entries as JSON files:

```bash
python3 lux_jsonl_extractor.py -i export_full_0.jsonl -r 259 -j
```

3. To process a range of lines and save entries as JSON files:

```bash
python3 lux_jsonl_extractor.py -i export_full_0.jsonl -r 240-800 -j
```

4. To process a range of lines without saving as JSON files:

```bash
python3 lux_jsonl_extractor.py -i export_full_0.jsonl -r 240-800
```

5. To process a specific number of lines and save entries as JSON files:

```bash
python3 lux_jsonl_extractor.py -i export_full_0.jsonl -n 100 -j
```

6. To process a specific number of lines:

```bash
python3 lux_jsonl_extractor.py -i export_full_0.jsonl -n 100
```

## Content

One LUX JSONL represents one 24th of the whole LUX dataset. The JSON files are also not exactly the same as what is available online through the API and are much more verbose. 

Compare `https://lux.collections.yale.edu/data/text/0000075c-f59a-419e-8d92-cb41565b5a18` with: 

```json
{
    "json": {
        "id": "https://lux.collections.yale.edu/data/person/0000113d-3239-4cc7-a277-f4e701cb3255",
        "type": "Person",
        "_label": "Lovy, Alex",
        "@context": "https://linked.art/ns/v1/linked-art.json",
        "equivalent": [
            {
                "id": "https://linked-art.library.yale.edu/node/dff3c65b-9162-408d-9aac-7f4456a7d586",
                "type": "Person",
                "_label": "Lovy, Alex"
            }
        ],
        "identified_by": [
            {
                "type": "Name",
                "content": "Lovy, Alex",
                "classified_as": [
                    {
                        "id": "https://lux.collections.yale.edu/data/concept/f7ef5bb4-e7fb-443d-9c6b-371a23e717ec",
                        "type": "Type",
                        "_label": "Primary Name"
                    },
                    {
                        "id": "https://lux.collections.yale.edu/data/concept/31497b4e-24ad-47fe-88ad-af2007d7fb5a",
                        "type": "Type",
                        "_label": "Sort Name"
                    }
                ]
            }
        ]
    },
    "triples": [
        {
            "triple": {
                "subject": "https://lux.collections.yale.edu/data/person/0000113d-3239-4cc7-a277-f4e701cb3255",
                "predicate": "http://www.w3.org/1999/02/22-rdf-syntax-ns#type",
                "object": "http://www.cidoc-crm.org/cidoc-crm/E21_Person"
            }
        },
        {
            "triple": {
                "subject": "https://lux.collections.yale.edu/data/person/0000113d-3239-4cc7-a277-f4e701cb3255",
                "predicate": "http://www.w3.org/1999/02/22-rdf-syntax-ns#type",
                "object": "https://lux.collections.yale.edu/ns/Agent"
            }
        },
        {
            "triple": {
                "subject": "https://lux.collections.yale.edu/data/person/0000113d-3239-4cc7-a277-f4e701cb3255",
                "predicate": "https://linked.art/ns/terms/equivalent",
                "object": "https://linked-art.library.yale.edu/node/dff3c65b-9162-408d-9aac-7f4456a7d586"
            }
        }
    ],
    "admin": {
        "conversion-date": "2023-04-27T20:58:58.421062"
    },
    "indexedProperties": {
        "dataType": "Person",
        "uiType": "Agent",
        "isCollectionItem": 0,
        "nationalityId": [],
        "occupationId": [],
        "agentActivePlaceId": [],
        "personId": "https://lux.collections.yale.edu/data/person/0000113d-3239-4cc7-a277-f4e701cb3255",
        "genderId": [],
        "hasDigitalImage": 0,
        "isOnline": 0
    }
}

```






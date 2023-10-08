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

One LUX JSONL represents one 24th of the whole LUX dataset. The JSON files extracted from JSONL are much more verbose and are also not exactly the same as what is available online, where `_links` from the [Hypertext Application Language (HAL)](https://datatracker.ietf.org/doc/draft-kelly-json-hal/10/) are being leveraged.

Compare the last few lines of  `https://lux.collections.yale.edu/data/concept/000025c1-9521-440a-b637-516598cd856c` with: 

```json
{
    "json": {
        "id": "https://lux.collections.yale.edu/data/concept/000025c1-9521-440a-b637-516598cd856c",
        "type": "Type",
        "_label": "Ichthyosauridae",
        "broader": [
            {
                "id": "https://lux.collections.yale.edu/data/concept/de045f98-864b-4814-8baa-10fab96cf58a",
                "type": "Type"
            }
        ],
        "@context": "https://linked.art/ns/v1/linked-art.json",
        "equivalent": [
            {
                "id": "http://id.loc.gov/authorities/subjects/sh85064057",
                "type": "Type",
                "_label": "Ichthyosauridae"
            }
        ],
        "identified_by": [
            {
                "type": "Name",
                "content": "Ichthyosauridae",
                "language": [
                    {
                        "id": "https://lux.collections.yale.edu/data/concept/1fda962d-1edc-4fd7-bfa9-0c10e3153449",
                        "type": "Language",
                        "_label": "English"
                    }
                ],
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
                "subject": "https://lux.collections.yale.edu/data/concept/000025c1-9521-440a-b637-516598cd856c",
                "predicate": "http://www.w3.org/1999/02/22-rdf-syntax-ns#type",
                "object": "http://www.cidoc-crm.org/cidoc-crm/E55_Type"
            }
        },
        {
            "triple": {
                "subject": "https://lux.collections.yale.edu/data/concept/000025c1-9521-440a-b637-516598cd856c",
                "predicate": "http://www.w3.org/1999/02/22-rdf-syntax-ns#type",
                "object": "https://lux.collections.yale.edu/ns/Concept"
            }
        },
        {
            "triple": {
                "subject": "https://lux.collections.yale.edu/data/concept/000025c1-9521-440a-b637-516598cd856c",
                "predicate": "https://linked.art/ns/terms/equivalent",
                "object": "http://id.loc.gov/authorities/subjects/sh85064057"
            }
        },
        {
            "triple": {
                "subject": "https://lux.collections.yale.edu/data/concept/000025c1-9521-440a-b637-516598cd856c",
                "predicate": "http://www.w3.org/2004/02/skos/core#broader",
                "object": "https://lux.collections.yale.edu/data/concept/de045f98-864b-4814-8baa-10fab96cf58a"
            }
        }
    ],
    "admin": {
        "conversion-date": "2023-04-27T20:58:58.421062"
    },
    "indexedProperties": {
        "dataType": "Type",
        "uiType": "Concept",
        "isCollectionItem": 0,
        "hasDigitalImage": 0,
        "isOnline": 0
    }
}
```






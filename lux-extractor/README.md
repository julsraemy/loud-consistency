# LUX JSONL Data Extractor

This script processes a JSONL file and creates output files based on the specified parameters. It can extract a specified number of lines, a specified line range, or all lines from a JSONL file and save the main `id`, i.e. the LUX URI pointing to a given Linked Art object, in txt files (each 10,000 entries a new file is generated). Additionally, it can save entries as individual JSON files.

## Usage

```bash
python3 lux_jsonl_extractor.py [options]
```

## Options

`-i, --input_file <file_path>`: Path to the input JSONL file (required).
`-r, --line_range <start-end>`: Range of lines to process (start-end) or a single line (e.g., `240-800` or `259`). Use `-r start-` to process from a specific line until the end of the file.
`-n, --num_lines <num>`: Number of lines to process. Default is to process all available lines.
`-j, --json_output`: Save entries as JSON files.

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








import json
import os
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description='Process JSONL file and create output.')
    parser.add_argument('-i', '--input_file', type=str, required=True, help='Path to the input JSONL file.')
    parser.add_argument('-r', '--line_range', type=str, help='Range of lines to process (start-end). Example: 240-800')
    parser.add_argument('-n', '--num_lines', type=int, default=-1, help='Number of lines to process. Default is all.')
    parser.add_argument('-j', '--json_output', action='store_true', help='Save entries as JSON files.')
    return parser.parse_args()

def process_entries(input_file_path, line_range, num_lines_to_read, save_json=False):
    output_directory = os.path.join(os.getcwd(), 'data')
    os.makedirs(output_directory, exist_ok=True)
    main_ids = []
    current_lines = 0
    file_index = 0

    with open(input_file_path, 'r', encoding='utf-8') as input_file:
        for idx, line in enumerate(input_file):
            if num_lines_to_read != -1 and current_lines >= num_lines_to_read:
                break

            if line_range:
                start_line, end_line = map(int, line_range.split('-'))
                start_line += 1  # Adjusting for 1-based indexing
                if idx + 1 < start_line:
                    continue
                if idx + 1 > end_line:
                    break

            data = json.loads(line)
            main_id = data['json']['id']
            data['json']['id'] = main_id  # Set the first ID as the main ID

            # Get the content of the first ID to use as the file name
            first_id_content = main_id.split('/')[-1]

            # Always save the main IDs
            main_ids.append(main_id)
            current_lines += 1

            if current_lines % 100000 == 0:
                # Write current main IDs to the text file. One file per 100,000 entries
                start_idx = idx - current_lines + 1 if line_range else idx - current_lines + 2
                end_idx = idx if line_range else idx + 1

                output_file_extension = 'txt'
                lux_ids_file_path = os.path.join(output_directory, f'lux_ids_{start_idx}-{end_idx}.{output_file_extension}')
                with open(lux_ids_file_path, 'w', encoding='utf-8') as lux_ids_output_file:
                    for main_id in main_ids:
                        # Write the content of the first ID as the file name
                        first_id_content = main_id.split('/')[-1]
                        lux_ids_output_file.write(f'{first_id_content}\n')

                # Reset counters and open a new text file
                main_ids = []

            # Create the JSON file for the entry if saving JSON
            if save_json:
                json_output_directory = os.path.join(os.getcwd(), 'data', 'json')
                os.makedirs(json_output_directory, exist_ok=True)
                output_file_path = os.path.join(json_output_directory, f'{first_id_content}.json')
                with open(output_file_path, 'w', encoding='utf-8') as output_file:
                    json.dump(data, output_file, indent=4)

    # Write remaining main IDs to the text file
    if main_ids:
        start_idx = idx - current_lines + 1 if line_range else idx - current_lines + 2
        end_idx = idx if line_range else idx + 1

        output_file_extension = 'txt'
        lux_ids_file_path = os.path.join(output_directory, f'lux_ids_{start_idx}-{end_idx}.{output_file_extension}')
        with open(lux_ids_file_path, 'w', encoding='utf-8') as lux_ids_output_file:
            for main_id in main_ids:
                # Write the content of the first ID as the file name
                first_id_content = main_id.split('/')[-1]
                lux_ids_output_file.write(f'{first_id_content}\n')

    print(f"Successfully processed {current_lines} lines.")

if __name__ == "__main__":
    args = parse_arguments()

    if args.line_range and args.num_lines != -1:
        print("Please use either -r or -n, but not both.")
        exit()

    if args.line_range:
        print(f"Processing specified line range: {args.line_range}")
    elif args.num_lines != -1:
        print(f"Processing {args.num_lines} lines from the start.")
    else:
        print("Processing all available lines.")

    # By default, save only as .txt
    process_entries(args.input_file, args.line_range, args.num_lines, save_json=args.json_output)

import json
import pandas as pd
import matplotlib.pyplot as plt

# Path to the JSONL file
jsonl_file_path = 'lux-iiif-results.jsonl'

# Load data from the JSONL file
data = []
with open(jsonl_file_path, 'r') as file:
    for line in file:
        data.append(json.loads(line))

# Convert data to a pandas DataFrame
df = pd.DataFrame(data)

# Ensure that all entries in the 'warnings' column are lists
df['warnings'] = df['warnings'].apply(lambda x: x if isinstance(x, list) else [])

# Identify 404 responses
df['status'] = df.apply(lambda row: 'HTTP 404' if '404' in row['error'] else ('Valid Manifest' if row['okay'] == 1 else 'Invalid Manifest'), axis=1)

# Determine warnings
df['warnings_status'] = df['warnings'].apply(lambda x: 'With Warnings' if len(x) > 0 else 'Without Warnings')

# Combine status and warnings for valid manifests
df['combined_status'] = df.apply(lambda row: row['status'] if row['status'] != 'Valid Manifest' else ('Valid Manifest (with warnings)' if row['warnings_status'] == 'With Warnings' else 'Valid Manifest'), axis=1)

# Group by unit and version
grouped = df.groupby(['unit', 'version', 'combined_status']).size().unstack(fill_value=0).reset_index()

# Create a new combined unit and version column for plotting
grouped['unit_version'] = grouped['unit'] + ' (' + grouped['version'] + ')'

# Define colors
colors = {
    'Valid Manifest': '#10700F',  # Dark green
    'Valid Manifest (with warnings)': '#71AF64',  # Light green
    'Invalid Manifest': '#FF261D',  # Red
    'HTTP 404': '#A9A9A9'  # Dark grey
}

# Plot the stacked bar chart
fig, ax = plt.subplots(figsize=(14, 8))

bottom = [0] * len(grouped)

for status in ['Valid Manifest', 'Valid Manifest (with warnings)', 'Invalid Manifest', 'HTTP 404']:
    if status in grouped.columns:
        values = grouped[status].values
    else:
        values = [0] * len(grouped)
    ax.bar(grouped['unit_version'], values, bottom=bottom, label=status, color=colors[status])
    bottom = [i + j for i, j in zip(bottom, values)]

ax.set_title('Validation Results by Unit and IIIF Presentation API Version')
ax.set_ylabel('Count')
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('iiif_analysis_results.png')
plt.show()

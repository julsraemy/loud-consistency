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

# Statistics
total_manifests = len(df)
valid_manifests = df[df['okay'] == 1]
invalid_manifests = df[df['okay'] == 0]
valid_with_warnings = valid_manifests[valid_manifests['warnings'].apply(lambda x: len(x) > 0)]
valid_without_warnings = valid_manifests[valid_manifests['warnings'].apply(lambda x: len(x) == 0)]

# Print statistics
print(f"Total manifests: {total_manifests}")
print(f"Valid manifests: {len(valid_manifests)}")
print(f"Invalid manifests: {len(invalid_manifests)}")
print(f"Valid manifests with warnings: {len(valid_with_warnings)}")
print(f"Valid manifests without warnings: {len(valid_without_warnings)}")

# Group by unit and version
grouped_by_unit = df.groupby('unit').size()
grouped_by_version = df.groupby('version').size()
grouped_by_unit_and_version = df.groupby(['unit', 'version']).size()

# Plot statistics
fig, axs = plt.subplots(2, 2, figsize=(14, 10))

# Total manifests by unit
axs[0, 0].bar(grouped_by_unit.index, grouped_by_unit.values, color='skyblue')
axs[0, 0].set_title('Total Manifests by Unit')
axs[0, 0].set_ylabel('Count')

# Total manifests by version
axs[0, 1].bar(grouped_by_version.index, grouped_by_version.values, color='lightgreen')
axs[0, 1].set_title('Total Manifests by Version')
axs[0, 1].set_ylabel('Count')

# Valid and invalid manifests
df['status'] = df['okay'].apply(lambda x: 'Valid' if x == 1 else 'Invalid')
grouped_by_status = df.groupby('status').size()
axs[1, 0].bar(grouped_by_status.index, grouped_by_status.values, color=['lightgreen', 'salmon'])
axs[1, 0].set_title('Valid vs Invalid Manifests')
axs[1, 0].set_ylabel('Count')

# Valid manifests with and without warnings
valid_with_without_warnings = pd.Series([len(valid_with_warnings), len(valid_without_warnings)],
                                        index=['With Warnings', 'Without Warnings'])
axs[1, 1].bar(valid_with_without_warnings.index, valid_with_without_warnings.values, color=['orange', 'lightblue'])
axs[1, 1].set_title('Valid Manifests with/without Warnings')
axs[1, 1].set_ylabel('Count')

plt.tight_layout()
plt.savefig('iiif_analysis_results.png')
plt.show()
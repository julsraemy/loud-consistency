import pandas as pd
import matplotlib.pyplot as plt
from matplotlib_venn import venn2
import matplotlib.patches as mpatches

# Load the CSV file
file_path = 'vocabs-lux-alignment-trimmed.csv'

try:
    df = pd.read_csv(file_path)
except FileNotFoundError:
    print(f"File {file_path} not found. Please check the file path.")
    exit()

# Count the number of vocab terms present in the YCBA
ycba_count = df['ycba'].notna().sum()

# Count the number of vocab terms present in the YUAG
yuag_count = df['yuag'].notna().sum()

# Count the number of cross-unit concept terms (present in both YCBA and YUAG)
cross_unit_count = df[df['ycba'].notna() & df['yuag'].notna()].shape[0]

# Calculate the number of unique terms in YCBA and YUAG
ycba_unique = ycba_count - cross_unit_count
yuag_unique = yuag_count - cross_unit_count

# Create a Venn diagram with the updated title
plt.figure(figsize=(10, 6))
venn = venn2(subsets=(ycba_unique, yuag_unique, cross_unit_count), set_labels=('YCBA', 'YUAG'))

# Show the Venn diagram
plt.show()

import pandas as pd
import os

# File paths
csv_file = "data.csv"
excel_file = "output.xlsx"

# ✅ Step 1: Create a sample CSV if it doesn't exist
if not os.path.exists(csv_file):
    sample_data = pd.DataFrame({
        "Name": ["Purnima", "Raj", "Meena"],
        "Age": [22, 25, 28],
        "City": ["Hyderabad", "Delhi", "Mumbai"]
    })
    sample_data.to_csv(csv_file, index=False)
    print(f"Sample {csv_file} created!")

# ✅ Step 2: Read data from CSV
csv_data = pd.read_csv(csv_file)
print("\nData read from CSV:")
print(csv_data)

# ✅ Step 3: Write data to Excel
csv_data.to_excel(excel_file, index=False)
print(f"\nData written to {excel_file}")

# ✅ Step 4: Read back from Excel
read_back = pd.read_excel(excel_file)
print("\nData read back from Excel:")
print(read_back)

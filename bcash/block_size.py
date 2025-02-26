import pandas as pd

# Load block and transaction data
block_data = pd.read_csv("/local/scratch/master_project_utxo_2025/data/bcash/bch_block_data.csv")


print(f"Max Block Size (bytes): {block_data['Size (bytes)'].max()}")
print(f"Min Block Size (bytes): {block_data['Size (bytes)'].min()}")

print(f"Block Size: {block_data['Size (bytes)'].mean()}")
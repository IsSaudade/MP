import pandas as pd

# Load block and transaction data
block_data = pd.read_csv("/local/scratch/master_project_utxo_2025/data/bcash/bch_block_data.csv")
transaction_data = pd.read_csv("/local/scratch/master_project_utxo_2025/data/bcash/bch_transactions.csv")

# Strip any extra whitespace from column names
block_data.columns = block_data.columns.str.strip()
transaction_data.columns = transaction_data.columns.str.strip()

# Group transactions by block and calculate transactions per block
transactions_per_block = transaction_data.groupby('Block Height')['Tx ID'].count().reset_index()

# Merge with block data to analyze the relationship
block_data = block_data.merge(transactions_per_block, left_on='Height', right_on='Block Height')

# Ensure block data is sorted by timestamp
block_data['block_time'] = pd.to_datetime(block_data['Timestamp'])
block_data = block_data.sort_values(by='block_time')  # Sort by block_time

# Calculate block duration (time between consecutive blocks)
block_data['block_duration'] = block_data['block_time'].shift(-1) - block_data['block_time']


# Handle cases where block_duration might be NaT (Not a Time) by filling with zero or dropping
block_data['block_duration'] = block_data['block_duration'].fillna(pd.Timedelta(seconds=1))  # Use 1 second as fallback

# Debugging: Check for zero or negative block durations and handle them
block_data['block_duration'] = block_data['block_duration'].apply(lambda x: max(x, pd.Timedelta(seconds=1)))  # Set minimum duration to 1 second

# Calculate transactions per second (TPS)
block_data['transactions_per_second'] = block_data['Tx ID'] / block_data['block_duration'].dt.total_seconds()

# Show results
print(f"Average Transactions per Block: {block_data['Tx ID'].mean()}")
print(f"Average Transactions per Second: {block_data['transactions_per_second'].mean()}")

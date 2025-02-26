import pandas as pd

# Load data
mining_rewards = pd.read_csv("/local/scratch/master_project_utxo_2025/data/bcash/bch_mining_rewards.csv")
block_data = pd.read_csv("/local/scratch/master_project_utxo_2025/data/bcash/bch_block_data.csv")

# Strip any extra whitespace from column names
mining_rewards.columns = mining_rewards.columns.str.strip()
block_data.columns = block_data.columns.str.strip()

# Group rewards by block height to get mining rewards per block
mining_rewards_per_block = mining_rewards.groupby('Block Height')['Reward'].sum().reset_index()

# Merge block data with mining rewards data on Block Height
merged_data = pd.merge(block_data, mining_rewards_per_block, left_on='Height', right_on='Block Height')

# Calculate the Gini index for the merged mining rewards data (optional if needed)
def gini_index(data):
    sorted_data = sorted(data)
    n = len(data)
    cumulative_sum = 0
    total_sum = sum(data)
    for i, value in enumerate(sorted_data):
        cumulative_sum += value
    total_sum = sum([((i + 1) * value) for i, value in enumerate(sorted_data)])
    return (total_sum - cumulative_sum) / (n * total_sum)

gini_value = gini_index(merged_data['Reward'])

# Now calculate the correlation between block size and Gini index
correlation = merged_data['Size (bytes)'].corr(merged_data['Reward'])
print(f"Correlation between Block Size and Mining Reward: {correlation:.4f}")

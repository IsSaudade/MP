import pandas as pd
import numpy as np

# Load mining rewards data
mining_rewards = pd.read_csv("/local/scratch/master_project_utxo_2025/data/bcash/bch_mining_rewards.csv")
miner_rewards = mining_rewards.groupby('Miner Address')['Reward'].sum().reset_index()

# Calculate Gini index
def gini_index(data):
    # Sort the data in ascending order
    sorted_data = np.sort(data)
    n = len(data)
    cumulative_sum = np.cumsum(sorted_data)
    total_sum = cumulative_sum[-1]  # Total sum of the rewards
    gini_value = (n + 1 - 2 * np.sum(cumulative_sum) / total_sum) / n
    return gini_value

# Calculate and print Gini index
gini_value = gini_index(miner_rewards['Reward'])
print(f"Gini Index for Mining Rewards: {gini_value:.4f}")
print(miner_rewards['Reward'].describe())
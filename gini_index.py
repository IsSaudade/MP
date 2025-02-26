import pandas as pd
import numpy as np


df = pd.read_csv("/local/scratch/master_project_utxo_2025/data/bcash/bch_address_analysis.csv")



# Sort the balances in ascending order
balances = np.sort(df['Balance'])

# Calculate the mean balance
mean_balance = np.mean(balances)

# Calculate the absolute differences
n = len(balances)
sum_abs_diff = 0
for i in range(n):
    for j in range(n):
        sum_abs_diff += abs(balances[i] - balances[j])

# Calculate the Gini Index
gini_index = sum_abs_diff / (2 * n * n * mean_balance)

print(f"Gini Index: {gini_index}")


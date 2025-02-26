import pandas as pd
import numpy as np

from scipy.stats import pearsonr

transactions = pd.read_csv("/local/scratch/master_project_utxo_2025/data/bcash/bch_transactions.csv")

# 2. 预处理数据，去除无效值  
transactions = transactions[['Tx ID', 'Total Output', 'Fee']].dropna()

# 3. 计算手续费率 Fee Rate = Fee / Amount
transactions['Fee Rate'] = transactions['Fee'] / transactions['Total Output']

# 4. 计算手续费与交易金额的相关性
correlation, p_value = pearsonr(transactions['Total Output'], transactions['Fee'])
print(f"Pearson Correlation between Fee and Amount: {correlation:.4f} (p-value: {p_value:.4f})")




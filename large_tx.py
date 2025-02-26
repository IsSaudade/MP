import pandas as pd

# 读取交易数据
transactions = pd.read_csv("/local/scratch/master_project_utxo_2025/data/bcash/bch_transactions.csv")

# 设定大额交易阈值
large_tx_threshold = 1000  # 设定阈值为1000 LTC

# 筛选大额交易
large_transactions = transactions[transactions['Total Output'] > large_tx_threshold]

total_large_tx = large_transactions['Total Output'].sum()
total_tx = transactions['Total Output'].sum()


print("🔹 主要资金流出 Tx ID：")
print(large_transactions[['Tx ID', 'Total Output']])  
print(f"大额交易总金额: {total_large_tx}，占比: {total_large_tx / total_tx:.2%}")

import pandas as pd

# Load your UTXO data CSV
df = pd.read_csv('/local/scratch/master_project_utxo_2025/data/bcash/bch_utxo_analysis.csv')

# Filter the rows where UTXO was spent (Spent = True)
spent_utxos = df[df['Spent'] == True]

# Calculate the total amount spent (in BCH)
total_spent_amount = spent_utxos['Amount'].sum()

# Calculate the total lifespan of spent UTXOs (in days)
total_lifespan_days = spent_utxos['Lifespan (days)'].sum()

# Calculate the MicroVelocity (Amount spent per day of UTXO lifespan)
if total_lifespan_days != 0:
    micro_velocity = total_spent_amount / total_lifespan_days
else:
    micro_velocity = 0

print(f"Total_spent_amount: {total_spent_amount} BCH")
print(f"Total_lifespan_days: {total_lifespan_days} day")
print(f"MicroVelocity: {micro_velocity} BCH/day")


# ----------------------------------------
# CARGO COMMODITY ANALYSIS
# Chennai Port Authority
# ----------------------------------------

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ----------------------------
# 1. LOAD DATA
# ----------------------------

file_path = "chennai_port_cargo.xlsx"
df = pd.read_excel(file_path)

print("\nDataset Loaded Successfully!\n")
print(df.head())

# ----------------------------
# 2. BASIC SUMMARY
# ----------------------------

print("\nData Summary:\n")
print(df.describe())

# ----------------------------
# 3. TOTAL PORT TRAFFIC
# ----------------------------

total_imports = df['Import'].sum()
total_exports = df['Export'].sum()
grand_total = df['Total'].sum()

print("\n--- PORT TOTAL TRAFFIC ---\n")
print(f"Total Imports  : {total_imports} Million Tonnes")
print(f"Total Exports  : {total_exports} Million Tonnes")
print(f"Grand Total    : {grand_total} Million Tonnes")

# ----------------------------
# 4. COMMODITY SHARE %
# ----------------------------

df['Share_%'] = (df['Total'] / grand_total) * 100

print("\nCommodity Contribution (%):\n")
print(df[['Commodity', 'Share_%']].sort_values(by='Share_%', ascending=False))

# ----------------------------
# 5. TOP 5 COMMODITIES
# ----------------------------

top5 = df.sort_values(by='Total', ascending=False).head(5)

print("\nTop 5 Commodities:\n")
print(top5[['Commodity', 'Total']])

# ----------------------------
# 6. VISUALIZATIONS
# ----------------------------

sns.set_style("whitegrid")

# Top 10 Commodities by Total Cargo
top10 = df.sort_values(by='Total', ascending=False).head(10)

plt.figure(figsize=(10, 6))
sns.barplot(x='Total', y='Commodity', data=top10)
plt.title("Top 10 Commodities by Total Cargo")
plt.xlabel("Million Tonnes")
plt.tight_layout()
plt.savefig("top10_commodities.png")
plt.show()

# Import vs Export Comparison
plt.figure(figsize=(10, 6))
df[['Import', 'Export']].sum().plot(kind='bar')
plt.title("Total Imports vs Total Exports")
plt.ylabel("Million Tonnes")
plt.tight_layout()
plt.savefig("import_export_comparison.png")
plt.show()

# Pie Chart for Trade Structure
plt.figure(figsize=(6, 6))
plt.pie([total_imports, total_exports],
        labels=['Imports', 'Exports'],
        autopct='%1.1f%%')
plt.title("Trade Composition")
plt.tight_layout()
plt.savefig("trade_composition.png")
plt.show()

# ----------------------------
# 7. BUSINESS INSIGHTS
# ----------------------------

print("\n--- BUSINESS INSIGHTS ---\n")

if total_imports > total_exports:
    print("The port is import-dominant.")
else:
    print("The port is export-dominant.")

print("Major revenue-generating commodities are concentrated in top categories.")

print("\nAnalysis Complete. Graphs saved in project folder.\n")
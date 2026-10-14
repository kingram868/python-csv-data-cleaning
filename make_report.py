import csv

with open("sales_cleaned.csv", newline="") as f:
    rows = list(csv.DictReader(f))

valid = []
missing = 0

for row in rows:
    try:
        valid.append(float(row["amount"]))
    except (ValueError, TypeError):
        missing += 1

total = sum(valid)
average = total / len(valid) if valid else 0

report = f"""
SALES DATA CLEANING REPORT
==========================

Total cleaned rows: {len(rows)}
Valid amounts: {len(valid)}
Missing or invalid amounts: {missing}
Total valid sales: ${total:.2f}
Average sale: ${average:.2f}

Output file: sales_cleaned.csv
"""

with open("cleaning_report.txt", "w") as f:
    f.write(report)

print(report)
print("Report saved to cleaning_report.txt")

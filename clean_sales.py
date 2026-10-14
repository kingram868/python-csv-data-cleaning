import csv

with open("sales_raw.csv", newline="") as f:
    rows = list(csv.DictReader(f))

seen = set()
cleaned = []
duplicates = 0
invalid = 0

for row in rows:
    key = tuple(row.values())

    if key in seen:
        duplicates += 1
        continue

    seen.add(key)

    try:
        row["amount"] = f'{float(row["amount"]):.2f}'
    except (ValueError, TypeError):
        row["amount"] = ""
        invalid += 1

    cleaned.append(row)

with open("sales_cleaned.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=cleaned[0].keys())
    writer.writeheader()
    writer.writerows(cleaned)

print("Original rows:", len(rows))
print("Duplicates removed:", duplicates)
print("Invalid amounts:", invalid)
print("Cleaned rows:", len(cleaned))
print("Output: sales_cleaned.csv")

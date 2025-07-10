import csv

def read_csv(filepath):
    with open(filepath, newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))

def filter_by_age(rows, min_age):
    return [row for row in rows if int(row['age']) >= min_age]

def sort_by_name(rows):
    return sorted(rows, key=lambda r: r['name'])

def main():
    rows = read_csv("sample.csv")
    filtered = filter_by_age(rows, 30)
    sorted_rows = sort_by_name(filtered)

    for row in sorted_rows:
        print(f"{row['name']} ({row['age']}) – {row['email']}")

if __name__ == "__main__":
    main()

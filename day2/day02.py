import csv

def read_csv(filepath):
    with open(filepath, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return list(reader)

def main():
    rows = read_csv("./../sample.csv")
    for row in rows[:3]:
        print(row)

if __name__ == "__main__":
    main()

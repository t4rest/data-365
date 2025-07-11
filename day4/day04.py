import csv
import logging

logging.basicConfig(level=logging.INFO)

def read_and_clean_csv(filepath):
    valid_rows = []

    with open(filepath, newline='', encoding='utf-8') as f:
        for row in csv.DictReader(f):
            try:
                age = int(row['age'])
                row['age'] = age
                valid_rows.append(row)
            except ValueError:
                logging.warning(f"Invalid age for row: {row}")
            except KeyError:
                logging.error("Missing 'age' field in row")

    return valid_rows

def main():
    cleaned = read_and_clean_csv("./../sample.csv")
    for row in cleaned:
        print(f"{row['name']} ({row['age']}) – {row['email']}")

if __name__ == "__main__":
    main()

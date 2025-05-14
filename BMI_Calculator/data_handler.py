import csv
from datetime import datetime

CSV_FILE = "bmi_data.csv"

def save_bmi_record(name, bmi):
    with open(CSV_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, datetime.now().strftime("%Y-%m-%d"), round(bmi, 2)])

def load_user_data(name):
    records = []
    try:
        with open(CSV_FILE, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0].lower() == name.lower():
                    records.append((row[1], float(row[2])))
    except FileNotFoundError:
        pass
    return records

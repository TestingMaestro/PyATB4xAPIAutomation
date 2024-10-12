import pandas as pd
import csv


def test_read_csv_file1():
    df = pd.read_csv("secure_info.csv")
    print("\n", df)


def test_read_csv_file2():
    with open("secure_info.csv") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print(row[0], row[1])

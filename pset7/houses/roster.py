from sys import argv, exit
import csv
import cs50

# ensure that user has provided a house as command line argument
if len(argv) != 2:
    print("Usage: python import.py <house>")
    exit(1)
    
# initialize db
db = cs50.SQL("sqlite:///students.db")

# select relevant data based on house
data = db.execute("SELECT first, middle, last, birth FROM students WHERE house = ? ORDER BY last", argv[1]);

# print data to stdout
for row in data:
    first, middle, last, birth = row["first"], row["middle"], row["last"], row["birth"]
    if middle:
        name = f"{first} {middle} {last}"
    else:
        name = f"{first} {last}"
    print(f"{name}, born {birth}")

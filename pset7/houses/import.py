from sys import exit, argv
import csv
import cs50

# ensure that user has provided a csv file as command line argument 
if len(argv) != 2:
    print("Usage: python import.py filename.csv")
    exit(1)
    
# initialize db
db = cs50.SQL("sqlite:///students.db")

# process each line to extract the five fields 
def process_line(line):
    # split name into first, middle and last name
    names = line["name"].split()
    if len(names) == 2:
        first, last = names
        middle = None
    else:
        first, middle, last = names
    
    house = line["house"]
    birth = int(line["birth"])
    
    return first, middle, last, house, birth

# read csv file 
with open(argv[1], "r") as f:
    reader = csv.DictReader(f)
    for line in reader:
        db.execute("INSERT INTO students (first, middle, last, house, birth) VALUES (?, ?, ?, ?, ?)", *process_line(line))
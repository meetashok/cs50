import csv
from sys import argv, exit


def most_reps(seq, group):
    '''function to find the longest run'''
    
    # set up two pointers, for longest_run and current_run
    longest_run = 0
    current_run = 0
    
    # to check if a match was found on previous check 
    prev = False
    
    i = 0
    while True:
        # stopping condition when the index can't find any more matches
        if i >= len(seq) - len(group) + 1:
            break
        if group == seq[i:(i+len(group))]:
            if prev:
                current_run += 1
            else:
                current_run = 1
                prev = True
            i += len(group)
        else:
            prev = False
            i += 1
        if current_run > longest_run:
            longest_run = current_run
    return longest_run


# ensure that the data and sequence files are passed correctly 
while True:
    if len(argv) >= 3:
        break
    else:
        print("Usage: python dna.py data.csv sequence.txt")
        
# open sequence file
with open(argv[2], "r") as s:
    seq = s.read()

# calculate occurences in the sequence file 
s1 = most_reps(seq, "AGATC")
s2 = most_reps(seq, "AATG")
s3 = most_reps(seq, "TATC")

# print(s1, s2, s3)

# open dna file 
with open(argv[1], "r") as d:
    data_reader = csv.DictReader(d)
    
    # iterate through all rows 
    for row in data_reader:
        name = row["name"]
        d1 = int(row["AGATC"])
        d2 = int(row["AATG"])
        d3 = int(row["TATC"])
        
        # print(name, d1, d2, d3)
        
        if d1 != s1:
            continue
        if d2 != s2:
            continue
        if d3 != s3:
            continue
        
        # print name if match is found and exit(0)
        print(name)
        exit(0)
    
    print("No match")
    exit(0)
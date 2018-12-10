import os
import csv

pycsv = os.path.join('Resources', 'election_data.csv')

with open(pycsv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    # Initialize Variables
    total_votes = 0
    khan_votes = 0
    correy_votes = 0
    li_votes = 0
    o_votes = 0
    khan_avg = 0
    correy_avg = 0
    li_avg = 0
    o_avg = 0
    
    
    
    
    for row in csvreader:
        total_votes += 1
        if row[2] == "Khan":
            khan_votes +=1
        if row[2] == "Correy":
            correy_votes += 1
        if row[2] == "Li":
            li_votes += 1
        if row[2] == "O'Tooley":
            o_votes += 1

    khan_avg = (khan_votes / total_votes) * 100
    correy_avg = (correy_votes / total_votes) * 100
    li_avg = (li_votes / total_votes) * 100
    o_avg = (o_votes / total_votes) * 100

print(f"Total Votes:  {str(total_votes)}")
print(f"Khan: {str(khan_avg)} {str(khan_votes)}")
print(f"Correy: {str(correy_avg)} {str(correy_votes)}")
print(f"Li: {str(li_avg)} {str(li_votes)}")
print(f"O'Tooley: {str(o_avg)} {str(o_votes)}")
print(f"Winner: Khan")
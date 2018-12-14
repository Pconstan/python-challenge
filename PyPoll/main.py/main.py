
import os
import csv

# Assign file location with the pathlib library
csvpath = os.path.join('..','election_data.csv')

total_votes = 0 
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0

with open(csvpath, newline="") as elections:

    csvreader = csv.reader(elections, delimiter=",") 

    header = next(csvreader)     

    for row in csvreader: 

        # Count Voter IDs and store them in variable 'total_votes'
        total_votes +=1

        if row[2] == "Khan": 
            khan_votes +=1
        elif row[2] == "Correy":
            correy_votes +=1
        elif row[2] == "Li": 
            li_votes +=1
        elif row[2] == "O'Tooley":
            otooley_votes +=1

 # make a dictionary out of the two lists
candidates = ["Khan", "Correy", "Li","O'Tooley"]
votes = [khan_votes, correy_votes,li_votes,otooley_votes]

# zip them together
# Return the winner
dict_candidates_and_votes = dict(zip(candidates,votes))
key = max(dict_candidates_and_votes, key=dict_candidates_and_votes.get)

khan_percent = (khan_votes/total_votes) *100
correy_percent = (correy_votes/total_votes) * 100
li_percent = (li_votes/total_votes)* 100
otooley_percent = (otooley_votes/total_votes) * 100

print(f"Election Results")
print(f"----------------------------")
print(f"Total Votes: {total_votes}")
print(f"----------------------------")
print(f"Khan: {khan_percent:.3f}% ({khan_votes})")
print(f"Correy: {correy_percent:.3f}% ({correy_votes})")
print(f"Li: {li_percent:.3f}% ({li_votes})")
print(f"O'Tooley: {otooley_percent:.3f}% ({otooley_votes})")
print(f"----------------------------")
print(f"Winner: {key}")
print(f"----------------------------")
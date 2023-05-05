# In this Challenge, you are tasked with helping a small, rural town modernize its vote-counting process.
    # You will be given a set of poll data called election_data.csv. The dataset is composed of three columns: "Voter ID", "County", and "Candidate". Your task is to create a Python script that analyzes the votes and calculates each of the following values:
    # The total number of votes cast
    # A complete list of candidates who received votes
    # The percentage of votes each candidate won
    # The total number of votes each candidate won
    # The winner of the election based on popular vote
# In addition, your final script should both print the analysis to the terminal and export a text file with the results.

# Create file path across operating systems 
import os

# Read the CSV file
import csv

# Find file path
csvpath = os.path.join('Resources', 'election_data.csv')

# Create Variables 
total_votes = 0          
candidates = []        # store candidate list
candidate_votes = {}    # account for how many votes goes to each candidates

# Open and read the csv file
with open (csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    # read header row first
    header = next(csvreader)

    # loop through every row
    for row in csvreader:
       
       # Calculate total votes
       total_votes += 1
       
       # Find different candidates and add them into the list
       candidate = row[2]
       
       if candidate not in candidates:  
           candidates.append(candidate)
           candidate_votes[candidate] = 1
       else:
           candidate_votes[candidate] += 1


# Create a for loop to calculate percentage of votes each candidates have
for candidate in candidates:         
    vote = candidate_votes[candidate]
    percentage = vote / total_votes * 100


# Find winner 
winner = max(candidate_votes, key=candidate_votes.get)      


# Print output and export to text file
resultpath = os.path.join('Analysis', "Election_Analysis.txt")

with open(resultpath, 'w') as txt:
    print (f"Election Results")
    print (f"---------------------------------------------")
    print (f"Total Votes: {total_votes}")
    print (f"---------------------------------------------")
    for candidate in candidates:         
        vote = candidate_votes[candidate]
        percentage = vote / total_votes * 100
        print (f" {candidate}: {percentage:.3f}% ({vote})")
    print (f"---------------------------------------------")
    print (f"Winner: {winner}")
    print (f"---------------------------------------------")
    
    #print it in text file
    txt.write (f"Election Results\n")
    txt.write (f"---------------------------------------------\n")
    txt.write (f"Total Votes: {total_votes}\n")
    txt.write (f"---------------------------------------------\n")
    for candidate in candidates:         
        vote = candidate_votes[candidate]
        percentage = vote / total_votes * 100
        txt.write (f" {candidate}: {percentage:.3f}% ({vote})\n")
    txt.write (f"---------------------------------------------\n")
    txt.write (f"Winner: {winner}\n")
    txt.write (f"---------------------------------------------\n")
       
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
votes = []
candidates = []

# Open and read the csv file
with open (csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    # read header row first
    header = next(csvreader)

    # loop through every row
    for row in csvreader:

        # Find list of candidates
        if row not in candidates:
            


total_votes = len(votes)


# Print output into terminal for test
print("Election Analysis")
print("--------------------------------------------")

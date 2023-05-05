# Your task is to create a Python script that analyzes the records to calculate each of the following values:
    # The total number of months included in the dataset
    # The net total amount of "Profit/Losses" over the entire period
    # The changes in "Profit/Losses" over the entire period, and then the average of those changes
    # The greatest increase in profits (date and amount) over the entire period
    # The greatest decrease in profits (date and amount) over the entire period
# In addition, your final script should both print the analysis to the terminal and export a text file with the results.

# Create file paths across operating systems 
import os

# Read the CSV file
import csv

# Import the path of the file --> referenced from class activity on reading csv files
csvpath = os.path.join('Resources', 'budget_data.csv')

# Creating variables for storing lists and fo
month = []      # total number of months included in dataset
profit = []     # net total amount of "Profit/Losses" over entire period
profitchange = []    # for the changes in profit/loss over entire period
greatestincdate = ""
greatestdecdate = ""

# Open and read the csv file
with open (csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    # read header row first
    header = next(csvreader)

    # read each row of data after header 
    for row in csvreader:
        
        #Add months into month list using append function 
        month.append(row[0])    #goes through first value of each row and adds it into month list

        #Add the different profits shown into a list using append function
        profit.append (int(row[1]))  #goes through second value of each row 


    # create a for loop to loop through the profit list and calculate the difference between each value with the previous value
    for i in range(1, len(profit)):        #starts from second row 
        
        # create a second variable to store the difference in changes of the profit and loss values
        profitchange.append(profit[i] - profit[i-1])

    
    # create a for loop to find the greatest inc and dec in date
    for i in range(len(profitchange)):
      
       # Find the greatest increase and decrease in profits 
        greatest_increase = max(profitchange)
        greatest_decrease = min(profitchange)
       
        #Find min and max value dates 
        if profitchange [i] == greatest_increase:
            greatestincdate = month[i+1]
        if profitchange [i] == greatest_decrease:
            greatestdecdate = month[i+1]

# Calcuate average change
avg_change = sum(profitchange) / len(profitchange)

# Calculate total number of months
total_months = len(month)

# Calculate net total amount of "Profit/Losses"
net_total = sum(profit)

# Print output and export to text file 
resultpath = os.path.join('Analysis', "Financial_Analysis.txt")

with open(resultpath, 'w') as txt:
    output = (
        f"Financial Analysis\n",
        f"------------------------------------------------------------------------\n",
        f"Total Months: {total_months}\n",
        f"Total: ${net_total}\n",
        f"Average Change: ${avg_change:}\n",
        f"Greatest Increase in Profits: ({greatestincdate},${greatest_increase})\n",
        f"Greatest Decrease in Profits: ({greatestdecdate}, ${greatest_decrease})\n"
    )
    print (output)
    
    #print it in text file
    for row in output:
        txt.write(row)
        txt.write('\n')
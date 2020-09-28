import os
import csv

#Variables
total_votes = 0
khan_count = 0
correy_count = 0
li_count = 0
otooley_count = 0

#Lists to store the CSV Data within Python
voter_IDs = []
counties = []
candidates = []

#Set path for file
election_csv = os.path.join("Resources", "election_data.csv")

#Set path for file
with open(election_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ",")

    #create loop to go through all rows
    for row in csv_reader:
       
        #total votes
        total_votes += 1
        voter_IDs.append(str(row[0]))

        #list of candidates
        candidates.append(str(row[2]))

#total number of votes for each candidate
khan_count = candidates.count("Khan")
correy_count = candidates.count("Correy")
li_count = candidates.count("Li")
otooley_count = candidates.count("O'Tooley")

print(khan_count)
print(correy_count)
print(li_count)
print(otooley_count)


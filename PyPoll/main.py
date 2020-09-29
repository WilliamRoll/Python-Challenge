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

    #column header
    csv_header = next (csv_reader)

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

#header
print("Election Results")
#break
print("-------------------------")
#total number of votes cast
print("Total Votes: " + str(total_votes))
#break
print("-------------------------")
#percentage of votes and number of votes for each candidate 
print("Khan: " + str(format(round((khan_count/total_votes)*100),'.3f')) + "% " + " (" + str(khan_count) + ")")
print("Correy: " + str(format(round((correy_count/total_votes)*100), '.3f')) + "% " + " (" + str(correy_count) + ")")
print("Li: " + str(format(round((li_count/total_votes)*100), '.3f')) + "% " + " (" + str(li_count) + ")")
print("O'Tooley: " + str(format(round((otooley_count/total_votes)*100), '.3f')) + "% " + " (" + str(otooley_count) + ")")

#break
print("-------------------------")

#winner of the elcetion based on popular vote
if khan_count > correy_count and khan_count > li_count and khan_count > otooley_count:
    print("Winner: Khan")
elif correy_count > khan_count and correy_count > li_count and correy_count > otooley_count:
    print("Winner: Correy")
elif li_count > khan_count and li_count > correy_count and li_count > otooley_count:
    print("Winner: Li")
elif otooley_count > khan_count and otooley_count > correy_count and otooley_count > li_count:
    print("Winner: O'Tooley")

#break
print("-------------------------")

#set variable for output file
output_file = os.path.join("Analysis", "polling_data.txt")

#open the file write mode
with open(output_file, "w") as txtfile:

    #write headers and columns for summary table
    txtfile.write("Election Results" +"\n")
    txtfile.write("-------------------------"+"\n")

    txtfile.write("Total Votes: " + str(total_votes)+"\n")
    txtfile.write("-------------------------"+"\n")

    txtfile.write("Khan: " + str(format(round((khan_count/total_votes)*100), '.3f')) + "% " + " (" + str(khan_count) + ")""\n")
    txtfile.write("Correy: " + str(format(round((correy_count/total_votes)*100), '.3f')) + "% " + " (" + str(correy_count) + ")"+"\n")
    txtfile.write("Li: " + str(format(round((li_count/total_votes)*100), '.3f')) + "% " + " (" + str(li_count) + ")"+"\n")
    txtfile.write("O'Tooley: " + str(format(round((otooley_count/total_votes)*100), '.3f')) + "% " + " (" + str(otooley_count) + ")"+"\n")
    txtfile.write("-------------------------"+"\n")
    
    if khan_count > correy_count and khan_count > li_count and khan_count > otooley_count:
        txtfile.write("Winner: Khan"+"\n")
    elif correy_count > khan_count and correy_count > li_count and correy_count > otooley_count:
        txtfile.write("Winner: Correy"+"\n")
    elif li_count > khan_count and li_count > correy_count and li_count > otooley_count:
        txtfile.write("Winner: Li"+"\n")
    elif otooley_count > khan_count and otooley_count > correy_count and otooley_count > li_count:
        txtfile.write("Winner: O'Tooley"+"\n")
    txtfile.write("-------------------------"+"\n")

    txtfile.close()

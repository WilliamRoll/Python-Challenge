#Import Modules
import os
import csv

#Variables
month_count = 1
max_rev = 0
min_rev = 0
monthly_change = 0
avg_monthly_change = 0

#Lists to store the CSV Data within Python
month = []
revenue = []
avg_change = []

#Set path for file
budget_csv = os.path.join("..","Resources", "budget_data.csv")
print(budget_csv)

with open(budget_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ",")

    #header and first row
    csv_header = next (csv_reader)
    first_row = next(csv_reader)
    row_before = (int(first_row[1]))
    monthly_change = int(row_before)
    
    #Add to the list 
    revenue.append(int(first_row[1]))
    month.append(first_row[0])

    #create loop to go through all rows
    for row in csv_reader:
        #count the tot rows in column 0 
        month_count += 1

        #revenue net total
        revenue.append(int(row[1]))

        #average changes
        avg_change.append(int(row[1]) - monthly_change)
        monthly_change = int(row[1])
        month.append(str(row[0]))
        
        #greatest increase
        max_rev = max(avg_change)

        #greatest decrease
        min_rev = min(avg_change)


#calculate the average monthly change
average_monthly_change = sum(avg_change) / (month_count - 1)

#display_results
print("Total Months: " + str(month_count))
print("Total: " + "$"+str(sum(revenue)))
print("Average Change: " + "$"+str(average_monthly_change))
print("Greatest Increase in Profits: " + str(month[avg_change.index(max_rev)+1]) + " $"+str(max_rev))
print("Greates Decrease in Profits: " + str(month[avg_change.index(min_rev)+1]) + " $"+str(min_rev))

#set variable for output file
output_file = os.path.join("Analysis", "budget_data.txt")

#open the file write mode
with open(output_file, "w") as txtfile:

    #write headers and columns 
    txtfile.write("Financial Analysis" +"\n")
    txtfile.write("----------------------------"+"\n")

    txtfile.write("Total Months: " + str(month_count)+"\n")
    txtfile.write("Total: " + "$"+str(sum(revenue))+"\n")
    txtfile.write("Average Change: " + "$"+str(average_monthly_change)+"\n")
    txtfile.write("Greatest Increase in Profits: " + str(month[avg_change.index(max_rev)+1]) + " $"+str(max_rev)+"\n")
    txtfile.write("Greates Decrease in Profits: " + str(month[avg_change.index(min_rev)+1]) + " $"+str(min_rev)+"\n")

    txtfile.close()

    
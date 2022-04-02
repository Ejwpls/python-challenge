#Import modules
import os 
import csv

from numpy import average, double

#csv pathcd
_csv =  os.path.join('Resources','budget_data.csv')

#Read CSV with CSV module
with open(_csv) as csvfile:
    #Specify delimiter
    csvreader = csv.reader(csvfile, delimiter=',')

    #Read the header row first 
    csv_header = next(csvreader)
    #Sum of profit

    #Put into a list 
    data = list(csvreader)

    #Financial analysis 
    total_month = 0
    total_sum = 0

    #Total month 
    total_month = len(data)
    
    #Declare variables
    i = 0
    change = []
    lastvalue = 0
    average_change =0

    #Total Profit/Loss
    for row in (data):
        total_sum = double(row[1]) + total_sum
        if i > 0:
            change.append((double(row[1])-lastvalue))
        lastvalue = double(row[1])    
        i +=1
        
    #Average change
    for v in change:
        average_change = average_change + v
    
    average_change = round(average_change/len(change),2)

    #Maximum Profit
    max_changeprofit = max(change)
    min_changeprofit = min(change)

    #Find the index
    indx_max = change.index(max_changeprofit)
    indx_min = change.index(min_changeprofit)
    
    #Declaring Variable
    date_max = ''
    date_min = ''

    i = 0

    #Index date from first list 
    for row in data:
        if i == indx_max+1:
            date_max = row[0]
        if i == indx_min+1:
            date_min = row[0]
        i += 1
    
    #Financial Analysis
    print("Financial Analysis" + "\n" + "---------------------------")
    print("Total Months: " + str((total_month)))
    print("Total: $" + str((total_sum)))
    print("Average Change: $" + str((average_change)))
    print(f"Greatest Increase in Profits: {date_max} (${str((max_changeprofit))})")
    print(f"Greatest Decrease in Profits: {date_min} (${str((min_changeprofit))})")

#Write CSV'
with open('financial_summary.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([("Financial Analysis")])
    writer.writerow([("---------------------------")])
    writer.writerow([("Total Months: " + str((total_month)))])
    writer.writerow([("Total: $" + str((total_sum)))])
    writer.writerow([("Average Change: $" + str((average_change)))])
    writer.writerow([(f"Greatest Increase in Profits: {date_max} (${str((max_changeprofit))})")])
    writer.writerow([(f"Greatest Decrease in Profits: {date_min} (${str((min_changeprofit))})")])

print("Success! .csv file saved in source folder")
    


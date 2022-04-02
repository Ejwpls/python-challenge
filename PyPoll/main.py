#Import modules
import os 
import csv

from numpy import append, average, double, maximum

#csv path
_csv =  os.path.join('Resources','election_data.csv')

with open(_csv) as election_csv:
    #Split the data on commas 
    csvreader = csv.reader(election_csv, delimiter=',')
    header = next(csvreader)
    
    election_list = list(csvreader)
    #Total Number of voters 
    total_votes = len(election_list)

#State a dictionary for each unique candidate
candidate_list = {}
vote_count = 0

#List of unique votes, while doing so put votes into each name
for row in election_list:
    if row[2] not in candidate_list:
        new_candidate = {row[2]: 1}
        candidate_list.update(new_candidate)
    candidate_list[row[2]] = int(candidate_list[row[2]]) + 1

#print(candidate_list)

with open('Election_Results.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    #Election Results
    print("Election Results" + "\n" + "---------------------------")
    writer.writerow([("Election Results")])
    writer.writerow([("---------------------------")])
    print("Total Votes: " + str((total_votes))+ "\n" + "---------------------------")
    writer.writerow([("Total Votes: " + str((total_votes)))])
    writer.writerow([("---------------------------")])

    counter = 0 

    for candidate in candidate_list:
        vote_percent = candidate_list[candidate]/total_votes*100
        if vote_percent >= counter:
                winner = str(candidate)
                counter = vote_percent
        print(f"{candidate}: {round(vote_percent,4)}% ({candidate_list[candidate]})")
        writer.writerow([(f"{candidate}: {round(vote_percent,4)}% ({candidate_list[candidate]})")])

    print("---------------------------")
    writer.writerow([("---------------------------")])
    print(f"Winner: {winner}")
    writer.writerow([(f"Winner: {winner}")])
    print("---------------------------")
    writer.writerow([("---------------------------")])

print("Success! .csv file saved in source folder")
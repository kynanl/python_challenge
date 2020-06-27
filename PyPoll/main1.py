# Import Modules
import os
import csv


# Set path for file and open file
#declare  variables
csvpath = os.path.join("Resources", "election_data.csv")


#read file, skipping the header line 
with open(csvpath) as csvfile: 
    csv_reader = csv.reader(csvfile, delimiter=",")
    csv_heading = next(csv_reader)
    votes_cast = 0
    vote_counter = []
    khan_votes = 0
    correy_votes = 0
    li_votes = 0
    otooley_votes = 0
    candidates_w_votes = []
    overall_list = []
    percent_votes = 0
    winner = str
    candidates = str
# calculate The total number of votes cast
    print(csv_heading)
    for row in csv_reader:
        votes_cast = votes_cast +1
        #create a complete list of candidates who received votes
        candidates = row[2]
        if candidates not in candidates_w_votes:
            candidates_w_votes.append(candidates)
        # create total number of votes for each candidate
        if candidates == candidates_w_votes[0]:
            khan_votes = khan_votes + 1
        elif candidates == candidates_w_votes[1]:
            correy_votes = correy_votes + 1
        elif candidates == candidates_w_votes[2]:
            li_votes = li_votes + 1
        else:
            otooley_votes = otooley_votes + 1
        #The winner of the election based on popular vote.
        overall_list =[khan_votes, correy_votes, li_votes, otooley_votes]
        if max(overall_list) == khan_votes:
            winner = "khan"
        elif max(overall_list) == correy_votes:
            winner = "correy"
        elif max(overall_list) == li_votes:
            winner = "Li"
        else: winner = "otooley"
            


# print results preview
print("Election Results")
print("-------------------------------")
print(f"Total Votes: {votes_cast}")
print("-------------------------------")
print(f"Khan: {khan_votes/votes_cast:.3%}  ({khan_votes})")   
print(f"Correy: {correy_votes/votes_cast:.3%}  ({correy_votes})")
print(f"Li: {li_votes/votes_cast:.3%}  ({li_votes})\n")
print(f"O'Tooley: {otooley_votes/votes_cast:.3%}  ({otooley_votes})")
print("--------------------------------")
print(f"Winner: {winner}\n")
print("--------------------------------")


#Export Output file
output_path = os.path.join("analysis", "pypoll_summary.txt")
#write text file
with open (output_path, 'w') as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("-------------------------------\n")
    txtfile.write(f"Total Votes: {votes_cast}\n")
    txtfile.write(f"Khan: {khan_votes/votes_cast:.3%}  ({khan_votes})\n")
    txtfile.write(f"Correy: {correy_votes/votes_cast:.3%}  ({correy_votes})\n")
    txtfile.write(f"Li: {li_votes/votes_cast:.3%}  ({li_votes})\n")
    txtfile.write(f"O'Tooley: {otooley_votes/votes_cast:.3%}  ({otooley_votes})\n")
    txtfile.write("--------------------------------\n")
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write("---------------------------------\n") 




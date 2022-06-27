# The data we need to retrieve
# 1. the total number of votes cast
# 2. a complete list of candidates who received votes
# 3. the percentage of votes each candidate won
# 4. the total number of votes each candidate won
# 5. the winner of the election based on popular vote

# Add our dependencies
import csv
import os

# load a file from path
file_to_load = os.path.join("Resources", "election_results.csv")

#create a filename variable to do a direct or indirect path to file
file_to_save = os.path.join("analysis", "election_analysis.txt")

# initialize a total vote counter
total_votes = 0
candidate_options = []
candidate_votes = {}

#winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#open the eletion results and read the file
with open(file_to_load) as election_data:
    print(election_data)

    #read the file object with the reader function
    file_reader = csv.reader(election_data)
    
    #read the header row
    headers = next(file_reader)

    #print each row in the CSV file
    for row in file_reader:

        # add to the total vote count
        total_votes += 1

        #print the candidate name from each row
        candidate_name = row[2]

        #show only the candidate names
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

            #begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0

        #add a vote
        candidate_votes[candidate_name] +=1

for candidate_name in candidate_votes:
    #retrieve vote count of a candidate
    votes = candidate_votes[candidate_name]
    #calculate percentage of votes
    vote_percentage = float(votes)/float(total_votes) * 100
    #print the candidate name and percentage of votes
    print(f"{candidate_name} received {vote_percentage:.1f}% of the vote.")

    #print out each candidate's name, vote count, and percentage of votes
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n") 

    #determine winning vote count and candidate
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        winning_count = votes
        winning_percentage = vote_percentage
        winning_candidate = candidate_name

winning_candidate_summary = (
    f"--------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"--------------------\n")
print(winning_candidate_summary)


   

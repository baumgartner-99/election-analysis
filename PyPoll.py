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

#open the eletion results and read the file
with open(file_to_load) as election_data:
    print(election_data)

    #read the file object with the reader function
    file_reader = csv.reader(election_data)
    
    #print the header row
    headers = next(file_reader)
    print(headers)

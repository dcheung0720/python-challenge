import os
import csv
import collections

#csv file path
csv_path = os.path.join("Resources", "election_data.csv")

#reading file
with open(csv_path) as csv_file:

    # csv_reader
    csv_reader = csv.reader(csv_file, delimiter = ",")

    # initializing csv_header
    csv_header = next(csv_reader)

    #list of name using list comprehension
    names = [row[2] for row in csv_reader]

    # counting using Python's collections lib
    counter = collections.Counter(names)

    #num votes using sum and list comprehension
    num_votes = len(names)

    # write the analyses in the analysis.txt file
    analysis_path = os.path.join("analysis", "analysis.txt")

    # opening and writing the analysis file
    with open(analysis_path, "w") as analysis_file:
        # 
        lines = [
                    "Election Results\n",
                    "-------------------------\n"
                    f"Total Votes: {num_votes}\n",
                    "-------------------------\n"
                ]
        
        # define the winner variable
        winner = ""
        winner_vote = 0

        # for every key (name) in the counter
        for key in counter.keys():
            # votes for this person
            votes = counter[key]

            # looking for the maximum vote/ winner
            if(votes > winner_vote):
                winner_vote = votes
                winner = key

            percent_vote = round(votes/num_votes * 100, 3)
            lines.append(f"{key} : {percent_vote}% ({votes})\n")

        lines.append( "-------------------------\n")

        lines.append(f"Winner: {winner}\n")

        lines.append( "-------------------------\n")

        # write into file
        analysis_file.writelines(lines)



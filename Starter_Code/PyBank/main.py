import os
import csv

#relative path to the csv file
csv_path = os.path.join('Resources', 'budget_data.csv')

#read file
with open(csv_path) as csv_file:
    #reading csv, removing commas
    csv_reader = csv.reader(csv_file, delimiter= ',')

    csv_header = next(csv_reader)

    # variables set up for write later
    total_months =  0
    total_reserve = 0
    #assume worst case for greatest increase and decrease
    greatest_increase_date = ""
    greatest_increase = float('-inf')
    greatest_decrease_date = ""
    greatest_decrease = float('inf')

    for row in csv_reader:
        #date
        date = row[0]

        #profit/loss one-time conversion 
        netProfit = int(row[1])

        #counter months
        total_months += 1

        #total_reserve
        total_reserve += netProfit

        # brute force search of min (since we are already looping, otherwise we can use min for optimization)
        if netProfit < greatest_decrease:
            greatest_decrease_date = date
            greatest_decrease = netProfit
        
        #brute force search of max (since we are already looping, otherwise we can use max for optimization)
        if netProfit > greatest_increase:
            greatest_increase_date = date
            greatest_increase = netProfit

    #write file
    analysis_path = os.path.join("Analysis", "analysis.txt")

    average_Change = total_reserve/ total_months

    # open analysis file
    with open(analysis_path, 'w') as analysis_file:
        # creating a list of lines to write with escape characters
        lines = ['Finanial Analysis\n',
                 "--------------------\n",
                 f"Total Months: {total_months}\n",
                 f"Total: {total_reserve}\n",
                 f"Average Change: {average_Change}\n",
                 f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n",
                 f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n" ]

        analysis_file.writelines(lines)



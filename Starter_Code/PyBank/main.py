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
    total_profit = 0
    average_Change = 0
    previous_profit = 0
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

        #total_profit
        total_profit += netProfit

        #change in profit
        delta_profit = netProfit - previous_profit

        #average_Change_sum, only check the previous value if the index is > 1
        if(total_months > 1):
            average_Change += delta_profit

        # brute force search of min 
        if delta_profit < greatest_decrease:
            greatest_decrease_date = date
            greatest_decrease = delta_profit
        
        #brute force search of max
        if delta_profit > greatest_increase:
            greatest_increase_date = date
            greatest_increase = delta_profit

        previous_profit = netProfit

    #write file path
    analysis_path = os.path.join("Analysis", "analysis.txt")

    average_Change /= (total_months - 1)

    # open analysis file
    with open(analysis_path, 'w') as analysis_file:
        # creating a list of lines to write with escape characters
        lines = ['Finanial Analysis\n',
                 "--------------------\n",
                 f"Total Months: {total_months}\n",
                 f"Total: ${total_profit}\n",
                 f"Average Change: ${round(average_Change, 2)}\n",
                 f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n",
                 f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n" ]
        
        #write the lines
        analysis_file.writelines(lines)



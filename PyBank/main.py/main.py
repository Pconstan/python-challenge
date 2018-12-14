import os
import csv

csvpath = os.path.join('..','budget_data.csv')
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    for row in csvreader:
        print(row)
    
    csvfile.seek(0) #resets so next for loop works
    row_count = sum(1 for row in csvreader) - 1
    #1 minus total number of rows gives
    #everything but the header
    print("-----------------------")
    print("Financial Analysis")
    print("Total Months:", row_count)
    #--------------------------------------- pt. 2
    sumprof=0
    sumloss = 0
    total = 0
    profit=0
    csvfile.seek(0)
    csv_header = next(csvreader) #this skips the header so we can count
                                 #only the integers
    for row in csvreader:
        profit = int(row[1])
        if profit > 0:
            sumprof = sumprof + profit
        elif profit < 0:
            sumloss = sumloss + profit
    total = sumprof - sumloss
    print(f"Total: {total}")
    # --------------------------------- pt.3
    csvfile.seek(0)
    next(csvreader) #skip the header again
    months = []
    total_profit = []
    avgchange = []
    for row in csvreader:
        months.append(row[0])
        total_profit.append(int(row[1]))
    for i in range(len(total_profit)-1):
        avgchange.append(total_profit[i+1]-total_profit[i])
    max_increase = max(avgchange)
    max_decrease = min(avgchange)
    max_increase_month = avgchange.index(max(avgchange)) + 1
    max_decrease_month = avgchange.index(min(avgchange)) + 1 
    print(f"Average Change: {round(sum(avgchange)/len(avgchange),2)}")
    print(f"Greatest Increase in Profits: {months[max_increase_month]} (${(str(max_increase))})")
    print(f"Greatest Decrease in Profits: {months[max_decrease_month]} (${(str(max_decrease))})")
with open('PyBank.txt', 'w') as f:
    print('Pybank:', filename, file=f)
import os
import csv

pycsv = os.path.join('Resources', 'budget_data.csv')

print(pycsv)
def getInfo():
    print("got here")

with open(pycsv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    # Variables should be initialized
    total_months = 0
    total = 0
    total_change = 0
    previous_month = 0
    average_change = 0
    greatest_increase = 0
    greatest_decrease = 0
    change = 0

    

    for row in csvreader:
        total_months += 1
        total += float(row[1])
        
        if total_months == 1:
            total_change += float(row[1]) - previous_month
            change = float(row[1]) - previous_month    
        if total_months > 1:
            total_change = float(row[1])
        if change > greatest_increase:
            greatest_increase = change
        if change < greatest_decrease:
            greatest_decrease = change

        total_change += previous_month
        
        previous_month = float(row[1])


average_change = total_change / 86

print(f"Total Months:  {str(total_months)}")
print(f"Total: {str(total)}")
print(f"Average Change: {str(average_change)}")
print(f"Greatest Increase in Profits: {str(greatest_increase)}")
print(f"Greatest Decrease in Profits: {str(greatest_decrease)}")

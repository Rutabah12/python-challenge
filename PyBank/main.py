import os
import csv
csvpath=os.path.join('budget_data.csv')
total_months = []
total_profit=[]
monthly_profit_change=[]


with open(csvpath, "r") as csvfile:
   
    csv_reader= csv.reader(csvfile, delimiter=',')
    header = next(csv_reader)
    
    
        
    for row in csv_reader:
        
        total_months.append(row[0])
        total_profit.append(int(row[1]))

   for i in range(len(total_profit)-1):
        monthly_profit_change.append(total_profit[i+1]-total_profit[i])
    
max_increase_value = max(monthly_profit_change)
max_decrease_value = min(monthly_profit_change)

increase_month = monthly_profit_change.index(max(monthly_profit_change)) + 1
decrease_month = monthly_profit_change.index(min(monthly_profit_change)) + 1 

increase_month_name=total_months[max_increase_month]
decrease_month_name=total_months[max_decrease_month]

print("Financial Analysis")
print("----------------------------")
print(f"total months: {len(total_months)}")
print(f"Total: ${sum(total_profit)}")
print(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
print(f"Greatest increase in Profits: {increase_month_name} (${(max_increase_value)})")
print (f"Greatest Decrease in Profits: {decrease_month_name} (${(max_decrease_value)})")

output_file=os.path.join("budget_analysis.csv")

with open(output_file, "w") as file: 
    file.write("Financial Analysis")
    file.write("----------------------------")
    file.write(f"total months: {len(total_months)}")
    file.write(f"Total: ${sum(total_profit)}")
    file.write(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
    file.write(f"Greatest increase in Profits: {increase_month_name} (${(max_increase_value)})")
    file.write(f"Greatest Decrease in Profits: {decrease_month_name} (${(max_decrease_value)})")





# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'

# %%
import csv
import os


# %%
csvpath=os.path.join('Resources','budget_data.csv')
file_to_output = os.path.join("analysis", "budget_analysis.txt")
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)
    total_months = 0
    month_of_change = []
    net_change_list = []
    greatest_increase = ["", 0]
    greatest_decrease = ["", 9999999999999999999]
    total_net = 0
    
    print(f"Header: {csv_header}")
    
    for row in csvreader:
        month.append(row[0])
        revenue.append(row[1])
    print(len(month))
 #Revenue 
    revenue_int = map(int,revenue)
    total_revenue = (sum(revenue_int))
    print(total_revenue)

 #Avg Change
    i = 0
    for i in range(len(revenue) - 1):
        profit_loss = int(revenue[i+1]) - int(revenue[i])
 # append profit_loss
        revenue_change.append(profit_loss)
    Total = sum(revenue_change)
    #print(revenue_change)
    monthly_change = Total / len(revenue_change)
    print(monthly_change)
    #print(Total)
    
#Greatest Increase
    profit_increase = max(revenue_change)
    print(profit_increase)
    k = revenue_change.index(profit_increase)
    month_increase = month[k+1]
    
#Greatest Decrease
    profit_decrease = min(revenue_change)
    print(profit_decrease)
    j = revenue_change.index(profit_decrease)
    month_decrease = month[j+1]


#Print Statements

print(f'Financial Analysis'+'\n')
print(f'----------------------------'+'\n')


print("Total number of months: " + str(len(month)))

print("Total Revenue in period: $ " + str(total_revenue))
      
print("Average monthly change in Revenue : $" + str(monthly_change))

print(f"Greatest Increase in Profits: {month_increase} (${profit_increase})")

print(f"Greatest Decrease in Profits: {month_decrease} (${profit_decrease})")



# Export the results to text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)


# %%



# %%

   


# %%



# %%




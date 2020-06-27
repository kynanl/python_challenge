# Import Modules
import os
import csv


# Set path for file and open file
csvpath = os.path.join('Resources', "budget_data.csv")

#read file, skipping the header line 
with open(csvpath) as csvfile: 
    csv_reader = csv.reader(csvfile, delimiter=",")
    csv_heading = next(csv_reader)
 
 # variables reminders
    months = [] 
    profit_loss = 0
    average_pl_change=0
    greatest_profit=[]
    greatest_loss= 0
    greatest = 0
    profit = []
    change = []
    max_row = 0
 #calcualte length of period and total P&L   
    for r in csv_reader:
        month = r[0]
        if month not in months:
            months.append(month)
        profit_loss += int(r[1])
        profit.append(r[1])
#calculate greates profit and loss   
    for i in range(len(profit)-1):
        changes = int(profit[i+1]) - int(profit[i])
        if changes not in change:
            change.append(changes)
    greatest = max(change)    
    greatest_loss = min(change)
 
 # identify greatest profit and greatest loss month   
    for a in range(len(change)):
        if greatest == change[a]:
            max_row = a + 1
        if greatest_loss == change[a]:
            min_row = a +1
#calculate average change for full period                    
total_change = (int(profit[85])) - (int(profit[0]))
average_change = total_change/(len(months)-1)
average_change = float(average_change)
average_change = round(average_change, 2)

#print final results 
print('Financial Analysis')
print('-------------------------------------')
print('Total Months = ' + str(len(months)))
print('Total P&L =  $' + str(profit_loss))

print('Maximum Profit = ' + months[max_row] + "  $" + str(greatest))
print('Maximum Loss = ' + months[min_row] + "  $"  + str(greatest_loss))
print('Average Change = $' + str(average_change))

#Export Output file
output_path = os.path.join("analysis", "pybank_summary.txt")
#write text file
with open (output_path, 'w') as txtfile:
    txtfile.write('Financial Analysis\n')
    txtfile.write('------------------------------------\n')
    txtfile.write(f'Total Months: {(len(months))}\n')
    txtfile.write(f'Total:  ${(profit_loss)}\n')
    txtfile.write(f'Greatest Increase in Profits:  {months[max_row]} ${str(greatest)}\n')
    txtfile.write(f'Greatest Decrease in Profits:  {months[min_row]}  ${str(greatest_loss)}\n')
    txtfile.write(f'Average Change: ${str(average_change)}\n')


   
    
print("Welcome to the Tip Calculator!")
valueOfBill = float(input("What was the total bill? $"))
tipPercentage = float(input("How much tip would you like to give? 10, 12, or 15? "))
peopleToSplit = float(input("How many people to split the bill? "))

fullValue = valueOfBill + tipPercentage / 100 * valueOfBill 
print('${:,.2f}'.format(fullValue / peopleToSplit))

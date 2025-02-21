# start taking the input from the user
salary= int(input("Enter your salary: "))
month= input("Enter the name of the month: ")
saving=int(input("Enter the percentage of saving: "))
rent=int(input("Enter the percentage of rent: "))
electricity=int(input("Enter the percentage of electricity: "))

savingAmmount=(salary*saving)/100
rentAmmount=(salary*rent)/100
electricityAmmount=(salary*electricity)/100

# Ammount Calculating
print("The ammount allocated to saving is: "+str(savingAmmount)+"!")
print("The ammount allocated to rent is: "+str(rentAmmount)+"!")
print("The ammount allocated to electricity is: "+str(electricityAmmount)+"!")

# Total expenses
totalExpenses=savingAmmount+rentAmmount+electricityAmmount
print("The total expenses is: " +str(totalExpenses))

# Calculating the remainder

remainder=salary-totalExpenses
print("The remainder of salary is: "+str(remainder))


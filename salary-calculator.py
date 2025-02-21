# start taking the input from the user
salary= int(input("Enter your salary: "))
month= input("Enter the name of the month: ")
saving=int(input("Enter the percentage of saving: "))
rent=int(input("Enter the percentage of rent: "))
electricity=int(input("Enter the percentage of electricity: "))

savingAmount=(salary*saving)/100
rentAmount=(salary*rent)/100
electricityAmount=(salary*electricity)/100

# Amount Calculating
print("The amount allocated to saving for "+month+" is: "+str(savingAmount)+"!")
print("The amount allocated to rent for "+month+" is: "+str(rentAmount)+"!")
print("The amount allocated to electricity for "+month+" is: "+str(electricityAmount)+"!")

# Total expenses
totalExpenses=savingAmount+rentAmount+electricityAmount
print("The total expenses is: " +str(totalExpenses))

# Calculating the remainder

remainder=salary-totalExpenses
print("The remainder of salary is: "+str(remainder))

# Yearly estimated for rent and electricity
yearlyRent=rentAmount*12
yearlyElectricity=electricityAmount*12
print("The estimated yearly rent is: "+str(yearlyRent))
print("The estimated yearly electricity is: "+str(yearlyElectricity))

# Squarring the salary
sqrSalary=salary**2
print("The salary squared is: "+str(sqrSalary))


# Additional Amount
isAdditional=input("Is there an additional amount (yes/no)?  ")
if isAdditional=="yes":
    additonalAmount=int(input("Enter the additional amount: "))
    savingRemainder = additonalAmount/savingAmount
    print("The remainder is: "+str(savingRemainder))



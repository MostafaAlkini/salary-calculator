# start taking the input from the user
salary= int(input("Enter your salary: "))
month= input("Enter the name of the month: ")
saving=int(input("Enter the percentage of saving: "))
rent=int(input("Enter the percentage of rent: "))
electricity=int(input("Enter the percentage of electricity: "))

savingAmmount=(salary*saving)/100
rentAmmount=(salary*rent)/100
electricityAmmount=(salary*electricity)/100

print("The ammount allocated to saving is: "+str(savingAmmount)+"!")
print("The ammount allocated to rent is: "+str(rentAmmount)+"!")
print("The ammount allocated to electricity is: "+str(electricityAmmount)+"!")


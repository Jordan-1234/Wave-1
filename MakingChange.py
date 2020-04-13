#Cost is the amount that the user inputs to indicate the change
cost = float(input('Product Cost: '))
#Put each variable into cents 
penny = 1
nickel = 5
dime = 10
quarter = 25
loonie = 100
toonie = 200
#Sorted each variable to ensure that each denomination would output the least amount of change.
num_of_toonies = int(cost // toonie)
cost %= toonie
num_of_loonies = int(cost // loonie)
cost %= loonie
num_of_quarters = int(cost // quarter)
cost %= quarter
num_of_dimes = int(cost // dime)
cost %= dime
num_of_nickels = int(cost // nickel)
cost %= nickel
num_of_pennies = int(cost)
print("The number of toonies will be " + str(num_of_toonies))
print("The number of loonies will be " + str(num_of_loonies))
print("The number of quarters will be " + str(num_of_quarters))
print("The number of dimes will be " + str(num_of_dimes))
print("The number of nickels will be " + str(num_of_nickels))
print("The number of pennies will be " + str(num_of_pennies))
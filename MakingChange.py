cost = float(input('Product Cost: '))
penny = 1
nickel = 5
dime = 10
quarter = 25
loonie = 100
toonie = 200
# Cost --> 500
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
print(num_of_toonies)
print(num_of_loonies)
print(num_of_quarters)
print(num_of_dimes)
print(num_of_nickels)
print(num_of_pennies)

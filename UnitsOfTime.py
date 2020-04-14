# Convert each variable to seconds
Days = int(input("What is the number of days ")) * 3600 * 24
Hours = int(input("What is the number of hours ")) * 3600
Minutes = int(input("what is the number of minutes ")) * 60
Seconds = int(input("What is the number of seconds "))
# Add the variables to get the total number of seconds
total_Time = Days + Hours + Minutes + Seconds  
print("The total number of seconds is: " + str(total_Time))
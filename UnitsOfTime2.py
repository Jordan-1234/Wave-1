#Convert seconds to days, hours, minutes, seconds
seconds_In_A_Minute = 60
seconds_In_A_Hour = 3600
seconds_In_A_Day = 86400

#User input for the number of seconds
seconds = int(input("What is the total amount of seconds: "))

# Find out the days, hours, minutes, seconds
days = seconds / seconds_In_A_Day
seconds = seconds % seconds_In_A_Day

hours = seconds / seconds_In_A_Hour
seconds = seconds % seconds_In_A_Day

minutes = seconds / seconds_In_A_Minute
seconds = seconds % seconds_In_A_Minute

print("The number of days is: " + str(round(days,1))) 
print("The number of hours is: " + str(round(hours,1)))
print("The number of minutes is: " + str(round(minutes,1)))
print("The number of seconds is: " + str(seconds))

# Eoin Lees
# This program reads in a students percentage result
# and prints out the corresponding grade

percentage = float(input("Enter the percentage: "))

if percentage < 0 or percentage > 100:
    print("Please enter a number between 0 and 100")
elif percentage < 40: # Less than 40
    print("Fail")
elif percentage < 50: # Between 40 and 49
    print("Pass")
elif percentage < 60: # Between 50 and 59
    print("Merit 1")
elif percentage < 70: # Between 60 and 69
    print("Merit 2")
else: #Only other options is between 70 and 100
    print ("Distinction")


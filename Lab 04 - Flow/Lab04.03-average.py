#Eoin Lees
#This program reads in numbers until the user enters a 0
#The numbers are printed along with the average

numbers = []

# first number tehn we check if it is 0 in the while loop
number = int(input("Enter number (0 to quit): "))

while number != 0:
    numbers.append(number)
    
    # Read teh next number and check if 0
    number = int(input("Enter number (0 to quit): "))

for value in numbers:
    print (value)

# Average to be float
average = float(sum(numbers)) / len(numbers)

print ("The average is {}".format(average))


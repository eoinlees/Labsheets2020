#Eoin Lees

#This program reads in two numbers and divides them leaving
# the output as teh integer answer plus the remainder

x = int(input("Insert the first number: "))
y = int(input("inster the second number you wish to divide by please: "))

answer = int(x/y)
remainder = x%y

print("{} divided by {} is {} with {} remainder.".format(x, y, answer, remainder))

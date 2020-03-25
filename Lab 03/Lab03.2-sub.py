#Eoin Lees
#Create a program to subtract one number from another

#Input reads in a string so we need to convert it into an int so 
# we can preform mathematical operations

x = int(input("Enter first number: "))
y = int(input("Enter Second number: "))

z = x - y

print("{} minus {} is {}".format(x, y, z))

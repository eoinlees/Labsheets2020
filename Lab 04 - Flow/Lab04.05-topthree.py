#Eoin Lees
#This program generates 10 random numbers and prints them out
#then prints out the top 3

import random
# I program the general case

howMany = 10
topHowMany = 3
rangeFrom = 0
rangeTo = 100

numbers = []

for i in range(0,10):
    numbers.append(random.randint(rangeFrom,rangeTo))
print ("{} random numbers\t {}".format(howMany, numbers))

#Keeping the origional list
#idea from stack overflow
# https://stackoverflow.com/questions/32296887/how-to-find-the-1st-2nd-3rd-highest-values-in-a-list-in-python

topOnes = numbers.copy()
topOnes.sort(reverse = True)
print ("The top {} numbers are \t\t {}".format(topHowMany, topOnes[0:topHowMany]))


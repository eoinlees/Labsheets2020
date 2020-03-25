#Eoin Lees
#This program reads in a string and strips any leading or trailing spaces. 
# it also converts all the letters to lower case
#this program also outputs the length of the origional string and the normalised one

rawString = input("Please enter a string:")
normalisedString = rawString.strip().lower()

lengthOfRawString = len(rawString)
lengthOfNormalisedStrinf = len(normalisedString)

print("That String normalised is: {}".format(normalisedString))
print("We reduced the imput string from {} to {} characters.".format(lengthOfRawString, lengthOfNormalisedStrinf))

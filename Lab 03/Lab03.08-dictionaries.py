#Eoin Lees


currentBook = {
    "Title" : "Harry Potter eats his dinner",
    "Author" : "Just Kidding Rowling",
    "Price" : 12
}
#print dictionary object
print(currentBook)

#print just the author
print(currentBook["Author"])

#Create and set attribute ISBN
currentBook["ISBN"] = "1234567"

#use for loop to iterare through the current books values
#notice the order the for loop gives the values.
print("The current book has these values:")
for value in currentBook.values():
    print (" => {}".format(value))
    
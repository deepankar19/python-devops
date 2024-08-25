# Reverse a String

text = input("Please enter value in string : ")
print("Using  String slicing : " + text[::-1])

newText = ''
for i in text:
    newText = i + newText
print("Using  for loop : " +newText)
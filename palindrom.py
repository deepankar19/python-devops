# Check if a string is a palindrome or not
# Palindrome is same chracter/text/string from front and back when we read 
# 'if len(text) == 1::' This line checks if the length of the string text is equal to 1. A string with a single character is always a palindrome   because it reads the same forwards and backwards.


def Palindrome(text):
    if len(text) == 1:
        return text + " is a Palindrome "
    else:
        if text == text[::-1]:
            return text + " is a Palindrome"
        else:
            return text + " is not a Palindrome"
            

print(Palindrome(input(" please input your text : ")))
# Calculate the sum of all the digits in a number

def sum(n):
    if int(n) < 10:
        return n
    else:
        allDigits = int(n) // 10
        lastDigit = int(n) % 10
        return sum(allDigits) + lastDigit

print("sum of digits : ", sum(input(" Please enter your Digit : ")))
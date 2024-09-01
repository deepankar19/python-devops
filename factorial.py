# Calculate the factorial of a number

def fac(n):
    if n == 1:
        return n
    else:
        return (n * fac(n-1))
    
# Get input from the user
n = int(input("Enter a number to calculate its factorial: "))

# Calculate and print the factorial
if n < 1:
    print("Please enter a positive integer.")
else:
   # print(f"The factorial of {n} is {fac(n)}")
   print(f"The factorial of {n}! =", fac(n))

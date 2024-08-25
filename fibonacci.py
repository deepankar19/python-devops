# Find the Fibonacci sequence

def fib(n):
    if n <= 1:
        return n
    return (fib(n-1) + fib(n-2))

term = 50
print("Fibonacci Sequence : ")
for i in range(term) :
    print(fib(i))
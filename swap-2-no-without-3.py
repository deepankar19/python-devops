# Swap two numbers without using third variable

a, b = input(" please enter frist value : "), input(" please enter second value : ")
a, b = b, a
print("Using in-build syntax : a is" , a , "& b is" , b)

a, b = input(" please enter frist value : "), input(" please enter second value : ")
a = a + b
b = (int(a) - int(b))
a = (int(a) - int(b))
print("Using arithmetic operations : a is" , a , "& b is" , b)
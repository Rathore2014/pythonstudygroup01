# Factorial: WAP to print factorial of given number.

n=int(input("Enter a number: "))
Factorial = 1
if n < 0:
    print("Factorial does not negative numbers")
elif n == 0:
    print("The factorial of 0 is:  1")
else:
    for i in range(1, n + 1):
        Factorial = Factorial * i
    print("The factorial of",n,"is",Factorial)



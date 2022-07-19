# 6-4........... Prime: Write a function that takes one or more number
#                as a parameter and check numbers are prime or not.
def prime(n):
    if (n==1):
        print("1 is not a prime number")
    elif (n==2):
        print("2 is prime number")
    else:
        for x in range(2,n):
            if(n % x==0):
                print(n,"is not prime number")
        print(n,"is a prime number")             
print(prime(7))

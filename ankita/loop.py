 # 1............Max number from List: WAP to find largest number from list.
#               Given list with values items = [10, 20, 30, 40, 50]


Items = [10,20,30,40,50]
largest_no = Items[0]
for n in Items:
    if n > largest_no:
        largest_no = n

print(f"The largest number in Items is: {largest_no}")



# 2.........Search: WAP to find given search value from dictionary values.
#                   Given dictionary with values
#                   users = {‘u1’:‘Administrator’, ‘u2’:‘ServerAdmin’, ‘u3’:‘NetworkAdmin’}

users = {'u1':'Administrator', 'u2':'ServerAdmin', 'u3':'NetworkAdmin'}
for i in users.keys():
 print(users[i])

for j in users.values():
 print(j)



# 3..............Palindrome number : WAP to accept a number and check for palindrome.

n=int(input("Accept a number: "))
temp=n
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
if(temp==rev):
    print("The number is a palindrome: ")
else:
    print("The number is not a palindrome: ")




# 4...........Factorial: WAP to print factorial of given number.

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




# 5.......... Prime Number: WAP to print first 100 Prime number.

print("Prime numbers between 1 and 100 are: ")
for num in range(2,101):
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print(num)

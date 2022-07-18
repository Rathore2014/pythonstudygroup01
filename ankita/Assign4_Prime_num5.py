# 5.......... Prime Number: WAP to print first 100 Prime number.

print("Prime numbers between 1 and 100 are: ")
for num in range(2,101):
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print(num)

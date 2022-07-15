number = int(input ("enter nmber"))
num = number
pali = 0 
while(number > 0):
    tmp = number % 10
    pali = pali * 10 + tmp
    number = number // 10   

if num == pali:
    print("Yes, it is palindrome")
else:
    print("Sorry, it's not a palindrome")

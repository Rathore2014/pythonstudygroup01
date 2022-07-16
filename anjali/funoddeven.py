def oddeven(num):
    if num % 2==0:
        res ="even"
    else :   
        res ="odd" 
    return res
num =int(input("enter anumber"))          
res = oddeven(num)
print(res)
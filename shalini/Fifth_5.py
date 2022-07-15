number = 1 
while(number <=100):
    tem = 0
    i = 2
    while(i <= number//2):
        if (number%i == 0):
            tem = tem+1
            break 
            i =i +1
        if (tem == 0 and number !=1):
            print("%d" %number,end =" ")
            number = number +1
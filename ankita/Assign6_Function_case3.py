# 3..........Count: Write a function that accepts a string and calculate the number of upper case
# letters and lower case letters, provide default value of string as a greeting message “Welcome
# To You in Python program.” 


def up_low():
    greet = " Welcome To You in Python program. " 
    count1 = 0
    count2 = 0
    for i in greet:
        if(i.islower()):
            count1 = count1+1
        elif(i.isupper()):
            count2 = count2+1
    return count1,count2     
res1,res2 = up_low()  
print("The number of lowercase characters is:",res1)
print("The number of uppercase characters is:",res2)

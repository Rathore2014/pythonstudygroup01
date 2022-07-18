#   2.......... Reverse: Write a function to reverse a given city name, prompt user to input city name,
# define function with one argument and return reverse of the city name.

def rev(s):
    s1 = ""
    for i in s:
        s1 = i + s1
    return s1
s = input("Enter the city name:  ")
print ("The original string city name  is : ",s)   
print ("The reversed string city name   is : ",rev(s))



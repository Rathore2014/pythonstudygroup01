# 3-2......... Greetings: Start with the list you used in Exercise 3-1,
#              but instead of just printing each users’s name, print a 
#              message to them. The text of each message should be the same, 
#              but each message should be personalized with the user’s name.
# Using List
girl = ["Rohini","Parwati","Lakshmi"]
print(f"The name of the Chandrma wife is: { girl[0]}")
print(f"The name of the Shiv wife is: { girl[1]}")
print(f"The name of the Vishnu wife is: { girl[2]}")
# Using Tuple
son = ("Ganesh","Narad","Kartik")
print(f"The name of the Shiv son is: { son[0]}")
print(f"The name of the Bharama son is: { son[1]}")
print(f"The name of the Parwati son is: { son[2]}")
# Using Dictionary
power = {
    "M":"Lakshmi",
    "K":"Sarswati",
    "P":"Durga"
}
print(power['M'])
print(power['K']) 
print(power['P'])
print(f"The Goddess of money is: { power['M']}")
print(f"The Goddess of knowledge is: { power['K']}")
print(f"The Goddess of power is: { power['P']}")

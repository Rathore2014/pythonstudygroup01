# 3-3......... Changing Users List: We just heard that one of the existing OV 
#              user is not valid anymore, so need to modify users.
#       Start with program from Exercise 3-2. Add a print() call at the end of
#       program stating the name of the user which is not valid any more.
#       Modify yours, replacing the name of the user which is not valid
#      any more with the name of the new user.
#       Print a second set of messages, one for each user which are still available.
# Using List
flower = ["Lotus","Rose","Lily"]
print(f"flower {flower[1]} is not valid")
flower[1] = "Hibicus"
print(f"Valid Flowers are { flower[0]}, {flower[1]} and {flower[2]}")
# Using Tuple
fruits = ("Apple","Banana","Orange")
print(f"fruits {fruits[2]} is not valid")
fruits = ("Apple","Banana","Mango")
print(f"Valid Fruits are { fruits[0]}, {fruits[1]} and {fruits[2]}")
# Using Dictionary
color = {
    "R":"Red",
    "G":"Green",
    "B":"Blue"
}
print(f"color {color['R']} is not valid ")
color['R'] = "RaniPink"
print(color['R']) 
print(color['G']) 
print(color['B']) 

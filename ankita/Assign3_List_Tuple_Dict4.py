 3-4......... More Users: We just found a request to create more users.
#             Start with the program from Exercise 3-3. 
#             Add a print() call to the end of program informing more users.
#       Use insert() to add one new user to the beginning of the list.
#       Use append() to add one new user to the end of the list.
#       Print new greeting messages for all existing users.
# Using List
from turtle import color


flower = ["Lotus","Rose","Lily"]
flower.insert(0, "Sunflower")
flower.append("Marigold")
print(flower)
# Using Tuple
fruits = ("Apple","Banana","Mango")
# insert and append is not held on Tuple.Because Tuple is immutable
fruits = ("Orange","Apple","Banana","Mango","Grapes")
print(fruits)
# Using dictionary
color = {
    "R":"Red",
    "G":"Green",
    "B":"Blue"
}
# Dictionary is unordered data, so append and insert invalid in case of dictionary.

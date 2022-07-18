# 3-5........ Shrinking User List: We just found out that few users are 
#             not valid any more, and we can have only two users.
#      Use pop() to remove users from the list one at a time until only
#     two names remain in the list. Each time pop a user from the list, print
#     a message confirming users removal.
#      Print a message to each of the two user still in the list, letting
#     them know they’re still available.
#      Use del to remove the last two users from the list, so you have
#     an empty list. Print your list to make sure you actually have an empty
#     list at the end of your program.

# Using List
flower = ['Sunflower', 'Lotus', 'Rose', 'Lily', 'Marigold']
flower.pop()
flower.pop()
print(flower)
del flower[0]
del flower[1]
print(flower)

# Tuple –
# A tuple is a sequence of immutable, so any edit operation is not valid, 
# we can re-initialize the user object with required data but pop and del 
# method cannot be used.

# Using Dictionary
# Dictionary is unordered data so pop method is not valid.
color = {
    "R":"Red",
    "G":"Green",
    "B":"Blue"
}
del color["R"]
del color["G"]
del color["B"]
print(color)

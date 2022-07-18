#   1.......... Sum: Write a function to sum all the numbers in a given list.
#             Note – No arguments, define variable inside the function an


def add():
    num = [1, 2, 3, 4, 5]
    total = 0
    for x in num:
       total += x
    return total   
print("Sum of the number in a list : ",add())

def sum():
    total = 0
    numbers = (8, 2, 3, 0, 7)
    for x in numbers:
        total += x
    return total
print(sum())


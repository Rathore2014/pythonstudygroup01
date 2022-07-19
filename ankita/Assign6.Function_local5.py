# 6-5. ...........Variables: Write a function to detect the number of local 
#                 variables declared in a function.


# 1 type
def scope():
   a = 25.5
   b = 5
   str_ = 'local'
print("Number of local varibales available:",scope.__code__.co_nlocals)


# 2 type
def empty():
   pass
def scope():
   a, b, c = 9, 23.4, True
   str = 'local'
print("Number of local varibales :",empty.__code__.co_nlocals)
print("Number of local varibales :",scope.__code__.co_nlocals)

class Cal():
    def init (self,a,b):
        self.a = a
        self.b = b
    def add(self):
        return a + b
    def sub(self):
        return a - b
    def multiply(self):
        return a * b
    def divide(self):
        return a / b
a = int(input("enter first number:  "))
b = int(input("enter second number:  "))
obj=Cal()
select = 1
while select != 0: 
    print(" 1.  +")
    print(" 2.  -")
    print(" 3.  *")
    print(" 4.  /")
    select = int(input ("select your choice:  "))
    if select == 1:
        print(obj.add())
    elif select == 2:
        print(obj.sub())
    elif select == 3:
        print(obj.multiply()) 
    elif select == 4:
        print(obj.divide())
    else:
        print("invalid option")     






























        
    
      





















            


        
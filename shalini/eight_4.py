class Cycle():
    def __init__(self,modelname,price,color):
        self.modelname = modelname
        self.price = price
        self.color = color 
    def cycle_details(self):
        print(f"the model of cycle is :",modelname)
        print(f"The price of cycle is :",price)
        print(f"The color of cycle:",color)
modelname = input("Enter maodel name")
price = int(input("Enter price"))
color = input("Enter color")    
obj =Cycle("modelname",price,color)
obj.cycle_details()
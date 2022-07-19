# 8.5 Bicycle
            # Create class bicycle, add as many data member and data method you can think of.
  
class Bicycle():
  def __init__(self,name,model,color,price):
    self.name = name
    self.model = model
    self.color = color
    self.price = price
  def Wheel(self,run,stop):
    self.run = run
    self.stop = stop
  def Pandel(self):
    print(f"run {self.run},stop {self.stop}")

b=Bicycle("bike",657,"blue",5487)
print(b.name)
print(b.model)
print(b.color)
print(b.price)
b.Wheel(" 1 km "," after break")
b.Pandel()

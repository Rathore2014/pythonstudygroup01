class Cycle() :
    def __init__ (self, name, model, cost,color):
        self.name = name
        self.model = model 
        self.cost = cost 
        self.color = color 
    def wheel (self, run, stop):
        self.run = run
        self.stop = stop
    def Break(self ):
        print(f"run(self.run) ,stop(self.stop)")
d=Cycle("alka" ,"atlas" ,3000 ,"black")
print(d.name)
print(d.model)
print(d.cost)
print(d.color)
d.wheel("before break" ,"after break")
d.Break()           
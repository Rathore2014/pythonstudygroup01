#student................
class Student () :
    def  __init__ (self, name, roll ,fathername) :
      self.name = name
      self.roll = roll
      self.fathername = fathername
    def  admission  (self,name,roll, age, fathername) :
        obj = Student(name, roll, age, fathername)
        mylist.append(obj) 
    def setage(self,age):
        if age < 4 :
         print("not eligible for admission: ")
        elif age > 20 :
         print("overage for admission")
        else :
              print("eligible for admission: ")
        self.age = age
    def details(self):
        print("student name is: " ,self.name)
        print("student roll number is: ",self.roll)
        print("student age is:" ,self.age) 
        print("student father name is: ",self.fathername)
mylist=[]                   
obj=Student("Alka",2, "uday")  
obj.setage(age = 12)            
obj.details()
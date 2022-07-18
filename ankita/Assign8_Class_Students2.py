# 8-2. Students: 
      #  User Story: As a consumer, I want to be able to maintain student records, So that I can make we
      # can maintain students admission system.
      #  Acceptance Criteria: school provide CBSE courses from play to 5 th , we should maintain
      # students records and should be able to query students records with name and father
      # name or some other combination.
      #  Assumptions: students age will be not less than 4 years and not more than 20 years.
class Student():
  def __init__(self,name,roll,fathername):
    self.name = name
    self.roll = roll
    self.fathername = fathername

  def addmission(self,Name, Roll, Age, Father_name):
    ob = Student(Name, Roll, Age, Father_name)
    mylist.append(ob)
  
  def setAge(self,age):
    if age < 4:
      print("You are underage: ") 
    elif age > 20:
      print("You are overage")
    else:
      print("Wel come to your new school ")
    self.age = age
    
  def setStd(self,std):
    self.std = std

  def Display(self):
    print("Student name is: ",self.name)
    print("Student roll number is: ",self.roll)
    print("Student fathername is: ",self.fathername)
    print("Student age is: ",self.age)
    print("Student class is: ",self.std)
mylist=[]
obj = Student("Ankita",1,"Uday")
obj.setAge(age = 14)
obj.setStd(4)
obj.Display()

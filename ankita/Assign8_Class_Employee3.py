# 8.3. Employee
            # Create class employee and maintain employee rank, salary and absence. Salary increase
            # max is 10% and leave can not be more than 5 days continuously, max leave in a year will
            # 12 days.
class Employees():
  rank = {
      "ram" : "1st",
      "shyam" : "2nd",
      "mohan" : "3rd"
    }

  def Rank(self):
    if self.rank["ram"] == "1st":
      print("Ram is number 1st rank in the office")
    else:
      print("Ram is number not 1st rank in the office")  
    if self.rank["shyam"] == "3nd":
      print("Shyam is number 2nd rank in the office")
    else:
      print("Shyam is number not 2nd rank in the office")
    if self.rank["mohan"] == "4rd":  
      print("Mohan is number 3rd rank in the office")
    else:
      print("Another is the 3rd  rank in the office")

  def Salary(self,check_employee): 
    Id = int(input("Enter Employee Id: "))
    if (check_employee(Id)) == False:
      print("Employee does not  exists")
    else:
      Increment = int(input("Enter increase in Salary"))  
      print("Increment  of salary successful")

  # def Leave(self):

obj = Employees()
test = obj.Rank()
def Display():
    print("Welcome to Employee Management Record")
    print("1. to Rank of Employee")
    print("2. to Salary of Employee ")
    print("3. to  Absence of Employee")
    print("4. to Display Employees")
    print("5. to Exit")
    ch = int(input("Enter your Choice "))
    if ch == 1:
        obj.Rank()  
    elif ch == 2:
        obj.Salary()
    elif ch == 3:
        obj.Absence()
    elif ch == 4:
        obj.Display()
    elif ch == 5:   
        exit(0)
    else:
        print("Invalid Choice")


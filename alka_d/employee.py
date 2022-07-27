class Employee():   
    count = 0
    def __init__(self ,name ,rank ,salary, absent ) :
        self.name = name
        self.rank = rank
        self.salary = salary
        self.absent = absent
        if self.absent > 5:
            self.absent = 'Not allowed to take  leave of more than 5 days as you are applying for {} days'.format(self.absent)
    def displayCount (self ) :
        print("number of employees in the organization are :" ,self.count)
    def displayEmp (self) :
        print("name of employee is :",self.name)
        print("rank of employee is :",self.rank)
        print("salary of employee is :",self.salary)
        print("absent  : ",self.absent)
a = Employee ("Alka" ,"Manager" ,70000,3)
b = Employee ("Ankita" ,"Teamleader",80000,6)
c = Employee ("shalini" ,"developer" ,60000,2)
a.displayCount()
print("employee detail is :")
a.displayEmp()
b.displayEmp()
c.displayEmp()









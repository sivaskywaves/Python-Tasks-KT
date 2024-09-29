#Task 1:

class Person:
    print("Person's Information")
    def __init__(self) -> None:

        self.name="Siva"
        self.age="24"
        self.gender="Male"
    def info (self):
       
       print("Name:",self.name)
       print("Age:",self.age)
       print("Gender:",self.gender)
       
    def updatedinfo(self):
           
           update_age=int(input("If you want to update the age press 1 else 2: "))
           if update_age==1:
            new_age=int(input("Enter the age to update: "))
            self.age=new_age
           else:
               print("It is shows previous information")
               
               
details=Person()        
details.info()
details.updatedinfo()
details.info()

#Task 2:

class Employees:
        def __init__(self) -> None:
             self.employees = {}
        
        def addemployee(self,name,employeeid):
               self.name=name
               self.employeeid=employeeid
               self.employees[self.name]=self.employeeid
               print(self.employees)
        
         #print(self.name,self.employeeid)
        

new_employee=Employees()

new_employee.addemployee("siva","2")
new_employee.addemployee("sankar","24")
new_employee.addemployee("samba","26")

#Task 3:

class Rectangle:

    def __init__(self) -> None:#Intialising the length and width of the rectangles
       
       length=int(input("Enter the length of Rectangle: "))
       width=int(input("Enter the width of Rectangle: "))
       self.length=length
       self.width=width

    def area(self):#Method to calculating the area
        print("The area of the rectange:",self.length*self.width)

newrectangle=Rectangle()

newrectangle.area()        
       
#Task 4:
class Salary:

    bonus=1500            #the bonus allocated to each employee

    def emp_salary(self):

        salary=int(input("Enter the salary of employee: "))
        self.salary=salary
        print("The Net salary of Employee is:",self.bonus+self.salary)

new_emp_salary=Salary()    

new_emp_salary.emp_salary()    
        
        


       




      
        
        
   
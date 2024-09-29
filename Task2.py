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
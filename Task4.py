class Salary:

    bonus=1500            #the bonus allocated to each employee

    def emp_salary(self):

        salary=int(input("Enter the salary of employee: "))
        self.salary=salary
        print("The Net salary of Employee is:",self.bonus+self.salary)

new_emp_salary=Salary()    

new_emp_salary.emp_salary()    
        
        


       
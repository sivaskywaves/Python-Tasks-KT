#Single inheritance

#Problem 1:

class Animal:
    def __init__(self,name):
        self.name=name
        print("Animal name: ",self.name)
    def speak(self):
            print("Animal sound: Bark")  
class Animal2(Animal):
    Animal.__init__
obj=Animal2("Dog")
Animal2.speak(obj) 

#Multiple inheritance

#Problem 2:
class Teacher():
   
   subject="Python"         

class Researcher():
 
    field="Information Technology"
     
                
class TeachingResearcher(Teacher,Researcher):
          
        def display(self):
                print("Subject                    : ",self.subject)
                print("  Field                    : ",self.field)
            
                      
obj=TeachingResearcher()
obj.display()

#Problem 3:
class Bird():
 species="""             Species:
                      Booted eagle
                      Black howk eagle
                      little eagle
                      Golden Eagle
"""
class Flyable:
    capability="Flying" 
    def fly(self): 
        return "They have capability of Flying"
class Eagle(Flyable,Bird):
    def display(self):
        print(self.species)
        print(self.fly())
        
    
        
obj=Eagle()   
Eagle.display(obj) 

#Multi level inheritance

#Problem 4:
class Person:
    name="Rakesh"
    age="40"
         
class Employee(Person):
    salary="30000"
    
        
class Manager(Employee):
    department="Police"
        
    def display(self):
        print("Name        : ",self.name)
        print("Age         : ",self.age)
        print("Salary      : ",self.salary)
        print("Department  : ",self.department)

        
obj=Manager()
obj.display()

#Hierarchical Inheritance
#Problem 5:

class Employee:
 name=input("Enter the name of the Employee:\n")
 salary=input("Enter the salary of the Employee:\n")
   
class Developer(Employee):
 programming_language=input("Enter the Programming language:\n")
 
  
class Manager(Employee):
 team_size=input("Enter the team size:\n")
 def __init__(self) -> None:
  print("Team size            : ",self.team_size)
class Intern(Developer):
 internship_duration=input("Enter the Internhip duration:\n")
 def display(self):
  print("Name                 : ",self.name) 
  print("Salary               : ",self.salary)
  print("Programming Language : ",self.programming_language)
  print("Internship Duration  : ",self.internship_duration)
obj1=Intern()
obj1.display() 
obj2=Manager() 

#Problem 6:
class Vehicle:
    brand=input("Enter the name of the Brand:\n")
    model=input("Enter the model:\n")

        
class Car(Vehicle):
    num_doors="4"
    def __init__(self) -> None:
        print("Brand               : ",self.brand)  
        print("Model               : ",self.model)
        print("Number of Doors     : ",self.num_doors)
class Bike(Vehicle):
    type="NS200"
    def __init__(self) -> None:
        print("Brand               : ",self.brand)  
        print("Model               : ",self.model)
        print("Type of the Vehicle : ",self.type)

c=Car()
b=Bike()

#Basic Inheritance

#Problem 7:

class Device:
    name="Vivo"
class Phone( Device):
    phone_number="1122334455"
class Tablet(Device):
    screen_size="6 inches"
class Smartphone(Phone,Tablet):
    os="Android 15"
    def __init__(self) -> None:
        print("Name of the brand: ",self.name)
        print("Phone number     : ",self.phone_number)
        print("Screen size      : ",self.screen_size)
        print("os               : ",self.os)

s=Smartphone()



#Problem 7:


class Person:
    name="Samba"
    age="30"
     
class Student(Person):
    grade="A" 
    def __init__(self) -> None:
       print("Name : ",self.name)
       print("Age  : ",self.age)
       print("Grade: ",self.grade)
s=Student()   
 
  


        


    

      
        


        
               

                


    


   

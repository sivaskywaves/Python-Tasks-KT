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
            new_age=int(input("Enter to update the age: "))
            self.age=new_age
           else:
               print("It is shows previous information")
               
               
details=Person()        
details.info()
details.updatedinfo()
details.info()



      
        
        
   
""""
Task 1:
Create a class Vehicle with attributes brand and year. 
The class should have a method get_info() that returns the brand and year of the vehicle. 
Then, create two subclasses:

Car, which adds an attribute number_of_doors.
Motorcycle, which adds an attribute has_sidecar.
Both subclasses should override the get_info() method to include their respective additional attributes in the returned string.

"""
class Vehicle:                                     #Super class is created

 Brand=input("Enter the brand name:\n")            #Taking the input from the user
 Model=input("Enter the model     :\n")
        
def get_info(self):                                #It is a base class method 
    print("Brand: ",self.Brand)
    print("Model: ",self.Model)
class Car(Vehicle):                                #If we want to method overriding, the class will be inherited from the super class
    
 num_of_doors=input("Enter the No.of doors for the car:\n")

 def get_info(self):                               #Create a same method name as super class method and added the extra property
    print("Brand                  : ",self.Brand)
    print("Model                  : ",self.Model)
    print("No.of Doors of the car : ",self.num_of_doors)
class Bike(Vehicle):
    
 side_car=input("Is Bike having side car:\n")

 def get_info(self):
    print("Brand                  : ",self.Brand)
    print("Model                  : ",self.Model)
    print("Side Car               : ",self.side_car)    
c=Car()
c.get_info
b=Bike()
b.get_info()                          #The method will be overrided and child class method will called

"""
Task 2:
Define an abstract class Animal with an abstract method make_sound().
Then, create three classes that inherit from Animal:

Dog with the sound "Woof".
Cat with the sound "Meow".
Cow with the sound "Moo".
Create a function play_sound(animal) that takes an object of type Animal and calls its make_sound() method.

"""

from abc import ABC,abstractmethod    #Importing abc module for accessing Abstract Class and Method
class Animal(ABC):                    #Abstract class is created by passing parameter as ABC
    @abstractmethod                   #It is a method which is declared without implementation & Declared by using @abstract method decorator
    def make_sound(self):             #It is abstarct method
        pass
class Dog(Animal):                    #Inheritance 
    def make_sound(self):             #To execute abstract method, the abstract method will be defined as same name in sub class.
        return"Dog Sound  : Woof"
class Cat(Animal):
    def make_sound(self):
        return " Cat Sound : Meow"   
class Cow(Animal):
    def make_sound(self):
        return " Cow Sound : Moo"
d=Dog()

c=Cat()

C=Cow()

for obj in [d,c,C]:                  #Looping statement for execute the methods
    print(obj.make_sound())


"""
Task 3:
Create an abstract class BankAccount with methods deposit(), withdraw(), and get_balance(). Then, create two subclasses:

SavingsAccount, where the withdraw() method ensures that the balance cannot go below $500.
CurrentAccount, where the withdraw() method allows the balance to go negative (up to $1000 overdraft).
Ensure that only deposit() and withdraw() are exposed to the user, and the balance is encapsulated (hidden).

"""
class BankAccount(ABC): 
    balance=100                   #Abstract class is created by passing parameter as ABC
    @abstractmethod                   #It is a method which is declared without implementation & Declared by using @abstract method decorator
    def deposit(self):             #It is abstarct method
        pass
    @abstractmethod
    def withdraw(self):
        pass
    @abstractmethod
    def get_balance(self):
        pass
class SavingsAccount(BankAccount):
    def deposit(self):                            #Implementation for adding deposit balance
        amount=int(input("Enter the deposit amount for the Savings account:\n"))
        self.amount=amount
        self.balance+=amount
    def withdraw(self):
        w_amount=int(input("Enter the withdrawl amount for the Savings account:\n"))
        self.w_amount=w_amount
        min_amount=500
        self.min_amount=min_amount
        a_balance=self.balance-self.w_amount
        if (self.balance>=w_amount):            #Condition for withdrawl amount doesn't exceed balance amount

         if (self.balance<=min_amount):           #Condition minimum amount should be maintained 
         
            print( "Min balance required: 500")
         else:
           self.balance-=w_amount  
        else:
           print("Enter the Correct amount")
    
          
    def get_balance(self):
       pass
class CurrentAccount(BankAccount):
   def deposit(self):                 
        amount=int(input("Enter the deposit amount for the Current account:\n"))
        self.amount=amount
        self.balance+=amount
   def withdraw(self):
        w_amount=int(input("Enter the withdrawl amount for the Current account:\n"))
        self.w_amount=w_amount
        min_amount=-1000
        self.min_amount=min_amount
        a_balance=self.balance-self.w_amount
        if (self.balance>=w_amount):

         if (a_balance<min_amount):
         
          return("Min balance required :-1000")
         else:
          self.balance-=w_amount 
        else:
         print("Enter the Correct amount") 
         
   def get_balance(self):
       pass
s=SavingsAccount() 
s.deposit()
s.withdraw()
s.get_balance()  
c=CurrentAccount()
c.deposit()
c.withdraw()
c.get_balance
# for obj in [s,c]:
#    print(obj.deposit())
#    print(obj.withdraw())
#    print(obj.get_balance())


"""
Task 4:
Create a base class Employee with attributes name and salary, and methods get_details() and get_salary(). 
Then create two subclasses:

Manager, which adds an attribute department.
Developer, which adds an attribute programming_language.
Both subclasses should override the get_details() method to include their respective additional attributes in the returned string.

Add a method increase_salary(percent) in the Employee class that increases the salary by a given percentage.

"""
class Employee:
    name   =input("Enter the name of the employee:\n")
    salary =int(input("Enter the salary of the employee:\n"))
    def get_details(self):
        print("Name  : ",self.name)
    def get_salary(self):
        print("Salary: ",self.salary)
    def increase_salary(self):
        global increased_salary
        increased_salary=int(input("Enter the salary increment in percentage to the employee:\n"))
        increased_salary=self.salary+(self.salary*(increased_salary/100))
        print("Updated salary: ",increased_salary)     
class Manager(Employee):
    
    def get_details(self):
        department=input("Enter the dept:\n")
        self.department=department
        print("Name                : ",self.name)
        print("Salary              : ",self.salary)
        print("Department          : ",self.department)
class Developer(Employee):

    def get_details(self):
     programming_language=input("Enter the type of the programming language:\n")
     self.programming_language=programming_language
     print("Name                : ",self.name)
     print("Salary              : ",self.salary)
     print("Programming Language: ",self.programming_language)
 
    def get_details_updated(self):
     programming_language=input("Enter the type of the programming language:\n")
     self.programming_language=programming_language
     print("Name                : ",self.name)
     print("Salary              : ",increased_salary)
     print("Programming Language: ",self.programming_language)
     print("Updated salary      : ",increased_salary)
# m=Manager()
# m.get_details()    
e=Employee()
# e.increase_salary()
d=Developer()
d.get_details()
# d.get_details_updated()

""""
Task 5:
Create an abstract class Media with an abstract method play(). Then create the following subclasses:

Audio, which plays a .mp3 file.
Video, which plays a .mp4 file.
LiveStream, which plays a live stream.
Implement a function start_media(media) that takes an object of type Media and calls its play() method.
Demonstrate polymorphism by passing different types of media to this function.

"""
      
class Media(ABC):                     #By passing the ABC parameter in the class mrthod to declare the abstract class 
 @abstractmethod                      #Declaring the abstract method using by adding decorator "@Abstractmethod"
 def play(self):                
    pass

class Audio(Media):                   # in each subclass abstract method should be defined for execute without error
  def play(self):
    print("Plays .mp3 file")
class Video(Media):
  def play(self):
    print("Plays .mp4 file")
class Livestream(Media):
  def play(self):
    print("Plays Livestream")
  def start_media(self):             # Method for the selecting the type of media to play
   files="""
    1: Audio file
    2: Video file
    3: Livestream
     """
   print(files)
   play=int(input("Choose the file to play(.mp3,.mp4,.livestream):\n"))
   if play==1:
    return Audio.play(self)
   if play==2:
    return Video.play(self)
   if play==3:
    return Livestream.play(self)

a=Audio()
v=Video()
l=Livestream()
l.start_media()
"""
Task 6:
Create an abstract class LibraryItem with abstract methods borrow() and return_item(). Then create two subclasses:

Book, with attributes title, author, and num_copies.
DVD, with attributes title, director, and duration.
Implement a function borrow_item(item) that borrows the library item and decreases the number of available copies (for books) or marks the DVD as borrowed.


"""
class LibraryItem(ABC):
    @abstractmethod
    def borrow(self):
        pass
    @abstractmethod
    def return_item():
        pass
class Book(LibraryItem):
    def __init__(self) -> None:
       
     self.title=input("Enter the title of the book:\n")
     self.author=input("Enter the author of the book:\n")
     self.num_copies=int(input("Enter the no.of books available:\n"))
    def borrow(self):
     b_borrow=int(input("Enter to borrow the no.of books:\n"))
     self.available_copies=self.num_copies-b_borrow
    def return_item(self):
        print("Available copies: ",self.available_copies)

class DVD(LibraryItem):
    def __init__(self) -> None:
     self.title=input("Enter the title of the DVD:\n")
     self.director=input("Enter the Director of the DVD:\n")
     self.duration=input("Enter the Duration:\n")
    def borrow(self):
     self.b_borrow=int(input("You want to borrow DVD press 1:\n"))
    def return_item(self):
       if (self.b_borrow==1):
          print( "The DVD as borrowed")
       
# b=Book()     
# b.borrow()
# b.return_item
d=DVD()
d.borrow()
d.return_item()

        



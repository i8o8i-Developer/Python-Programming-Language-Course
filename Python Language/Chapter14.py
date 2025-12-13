# Chapter 14: Object-Oriented Programming - Advanced

"""
TABLE OF CONTENTS:
1. Class Methods (@classmethod)
   - Bound To Class, Not Instance
   - Accessing Class Variables
2. Property Decorator (@property)
   - Getter Methods
   - Setter Methods
   - Deleter Methods
   - Encapsulation
3. Static Methods (@staticmethod)
4. Advanced OOP Concepts
"""

# ========================================
# CLASS METHODS
# ========================================

# Class Method

class Test:
    H = "Anubhav"
    @classmethod
    def Info(cls):
        return cls.H

Hello = Test.Info()
# Used To Bound With Class Not Obj

# -------------------------------------------
'Property Decorater'

class Employee:
    def __init__(self,Name,Salary,Language):
        self.Name = Name
        self.Salary = Salary
        self.Language = Language
        # self.Email = f"{Name}@gmail.com"
    def Info(self):
        return f"The Name Is {self.Name} And The Salary Is {self.Salary} And The Language Is {self.Language}"
    @property
    def Email(self):
        return f"{self.Name}@gmail.com"

Anubhav = Employee("Anubhav",1200000,"Hindi")
print(Anubhav.Info())
print(Anubhav.Email)
Anubhav.Name = "Harry"
print(Anubhav.Email)

# Used For Directly Printing ( Not By Calling It )
# Anubhav.Email Instead Of Anubhav.Email()

'-----------------------------Setter-----------------------------------'
# Used For Changing Other Value For Given Data

class Employee:
    def __init__(self,Name,Salary,Language):
        self.Name = Name
        self.Salary = Salary
        self.Language = Language
        # self.Email = f"{Name}@gmail.com"
    def Info(self):
        return f"The Name Is {self.Name} And The Salary Is {self.Salary} And The Language Is {self.Language}"
    @property
    def Email(self):
        return f"{self.Name}@gmail.com"
    @Email.setter
    def Email(self,Email):
        self.Name = Email.split('@')[0]

Anubhav = Employee("Anubhav",1200000,"Hindi")
print(Anubhav.Info())
print(Anubhav.Email)
Anubhav.Email = "Asha@gmail.com"
print(Anubhav.Info())
print(Anubhav.Email)

# By Taking Email It Will Change The Name Variable 

'------------------------------Deleter Decorater --------------------------------'

class Employee:
    def __init__(self,Name,Salary,Language):
        self.Name = Name
        self.Salary = Salary
        self.Language = Language
        # self.Email = f"{Name}@gmail.com"
    def Info(self):
        return f"The Name Is {self.Name} And The Salary Is {self.Salary} And The Language Is {self.Language}"
    @property
    def Email(self):
        if self.Name == None:
            return "Email Not Found"
        return f"{self.Name}@gmail.com"
    @Email.setter
    def Email(self,Email):
        self.Name = Email.split('@')[0]
    @Email.deleter
    def Email(self):
        self.Name = None


Anubhav = Employee("Anubhav",1200000,"Hindi")
print(Anubhav.Info())
print(Anubhav.Email)
Anubhav.Email = "Asha@gmail.com"
print(Anubhav.Info())
print(Anubhav.Email)
# Deleting Email
del Anubhav.Email
print(Anubhav.Email)

# Abstract Base Classes
"""
Abstract Classes Define Methods That Must Be Implemented By Subclasses.
They Cannot Be Instantiated Directly.
Use abc Module For Abstract Classes.
"""

from abc import ABC, abstractmethod

class Shape(ABC):  # Abstract Class
    @abstractmethod
    def area(self):
        pass  # Must Be Implemented By Subclasses
    
    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14 * self.radius

# shape = Shape()  # TypeError: Can't Instantiate Abstract Class
rect = Rectangle(10, 5)
print(f"Rectangle Area: {rect.area()}, Perimeter: {rect.perimeter()}")

circle = Circle(7)
print(f"Circle Area: {circle.area()}, Perimeter: {circle.perimeter()}")

print("\nAbstract Classes Ensure Subclasses Implement Required Methods.")
print(Anubhav.Email)
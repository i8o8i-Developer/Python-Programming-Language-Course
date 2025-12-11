# ╔═══════════════════════════════════════════════════════════════╗
# ║              CHAPTER 13: OOP - INHERITANCE                    ║
# ╠═══════════════════════════════════════════════════════════════╣
# ║                                                               ║
# ║  TABLE OF CONTENTS:                                           ║
# ║  ═════════════════                                            ║
# ║                                                               ║
# ║  1. Inheritance Fundamentals                                  ║
# ║  2. Single Inheritance (Parent -> Child)                      ║
# ║  3. Multiple Inheritance (Multiple Parents)                   ║
# ║  4. Multilevel Inheritance (Chain Of Inheritance)             ║
# ║  5. Method Overriding (Polymorphism)                          ║
# ║  6. Super() Function                                          ║
# ║  7. MRO (Method Resolution Order)                             ║
# ║                                                               ║
# ╚═══════════════════════════════════════════════════════════════╝

"""
╔════════════════════════════════════════════════════════╗
║           INHERITANCE HIERARCHY DIAGRAM                ║
╠════════════════════════════════════════════════════════╣
║                                                        ║
║              ┌──────────────┐                          ║
║              │    PARENT    │  (Base Class)            ║
║              │  Attributes  │                          ║
║              │  Methods     │                          ║
║              └──────┬───────┘                          ║
║                     │                                  ║
║                     ↓  Inherits                        ║
║                     │                                  ║
║              ┌──────▼───────┐                          ║
║              │    CHILD     │  (Derived Class)         ║
║              │  + Own Attrs │                          ║
║              │  + Override  │                          ║
║              └──────────────┘                          ║
║                                                        ║
╚════════════════════════════════════════════════════════╝
"""


# ═══════════════════════════════════════════════════════════════
#  TOPIC 1: Inheritance Fundamentals
# ═══════════════════════════════════════════════════════════════

# Inheritance 

' Used To Create New Class From Existing Class '


# ═══════════════════════════════════════════════════════════════
#  TOPIC 2: Single Inheritance
# ═══════════════════════════════════════════════════════════════

# -------------------Synatax--------------------

# Parent Class
class ProgrammerLang:
    Language = "Python"
    def PrintLang(self):
        return (f"Language : {self.Language}")

# Child Class
class Programmer(ProgrammerLang):
    def __init__(self , Name):
        self.Name = Name
    def Info(self):
        return f"Name : {self.Name}"
        
MainData = Programmer("Anubhav")
H = f"{MainData.Info()}\n"
J = f"{MainData.PrintLang()}"

# ------------------------------------------END


# ═══════════════════════════════════════════════════════════════
#  TOPIC 3: Multiple Inheritance
# ═══════════════════════════════════════════════════════════════

"Multiple Inheritance"

class CoderAge:
    Age = 21
    def CoderInfo0(self):
        return f"Your Age : {self.Age}"

class CoderLang:
    Language = "Python"
    def CoderInfo(self):
        return f"Your Programming Lang : {self.Language}"
    
class Coder(CoderAge , CoderLang):
    def __init__(self , Name):
        self.Name = Name
    def Info(self):
        return f"Name : {self.Name}"

MainData = Coder("Anubhav")
H = f"{MainData.Info()}\n"
K = f"{MainData.CoderInfo0()}\n"
J = f"{MainData.CoderInfo()}"

# ------------------------------------------END


# ═══════════════════════════════════════════════════════════════
#  TOPIC 4: Polymorphism (Method Overriding)
# ═══════════════════════════════════════════════════════════════

# Polymorphism: Method Overriding
"""
Polymorphism Allows Different Classes To Have Methods With The Same Name But Different Behavior.
Method Overriding: Subclass Provides Specific Implementation Of A Method From Parent Class.
"""

class Animal:
    def speak(self):
        return "Animal Makes A Sound"

class Dog(Animal):
    def speak(self):  # Override Parent Method
        return "Woof!"

class Cat(Animal):
    def speak(self):  # Override Parent Method
        return "Meow!"

animals = [Dog(), Cat(), Animal()]
for animal in animals:
    print(f"{animal.__class__.__name__}: {animal.speak()}")

# Method Resolution Order (MRO) In Multiple Inheritance
"""
MRO Determines The Order In Which Base Classes Are Searched For Methods.
Use mro() Or __mro__ To See The Order.
"""

class A:
    def method(self):
        return "A"

class B(A):
    def method(self):
        return "B"

class C(A):
    def method(self):
        return "C"

class D(B, C):  # Multiple Inheritance
    pass

d = D()
print("MRO:", [cls.__name__ for cls in D.__mro__])
print("Method Call:", d.method())  # B (First In MRO)

# Composition: "Has-A" Relationship
"""
Composition Is When A Class Contains Objects Of Other Classes.
Preferred Over Multiple Inheritance For Complex Relationships.
"""

class Engine:
    def start(self):
        return "Engine Started"

class Wheels:
    def rotate(self):
        return "Wheels Rotating"

class Car:
    def __init__(self):
        self.engine = Engine()  # Composition
        self.wheels = Wheels()  # Composition
    
    def drive(self):
        return f"{self.engine.start()} And {self.wheels.rotate()}"

my_car = Car()
print("Driving:", my_car.drive())

print("\nInheritance Creates 'Is-A' Relationships, Composition Creates 'Has-A' Relationships.")

# MultiLevel Inheritance
class CoderAge:
    Age = 21
    def CoderInfo0(self):
        return f"Your Age : {self.Age}"
    
class CoderLang(CoderAge):
    Language = "Python"
    def CoderInfo(self):
        return f"Your Programming Lang : {self.Language}"

class Coder(CoderLang):
    def __init__(self , Name):
        self.Name = Name
    def Info(self):
        return f"Name : {self.Name}"

Obj = Coder("Anubhav")
H = f"{Obj.Info()}\n"
K = f"{Obj.CoderInfo0()}\n"
J = f"{Obj.CoderInfo()}"

# ------------------------------------------END

# SUPER() Method

class Super:
    def __init__(self , Name):
        self.Name = Name

class Use(Super):
    def __init__(self , Name):
        super().__init__(Name)
    def Info(self):
        return f"Name : {self.Name}"
    
Obj = Use("Anubhav")
H = f"{Obj.Info()}"


class WithoutArgument:
    def __init__(self):
        print("Hello")

class Use(WithoutArgument):
    def __init__(self):
        super().__init__()
        print("Test Done")

Obj = Use()
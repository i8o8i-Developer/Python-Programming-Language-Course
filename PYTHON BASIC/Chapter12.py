# ╔═══════════════════════════════════════════════════════════════╗
# ║         CHAPTER 12: OBJECT-ORIENTED PROGRAMMING (OOP)         ║
# ╠═══════════════════════════════════════════════════════════════╣
# ║                                                               ║
# ║  TABLE OF CONTENTS:                                           ║
# ║  ═════════════════                                            ║
# ║                                                               ║
# ║  1. OOP Fundamentals (DRY Principle)                          ║
# ║  2. Classes And Objects                                       ║
# ║  3. Attributes (Class Vs Instance)                            ║
# ║  4. Methods And Self Parameter                                ║
# ║  5. Static Methods (@staticmethod)                            ║
# ║  6. __init__ Constructor                                      ║
# ║  7. Encapsulation (Private Attributes)                        ║
# ║                                                               ║
# ╚═══════════════════════════════════════════════════════════════╝

"""
╔════════════════════════════════════════════════════════╗
║              OOP CORE CONCEPTS                         ║
╠════════════════════════════════════════════════════════╣
║                                                        ║
║         ┌──────────────┐                               ║
║         │    CLASS     │   Blueprint/Template          ║
║         │              │                               ║
║         │  Attributes  │   Data/Properties             ║
║         │  Methods     │   Functions/Behaviors         ║
║         └──────┬───────┘                               ║
║                │                                       ║
║                ├──> Object 1 (Instance)                ║
║                ├──> Object 2 (Instance)                ║
║                └──> Object 3 (Instance)                ║
║                                                        ║
╚════════════════════════════════════════════════════════╝
"""


# ═══════════════════════════════════════════════════════════════
#  TOPIC 1: OOP Fundamentals
# ═══════════════════════════════════════════════════════════════

# Object Oriented Programming ( DRY Principle )
'''
Class # BluePrint For Creating Objects
Object # Instantation Of A Class
Attribute
Method
Instance
'''


# ═══════════════════════════════════════════════════════════════
#  TOPIC 2: Classes And Objects
# ═══════════════════════════════════════════════════════════════

# Class  
 
class Employee:
    Name = "Anubhav"
    Language = "Hindi"
    Salary = 1200000

# Object ( Anubhav )
Anubhav = Employee()
H = Anubhav.Name , Anubhav.Salary , Anubhav.Language
print(H)

# Class Attribute ( Salary , Language ) & " Instance Attribute Is ( Name ) "
Asha = Employee()
Asha.Name = "Asha" # Changing Instance Attribute
H = Asha.Name , Asha.Salary , Asha.Language
print(H)

# Self Parameter
class Employee:
    Language = "Hindi"
    Salary = 1200000
    def TestPara(self):
        print(f"The Language Is {self.Language}")
    # It Compulsory To Create Self In Methods

Test = Employee()
# Self Parameter
Test.TestPara() # Or Employee.TestPara(Test)

# Static Method 
class Employee:
    Language = "Hindi"
    Salary = 1200000
    def TestPara(self):
        print(f"The Language Is {self.Language}")
    @staticmethod
    def TestPara2():
        print("The Salary Is 1200000")

Test = Employee()
Test.TestPara()
Test.TestPara2()

# Encapsulation: Private Attributes And Methods
"""
Encapsulation Hides Internal Details Of A Class.
Use Double Underscore (__) To Make Attributes Private.
Private Attributes Can't Be Accessed Directly From Outside The Class.
"""

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner  # Public Attribute
        self.__balance = balance  # Private Attribute
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New Balance: {self.__balance}")
        else:
            print("Invalid Amount")
    
    def get_balance(self):
        return self.__balance  # Access Private Attribute Via Method
    
    def __private_method(self):
        print("This Is A Private Method")

account = BankAccount("Anubhav", 1000)
print("Owner:", account.owner)  # Public
print("Balance:", account.get_balance())  # Via Method
account.deposit(500)
# print(account.__balance)  # AttributeError: Private
# account.__private_method()  # AttributeError: Private

# Name Mangling: Python Changes __var To _ClassName__var
print("Mangled Name:", account._BankAccount__balance)  # Access Private (Not Recommended)

print("\nEncapsulation Protects Data And Hides Implementation Details.")

# __init__() Constructer
'Special Method Which is First Run As Soon As The Object Is Created'
class Employee:
    Language = "Hindi"
    def __init__(self): # Executed It Self When A Object Is Created
        print("Anubhav")
    def TestPara(self):
        print(f"The Language Is {self.Language}")
    @staticmethod
    def TestPara2():
        print("The Salary Is 1200000")

Test = Employee()
Test.TestPara2()
Test.TestPara()

# __del__() Destructer
'Special Method Which is Last Run As Soon As The Object Is Deleted'
class Employee:
    Language = "Hindi"
    def __init__(self): # Executed It Self When A Object Is Created
        print("Anubhav")
    def TestPara(self):
        print(f"The Language Is {self.Language}")
    @staticmethod
    def TestPara2():
        print("The Salary Is 1200000")
    def __del__(self): # Executed It Self When A Object Is Deleted
        print("Class Deleted")

Test = Employee()
Test.TestPara2()
Test.TestPara()
# Test = Object Is Deleted

'----------------------'

# Another __init__ 
class Employee:
    def __init__(self, Name, Age , Language): # Executed It Self When A Object Is Created
        self.Name = Name
        self.Age = Age
        self.Language = Language
    def TestPara(self):
        print(f"The Language Is {self.Language}")
    @staticmethod
    def TestPara2():
        print("The Salary Is 1200000")

Test = Employee("Anubhav",12,"Python")
Test.TestPara2()
Test.TestPara()
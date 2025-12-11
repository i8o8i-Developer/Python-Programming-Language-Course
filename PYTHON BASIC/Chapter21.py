# ╔═══════════════════════════════════════════════════════════════╗
# ║              CHAPTER 21: MODULES AND PACKAGES                 ║
# ╠═══════════════════════════════════════════════════════════════╣
# ║                                                               ║
# ║  TABLE OF CONTENTS:                                           ║
# ║  ═════════════════                                            ║
# ║                                                               ║
# ║  1. What Are Modules?                                         ║
# ║  2. Importing Modules                                         ║
# ║     - import module                                           ║
# ║     - import module as alias                                  ║
# ║     - from module import item                                 ║
# ║                                                               ║
# ║  3. __name__ Variable                                         ║
# ║     - __name__ == "__main__"                                  ║
# ║                                                               ║
# ║  4. Packages                                                  ║
# ║     - Directory Structure                                     ║
# ║     - __init__.py File                                        ║
# ║     - Subpackages                                             ║
# ║                                                               ║
# ║  5. Standard Library Packages                                 ║
# ║  6. Reloading Modules (importlib)                             ║
# ║  7. sys.path And Module Search                                ║
# ║                                                               ║
# ╚═══════════════════════════════════════════════════════════════╝

# Chapter 21: Modules And Packages
"""
Modules And Packages In Python

Modules Are Files Containing Python Code (Functions, Classes, Variables) That Can Be Imported And Reused.
Packages Are Directories Containing Multiple Modules, Organized For Better Structure.

How It Works:
- Python Searches For Modules In sys.path (Includes Current Directory, Installed Packages, etc.)
- Use 'import' To Load Modules
- Modules Are Executed Only Once When First Imported
- Use 'from module import item' For Specific Imports
- Packages Use __init__.py To Mark Directories As Packages
"""

# Importing Built-In Modules
import math
print("Math Module Imported. Pi:", math.pi)

# Importing With Alias
import random as rand
print("Random Number:", rand.randint(1, 10))

# Importing Specific Items
from datetime import datetime
print("Current Time:", datetime.now())


# __name__ Variable
"""
When A Module Is Run Directly : __name__ == "__main__"
When Imported : __name__ == "module_name"
This Allows Code To Run Only When The File Is Executed Directly.
"""
if __name__ == "__main__":
    print("This Code Runs Only When Chapter21.py Is Executed Directly")
    print("Not When Imported As A Module")

# Packages Example
"""
Create A Directory Structure Like:
MyPackage/
    __init__.py  # Makes It A Package
    Module1.py
    Module2.py
    SubPackage/
        __init__.py
        SubModule.py

Then import Like:
from MyPackage import Module1
from MyPackage.SubPackage import SubModule
"""

# Standard Library Packages
import os.path  # SubModule Of Os
print("Path Exists:", os.path.exists("Chapter21.py"))

# Reloading Modules (For Development)
import importlib
# importlib.reload(Module_Name)  # Use If You Modify A Module During Runtime

# Scopes In Python
"""
Scopes Define Where Variables Are Accessible.
- Local Scope: Inside A Function
- Enclosing Scope: In Nested Functions
- Global Scope: Module Level
- Built-In Scope: Python Built-Ins
"""

# Global Variable
global_var = "I'm global"

def outer_function():
    # Enclosing Variable
    enclosing_var = "I'm enclosing"
    
    def inner_function():
        # Local Variable
        local_var = "I'm local"
        print("Local:", local_var)
        print("Enclosing:", enclosing_var)
        print("Global:", global_var)
    
    inner_function()

outer_function()

# Modifying Global From Function
def modify_global():
    global global_var
    global_var = "Modified global"

modify_global()
print("Modified Global:", global_var)

# Closures
"""
Closures Are Functions That Remember Variables From Their Enclosing Scope Even After The Outer Function Has Finished.
"""

def make_multiplier(factor):
    """Returns A Function That Multiplies By Factor"""
    def multiplier(number):
        return number * factor  # Remembers 'factor' from enclosing scope
    return multiplier

double = make_multiplier(2)
triple = make_multiplier(3)

print("Double 5:", double(5))  # 10
print("Triple 5:", triple(5))  # 15

# Closures Are Useful For Callbacks, Factories, Etc.

# Membership Operators
"""
Membership Operators Check If An Item Is In A Sequence.
- in: True If Item Is Found
- not in: True If Item Is Not Found
"""

# Examples
numbers = [1, 2, 3, 4, 5]
print("3 in numbers:", 3 in numbers)  # True
print("6 in numbers:", 6 in numbers)  # False
print("6 not in numbers:", 6 not in numbers)  # True

string = "Hello World"
print("'H' in string:", 'H' in string)  # True
print("'z' in string:", 'z' in string)  # False

# Works With Dicts (Checks Keys), Sets, Tuples, Etc.
person = {"name": "Anubhav", "age": 21}
print("'name' in person:", 'name' in person)  # True
print("'city' in person:", 'city' in person)  # False

print("\nModules Allow Code Reuse, Organization, And Separation Of Concerns.")
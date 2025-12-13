# ╔═══════════════════════════════════════════════════════════════╗
# ║         CHAPTER 27: DEBUGGING AND BEST PRACTICES              ║
# ╠═══════════════════════════════════════════════════════════════╣
# ║                                                               ║
# ║  TABLE OF CONTENTS:                                           ║
# ║  ═════════════════                                            ║
# ║                                                               ║
# ║  1. Debugging Techniques                                      ║
# ║     - print() Debugging                                       ║
# ║     - Reading Error Messages                                  ║
# ║     - Common Mistakes (Indentation, Typos, Logic)             ║
# ║                                                               ║
# ║  2. Python Debugger (pdb)                                     ║
# ║     - pdb.set_trace() - Breakpoints                           ║
# ║     - Step-By-Step Execution                                  ║
# ║     - Inspecting Variables                                    ║
# ║                                                               ║
# ║  3. Best Practices                                            ║
# ║     - Meaningful Variable Names                               ║
# ║     - Single Responsibility Principle                         ║
# ║     - DRY (Don't Repeat Yourself)                             ║
# ║     - Code Comments And Documentation                         ║
# ║     - Proper Error Handling                                   ║
# ║     - Consistent Code Formatting                              ║
# ║                                                               ║
# ║  4. Code Quality Tips                                         ║
# ║     - Function Length                                         ║
# ║     - Type Hints                                              ║
# ║     - Testing Your Code                                       ║
# ║                                                               ║
# ╚═══════════════════════════════════════════════════════════════╝

# Chapter 27: Debugging And Best Practices
"""
Debugging Finds And Fixes Errors In Code.
Best Practices Make Code Readable, Maintainable, And Efficient.

How Debugging Works:
- Use print() Statements To Check Values
- Python Debugger (pdb) For Step-By-Step Execution
- Read Error Messages Carefully
- Check For Common Mistakes: Indentation, Typos, Logic Errors
"""

# Common Debugging Techniques
def Buggy_Function(x):
    # Bug: Will Fail If x Is Not Int
    return x * 2

# Debugging With Print
def Debug_Example():
    data = [1, 2, "Three", 4]
    Result = []
    for item in data:
        print(f"Processing: {item}, Type: {type(item)}")
        if isinstance(item, int):
            Result.append(Buggy_Function(item))
            print(f"Added: {item * 2}")
        else:
            print(f"Skipped Non-Int : {item}")
    return Result

print("Debug Output :")
Result = Debug_Example()
print("Final Result:", Result)

# Using pdb (Python Debugger)
# Uncomment Yo Use:
import pdb
pdb.set_trace()  # Add This Line Where You Want To Start Debugging

def Function_With_pdb():
    x = 5
    y = 10
    pdb.set_trace()  # Execution Pauses Here
    z = x + y
    return z

# Best Practices

# 1. Meaningful Variable Names
# Bad: a = 5, b = 10, c = a + b
# Good:
Total_Score = 5
Bonus_Points = 10
Final_Score = Total_Score + Bonus_Points

# 2. Functions Should Do One Thing
def Calculate_Area(length, width):
    """Calculate Rectangle Area"""
    return length * width

def Print_Area(length, width):
    """Print Formatted Area"""
    area = Calculate_Area(length, width)
    print(f"Area: {area} Square Units")

# 3. Use Constants For Magic Numbers
PI = 3.14159
MAX_USERS = 100

def Circle_Area(radius):
    return PI * radius ** 2

# 4. Error Handling
def Safe_Divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot Divide By Zero"
    except TypeError:
        return "Invalid Types"

# 5. Docstrings
def Greet_User(name):
    """
    Greet A User By Name.

    Args:
        name (str): The User's Name

    Returns:
        str: Greeting Message
    """
    return f"Hello, {name}!"

# 6. PEP 8 Style Guide
# - 4 Spaces Indentation (Not Tabs)
# - Lines < 79 Characters
# - snake_case For Variables/Functions
# - CamelCase For Classes
# - Meaningful Names
# - One Statement Per Line

# 7. Comments Explain WHY, Not WHAT
# Bad: x = x + 1  # Add 1 to x
# Good: x = x + 1  # Increment Counter For Next Iteration

# 8. DRY Principle (Don't Repeat Yourself)
# Bad: Repeated Code
# Good: Extract To Functions

def Validate_Age(age):
    """Validate Age Is Reasonable"""
    return 0 <= age <= 150

def Validate_Name(name):
    """Validate Name Is Not Empty"""
    return bool(name.strip())

# 9. Use list/dict Comprehensions For Simple Operations
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]  # Clean and Readable

# 10. Handle Edge Cases
def Get_First_Item(items):
    """Safely Get First Item From List"""
    if not items:
        return None
    return items[0]

# Common Python Mistakes To Avoid:
# - Mutable Default Arguments
# - Comparing With == vs Is
# - Forgetting To Handle Exceptions
# - Not Closing Files (Use 'With')
# - Using Global Variables Excessively

print("\nDebugging And Best Practices Lead To Better, More Reliable Code.")
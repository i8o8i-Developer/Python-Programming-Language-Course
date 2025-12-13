# Chapter 6: Conditional Statements And Ternary Operator

"""
TABLE OF CONTENTS:
1. If, Elif, Else Statements
   - Basic Conditional Logic
   - Multiple Conditions
2. Ternary Operator (Conditional Expression)
   - Basic Ternary Syntax
   - Nested Ternary
   - Ternary In List Comprehension
   - Ternary In Functions
   - Ternary With Multiple Conditions
   - Ternary In Dictionaries
   - Ternary For Default Values
   - When To Use Ternary
   - 20+ Practical Examples
"""

# ========================================
# CONDITIONAL STATEMENTS
# ========================================

# Conditional Statements 

"Syntax" # => If , Elif , Else 

# If Elif Else Ladder
Condition = "Hello"
Condition2 = "Anubhav"
if (Condition):
    print("True")
elif(Condition2):
    print("False")
else:
    print("False Or True")
# Uses Indentation 

# There Are Multiple Statements 


"""Ternary Operator (Conditional Expression)"""
print("\n--- Ternary Operator ---")

# Syntax: value_if_true if condition else value_if_false
# This Is A One-Line If-Else Statement

# Basic Example
age = 20
status = "Adult" if age >= 18 else "Minor"
print(f"Age: {age}, Status: {status}")

# Example 2: Finding Maximum
a = 10
b = 25
maximum = a if a > b else b
print(f"\nMaximum Of {a} And {b} : {maximum}")

# Example 3: Even Or Odd
number = 7
result = "Even" if number % 2 == 0 else "Odd"
print(f"\n{number} Is {result}")

# Example 4: Absolute Value
num = -15
absoluteValue = num if num >= 0 else -num
print(f"\nAbsolute Value Of {num} : {absoluteValue}")

# Example 5: Grade Assignment
score = 85
grade = "Pass" if score >= 50 else "Fail"
print(f"\nScore: {score}, Grade: {grade}")

# Nested Ternary Operators
print("\n--- Nested Ternary Operators ---")

# Example: Grade Based On Score
marks = 75
grade = "A" if marks >= 90 else "B" if marks >= 75 else "C" if marks >= 60 else "D" if marks >= 50 else "F"
print(f"Marks: {marks}, Grade: {grade}")

# Better Formatted For Readability
marks = 62
grade = (
    "A" if marks >= 90 else
    "B" if marks >= 75 else
    "C" if marks >= 60 else
    "D" if marks >= 50 else
    "F"
)
print(f"Marks: {marks}, Grade: {grade}")

# Example: Number Classification
num = 0
classification = "Positive" if num > 0 else "Negative" if num < 0 else "Zero"
print(f"\n{num} Is {classification}")

# Ternary In List Comprehension
print("\n--- Ternary In List Comprehension ---")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evenOdd = ["Even" if x % 2 == 0 else "Odd" for x in numbers]
print(f"Even/Odd List : {evenOdd}")

# Example: Replace Negative With Zero
values = [-5, 3, -2, 7, -1, 9]
positiveOnly = [x if x >= 0 else 0 for x in values]
print(f"\nOriginal : {values}")
print(f"Non-Negative : {positiveOnly}")

# Ternary In Function Return
print("\n--- Ternary In Functions ---")

def getDiscount(isMember):
    """Return Discount Based On Membership"""
    return 20 if isMember else 0

print(f"Member Discount : {getDiscount(True)}%")
print(f"Non-Member Discount : {getDiscount(False)}%")

def checkEligibility(age):
    """Check Voting Eligibility"""
    return "Eligible To Vote" if age >= 18 else "Not Eligible To Vote"

print(f"\nAge 20 : {checkEligibility(20)}")
print(f"Age 15 : {checkEligibility(15)}")

# Ternary With Multiple Conditions
print("\n--- Ternary With Multiple Conditions ---")

temperature = 25
weather = "Hot" if temperature > 30 else "Cold" if temperature < 15 else "Moderate"
print(f"Temperature: {temperature}°C, Weather: {weather}")

# Example: Weekend Or Weekday
day = "Saturday"
dayType = "Weekend" if day in ["Saturday", "Sunday"] else "Weekday"
print(f"\n{day} Is A {dayType}")

# Ternary In Dictionary
print("\n--- Ternary In Dictionary ---")
age = 22
person = {
    "name": "Anubhav",
    "age": age,
    "status": "Adult" if age >= 18 else "Minor"
}
print(f"Person : {person}")

# Ternary With Boolean
print("\n--- Ternary With Boolean ---")
isLoggedIn = True
message = "Welcome Back!" if isLoggedIn else "Please Log In"
print(f"Message : {message}")

# Example: Access Control
hasPermission = False
access = "Granted" if hasPermission else "Denied"
print(f"\nAccess : {access}")

# Ternary For Default Values
print("\n--- Ternary For Default Values ---")
userName = ""
displayName = userName if userName else "Guest"
print(f"Display Name : {displayName}")

userName = "Anubhav"
displayName = userName if userName else "Guest"
print(f"Display Name : {displayName}")

# Comparison: Regular If-Else Vs Ternary
print("\n--- Comparison ---")

# Regular If-Else
x = 10
if x > 5:
    result1 = "Greater"
else:
    result1 = "Smaller Or Equal"

# Ternary Operator (More Concise)
result2 = "Greater" if x > 5 else "Smaller Or Equal"

print(f"Regular If-Else Result : {result1}")
print(f"Ternary Operator Result : {result2}")

# When To Use Ternary Operator:
print("\n--- When To Use Ternary Operator ---")
print("Use Ternary When:")
print("  - Simple Condition With Two Outcomes")
print("  - Assigning Value Based On Condition")
print("  - Code Readability Is Not Compromised")
print("\nAvoid Ternary When:")
print("  - Complex Logic With Multiple Conditions")
print("  - Nested Ternaries Become Hard To Read")
print("  - Multiple Statements Need To Execute")

# Practical Examples
print("\n--- Practical Examples ---")

# Example 1: Price Calculation
price = 100
isMember = True
finalPrice = price * 0.8 if isMember else price
print(f"Final Price : ${finalPrice}")

# Example 2: String Formatting
count = 1
message = f"You have {count} item" if count == 1 else f"You have {count} items"
print(message)

count = 5
message = f"You have {count} item" if count == 1 else f"You have {count} items"
print(message)

# Example 3: Min/Max Without Built-In Functions
num1, num2 = 45, 78
minimum = num1 if num1 < num2 else num2
maximum = num1 if num1 > num2 else num2
print(f"\nMinimum : {minimum}, Maximum : {maximum}")

# Example 4: Sign Of Number
number = -42
sign = "+" if number > 0 else "-" if number < 0 else "0"
print(f"Sign Of {number} : {sign}")

# Example 5: Leap Year Check (Simplified)
year = 2024
isLeap = "Leap Year" if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) else "Not Leap Year"
print(f"\n{year} Is A {isLeap}")
 
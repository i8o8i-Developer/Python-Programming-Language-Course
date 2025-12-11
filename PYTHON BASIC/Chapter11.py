# ╔═══════════════════════════════════════════════════════════════╗
# ║              CHAPTER 11: EXCEPTION HANDLING                   ║
# ╠═══════════════════════════════════════════════════════════════╣
# ║                                                               ║
# ║  TABLE OF CONTENTS:                                           ║
# ║  ═════════════════                                            ║
# ║                                                               ║
# ║  1. Try-Except-Else-Finally Structure                         ║
# ║  2. Specific Exception Handling (ZeroDivisionError, etc.)     ║
# ║  3. Printing Exception Messages (Exception as e)              ║
# ║  4. Raising Exceptions (raise Keyword)                        ║
# ║  5. User-Defined Custom Exceptions                            ║
# ║  6. Multiple Except Blocks                                    ║
# ║  7. Best Practices For Exception Handling                     ║
# ║                                                               ║
# ╚═══════════════════════════════════════════════════════════════╝

"""
╔════════════════════════════════════════════════════════╗
║          TRY-EXCEPT-FINALLY FLOW DIAGRAM               ║
╠════════════════════════════════════════════════════════╣
║                                                        ║
║    Try Block                                           ║
║        │                                               ║
║        ├─ No Error ──> Else Block ──> Finally Block    ║
║        │                                               ║
║        └─ Error ──> Except Block ──> Finally Block     ║
║                                                        ║
╚════════════════════════════════════════════════════════╝
"""


# ═══════════════════════════════════════════════════════════════
#  TOPIC 1: Try-Except-Else-Finally Structure
# ═══════════════════════════════════════════════════════════════

"""Execption Handling"""

# Syntax Of try , except , else , finally  

try:
    print(10/5)
    # Code Containing Exceptions (Suspicious Code)
except ZeroDivisionError: # except [ExceptionName]
    print("Zero Division Error")
    # Code To Handle Exceptions
else: 
    print("Else Statement")
    # Code To Excute If No Exceptions Occured
finally:
    print("Finally Statement")
    # Code To Excute Always


# Priniting Exceptions
try:
    print(10/0)
    # Code Containing Exceptions (Suspicious Code)
except Exception as e: # except Exception as {YourVariable} 
    print(e)
    # Code To Handle Exceptions
else: 
    print("Else Statement")
    # Code To Excute If No Exceptions Occured
finally:
    print("Finally Statement")
    # Code To Excute Always


# Exception With Raise KeyWord
try:
    Age = int(input("Enter Your Age : "))
    if Age < 18:
        raise Exception
except Exception:
    print("Not Eligible For Voting")


# User Defined Exception
class VotingAgeError(Exception):
    pass
try:
    Age = int(input("Enter Your Age : "))
    if Age < 18:
        raise VotingAgeError
except VotingAgeError:
    print("Not Eligible For Voting")


# Multiple Exceptions
class VotingAgeError(Exception):
    pass
try:
    Age = int(input("Enter Your Age : "))
    if Age < 18:
        raise VotingAgeError
    elif Age > 60:
        raise Exception
except VotingAgeError:
    print("Not Eligible For Voting")
except Exception:
    print("Not Eligible For Voting & Above 60 Years")
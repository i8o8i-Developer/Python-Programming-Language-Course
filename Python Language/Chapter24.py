# ╔═══════════════════════════════════════════════════════════════╗
# ║                  CHAPTER 24: DECORATORS                       ║
# ╠═══════════════════════════════════════════════════════════════╣
# ║                                                               ║
# ║  TABLE OF CONTENTS:                                           ║
# ║  ═════════════════                                            ║
# ║                                                               ║
# ║  1. What Are Decorators?                                      ║
# ║  2. Basic Decorator Function                                  ║
# ║     - Wrapper Pattern                                         ║
# ║     - @decorator Syntax                                       ║
# ║                                                               ║
# ║  3. Common Decorators                                         ║
# ║     - Timing Decorator (Performance Measurement)              ║
# ║     - Logging Decorator                                       ║
# ║     - Caching Decorator                                       ║
# ║                                                               ║
# ║  4. Decorators With Parameters                                ║
# ║     - Decorator Factories                                     ║
# ║     - Configurable Decorators                                 ║
# ║                                                               ║
# ║  5. Class-Based Decorators                                    ║
# ║     - Using __call__ Method                                   ║
# ║                                                               ║
# ║  6. Built-in Decorators                                       ║
# ║     - @property                                               ║
# ║     - @staticmethod                                           ║
# ║     - @classmethod                                            ║
# ║                                                               ║
# ║  7. Preserving Metadata (@wraps)                              ║
# ║  8. Real-World Examples                                       ║
# ║                                                               ║
# ╚═══════════════════════════════════════════════════════════════╝

"""
╔════════════════════════════════════════════════════════╗
║              DECORATOR PATTERN                         ║
╠════════════════════════════════════════════════════════╣
║                                                        ║
║  @my_decorator                                         ║
║  def function():                                       ║
║      pass                                              ║
║                                                        ║
║  ≡  (Equivalent To)                                    ║
║                                                        ║
║  def function():                                       ║
║      pass                                              ║
║  function = my_decorator(function)                     ║
║                                                        ║
╚════════════════════════════════════════════════════════╝
"""

# Chapter 24: Decorators
"""
Decorators Are Functions That Modify Other Functions Or Classes.
They Allow Adding Functionality Without Changing The Original Code.

How It Works:
- Decorators Take A Function As Input And Return A Modified Function
- Use @decorator_name Syntax Above Function Definition
- Common Uses: Logging, Timing, Authentication, Caching
- Can Be Functions Or Classes
"""

from functools import wraps
import time

# Basic Decorator Function
def My_Decorator(Func):
    """Basic Decorator That Prints Before And After Function Call"""
    def Wrapper(*args, **kwargs):
        print(f"Calling {Func.__name__} With Args: {args}")
        result = Func(*args, **kwargs)
        print(f"{Func.__name__} Returned: {result}")
        return result
    return Wrapper

@My_Decorator
def Greet(Name):
    return f"Hello, {Name}!"

print(Greet("Anubhav"))

# Timing Decorator
def Timing_Decorator(Func):
    """Decorator To Measure Function Execution Time"""
    @wraps(Func)  # Preserves Original Function Metadata
    def Wrapper(*args, **kwargs):
        Start_Time = time.time()
        Result = Func(*args, **kwargs)
        End_Time = time.time()
        print(f"{Func.__name__} Took {End_Time - Start_Time:.4f} Seconds")
        return Result
    return Wrapper

@Timing_Decorator
def Slow_Function():
    time.sleep(1)
    return "Done!"

print(Slow_Function())

# Decorator With Parameters
def Repeat(Times):
    """Decorator Factory That Creates A Repeater Decorator"""
    def Decorator(Func):
        @wraps(Func)
        def Wrapper(*args, **kwargs):
            Results = []
            for _ in range(Times):
                Results.append(Func(*args, **kwargs))
            return Results
        return Wrapper
    return Decorator

@Repeat(3)
def Say_Hi():
    return "Hi!"

print(Say_Hi())  # Returns ["Hi!", "Hi!", "Hi!"]

# Class-Based Decorator
class CountCalls:
    """Class Decorator That Counts Function Calls"""
    def __init__(self, Func):
        self.Func = Func
        self.call_count = 0
        wraps(Func)(self)  # Apply Wraps

    def __call__(self, *args, **kwargs):
        self.call_count += 1
        print(f"Call {self.call_count} To {self.Func.__name__}")
        return self.Func(*args, **kwargs)

@CountCalls
def Add(a, b):
    return a + b

print(Add(1, 2))
print(Add(3, 4))

# Property Decorator (Already Seen In Chapter14)
# @property Makes A Method Act Like An Attribute

# Multiple Decorators (Applied Bottom-Up)
@Timing_Decorator
@My_Decorator
def Complex_Function(x):
    return x * 2

print(Complex_Function(5))

# Real-World Example: Authentication Decorator
def Requires_Auth(Func):
    @wraps(Func)
    def Wrapper(User, *args, **kwargs):
        if User.get('Authenticated', False):
            return Func(User, *args, **kwargs)
        else:
            return "Access Denied!"
    return Wrapper

@Requires_Auth
def Secret_Data(User):
    return "Top Secret Information"

User1 = {'name': 'Anubhav', 'Authenticated': True}
User2 = {'name': 'Guest', 'Authenticated': False}

print(Secret_Data(User1))
print(Secret_Data(User2))

print("\nDecorators Enable Clean, Reusable Code Modifications.")
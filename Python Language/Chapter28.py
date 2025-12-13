# Chapter 28: Advanced Python Topics And Leftover Concepts

"""
This Chapter Covers Important Python Topics That Were Not Covered In Previous Chapters:

TABLE OF CONTENTS:
1. Context Managers (with Statement)
2. Collections Module (Counter, defaultdict, deque, namedtuple, ChainMap)
3. Itertools Module
4. Functools Module (partial, lru_cache, reduce, wraps)
5. Data Classes (@dataclass)
6. Enum (Enumerations)
7. Pathlib (Modern File Paths)
8. Advanced *args And **kwargs
9. Global, Local, Nonlocal Scope
10. Set And Dict Comprehensions
11. Advanced String Formatting (F-strings)
12. Struct Module (Binary Data)
13. Array Module
14. Heapq Module (Priority Queue)
15. __slots__ (Memory Optimization)
16. Weak References
17. AsyncIO (Asynchronous Programming) - Comprehensive
18. Miscellaneous Topics (Ellipsis, Underscore, Identity, etc.)
"""


# ========================================
# 1. CONTEXT MANAGERS (WITH STATEMENT)
# ========================================
print("="*60)
print("1. CONTEXT MANAGERS (WITH STATEMENT)")
print("="*60)

print("""
Context Manager = Object That Defines Runtime Context
Used With 'with' Statement For Resource Management
Automatically Handles Setup And Cleanup
""")

# Basic File Context Manager
print("\n--- File Context Manager ---")
with open("OuputFolder/Text.txt", "w") as file:
    file.write("Hello World")
# File Automatically Closed After Block

print("File Written And Automatically Closed")

# Multiple Context Managers
print("\n--- Multiple Context Managers ---")
with open("OuputFolder/Text01.txt", "r") as input_file, open("OuputFolder/Output.txt", "w") as output_file:
    content = input_file.read()
    output_file.write(content.upper())
print("Multiple Files Handled Together")

# Creating Custom Context Manager (Class-Based)
print("\n--- Custom Context Manager (Class) ---")

class DatabaseConnection:
    """Simulate Database Connection"""
    
    def __init__(self, dbName):
        self.dbName = dbName
        self.isConnected = False
    
    def __enter__(self):
        """Called When Entering 'with' Block"""
        print(f"Connecting To Database: {self.dbName}")
        self.isConnected = True
        return self
    
    def __exit__(self, excType, excValue, excTraceback):
        """Called When Exiting 'with' Block"""
        print(f"Closing Database: {self.dbName}")
        self.isConnected = False
        # Return False To Propagate Exception, True To Suppress
        return False
    
    def query(self, sql):
        if self.isConnected:
            return f"Executing: {sql}"
        return "Not Connected"

# Using Custom Context Manager
with DatabaseConnection("MyDB") as db:
    print(db.query("SELECT * FROM users"))
# Connection Automatically Closed

# Context Manager With Decorator
print("\n--- Context Manager Using contextlib ---")

from contextlib import contextmanager

@contextmanager
def timerContext(name):
    """Time Execution Of Code Block"""
    import time
    print(f"Starting: {name}")
    startTime = time.time()
    
    try:
        yield  # Code Block Executes Here
    finally:
        endTime = time.time()
        print(f"Finished: {name} in {endTime - startTime:.4f} seconds")

# Using Timer Context
with timerContext("Data Processing"):
    total = sum(range(1000000))
    print(f"Sum: {total}")

# Suppress Exceptions Context Manager
print("\n--- Suppress Exceptions ---")

from contextlib import suppress

# Without Suppress (Would Raise Error)
try:
    with suppress(FileNotFoundError):
        with open("nonexistent.txt", "r") as f:
            content = f.read()
except FileNotFoundError:
    print("File Not Found - But Suppressed")

print("Continued Execution After Suppressed Exception")


# ========================================
# 2. COLLECTIONS MODULE
# ========================================
print("\n\n" + "="*60)
print("2. COLLECTIONS MODULE")
print("="*60)

from collections import Counter, defaultdict, deque, namedtuple, OrderedDict, ChainMap

# Counter - Count Hashable Objects
print("\n--- Counter ---")
print("Counter = Dict Subclass For Counting")

words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
wordCount = Counter(words)
print(f"Word Count: {wordCount}")
print(f"Most Common: {wordCount.most_common(2)}")

# Counter Operations
counter1 = Counter("hello")
counter2 = Counter("world")
print(f"\nCounter 'hello': {counter1}")
print(f"Counter 'world': {counter2}")
print(f"Addition: {counter1 + counter2}")
print(f"Subtraction: {counter1 - counter2}")

# defaultdict - Dict With Default Values
print("\n--- defaultdict ---")
print("defaultdict = Dict That Provides Default Value For Missing Keys")

from collections import defaultdict

# Regular Dict (Would Raise KeyError)
regularDict = {}
# regularDict['missing']  # KeyError

# defaultdict With List
groupedData = defaultdict(list)
groupedData['fruits'].append('apple')
groupedData['fruits'].append('banana')
groupedData['vegetables'].append('carrot')
print(f"Grouped Data: {dict(groupedData)}")

# defaultdict With Int (For Counting)
letterCount = defaultdict(int)
for letter in "hello world":
    letterCount[letter] += 1
print(f"Letter Count: {dict(letterCount)}")

# deque - Double-Ended Queue
print("\n--- deque ---")
print("deque = Efficient Queue/Stack With O(1) Operations At Both Ends")

queue = deque([1, 2, 3])
print(f"Initial: {queue}")

queue.append(4)          # Add Right
queue.appendleft(0)      # Add Left
print(f"After Appends: {queue}")

queue.pop()              # Remove Right
queue.popleft()          # Remove Left
print(f"After Pops: {queue}")

# Rotate
queue.rotate(1)          # Rotate Right
print(f"After Rotate Right: {queue}")
queue.rotate(-2)         # Rotate Left
print(f"After Rotate Left: {queue}")

# Max Length Deque
limitedQueue = deque(maxlen=3)
for i in range(5):
    limitedQueue.append(i)
    print(f"  After Adding {i}: {limitedQueue}")

# namedtuple - Tuple With Named Fields
print("\n--- namedtuple ---")
print("namedtuple = Tuple With Named Fields (Immutable)")

# Define namedtuple
Point = namedtuple('Point', ['x', 'y'])
person = namedtuple('Person', ['name', 'age', 'city'])

p = Point(10, 20)
print(f"Point: {p}")
print(f"X: {p.x}, Y: {p.y}")

john = person('John', 30, 'New York')
print(f"\nPerson: {john}")
print(f"Name: {john.name}, Age: {john.age}")

# Convert To Dict
print(f"As Dict: {john._asdict()}")

# OrderedDict - Remembers Insertion Order
print("\n--- OrderedDict ---")
print("OrderedDict = Dict That Remembers Insertion Order")
print("Note: Regular Dicts Also Maintain Order In Python 3.7+")

ordDict = OrderedDict()
ordDict['c'] = 3
ordDict['a'] = 1
ordDict['b'] = 2
print(f"Ordered Dict: {ordDict}")

# Move To End
ordDict.move_to_end('a')
print(f"After Moving 'a' To End: {ordDict}")

# ChainMap - Combine Multiple Dicts
print("\n--- ChainMap ---")
print("ChainMap = Combines Multiple Dicts Into Single View")

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
dict3 = {'d': 5}

combined = ChainMap(dict1, dict2, dict3)
print(f"ChainMap: {combined}")
print(f"Get 'b' (From First Dict): {combined['b']}")  # 2 (from dict1)
print(f"Get 'c': {combined['c']}")  # 4 (from dict2)
print(f"All Keys: {list(combined.keys())}")


# ========================================
# 3. ITERTOOLS MODULE
# ========================================
print("\n\n" + "="*60)
print("3. ITERTOOLS MODULE")
print("="*60)

import itertools

print("itertools = Functions For Efficient Looping")

# count - Infinite Counter
print("\n--- count ---")
counter = itertools.count(start=10, step=2)
print("First 5 From count(10, 2):", [next(counter) for _ in range(5)])

# cycle - Cycle Through Iterable
print("\n--- cycle ---")
cycler = itertools.cycle(['A', 'B', 'C'])
print("First 7 From cycle:", [next(cycler) for _ in range(7)])

# repeat - Repeat Value
print("\n--- repeat ---")
print("Repeat 'X' 5 Times:", list(itertools.repeat('X', 5)))

# chain - Combine Iterables
print("\n--- chain ---")
combined = itertools.chain([1, 2], [3, 4], [5, 6])
print("Chained:", list(combined))

# combinations - All Combinations
print("\n--- combinations ---")
items = ['A', 'B', 'C']
combs = itertools.combinations(items, 2)
print(f"Combinations Of {items} (r=2): {list(combs)}")

# permutations - All Permutations
print("\n--- permutations ---")
perms = itertools.permutations(['A', 'B', 'C'], 2)
print(f"Permutations (r=2): {list(perms)}")

# product - Cartesian Product
print("\n--- product ---")
prod = itertools.product([1, 2], ['A', 'B'])
print("Product [1,2] × ['A','B']:", list(prod))

# groupby - Group Consecutive Elements
print("\n--- groupby ---")
data = [1, 1, 2, 2, 2, 3, 1, 1]
grouped = itertools.groupby(data)
for key, group in grouped:
    print(f"  Key {key}: {list(group)}")

# accumulate - Cumulative Sum
print("\n--- accumulate ---")
numbers = [1, 2, 3, 4, 5]
cumSum = itertools.accumulate(numbers)
print(f"Cumulative Sum Of {numbers}: {list(cumSum)}")

# zip_longest - Zip With Fillvalue
print("\n--- zip_longest ---")
from itertools import zip_longest
list1 = [1, 2, 3]
list2 = ['A', 'B']
zipped = zip_longest(list1, list2, fillvalue='X')
print(f"zip_longest: {list(zipped)}")

# islice - Slice Iterator
print("\n--- islice ---")
from itertools import islice
numbers = range(100)
sliced = islice(numbers, 5, 15, 2)  # [start:stop:step]
print(f"islice(range(100), 5, 15, 2): {list(sliced)}")


# ========================================
# 4. FUNCTOOLS MODULE
# ========================================
print("\n\n" + "="*60)
print("4. FUNCTOOLS MODULE")
print("="*60)

from functools import partial, lru_cache, reduce, wraps

print("functools = Higher-Order Functions And Operations")

# partial - Partial Function Application
print("\n--- partial ---")

def multiply(x, y):
    return x * y

double = partial(multiply, 2)  # Fix First Argument To 2
triple = partial(multiply, 3)

print(f"double(5) = {double(5)}")
print(f"triple(5) = {triple(5)}")

# lru_cache - Memoization/Caching
print("\n--- lru_cache ---")

@lru_cache(maxsize=128)
def fibonacci(n):
    """Cached Fibonacci"""
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

import time
start = time.time()
result = fibonacci(35)
end = time.time()
print(f"fibonacci(35) = {result}")
print(f"Time: {end - start:.6f} seconds (With Cache)")
print(f"Cache Info: {fibonacci.cache_info()}")

# reduce - Already Covered In Chapter 17
print("\n--- reduce ---")
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(f"Product Of {numbers}: {product}")

# wraps - Preserve Function Metadata
print("\n--- wraps ---")
print("Use @wraps In Decorators To Preserve Function Metadata")


# ========================================
# 5. DATA CLASSES
# ========================================
print("\n\n" + "="*60)
print("5. DATA CLASSES (Python 3.7+)")
print("="*60)

from dataclasses import dataclass, field, asdict, astuple

print("dataclass = Decorator To Automatically Generate __init__, __repr__, etc.")

# Basic Dataclass
@dataclass
class Person:
    """Person Data Class"""
    name: str
    age: int
    city: str = "Unknown"  # Default Value

person1 = Person("Alice", 30, "New York")
person2 = Person("Bob", 25)

print(f"\nPerson 1: {person1}")
print(f"Person 2: {person2}")

# Dataclass Features
print(f"\nEquality: {person1 == person2}")
print(f"As Dict: {asdict(person1)}")
print(f"As Tuple: {astuple(person1)}")

# Dataclass With Methods
@dataclass
class Rectangle:
    width: float
    height: float
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

rect = Rectangle(10, 5)
print(f"\nRectangle: {rect}")
print(f"Area: {rect.area()}")
print(f"Perimeter: {rect.perimeter()}")

# Dataclass With field()
@dataclass
class Student:
    name: str
    grades: list = field(default_factory=list)  # Mutable Default
    
    def averageGrade(self):
        return sum(self.grades) / len(self.grades) if self.grades else 0

student = Student("John")
student.grades.extend([85, 90, 88])
print(f"\nStudent: {student}")
print(f"Average: {student.averageGrade():.2f}")

# Frozen Dataclass (Immutable)
@dataclass(frozen=True)
class Point:
    x: float
    y: float

point = Point(10, 20)
print(f"\nFrozen Point: {point}")
# point.x = 30  # Would Raise FrozenInstanceError


# ========================================
# 6. ENUM
# ========================================
print("\n\n" + "="*60)
print("6. ENUM (ENUMERATIONS)")
print("="*60)

from enum import Enum, IntEnum, auto

print("Enum = Set Of Symbolic Names Bound To Unique Values")

# Basic Enum
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

print(f"\nColor.RED: {Color.RED}")
print(f"Value: {Color.RED.value}")
print(f"Name: {Color.RED.name}")

# Iterate Over Enum
print("\nAll Colors:")
for color in Color:
    print(f"  {color.name} = {color.value}")

# Enum Comparison
print(f"\nColor.RED == Color.RED: {Color.RED == Color.RED}")
print(f"Color.RED == 1: {Color.RED == 1}")  # False (Strict Comparison)

# IntEnum - Integer Enum
class Status(IntEnum):
    PENDING = 1
    ACTIVE = 2
    COMPLETED = 3

print(f"\nStatus.ACTIVE: {Status.ACTIVE}")
print(f"Status.ACTIVE == 2: {Status.ACTIVE == 2}")  # True

# Auto Values
class Priority(Enum):
    LOW = auto()
    MEDIUM = auto()
    HIGH = auto()

print(f"\nAuto Values:")
for p in Priority:
    print(f"  {p.name} = {p.value}")


# ========================================
# 7. PATHLIB (MODERN FILE PATHS)
# ========================================
print("\n\n" + "="*60)
print("7. PATHLIB (MODERN FILE HANDLING)")
print("="*60)

from pathlib import Path

print("Pathlib = Object-Oriented File System Paths")

# Current Directory
currentDir = Path.cwd()
print(f"\nCurrent Directory: {currentDir}")

# Home Directory
homeDir = Path.home()
print(f"Home Directory: {homeDir}")

# Create Path Object
filePath = Path("OuputFolder/Text.txt")
print(f"\nFile Path: {filePath}")
print(f"Absolute: {filePath.absolute()}")
print(f"Exists: {filePath.exists()}")
print(f"Is File: {filePath.is_file()}")

# Path Components
fullPath = Path(r"h:\PYTHON COURSE\PYTHON BASIC\Chapter28.py")
print(f"\nFull Path: {fullPath}")
print(f"Parent: {fullPath.parent}")
print(f"Name: {fullPath.name}")
print(f"Stem: {fullPath.stem}")
print(f"Suffix: {fullPath.suffix}")
print(f"Parts: {fullPath.parts}")

# Join Paths
newPath = Path("folder") / "subfolder" / "file.txt"
print(f"\nJoined Path: {newPath}")

# Read/Write Files
testPath = Path("test_pathlib.txt")
testPath.write_text("Hello From Pathlib!")
content = testPath.read_text()
print(f"\nFile Content: {content}")

# List Directory
print("\nFiles In Current Directory (First 5):")
for i, item in enumerate(Path.cwd().iterdir()):
    if i >= 5:
        break
    print(f"  {item.name}")

# Glob Pattern Matching
print("\nPython Files (*.py):")
for pyFile in list(Path.cwd().glob("*.py"))[:3]:
    print(f"  {pyFile.name}")


# ========================================
# 8. ADVANCED *ARGS AND **KWARGS
# ========================================
print("\n\n" + "="*60)
print("8. ADVANCED *ARGS AND **KWARGS")
print("="*60)

print("*args = Variable Positional Arguments (Tuple)")
print("**kwargs = Variable Keyword Arguments (Dict)")

# Basic Usage
def printInfo(*args, **kwargs):
    print(f"Args: {args}")
    print(f"Kwargs: {kwargs}")

print("\nprintInfo(1, 2, 3, name='Alice', age=30):")
printInfo(1, 2, 3, name='Alice', age=30)

# Args Unpacking
def add(a, b, c):
    return a + b + c

numbers = [1, 2, 3]
result = add(*numbers)  # Unpack List
print(f"\nadd(*[1,2,3]) = {result}")

# Kwargs Unpacking
def greet(name, age):
    return f"Hello {name}, you are {age} years old"

person = {'name': 'Bob', 'age': 25}
greeting = greet(**person)  # Unpack Dict
print(f"greet(**person) = {greeting}")

# Combining Everything
def complexFunction(required, *args, default=10, **kwargs):
    print(f"Required: {required}")
    print(f"Args: {args}")
    print(f"Default: {default}")
    print(f"Kwargs: {kwargs}")

print("\ncomplex_function(1, 2, 3, default=20, x=100):")
complexFunction(1, 2, 3, default=20, x=100)

# Forwarding Arguments
def wrapper(*args, **kwargs):
    """Forward All Arguments To Another Function"""
    print("Wrapper Called")
    return printInfo(*args, **kwargs)

print("\nwrapper(1, 2, key='value'):")
wrapper(1, 2, key='value')


# ========================================
# 9. GLOBAL, LOCAL, NONLOCAL
# ========================================
print("\n\n" + "="*60)
print("9. GLOBAL, LOCAL, NONLOCAL")
print("="*60)

# Global Variable
globalVar = "I'm Global"

def modifyGlobal():
    global globalVar  # Declare Global
    globalVar = "Modified Global"
    print(f"Inside Function: {globalVar}")

print(f"Before: {globalVar}")
modifyGlobal()
print(f"After: {globalVar}")

# Local Variable
def localExample():
    localVar = "I'm Local"
    print(f"Local: {localVar}")

localExample()
# print(localVar)  # NameError

# Nonlocal Variable
print("\n--- nonlocal ---")

def outer():
    outerVar = "Outer"
    
    def inner():
        nonlocal outerVar  # Access Enclosing Scope
        outerVar = "Modified By Inner"
        print(f"Inner: {outerVar}")
    
    print(f"Before Inner: {outerVar}")
    inner()
    print(f"After Inner: {outerVar}")

outer()

# Scope Hierarchy
print("\n--- Scope Hierarchy ---")
print("LEGB Rule: Local -> Enclosing -> Global -> Built-in")


# ========================================
# 10. SET AND DICT COMPREHENSIONS
# ========================================
print("\n\n" + "="*60)
print("10. SET AND DICT COMPREHENSIONS")
print("="*60)

# Set Comprehension
print("--- Set Comprehension ---")
numbers = [1, 2, 2, 3, 3, 3, 4, 5, 5]
uniqueSquares = {x**2 for x in numbers}
print(f"Numbers: {numbers}")
print(f"Unique Squares: {uniqueSquares}")

# Conditional Set Comprehension
evenSquares = {x**2 for x in range(10) if x % 2 == 0}
print(f"Even Squares: {evenSquares}")

# Dict Comprehension
print("\n--- Dict Comprehension ---")
numbers = [1, 2, 3, 4, 5]
squareDict = {x: x**2 for x in numbers}
print(f"Square Dict: {squareDict}")

# Swap Keys And Values
originalDict = {'a': 1, 'b': 2, 'c': 3}
swappedDict = {v: k for k, v in originalDict.items()}
print(f"Original: {originalDict}")
print(f"Swapped: {swappedDict}")

# Conditional Dict Comprehension
evenDict = {x: x**2 for x in range(10) if x % 2 == 0}
print(f"Even Dict: {evenDict}")

# From Two Lists
keys = ['name', 'age', 'city']
values = ['Alice', 30, 'NYC']
combined = {k: v for k, v in zip(keys, values)}
print(f"Combined: {combined}")


# ========================================
# 11. ADVANCED STRING FORMATTING
# ========================================
print("\n\n" + "="*60)
print("11. ADVANCED STRING FORMATTING")
print("="*60)

# F-String Advanced
print("--- F-String Advanced ---")
name = "Alice"
age = 30
pi = 3.14159265359

# Basic
print(f"Name: {name}, Age: {age}")

# Expressions
print(f"Age In 10 Years: {age + 10}")

# Formatting Numbers
print(f"Pi: {pi:.2f}")  # 2 Decimal Places
print(f"Pi: {pi:.5f}")  # 5 Decimal Places

# Padding And Alignment
print(f"Left:   |{name:<10}|")
print(f"Right:  |{name:>10}|")
print(f"Center: |{name:^10}|")

# Numbers With Thousands Separator
number = 1234567
print(f"With Comma: {number:,}")
print(f"With Underscore: {number:_}")

# Binary, Octal, Hex
num = 42
print(f"Binary: {num:b}")
print(f"Octal: {num:o}")
print(f"Hex: {num:x}")

# Percentage
ratio = 0.857
print(f"Percentage: {ratio:.1%}")

# Date Formatting
from datetime import datetime
now = datetime.now()
print(f"Date: {now:%Y-%m-%d}")
print(f"Time: {now:%H:%M:%S}")

# Nested F-Strings
width = 10
precision = 3
value = 12.3456
print(f"Dynamic Format: {value:{width}.{precision}f}")

# Debug Feature (Python 3.8+)
x = 10
y = 20
print(f"{x=}, {y=}, {x+y=}")


# ========================================
# 12. STRUCT MODULE (BINARY DATA)
# ========================================
print("\n\n" + "="*60)
print("12. STRUCT MODULE (BINARY DATA)")
print("="*60)

import struct

print("struct = Convert Between Python Values And C Structs")

# Pack Data Into Binary
print("\n--- Pack Data ---")
packedData = struct.pack('i 4s f', 7, b'spam', 3.14)
print(f"Packed: {packedData}")
print(f"Length: {len(packedData)} bytes")

# Unpack Binary Data
unpacked = struct.unpack('i 4s f', packedData)
print(f"Unpacked: {unpacked}")

# Format Characters
print("\n--- Format Characters ---")
print("i = integer (4 bytes)")
print("f = float (4 bytes)")
print("d = double (8 bytes)")
print("s = char[] (string)")
print("c = char (1 byte)")

# Calculate Size
size = struct.calcsize('i 4s f')
print(f"\nSize Of 'i 4s f': {size} bytes")


# ========================================
# 13. ARRAY MODULE
# ========================================
print("\n\n" + "="*60)
print("13. ARRAY MODULE")
print("="*60)

import array

print("array = Efficient Arrays Of Numeric Values")

# Create Array
intArray = array.array('i', [1, 2, 3, 4, 5])
print(f"\nInteger Array: {intArray}")

# Array Operations
intArray.append(6)
print(f"After Append: {intArray}")

intArray.extend([7, 8, 9])
print(f"After Extend: {intArray}")

# Type Codes
print("\n--- Type Codes ---")
print("'i' = signed int")
print("'I' = unsigned int")
print("'f' = float")
print("'d' = double")

# Array Is More Memory Efficient Than List For Numeric Data
floatArray = array.array('f', [1.1, 2.2, 3.3])
print(f"\nFloat Array: {floatArray}")


# ========================================
# 14. HEAPQ MODULE (PRIORITY QUEUE)
# ========================================
print("\n\n" + "="*60)
print("14. HEAPQ MODULE (PRIORITY QUEUE)")
print("="*60)

import heapq

print("heapq = Heap Queue Algorithm (Priority Queue)")

# Create Heap
heap = []
heapq.heappush(heap, 5)
heapq.heappush(heap, 2)
heapq.heappush(heap, 9)
heapq.heappush(heap, 1)
print(f"\nHeap: {heap}")

# Pop Smallest
smallest = heapq.heappop(heap)
print(f"Popped Smallest: {smallest}")
print(f"Heap After Pop: {heap}")

# N Largest/Smallest
numbers = [5, 2, 9, 1, 7, 3]
largest3 = heapq.nlargest(3, numbers)
smallest3 = heapq.nsmallest(3, numbers)
print(f"\nNumbers: {numbers}")
print(f"3 Largest: {largest3}")
print(f"3 Smallest: {smallest3}")

# Heapify Existing List
data = [5, 2, 9, 1, 7]
heapq.heapify(data)
print(f"\nHeapified: {data}")


# ========================================
# 15. __SLOTS__ (MEMORY OPTIMIZATION)
# ========================================
print("\n\n" + "="*60)
print("15. __SLOTS__ (MEMORY OPTIMIZATION)")
print("="*60)

print("__slots__ = Restrict Attributes, Reduce Memory Usage")

# Regular Class
class RegularPerson:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Class With __slots__
class SlottedPerson:
    __slots__ = ['name', 'age']
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

regularPerson = RegularPerson("Alice", 30)
slottedPerson = SlottedPerson("Bob", 25)

print(f"\nRegular Person: {regularPerson.name}")
print(f"Slotted Person: {slottedPerson.name}")

# Regular Class Has __dict__
print(f"Regular __dict__: {regularPerson.__dict__}")

# Slotted Class Doesn't Have __dict__
# print(slottedPerson.__dict__)  # AttributeError

# Can't Add New Attributes To Slotted Class
# slottedPerson.city = "NYC"  # AttributeError

print("\nBenefits Of __slots__:")
print("  - Faster Attribute Access")
print("  - Less Memory Usage (No __dict__)")
print("  - Prevents Dynamic Attribute Addition")


# ========================================
# 16. WEAK REFERENCES
# ========================================
print("\n\n" + "="*60)
print("16. WEAK REFERENCES")
print("="*60)

import weakref

print("weakref = References That Don't Prevent Garbage Collection")

class BigObject:
    def __init__(self, name):
        self.name = name
    
    def __del__(self):
        print(f"BigObject '{self.name}' Deleted")

# Strong Reference
obj = BigObject("Strong")
print(f"Strong Ref: {obj.name}")

# Weak Reference
weakRef = weakref.ref(obj)
print(f"Weak Ref: {weakRef().name}")

# Delete Strong Reference
del obj
print("Strong Reference Deleted")

# Weak Reference Now Returns None
print(f"Weak Ref After Delete: {weakRef()}")


# ========================================
# 17. ASYNCIO (ASYNCHRONOUS PROGRAMMING)
# ========================================
print("\n\n" + "="*60)
print("17. ASYNCIO (ASYNCHRONOUS PROGRAMMING)")
print("="*60)

import asyncio

print("AsyncIO = Asynchronous I/O For Concurrent Programming")
print("Note: Chapter 20 Has Basic AsyncIO, This Covers Advanced Topics")

# Basic Async Function (Coroutine)
print("\n--- Basic Coroutine ---")

async def simpleCoroutine():
    """Basic Async Function"""
    print("  Coroutine Started")
    await asyncio.sleep(0.1)  # Non-Blocking Sleep
    print("  Coroutine Finished")
    return "Done"

# Run Coroutine
result = asyncio.run(simpleCoroutine())
print(f"Result: {result}")

# Multiple Concurrent Tasks
print("\n--- Concurrent Tasks With gather() ---")

async def fetchData(id, delay):
    """Simulate Fetching Data"""
    print(f"  Fetching Data {id}...")
    await asyncio.sleep(delay)
    print(f"  Data {id} Fetched")
    return f"Data-{id}"

async def runConcurrent():
    """Run Multiple Tasks Concurrently"""
    results = await asyncio.gather(
        fetchData(1, 0.2),
        fetchData(2, 0.1),
        fetchData(3, 0.15)
    )
    return results

results = asyncio.run(runConcurrent())
print(f"All Results: {results}")

# Create Tasks
print("\n--- Creating Tasks ---")

async def countDown(name, seconds):
    """Count Down"""
    for i in range(seconds, 0, -1):
        print(f"  {name}: {i}")
        await asyncio.sleep(0.1)
    print(f"  {name}: Done!")

async def runWithTasks():
    """Create And Run Tasks"""
    # Create Tasks
    task1 = asyncio.create_task(countDown("Task1", 3))
    task2 = asyncio.create_task(countDown("Task2", 2))
    
    # Wait For Both
    await task1
    await task2

asyncio.run(runWithTasks())

# Task With Timeout
print("\n--- Task With Timeout ---")

async def longOperation():
    """Long Running Operation"""
    print("  Starting Long Operation...")
    await asyncio.sleep(5)
    return "Completed"

async def runWithTimeout():
    """Run Task With Timeout"""
    try:
        result = await asyncio.wait_for(longOperation(), timeout=0.5)
        return result
    except asyncio.TimeoutError:
        return "Operation Timed Out!"

result = asyncio.run(runWithTimeout())
print(f"Result: {result}")

# Task Cancellation
print("\n--- Task Cancellation ---")

async def cancellableTask():
    """Task That Can Be Cancelled"""
    try:
        print("  Task Started")
        await asyncio.sleep(10)
        print("  Task Completed")
    except asyncio.CancelledError:
        print("  Task Was Cancelled!")
        raise  # Re-raise To Properly Cancel

async def runWithCancellation():
    """Cancel A Task"""
    task = asyncio.create_task(cancellableTask())
    
    # Wait A Bit Then Cancel
    await asyncio.sleep(0.1)
    task.cancel()
    
    try:
        await task
    except asyncio.CancelledError:
        print("Caught Cancellation")

asyncio.run(runWithCancellation())

# Async Context Manager
print("\n--- Async Context Manager ---")

class AsyncResource:
    """Async Context Manager"""
    
    async def __aenter__(self):
        """Called When Entering Async With Block"""
        print("  Acquiring Resource...")
        await asyncio.sleep(0.1)
        print("  Resource Acquired")
        return self
    
    async def __aexit__(self, excType, excValue, excTraceback):
        """Called When Exiting Async With Block"""
        print("  Releasing Resource...")
        await asyncio.sleep(0.1)
        print("  Resource Released")
        return False

async def useAsyncResource():
    """Use Async Context Manager"""
    async with AsyncResource() as resource:
        print("  Using Resource")
        await asyncio.sleep(0.1)

asyncio.run(useAsyncResource())

# Async Iterator
print("\n--- Async Iterator ---")

class AsyncCounter:
    """Async Iterator"""
    
    def __init__(self, maxCount):
        self.maxCount = maxCount
        self.count = 0
    
    def __aiter__(self):
        return self
    
    async def __anext__(self):
        if self.count >= self.maxCount:
            raise StopAsyncIteration
        
        await asyncio.sleep(0.1)  # Simulate Async Operation
        self.count += 1
        return self.count

async def useAsyncIterator():
    """Use Async Iterator"""
    print("  Async Iteration:")
    async for num in AsyncCounter(5):
        print(f"    Count: {num}")

asyncio.run(useAsyncIterator())

# Async Generator
print("\n--- Async Generator ---")

async def asyncRange(start, stop):
    """Async Generator"""
    for i in range(start, stop):
        await asyncio.sleep(0.1)
        yield i

async def useAsyncGenerator():
    """Use Async Generator"""
    print("  Async Generator:")
    async for num in asyncRange(1, 6):
        print(f"    Value: {num}")

asyncio.run(useAsyncGenerator())

# Async Comprehension
print("\n--- Async Comprehension ---")

async def asyncSquares():
    """Async Comprehension"""
    # Async List Comprehension
    squares = [i**2 async for i in asyncRange(1, 6)]
    print(f"  Squares: {squares}")

asyncio.run(asyncSquares())

# Queue For Producer-Consumer Pattern
print("\n--- Async Queue (Producer-Consumer) ---")

async def producer(queue, id):
    """Producer Task"""
    for i in range(3):
        item = f"Item-{id}-{i}"
        await queue.put(item)
        print(f"  Produced: {item}")
        await asyncio.sleep(0.1)

async def consumer(queue, id):
    """Consumer Task"""
    while True:
        item = await queue.get()
        print(f"  Consumer-{id} Got: {item}")
        await asyncio.sleep(0.15)
        queue.task_done()

async def producerConsumerDemo():
    """Producer-Consumer Pattern"""
    queue = asyncio.Queue(maxsize=5)
    
    # Create Producers And Consumers
    producers = [asyncio.create_task(producer(queue, i)) for i in range(2)]
    consumers = [asyncio.create_task(consumer(queue, i)) for i in range(2)]
    
    # Wait For Producers To Finish
    await asyncio.gather(*producers)
    
    # Wait For Queue To Be Processed
    await queue.join()
    
    # Cancel Consumers
    for c in consumers:
        c.cancel()

asyncio.run(producerConsumerDemo())

# Semaphore For Rate Limiting
print("\n--- Async Semaphore (Rate Limiting) ---")

async def limitedTask(semaphore, id):
    """Task With Semaphore"""
    async with semaphore:
        print(f"  Task {id} Running")
        await asyncio.sleep(0.2)
        print(f"  Task {id} Done")

async def semaphoreDemo():
    """Limit Concurrent Tasks"""
    # Only 2 Tasks Can Run At Once
    semaphore = asyncio.Semaphore(2)
    
    tasks = [limitedTask(semaphore, i) for i in range(5)]
    await asyncio.gather(*tasks)

print("Running With Semaphore (Max 2 Concurrent):")
asyncio.run(semaphoreDemo())

# Lock For Shared Resource
print("\n--- Async Lock ---")

sharedCounter = 0
lock = asyncio.Lock()

async def incrementWithLock(lockObj, id):
    """Increment Counter With Lock"""
    global sharedCounter
    
    async with lockObj:
        # Critical Section
        temp = sharedCounter
        await asyncio.sleep(0.01)  # Simulate Work
        sharedCounter = temp + 1
        print(f"  Task {id}: Counter = {sharedCounter}")

async def lockDemo():
    """Demonstrate Lock"""
    global sharedCounter
    sharedCounter = 0
    lock = asyncio.Lock()
    
    tasks = [incrementWithLock(lock, i) for i in range(5)]
    await asyncio.gather(*tasks)
    print(f"Final Counter: {sharedCounter}")

asyncio.run(lockDemo())

# Event For Signaling
print("\n--- Async Event ---")

async def waiter(event, id):
    """Wait For Event"""
    print(f"  Waiter {id} Waiting...")
    await event.wait()
    print(f"  Waiter {id} Notified!")

async def setter(event):
    """Set Event After Delay"""
    await asyncio.sleep(0.2)
    print("  Setting Event...")
    event.set()

async def eventDemo():
    """Event Signaling"""
    event = asyncio.Event()
    
    # Create Waiters And Setter
    await asyncio.gather(
        waiter(event, 1),
        waiter(event, 2),
        waiter(event, 3),
        setter(event)
    )

asyncio.run(eventDemo())

# as_completed For Processing As They Finish
print("\n--- as_completed() ---")

async def taskWithDelay(id, delay):
    """Task With Variable Delay"""
    await asyncio.sleep(delay)
    return f"Task-{id}"

async def asCompletedDemo():
    """Process Tasks As They Complete"""
    tasks = [
        taskWithDelay(1, 0.3),
        taskWithDelay(2, 0.1),
        taskWithDelay(3, 0.2)
    ]
    
    print("  Processing As They Complete:")
    for coro in asyncio.as_completed(tasks):
        result = await coro
        print(f"    Completed: {result}")

asyncio.run(asCompletedDemo())

# Shield Task From Cancellation
print("\n--- Shield From Cancellation ---")

async def criticalTask():
    """Task That Should Not Be Cancelled"""
    print("  Critical Task Started")
    await asyncio.sleep(0.3)
    print("  Critical Task Completed")
    return "Important Result"

async def shieldDemo():
    """Shield Task From Cancellation"""
    task = asyncio.create_task(
        asyncio.shield(criticalTask())
    )
    
    await asyncio.sleep(0.1)
    task.cancel()  # Try To Cancel
    
    try:
        result = await task
        print(f"  Result: {result}")
    except asyncio.CancelledError:
        print("  Task Was Cancelled (But Inner Task Continues)")

asyncio.run(shieldDemo())

# Run In Executor (Run Blocking Code)
print("\n--- Run Blocking Code In Executor ---")

def blockingFunction(n):
    """Blocking Function"""
    import time
    print(f"  Blocking Function Started ({n})")
    time.sleep(0.2)  # Blocking Sleep
    print(f"  Blocking Function Done ({n})")
    return n * 2

async def runInExecutor():
    """Run Blocking Code In Thread Pool"""
    loop = asyncio.get_event_loop()
    
    # Run In Default Executor (ThreadPoolExecutor)
    results = await asyncio.gather(
        loop.run_in_executor(None, blockingFunction, 1),
        loop.run_in_executor(None, blockingFunction, 2),
        loop.run_in_executor(None, blockingFunction, 3)
    )
    
    print(f"  Results: {results}")

asyncio.run(runInExecutor())

# Real-World Example: Concurrent HTTP Requests Simulation
print("\n--- Real-World Example: Concurrent API Calls ---")

async def fetchUrl(url, session):
    """Simulate Fetching URL"""
    print(f"  Fetching: {url}")
    await asyncio.sleep(0.15)  # Simulate Network Delay
    return f"Content From {url}"

async def fetchAllUrls():
    """Fetch Multiple URLs Concurrently"""
    urls = [
        "https://api.example.com/users",
        "https://api.example.com/posts",
        "https://api.example.com/comments"
    ]
    
    session = "SessionObject"  # Simulated Session
    
    tasks = [fetchUrl(url, session) for url in urls]
    results = await asyncio.gather(*tasks)
    
    for result in results:
        print(f"  Got: {result}")

import time
start = time.time()
asyncio.run(fetchAllUrls())
end = time.time()
print(f"Total Time: {end - start:.2f} seconds (Concurrent)")

# Error Handling In Async Code
print("\n--- Error Handling ---")

async def taskThatFails():
    """Task That Raises Exception"""
    await asyncio.sleep(0.1)
    raise ValueError("Something Went Wrong!")

async def errorHandlingDemo():
    """Handle Errors In Async Code"""
    try:
        await taskThatFails()
    except ValueError as e:
        print(f"  Caught Error: {e}")

asyncio.run(errorHandlingDemo())

# gather() With return_exceptions
print("\n--- gather() With return_exceptions ---")

async def successTask():
    await asyncio.sleep(0.1)
    return "Success"

async def failTask():
    await asyncio.sleep(0.1)
    raise RuntimeError("Failed!")

async def gatherWithExceptions():
    """Gather With Exception Handling"""
    results = await asyncio.gather(
        successTask(),
        failTask(),
        successTask(),
        return_exceptions=True  # Return Exceptions Instead Of Raising
    )
    
    print("  Results:")
    for i, result in enumerate(results):
        if isinstance(result, Exception):
            print(f"    Task {i}: Error - {result}")
        else:
            print(f"    Task {i}: {result}")

asyncio.run(gatherWithExceptions())

print("\n--- AsyncIO Best Practices ---")
print("""
1. Use asyncio.run() For Top-Level Entry Point
2. Always Use 'await' For Coroutines
3. Use asyncio.create_task() To Run Coroutines Concurrently
4. Use Semaphore For Rate Limiting
5. Use Lock For Shared Resources
6. Handle Cancellation With try/except asyncio.CancelledError
7. Use run_in_executor() For Blocking I/O
8. Use gather() With return_exceptions For Error Handling
9. Always Close Resources In Finally Or With Context Managers
10. Test Async Code Thoroughly
""")


# ========================================
# 18. MISCELLANEOUS TOPICS
# ========================================
print("\n\n" + "="*60)
print("18. MISCELLANEOUS TOPICS")
print("="*60)

# Ellipsis
print("\n--- Ellipsis (...) ---")
print("Ellipsis = Built-in Constant, Used As Placeholder")

def functionStub():
    ...  # Placeholder

matrix = [[...] for _ in range(3)]
print(f"Matrix Stub: {matrix}")

# Underscore Uses
print("\n--- Underscore (_) Uses ---")
print("1. Ignore Values:")
for _ in range(3):
    print("  Loop")

a, _, c = (1, 2, 3)
print(f"2. Unpacking: a={a}, c={c}")

# Walrus Operator (Already Covered In Chapter 16)
print("\n--- Walrus Operator := ---")
if (n := len([1, 2, 3, 4, 5])) > 3:
    print(f"List Length {n} Is Greater Than 3")

# Multiple Assignment
print("\n--- Multiple Assignment ---")
x = y = z = 0
print(f"x={x}, y={y}, z={z}")

a, b = 1, 2
print(f"a={a}, b={b}")

# Swap
a, b = b, a
print(f"After Swap: a={a}, b={b}")

# Chained Comparison
print("\n--- Chained Comparison ---")
x = 5
result = 1 < x < 10
print(f"1 < {x} < 10: {result}")

# Identity vs Equality
print("\n--- Identity (is) vs Equality (==) ---")
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(f"a == b: {a == b}")  # True (Equal Values)
print(f"a is b: {a is b}")  # False (Different Objects)
print(f"a is c: {a is c}")  # True (Same Object)

# None Check
print("\n--- None Check ---")
value = None
print(f"value is None: {value is None}")  # Correct
print(f"value == None: {value == None}")  # Works But Not Recommended


# ========================================
# 19. SUMMARY
# ========================================
print("\n\n" + "="*60)
print("CHAPTER 28 SUMMARY")
print("="*60)

print("""
Topics Covered In This Chapter:

1. Context Managers - Resource Management With 'with'
2. Collections Module - Counter, defaultdict, deque, namedtuple, etc.
3. Itertools Module - Efficient Iteration Tools
4. Functools Module - Higher-Order Functions (partial, lru_cache)
5. Data Classes - Simplified Class Creation
6. Enum - Enumerations For Symbolic Names
7. Pathlib - Modern File Path Handling
8. Advanced *args/**kwargs - Variable Arguments
9. Global/Local/Nonlocal - Scope Management
10. Set/Dict Comprehensions - Concise Creation
11. Advanced String Formatting - F-strings And More
12. Struct Module - Binary Data Handling
13. Array Module - Efficient Numeric Arrays
14. Heapq Module - Priority Queues
15. __slots__ - Memory Optimization
16. Weak References - Garbage Collection Control
17. AsyncIO - Asynchronous Programming (Comprehensive)
18. Miscellaneous - Ellipsis, Underscore, Identity, etc.

These Topics Complete The Python Fundamentals Course!
""")

print("="*60)
print("END OF CHAPTER 28")
print("="*60)
# Chapter 4: Lists And Tuples

"""
TABLE OF CONTENTS:
1. List Basics
   - Creating Lists
   - Indexing And Slicing
   - List Methods (append, extend, insert, remove, pop, etc.)
2. Advanced List Operations
   - List Comprehension
   - Sorting And Reversing
   - Stack And Queue Implementation
3. Shallow Copy And Deep Copy
   - Understanding Shallow Copy
   - Understanding Deep Copy
   - When To Use Each
4. Comprehensive List Guide
   - All List Methods Explained
   - Practical Examples
5. Tuples
   - Creating Tuples
   - Tuple Operations
   - Tuple Methods
"""

# ========================================
# LIST BASICS
# ========================================

# Lists And Tuple 

Example = ["Hello",7,76.8,False]

print(Example)

print(Example[2])
#       |     |
#     List  Index  ( For Extrating The Value Of That Index )

# Lists Are Mutable

Example[2] = "Anubhav"

print(Example)


"""Advanced List Operations And Methods"""
print("\n--- Comprehensive List Guide ---")

# Creating Lists
emptyList = []
numberList = [1, 2, 3, 4, 5]
mixedList = [1, "Hello", 3.14, True, [1, 2]]
rangeList = list(range(1, 11))  # [1, 2, 3, ..., 10]
print(f"Range List : {rangeList}")

# List Indexing (Positive And Negative)
fruits = ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry']
print(f"\nFirst Element : {fruits[0]}")
print(f"Last Element : {fruits[-1]}")
print(f"Second Last : {fruits[-2]}")

# List Slicing - [start:end:step]
print(f"\nFirst 3 Elements : {fruits[0:3]}")
print(f"From Index 2 To End : {fruits[2:]}")
print(f"Last 2 Elements : {fruits[-2:]}")
print(f"Every Second Element : {fruits[::2]}")
print(f"Reverse List : {fruits[::-1]}")
print(f"Every 2nd In Reverse : {fruits[::-2]}")

# Adding Elements
fruits.append('Fig')  # Add At End
print(f"\nAfter Append : {fruits}")

fruits.insert(1, 'Apricot')  # Insert At Index
print(f"After Insert At Index 1 : {fruits}")

fruits.extend(['Grape', 'Honeydew'])  # Add Multiple Elements
print(f"After Extend : {fruits}")

# Using + Operator To Concatenate
newFruits = fruits + ['Kiwi', 'Lemon']
print(f"Concatenated : {newFruits}")

# Removing Elements
fruits.remove('Apricot')  # Remove First Occurrence
print(f"\nAfter Remove 'Apricot' : {fruits}")

poppedItem = fruits.pop()  # Remove And Return Last
print(f"Popped Item : {poppedItem}")
print(f"After Pop : {fruits}")

poppedAtIndex = fruits.pop(2)  # Remove At Index
print(f"Popped At Index 2 : {poppedAtIndex}")
print(f"After Pop(2) : {fruits}")

# del Keyword
del fruits[0]  # Delete By Index
print(f"After del fruits[0] : {fruits}")

# Clear All Elements
tempList = [1, 2, 3]
tempList.clear()
print(f"After Clear : {tempList}")

# Searching In Lists
numbers = [10, 20, 30, 20, 40, 20]
print(f"\nIndex Of 20 : {numbers.index(20)}")  # First Occurrence
print(f"Index Of 20 After Index 2 : {numbers.index(20, 2)}")  # Search From Index 2
print(f"Count Of 20 : {numbers.count(20)}")  # Count Occurrences

# Check If Element Exists
print(f"30 In numbers? : {30 in numbers}")
print(f"50 In numbers? : {50 in numbers}")
print(f"50 Not In numbers? : {50 not in numbers}")

# Sorting Lists
unsorted = [5, 2, 9, 1, 7]
unsorted.sort()  # In-Place Sorting
print(f"\nSorted In-Place : {unsorted}")

unsorted2 = [5, 2, 9, 1, 7]
unsorted2.sort(reverse=True)  # Descending
print(f"Sorted Descending : {unsorted2}")

unsorted3 = [5, 2, 9, 1, 7]
newSorted = sorted(unsorted3)  # Returns New Sorted List
print(f"Original : {unsorted3}")
print(f"New Sorted : {newSorted}")

# Sorting Strings
words = ['banana', 'Apple', 'cherry', 'Date']
words.sort()  # Case-Sensitive
print(f"Sorted Words : {words}")

words.sort(key=str.lower)  # Case-Insensitive
print(f"Case-Insensitive Sort : {words}")

# Reverse List
nums = [1, 2, 3, 4, 5]
nums.reverse()  # In-Place Reverse
print(f"\nReversed : {nums}")

# List Comprehensions
squares = [x**2 for x in range(1, 11)]
print(f"\nSquares : {squares}")

evens = [x for x in range(1, 21) if x % 2 == 0]
print(f"Even Numbers : {evens}")

# Nested List Comprehensions
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print(f"Flattened Matrix : {flattened}")

# List Unpacking
a, b, c = [1, 2, 3]
print(f"\nUnpacked : a={a}, b={b}, c={c}")

# Extended Unpacking
first, *middle, last = [1, 2, 3, 4, 5]
print(f"First : {first}, Middle : {middle}, Last : {last}")

# List Multiplication
repeated = [0] * 5
print(f"\nRepeated : {repeated}")

# Nested Lists (2D Arrays)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(f"\nMatrix : {matrix}")
print(f"Element At [1][2] : {matrix[1][2]}")  # 6

# Iterating Through Lists
print("\nIterating Through List:")
for fruit in fruits:
    print(f"  - {fruit}")

# Enumerate - Get Index And Value
print("\nWith Enumerate:")
for index, fruit in enumerate(fruits):
    print(f"  {index}: {fruit}")

# Enumerate With Custom Start
for index, fruit in enumerate(fruits, start=1):
    print(f"  Item {index}: {fruit}")

# Zip - Iterate Multiple Lists
names = ['Anubhav', 'Asha', 'Harry']
ages = [21, 20, 22]
for name, age in zip(names, ages):
    print(f"  {name} Is {age} Years Old")

# List Methods Summary
print("\n--- List Methods Summary ---")
methodsList = [3, 1, 4, 1, 5]
print(f"Original : {methodsList}")
print(f"append(9) Adds 9 At End")
print(f"insert(2, 7) Inserts 7 At Index 2")
print(f"extend([2, 6]) Adds Multiple Elements")
print(f"remove(1) Removes First 1")
print(f"pop() Removes And Returns Last")
print(f"pop(0) Removes And Returns Element At Index 0")
print(f"clear() Removes All Elements")
print(f"index(4) Returns Index Of 4")
print(f"count(1) Returns Count Of 1")
print(f"sort() Sorts In-Place")
print(f"reverse() Reverses In-Place")
print(f"copy() Creates Shallow Copy")

# List As Stack (LIFO - Last In First Out)
print("\n--- List As Stack ---")
stack = []
stack.append(1)  # Push
stack.append(2)
stack.append(3)
print(f"Stack : {stack}")
print(f"Pop : {stack.pop()}")  # Pop
print(f"Stack After Pop : {stack}")

# List As Queue (FIFO - First In First Out) - Use collections.deque For Better Performance
from collections import deque
queue = deque([1, 2, 3])
queue.append(4)  # Enqueue
print(f"\nQueue : {list(queue)}")
print(f"Dequeue : {queue.popleft()}")
print(f"Queue After Dequeue : {list(queue)}")

# List Min, Max, Sum
nums = [5, 2, 9, 1, 7]
print(f"\nMin : {min(nums)}")
print(f"Max : {max(nums)}")
print(f"Sum : {sum(nums)}")
print(f"Length : {len(nums)}")

# All And Any
boolList1 = [True, True, True]
boolList2 = [True, False, True]
boolList3 = [False, False, False]
print(f"\nall([True, True, True]) : {all(boolList1)}")  # True If All Are True
print(f"all([True, False, True]) : {all(boolList2)}")   # False
print(f"any([True, False, True]) : {any(boolList2)}")   # True If Any Is True
print(f"any([False, False, False]) : {any(boolList3)}") # False


SLICING = Example[0:2] 
print(SLICING) # Take 1 Less Than Given Index

# Append Fuction = Used For Adding Value In The Last Of List 
Example.append("Durgaai")

print(Example)


# Sorting The List In Lower To Higher Order 
Example1 = [4,5,3,2,0,9]

Example1.sort() # Only Support Integer

print(Example1)

# For Reversing The Order Of List 
Example1.reverse()
print(Example1)

# Adding An Item At Particular Index 
Example1.insert(3,"Harry")
#               |     |
#            Index (Value To Be Added )
print(Example1)

# Making A true Copy Of List 
Hello = Example1.copy()
print(Hello)

# Delete Element At Particular Index 
print("The Original List : ",Example1)
Example1.pop(3)
print("After pop(3):", Example1)

# Tuples - Immutable Sequences, Similar To Lists But Cannot Be Changed After Creation
print("\n--- Tuples ---")
# Creating Tuples
TupleExample = (1, 2, 3, "Hello", 4.5)
print("Tuple:", TupleExample)

# Tuple Packing And Unpacking
a, b, c = (10, 20, 30)  # Unpacking
print(f"Unpacked : a={a}, b={b}, c={c}")

# Single Element Tuple (Note The Comma)
SingleTuple = (5,)  # Without Comma, It's Just An Int
print("Single Tuple :", SingleTuple, type(SingleTuple))

# Tuple Methods
print("Count Of 2 In Tuple:", TupleExample.count(2))  # Count Occurrences
print("Index Of 'Hello':", TupleExample.index("Hello"))  # Find Index

# Tuples Are Immutable - This Will Error If Uncommented
# TupleExample[0] = 99  # TypeError: 'tuple' Object Does Not Support Item Assignment

# Use Cases: As Dictionary Keys (Since Immutable), Returning Multiple Values From Functions

# For Join Two List 
Example.extend(Example1)
print(Example)

# Remove The Value In List By Defining Value 
Example.remove("Anubhav")
print(Example)

# To Count Particular Value In List
C = Example.count(9)
print(C)

# Creating New Sorted List Without Distrubing Old List
Example3 = [4,6,2,7,9,0,23,46]
Example2 = sorted(Example3)
print(Example3)
print(Example2)

# To Clear All Values In List 
Example3.clear()
print(Example3) 

NUM1 = [1,2,3,4]
# We Can Do Unpacking Of List 
A1,B1,C1,D1 = NUM1
# We Can Sum Of Int In The List 
Sum = sum(NUM1)
print(Sum)

# Iterating Two List At Same Time 
'We Use Zip(a,b)'

Example4 = [1,2,3,4]
Example5 = [5,6,7,8]
Example6 = zip(Example4,Example5)
print(Example6)

"""Nested List"""

Example7 = [[1,2,3],[4,5,6],[7,8,9]]
print(Example7[2][1])


# Tuples Created By "()"

# For Empty Tuple 
ExampleT = ()
print(type(ExampleT))

# Tuple With Only One Value
ExampleTR = (1,)
print(type(ExampleTR))

" Tuples Are Immutable "

# For Finding Index Of Value 
Tuple = (2,6,"Anu",98.0,True)
print(Tuple.index(98.0))

# Slicing Tuple 
Tuple = (2,6,"Anu",98.0,True)
print(Tuple[1:3])

# Deleting Tuple 
del Tuple

# Length Of Tuple
Tuple = (2,6,"Anu",98.0,True)
print(len(Tuple))

# Unpacking Tuples In Individual Variable 
Tuple = (2,6,"Anu",98.0,True)
A , B , C , D , E = Tuple
print(A , B , C , D , E)


"""Shallow Copy And Deep Copy"""
print("\n--- Shallow Copy And Deep Copy ---")

import copy

# Shallow Copy - Creates A New Object But References Same Nested Objects
print("\n=== Shallow Copy ===")

originalList = [1, 2, [3, 4], 5]
print(f"Original List : {originalList}")

# Method 1: Using copy() Method
shallowCopy1 = originalList.copy()

# Method 2: Using list() Constructor
shallowCopy2 = list(originalList)

# Method 3: Using Slicing
shallowCopy3 = originalList[:]

# Method 4: Using copy.copy()
shallowCopy4 = copy.copy(originalList)

print(f"Shallow Copy : {shallowCopy1}")

# Modify Top-Level Element
shallowCopy1[0] = 999
print(f"\nAfter Modifying Top-Level Element In Shallow Copy:")
print(f"Original List : {originalList}")  # Unchanged
print(f"Shallow Copy : {shallowCopy1}")    # Changed

# Modify Nested Element (THIS IS THE KEY DIFFERENCE!)
shallowCopy1[2][0] = 'CHANGED'
print(f"\nAfter Modifying Nested Element In Shallow Copy:")
print(f"Original List : {originalList}")  # ALSO CHANGED! (Because Nested List Is Shared)
print(f"Shallow Copy : {shallowCopy1}")    # Changed

# Explanation: Shallow Copy Creates New Container But References Same Nested Objects
print("\n*** Shallow Copy Only Copies The Outer Container ***")
print("*** Nested Objects Are Still Shared Between Original And Copy ***")

# Deep Copy - Creates Completely Independent Copy (Including Nested Objects)
print("\n\n=== Deep Copy ===")

originalList2 = [1, 2, [3, 4], 5]
print(f"Original List : {originalList2}")

# Using copy.deepcopy()
deepCopy = copy.deepcopy(originalList2)
print(f"Deep Copy : {deepCopy}")

# Modify Top-Level Element
deepCopy[0] = 999
print(f"\nAfter Modifying Top-Level Element In Deep Copy:")
print(f"Original List : {originalList2}")  # Unchanged
print(f"Deep Copy : {deepCopy}")            # Changed

# Modify Nested Element
deepCopy[2][0] = 'CHANGED'
print(f"\nAfter Modifying Nested Element In Deep Copy:")
print(f"Original List : {originalList2}")  # UNCHANGED! (Nested List Is Copied)
print(f"Deep Copy : {deepCopy}")            # Changed

print("\n*** Deep Copy Creates Completely Independent Copy ***")
print("*** Including All Nested Objects ***")

# Practical Example With Dictionary
print("\n\n=== Shallow Copy Vs Deep Copy With Dictionary ===")

originalDict = {
    'name': 'Anubhav',
    'age': 21,
    'skills': ['Python', 'JavaScript'],
    'address': {
        'city': 'Mumbai',
        'country': 'India'
    }
}

# Shallow Copy Of Dictionary
shallowDict = originalDict.copy()
# Or: shallowDict = copy.copy(originalDict)

# Deep Copy Of Dictionary
deepDict = copy.deepcopy(originalDict)

# Modify Nested List In Shallow Copy
shallowDict['skills'].append('SQL')
print(f"\nOriginal Dict Skills : {originalDict['skills']}")  # CHANGED!
print(f"Shallow Dict Skills : {shallowDict['skills']}")      # Changed

# Modify Nested Dict In Deep Copy
deepDict['address']['city'] = 'Delhi'
print(f"\nOriginal Dict City : {originalDict['address']['city']}")  # UNCHANGED
print(f"Deep Dict City : {deepDict['address']['city']}")            # Changed

# When To Use Each:
print("\n=== When To Use Shallow Copy Vs Deep Copy ===")
print("Shallow Copy:")
print("  - When List/Dict Contains Only Immutable Objects (int, str, tuple)")
print("  - Faster And Uses Less Memory")
print("  - Example: [1, 2, 3, 'hello', 5.5]")

print("\nDeep Copy:")
print("  - When List/Dict Contains Mutable Nested Objects (lists, dicts)")
print("  - Need Complete Independence From Original")
print("  - Example: [[1, 2], {'key': [3, 4]}]")

# Assignment Vs Copy
print("\n\n=== Assignment Vs Copy ===")
list1 = [1, 2, 3]
list2 = list1           # Assignment (Same Object)
list3 = list1.copy()    # Shallow Copy (New Object)

list2[0] = 999
print(f"List1 : {list1}")  # Changed! (list2 Is Same Object)
print(f"List2 : {list2}")  # Changed
print(f"List3 : {list3}")  # Unchanged (Different Object)

print(f"\nlist1 Is list2 : {list1 is list2}")  # True (Same Object)
print(f"list1 Is list3 : {list1 is list3}")    # False (Different Objects)


# ========================================
# TUPLES - COMPREHENSIVE GUIDE
# ========================================
print("\n\n" + "="*60)
print("TUPLES - COMPREHENSIVE GUIDE")
print("="*60)

print("""
ASCII Art: Tuple Structure
┌─────────────────────────────────────┐
│   TUPLE = IMMUTABLE SEQUENCE        │
│                                     │
│   ( 'apple', 'banana', 'cherry' )   │
│     ↑         ↑          ↑          │
│   Index 0   Index 1   Index 2       │
│                                     │
│   ✓ Cannot Modify Elements         │
│   ✓ Faster Than Lists              │
│   ✓ Can Be Dictionary Keys         │
└─────────────────────────────────────┘
""")

# Creating Tuples
print("\n=== Creating Tuples ===")

# Empty Tuple
emptyTuple = ()
print(f"Empty Tuple: {emptyTuple}, Type: {type(emptyTuple)}")

# Single Element Tuple (Note The Comma!)
singleTuple = (42,)  # Comma Is Required
notTuple = (42)      # This Is Just An Integer
print(f"Single Element Tuple: {singleTuple}, Type: {type(singleTuple)}")
print(f"Not A Tuple: {notTuple}, Type: {type(notTuple)}")

# Multiple Elements
fruits = ('apple', 'banana', 'cherry')
numbers = (1, 2, 3, 4, 5)
mixed = (1, 'hello', 3.14, True, [1, 2])
print(f"\nFruits Tuple: {fruits}")
print(f"Numbers Tuple: {numbers}")
print(f"Mixed Tuple: {mixed}")

# Tuple Without Parentheses (Tuple Packing)
coordinates = 10, 20, 30
print(f"\nTuple Packing: {coordinates}")

# Nested Tuples
nestedTuple = ((1, 2), (3, 4), (5, 6))
print(f"Nested Tuple: {nestedTuple}")

# Tuple From Other Iterables
tupleFromList = tuple([1, 2, 3, 4])
tupleFromString = tuple("hello")
tupleFromRange = tuple(range(1, 6))
print(f"\nFrom List: {tupleFromList}")
print(f"From String: {tupleFromString}")
print(f"From Range: {tupleFromRange}")

# Tuple Indexing And Slicing
print("\n\n=== Tuple Indexing And Slicing ===")

colors = ('red', 'green', 'blue', 'yellow', 'purple')
print(f"Colors: {colors}")

# Positive Indexing
print(f"\nFirst Color: {colors[0]}")
print(f"Third Color: {colors[2]}")
print(f"Last Color: {colors[4]}")

# Negative Indexing
print(f"\nLast Color (Negative): {colors[-1]}")
print(f"Second Last: {colors[-2]}")

# Slicing
print(f"\nFirst Three: {colors[0:3]}")
print(f"From Index 2: {colors[2:]}")
print(f"Up To Index 3: {colors[:3]}")
print(f"Every Second: {colors[::2]}")
print(f"Reverse: {colors[::-1]}")

# Tuple Unpacking
print("\n\n=== Tuple Unpacking ===")

# Basic Unpacking
person = ('Anubhav', 21, 'Mumbai')
name, age, city = person
print(f"Name: {name}, Age: {age}, City: {city}")

# Unpacking With * (Star)
numbers = (1, 2, 3, 4, 5, 6, 7)
first, *middle, last = numbers
print(f"\nFirst: {first}")
print(f"Middle: {middle}")
print(f"Last: {last}")

# Swapping Variables Using Tuples
a, b = 10, 20
print(f"\nBefore Swap: a={a}, b={b}")
a, b = b, a  # Tuple Unpacking For Swap
print(f"After Swap: a={a}, b={b}")

# Function Returning Multiple Values (Returns Tuple)
def getPersonInfo():
    return "Anubhav", 21, "Developer"

personName, personAge, profession = getPersonInfo()
print(f"\nFunction Return: {personName}, {personAge}, {profession}")

# Tuple Methods
print("\n\n=== Tuple Methods ===")
print("Tuples Have Only 2 Methods (Immutable!)")

sample = (1, 2, 3, 2, 4, 2, 5)
print(f"\nSample Tuple: {sample}")

# count() - Count Occurrences
count2 = sample.count(2)
print(f"Count Of 2: {count2}")

# index() - Find First Index
index2 = sample.index(2)
print(f"First Index Of 2: {index2}")

# index() With Start And End
index2Start = sample.index(2, 2, 7)  # Search From Index 2 To 7
print(f"Index Of 2 (Starting From Index 2): {index2Start}")

# Tuple Operations
print("\n\n=== Tuple Operations ===")

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

# Concatenation
combined = tuple1 + tuple2
print(f"Concatenation: {tuple1} + {tuple2} = {combined}")

# Repetition
repeated = tuple1 * 3
print(f"Repetition: {tuple1} * 3 = {repeated}")

# Membership
print(f"\n2 In tuple1: {2 in tuple1}")
print(f"7 In tuple1: {7 in tuple1}")

# Length
print(f"Length Of tuple1: {len(tuple1)}")

# Min, Max, Sum (For Numeric Tuples)
numTuple = (5, 2, 9, 1, 7)
print(f"\nNumeric Tuple: {numTuple}")
print(f"Min: {min(numTuple)}")
print(f"Max: {max(numTuple)}")
print(f"Sum: {sum(numTuple)}")

# Sorted (Returns List!)
sortedResult = sorted(numTuple)
print(f"Sorted (Returns List): {sortedResult}")

# Tuple Vs List Comparison
print("\n\n=== Tuple Vs List Comparison ===")

print("""
┌──────────────────┬────────────────┬──────────────────┐
│    Feature       │     Tuple      │      List        │
├──────────────────┼────────────────┼──────────────────┤
│  Mutability      │   Immutable    │    Mutable       │
│  Syntax          │   ( )          │     [ ]          │
│  Speed           │   Faster       │    Slower        │
│  Memory          │   Less         │     More         │
│  Methods         │   2 Only       │   Many (11+)     │
│  Dict Keys       │   Yes ✓       │     No ✗        │
│  Use Case        │   Fixed Data   │  Dynamic Data    │
└──────────────────┴────────────────┴──────────────────┘
""")

# Immutability Demonstration
print("\n=== Immutability Demonstration ===")

myTuple = (1, 2, 3)
print(f"Original Tuple: {myTuple}")

# This Will Raise Error (Commented Out)
# myTuple[0] = 100  # TypeError: 'tuple' object does not support item assignment

# But Tuple With Mutable Elements Can Have Those Elements Modified
tupleWithList = (1, 2, [3, 4])
print(f"\nTuple With List: {tupleWithList}")
tupleWithList[2].append(5)  # Modify The List Inside
print(f"After Modifying Inner List: {tupleWithList}")
print("Note: Tuple Itself Didn't Change, But Mutable Element Did!")

# Tuples As Dictionary Keys
print("\n\n=== Tuples As Dictionary Keys ===")

# Valid - Tuple Keys
locations = {
    (40.7128, -74.0060): "New York",
    (51.5074, -0.1278): "London",
    (35.6762, 139.6503): "Tokyo"
}
print("Locations Dict With Tuple Keys:")
for coords, city in locations.items():
    print(f"  {coords} -> {city}")

# Invalid - List Keys (Would Raise Error)
# locations = {[40.7128, -74.0060]: "New York"}  # TypeError: unhashable type: 'list'

# Named Tuples (Preview - More In Chapter 28)
print("\n\n=== Named Tuples (Preview) ===")
from collections import namedtuple

# Define Named Tuple
Student = namedtuple('Student', ['name', 'age', 'grade'])

# Create Instance
student1 = Student('Anubhav', 21, 'A')
student2 = Student(name='Priya', age=20, grade='A+')

print(f"Student 1: {student1}")
print(f"Access By Index: {student1[0]}")
print(f"Access By Name: {student1.name}")
print(f"\nStudent 2 Grade: {student2.grade}")

# Convert To Dict
studentDict = student1._asdict()
print(f"\nAs Dictionary: {studentDict}")

# Advanced Tuple Techniques
print("\n\n=== Advanced Tuple Techniques ===")

# Tuple Comprehension (Actually Generator!)
tupleComp = tuple(x**2 for x in range(1, 6))
print(f"Tuple From Generator: {tupleComp}")

# Zip With Tuples
names = ('Alice', 'Bob', 'Charlie')
ages = (25, 30, 35)
combined = tuple(zip(names, ages))
print(f"\nZipped Tuples: {combined}")

# Enumerate With Tuples
fruits = ('apple', 'banana', 'cherry')
enumerated = tuple(enumerate(fruits))
print(f"Enumerated: {enumerated}")

# All And Any With Tuples
boolTuple1 = (True, True, True)
boolTuple2 = (True, False, True)
print(f"\nall({boolTuple1}): {all(boolTuple1)}")
print(f"any({boolTuple2}): {any(boolTuple2)}")

# Tuple Best Practices
print("\n\n=== Tuple Best Practices ===")
print("""
1. Use Tuples For Fixed Data That Shouldn't Change
   ✓ Coordinates: (x, y, z)
   ✓ RGB Colors: (255, 128, 0)
   ✓ Database Records: (id, name, email)

2. Use Tuples As Dictionary Keys
   ✓ locations = {(lat, lon): "City Name"}

3. Return Multiple Values From Functions
   ✓ return status, message, data

4. Use Tuples For Unpacking
   ✓ x, y, z = get_coordinates()

5. Use Named Tuples For Clarity
   ✓ Point = namedtuple('Point', ['x', 'y'])

REMEMBER: Single Element Tuple Needs Comma!
   ✓ (42,)  <- Tuple
   ✗ (42)   <- Integer
""")

# Performance Comparison
print("\n\n=== Performance: Tuple Vs List ===")
import time

# Tuple Creation Speed
start = time.time()
for _ in range(1000000):
    t = (1, 2, 3, 4, 5)
tupleTime = time.time() - start

# List Creation Speed
start = time.time()
for _ in range(1000000):
    l = [1, 2, 3, 4, 5]
listTime = time.time() - start

print(f"Tuple Creation: {tupleTime:.4f} seconds")
print(f"List Creation: {listTime:.4f} seconds")
print(f"Tuple Is {listTime/tupleTime:.2f}x Faster!")

# Memory Comparison
import sys
sampleTuple = (1, 2, 3, 4, 5)
sampleList = [1, 2, 3, 4, 5]
print(f"\nTuple Memory: {sys.getsizeof(sampleTuple)} bytes")
print(f"List Memory: {sys.getsizeof(sampleList)} bytes")
print(f"Tuple Uses Less Memory!")

print("\n" + "="*60)
print("END OF TUPLES COMPREHENSIVE GUIDE")
print("="*60)

# Chapter Finished 
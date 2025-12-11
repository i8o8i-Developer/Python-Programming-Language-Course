# Chapter 17: Lambda Functions, Map, Filter, Reduce

"""
TABLE OF CONTENTS:
1. Virtual Environment Setup
2. Pip Freeze And Requirements
3. Lambda Functions
   - Basic Lambda
   - Lambda With Conditionals
   - Lambda With Strings
   - Lambda In List Operations
   - Advanced Lambda Examples
4. Map Function
   - Basic Map Usage
   - Map With Multiple Lists
   - Map With Dictionaries
   - Advanced Map Examples
5. Filter Function
   - Basic Filter Usage
   - Filter With Multiple Conditions
   - Filter With Custom Functions
   - Advanced Filter Examples
6. Reduce Function
   - Basic Reduce Usage
   - Reduce With Custom Logic
   - Advanced Reduce Examples
7. Combining Map, Filter, Reduce
   - Chained Operations
   - Real-World Data Processing
"""

# ========================================
# VIRTUAL ENVIRONMENT
# ========================================

# Advanced Concepts Of Python 

# Virtual Environment 
'pip install virtualenv'

# To Create An Environment ( Windows )
' Execute This Command : virtualenv <Name> '
' Execute This Command : python -m venv <Name> '

# To Activate An Environment ( Windows )
' Execute This Command : .\<Name>\Scripts\activate.bat '

# To Deactivate An Environment ( Windows )
' Execute This Command : deactivate'

# Pip Freeze Command 
'pip freeze > OuputFolder/Requirements.txt'
# Returns All Installed Package Along With Their Version In Given FIle

# TO Install ALl The Packages From A File
'pip install -r OuputFolder/Requirements.txt'

# Lambda Function 
# Lambda Function Is A Function Which Takes An Argument And Returns A Value Without Any Name
# Lambda Function Is Also Called Anonymous Function
# Syntax : lambda arguments : expression
Square = lambda x : x**2
"""
Use Instead Of :
def Square(N):
    return N**2
"""
Square(8)

# Lambda Function With Multiple Arguments
# Lambda Function With Multiple Arguments And Multiple Return Statements
# Syntax : lambda arguments : ( Expression1 , Expression2 , Expression3 , Expression4 , Expression5 )
Sum = lambda A,B,C : ( A+B+C , A*B*C )
Sum(1,2,3)


"""Advanced Lambda Functions"""
print("\n--- Advanced Lambda Functions ---")

# Basic Lambda Examples
print("\n=== Basic Lambda Examples ===")

# Single Argument
square = lambda x: x ** 2
print(f"Square Of 5: {square(5)}")

# Multiple Arguments
add = lambda a, b: a + b
print(f"Sum Of 3 And 7: {add(3, 7)}")

multiply = lambda x, y: x * y
print(f"Product Of 4 And 6: {multiply(4, 6)}")

# Three Arguments
volume = lambda length, width, height: length * width * height
print(f"Volume Of Box (2x3x4): {volume(2, 3, 4)}")

# Lambda With Conditional (Ternary Operator)
print("\n=== Lambda With Conditional ===")

isEven = lambda x: "Even" if x % 2 == 0 else "Odd"
print(f"7 Is: {isEven(7)}")
print(f"10 Is: {isEven(10)}")

maximum = lambda a, b: a if a > b else b
print(f"Maximum Of 15 And 23: {maximum(15, 23)}")

absoluteValue = lambda x: x if x >= 0 else -x
print(f"Absolute Value Of -42: {absoluteValue(-42)}")

# Lambda With String Operations
print("\n=== Lambda With Strings ===")

upperCase = lambda s: s.upper()
print(f"Uppercase 'hello': {upperCase('hello')}")

reverseString = lambda s: s[::-1]
print(f"Reverse 'Python': {reverseString('Python')}")

fullName = lambda first, last: f"{first} {last}"
print(f"Full Name: {fullName('Anubhav', 'Chaurasia')}")

# Lambda In List Operations
print("\n=== Lambda In List Operations ===")

# Sorting With Lambda
students = [
    {"name": "Anubhav", "age": 21},
    {"name": "Asha", "age": 20},
    {"name": "Harry", "age": 22}
]

# Sort By Age
sortedByAge = sorted(students, key=lambda student: student["age"])
print(f"Sorted By Age: {sortedByAge}")

# Sort By Name
sortedByName = sorted(students, key=lambda student: student["name"])
print(f"Sorted By Name: {sortedByName}")

# Sorting Tuples
points = [(1, 5), (3, 2), (2, 8), (4, 1)]
sortedBySecond = sorted(points, key=lambda point: point[1])
print(f"Points Sorted By Second Element: {sortedBySecond}")

# Lambda With map()
print("\n=== Lambda With map() ===")

numbers = [1, 2, 3, 4, 5]

# Square Each Number
squares = list(map(lambda x: x ** 2, numbers))
print(f"Squares: {squares}")

# Double Each Number
doubled = list(map(lambda x: x * 2, numbers))
print(f"Doubled: {doubled}")

# Convert To String
stringNumbers = list(map(lambda x: str(x), numbers))
print(f"As Strings: {stringNumbers}")

# Multiple Lists With map()
list1 = [1, 2, 3, 4]
list2 = [10, 20, 30, 40]
summed = list(map(lambda x, y: x + y, list1, list2))
print(f"Sum Of Two Lists: {summed}")

# Lambda With filter()
print("\n=== Lambda With filter() ===")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filter Even Numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even Numbers: {evens}")

# Filter Odd Numbers
odds = list(filter(lambda x: x % 2 != 0, numbers))
print(f"Odd Numbers: {odds}")

# Filter Numbers Greater Than 5
greaterThan5 = list(filter(lambda x: x > 5, numbers))
print(f"Numbers > 5: {greaterThan5}")

# Filter Strings By Length
words = ["cat", "elephant", "dog", "butterfly", "ant"]
longWords = list(filter(lambda word: len(word) > 3, words))
print(f"Words Longer Than 3 Letters: {longWords}")

# Lambda With reduce()
print("\n=== Lambda With reduce() ===")

from functools import reduce

numbers = [1, 2, 3, 4, 5]

# Sum Using reduce
total = reduce(lambda x, y: x + y, numbers)
print(f"Sum: {total}")

# Product Using reduce
product = reduce(lambda x, y: x * y, numbers)
print(f"Product: {product}")

# Find Maximum
maximum = reduce(lambda x, y: x if x > y else y, numbers)
print(f"Maximum: {maximum}")

# Find Minimum
minimum = reduce(lambda x, y: x if x < y else y, numbers)
print(f"Minimum: {minimum}")

# Lambda In Dictionary Operations
print("\n=== Lambda In Dictionary Operations ===")

# Sort Dictionary By Value
scores = {"Alice": 85, "Bob": 92, "Charlie": 78, "Diana": 95}
sortedScores = dict(sorted(scores.items(), key=lambda item: item[1], reverse=True))
print(f"Sorted Scores: {sortedScores}")

# Filter Dictionary
highScores = dict(filter(lambda item: item[1] >= 85, scores.items()))
print(f"Scores >= 85: {highScores}")

# Transform Dictionary Values
doubledScores = dict(map(lambda item: (item[0], item[1] * 2), scores.items()))
print(f"Doubled Scores: {doubledScores}")

# Nested Lambda
print("\n=== Nested Lambda ===")

# Lambda Returning Lambda
multiply = lambda x: lambda y: x * y
multiplyBy5 = multiply(5)
print(f"5 * 7 = {multiplyBy5(7)}")

multiplyBy10 = multiply(10)
print(f"10 * 3 = {multiplyBy10(3)}")

# Power Function
power = lambda base: lambda exp: base ** exp
square = power(2)
print(f"2^3 = {square(3)}")
print(f"2^4 = {square(4)}")

# Lambda With All() And Any()
print("\n=== Lambda With all() And any() ===")

numbers = [2, 4, 6, 8, 10]
allEven = all(map(lambda x: x % 2 == 0, numbers))
print(f"All Even? {allEven}")

numbers2 = [1, 3, 5, 7, 8]
anyEven = any(map(lambda x: x % 2 == 0, numbers2))
print(f"Any Even? {anyEven}")

# Lambda For Data Processing
print("\n=== Lambda For Data Processing ===")

# Clean And Process Data
data = ["  apple  ", "BANANA", "  Cherry  "]
cleaned = list(map(lambda s: s.strip().lower(), data))
print(f"Cleaned Data: {cleaned}")

# Extract Specific Fields
users = [
    {"name": "Anubhav", "age": 21, "city": "Mumbai"},
    {"name": "Asha", "age": 20, "city": "Delhi"},
    {"name": "Harry", "age": 22, "city": "Bangalore"}
]

names = list(map(lambda user: user["name"], users))
print(f"Names: {names}")

adults = list(filter(lambda user: user["age"] >= 21, users))
print(f"Adults (>=21): {adults}")

# Lambda With enumerate()
print("\n=== Lambda With enumerate() ===")

fruits = ["apple", "banana", "cherry"]
indexed = list(map(lambda item: f"{item[0]}: {item[1]}", enumerate(fruits)))
print(f"Indexed Fruits: {indexed}")

# Lambda With zip()
print("\n=== Lambda With zip() ===")

names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
combined = list(map(lambda pair: f"{pair[0]} is {pair[1]} years old", zip(names, ages)))
for line in combined:
    print(f"  {line}")

# Practical Examples
print("\n=== Practical Examples ===")

# Calculate Grade
getGrade = lambda score: (
    "A" if score >= 90 else
    "B" if score >= 80 else
    "C" if score >= 70 else
    "D" if score >= 60 else
    "F"
)
print(f"Grade For 85: {getGrade(85)}")

# Temperature Conversion
celsiusToFahrenheit = lambda c: (c * 9/5) + 32
fahrenheitToCelsius = lambda f: (f - 32) * 5/9
print(f"25°C In Fahrenheit: {celsiusToFahrenheit(25)}")
print(f"77°F In Celsius: {fahrenheitToCelsius(77)}")

# Calculate Discount
applyDiscount = lambda price, discount: price * (1 - discount/100)
print(f"Price After 20% Discount On $100: ${applyDiscount(100, 20)}")

# Validate Email (Simple)
isValidEmail = lambda email: "@" in email and "." in email.split("@")[1]
print(f"Is 'user@example.com' Valid? {isValidEmail('user@example.com')}")
print(f"Is 'invalid.email' Valid? {isValidEmail('invalid.email')}")

# Lambda Limitations
print("\n=== Lambda Limitations ===")
print("1. Single Expression Only (No Multiple Statements)")
print("2. No Annotations Or Documentation")
print("3. Less Readable For Complex Logic")
print("4. Harder To Debug")
print("5. Use Regular Functions For Complex Logic")

# When To Use Lambda
print("\n=== When To Use Lambda ===")
print("Use Lambda For:")
print("  - Short, Simple Operations")
print("  - One-Time Use Functions")
print("  - map(), filter(), reduce() Operations")
print("  - Sorting With Custom Keys")
print("  - Functional Programming Patterns")

print("\nAvoid Lambda For:")
print("  - Complex Logic")
print("  - Multiple Lines Of Code")
print("  - Functions Needing Documentation")
print("  - Reusable Functions")


""" Map Filter Reduce """
# Map Function
# Map Function Is Used To Apply A Function To All The Elements Of A List
SquareList = [1,2,3,4,5]
Function = lambda x : x**2
Mapping = map(Function , SquareList) # ( <Function> , <List>)
for I in Mapping:
    H = I # Squaring Elements

# Filter Function
# Filter Function Is Used To Filter The Elements Of A List
FilterList = [1,2,3,4,5,6,7,8,9,10]
Function = lambda x : x%2==0
Filtering = filter(Function , FilterList) # ( <Function> , <List>)
for I in Filtering:
    H = I # Filtering Even Numbers

# Reduce Function
# Reduce Function Is Used To Apply A Rolling Computation To Sequential Pairs Of Values In An Iterable
from functools import reduce

ReduceList = [1,2,3,4,5,6,7,8,9,10]
Function = lambda x,y : x+y
Sum = reduce(Function , ReduceList) # ( <Function> , <List>)
# Explanation = (((((((((1+2)+3)+4)+5)+6)+7)+8)+9)+10) 


"""Advanced Map, Filter, And Reduce With Lambda"""
print("\n--- Advanced Map, Filter, Reduce ---")

# MAP FUNCTION - DETAILED EXAMPLES
print("\n=== MAP FUNCTION DETAILED ===")

# Example 1: Square Numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squared = list(map(lambda x: x ** 2, numbers))
print(f"Original: {numbers}")
print(f"Squared: {squared}")

# Example 2: Convert Temperatures
celsius = [0, 10, 20, 30, 40]
fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))
print(f"\nCelsius: {celsius}")
print(f"Fahrenheit: {fahrenheit}")

# Example 3: String Operations
words = ["hello", "world", "python", "programming"]
uppercase = list(map(lambda s: s.upper(), words))
capitalized = list(map(lambda s: s.capitalize(), words))
lengths = list(map(lambda s: len(s), words))
print(f"\nOriginal: {words}")
print(f"Uppercase: {uppercase}")
print(f"Capitalized: {capitalized}")
print(f"Lengths: {lengths}")

# Example 4: Map With Multiple Lists
list1 = [1, 2, 3, 4, 5]
list2 = [10, 20, 30, 40, 50]
list3 = [100, 200, 300, 400, 500]

summed = list(map(lambda x, y: x + y, list1, list2))
print(f"\nSum Of Two Lists: {summed}")

sumThree = list(map(lambda x, y, z: x + y + z, list1, list2, list3))
print(f"Sum Of Three Lists: {sumThree}")

multiplied = list(map(lambda x, y: x * y, list1, list2))
print(f"Element-Wise Multiplication: {multiplied}")

# Example 5: Map With Dictionary
students = [
    {"name": "Alice", "marks": 85},
    {"name": "Bob", "marks": 92},
    {"name": "Charlie", "marks": 78}
]

names = list(map(lambda student: student["name"], students))
marks = list(map(lambda student: student["marks"], students))
print(f"\nNames: {names}")
print(f"Marks: {marks}")

# Add Grade To Each Student
withGrades = list(map(
    lambda s: {**s, "grade": "A" if s["marks"] >= 90 else "B" if s["marks"] >= 80 else "C"},
    students
))
print(f"With Grades: {withGrades}")

# Example 6: Map With Tuples
points = [(1, 2), (3, 4), (5, 6), (7, 8)]
sumPoints = list(map(lambda p: p[0] + p[1], points))
productPoints = list(map(lambda p: p[0] * p[1], points))
print(f"\nPoints: {points}")
print(f"Sum Of Each Point: {sumPoints}")
print(f"Product Of Each Point: {productPoints}")

# Example 7: Complex Map Operations
numbers = [1, 2, 3, 4, 5]
complex = list(map(lambda x: x ** 2 if x % 2 == 0 else x ** 3, numbers))
print(f"\nSquare If Even, Cube If Odd: {complex}")

# FILTER FUNCTION - DETAILED EXAMPLES
print("\n\n=== FILTER FUNCTION DETAILED ===")

# Example 1: Filter Even And Odd
numbers = list(range(1, 21))
evens = list(filter(lambda x: x % 2 == 0, numbers))
odds = list(filter(lambda x: x % 2 != 0, numbers))
print(f"Numbers: {numbers}")
print(f"Evens: {evens}")
print(f"Odds: {odds}")

# Example 2: Filter By Range
greaterThan10 = list(filter(lambda x: x > 10, numbers))
between5And15 = list(filter(lambda x: 5 <= x <= 15, numbers))
print(f"\nGreater Than 10: {greaterThan10}")
print(f"Between 5 And 15: {between5And15}")

# Example 3: Filter Strings
words = ["apple", "banana", "cherry", "date", "elderberry", "fig"]
longWords = list(filter(lambda w: len(w) > 5, words))
startsWithC = list(filter(lambda w: w.startswith('c'), words))
containsE = list(filter(lambda w: 'e' in w, words))
print(f"\nWords: {words}")
print(f"Words > 5 Letters: {longWords}")
print(f"Starts With 'c': {startsWithC}")
print(f"Contains 'e': {containsE}")

# Example 4: Filter Divisibility
numbers = list(range(1, 51))
divisibleBy3 = list(filter(lambda x: x % 3 == 0, numbers))
divisibleBy5 = list(filter(lambda x: x % 5 == 0, numbers))
divisibleBy3And5 = list(filter(lambda x: x % 3 == 0 and x % 5 == 0, numbers))
print(f"\nDivisible By 3: {divisibleBy3}")
print(f"Divisible By 5: {divisibleBy5}")
print(f"Divisible By Both 3 And 5: {divisibleBy3And5}")

# Example 5: Filter Dictionary
students = [
    {"name": "Alice", "age": 20, "grade": 85},
    {"name": "Bob", "age": 22, "grade": 92},
    {"name": "Charlie", "age": 19, "grade": 78},
    {"name": "Diana", "age": 21, "grade": 95}
]

adults = list(filter(lambda s: s["age"] >= 21, students))
highScorers = list(filter(lambda s: s["grade"] >= 90, students))
print(f"\nAdults (>=21): {adults}")
print(f"High Scorers (>=90): {highScorers}")

# Example 6: Filter Prime Numbers
def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

numbers = list(range(1, 31))
primes = list(filter(lambda x: isPrime(x), numbers))
print(f"\nPrime Numbers (1-30): {primes}")

# Example 7: Filter Palindromes
words = ["radar", "hello", "level", "world", "noon", "python"]
palindromes = list(filter(lambda w: w == w[::-1], words))
print(f"\nWords: {words}")
print(f"Palindromes: {palindromes}")

# Example 8: Filter None And Empty
data = [1, None, "hello", "", 0, False, "world", [], {}, 42]
nonEmpty = list(filter(lambda x: x, data))  # Truthy Values
print(f"\nOriginal Data: {data}")
print(f"Non-Empty/Truthy: {nonEmpty}")

# REDUCE FUNCTION - DETAILED EXAMPLES
print("\n\n=== REDUCE FUNCTION DETAILED ===")

from functools import reduce

# Example 1: Sum And Product
numbers = [1, 2, 3, 4, 5]
total = reduce(lambda x, y: x + y, numbers)
product = reduce(lambda x, y: x * y, numbers)
print(f"Numbers: {numbers}")
print(f"Sum: {total}")
print(f"Product: {product}")

# Example 2: Find Maximum And Minimum
numbers = [45, 23, 78, 12, 89, 34, 67]
maximum = reduce(lambda x, y: x if x > y else y, numbers)
minimum = reduce(lambda x, y: x if x < y else y, numbers)
print(f"\nNumbers: {numbers}")
print(f"Maximum: {maximum}")
print(f"Minimum: {minimum}")

# Example 3: String Concatenation
words = ["Hello", "World", "Python", "Programming"]
sentence = reduce(lambda x, y: x + " " + y, words)
print(f"\nWords: {words}")
print(f"Sentence: {sentence}")

# Example 4: Factorial Using Reduce
n = 5
factorial = reduce(lambda x, y: x * y, range(1, n + 1))
print(f"\nFactorial Of {n}: {factorial}")

# Example 5: GCD Of Multiple Numbers
import math
numbers = [48, 64, 80, 96]
gcd = reduce(lambda x, y: math.gcd(x, y), numbers)
print(f"\nGCD Of {numbers}: {gcd}")

# Example 6: Flatten List Of Lists
nestedList = [[1, 2], [3, 4], [5, 6], [7, 8]]
flattened = reduce(lambda x, y: x + y, nestedList)
print(f"\nNested: {nestedList}")
print(f"Flattened: {flattened}")

# Example 7: Count Occurrences
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
counts = reduce(
    lambda acc, word: {**acc, word: acc.get(word, 0) + 1},
    words,
    {}
)
print(f"\nWords: {words}")
print(f"Counts: {counts}")

# Example 8: Reduce With Initial Value
numbers = [1, 2, 3, 4, 5]
sumWithInitial = reduce(lambda x, y: x + y, numbers, 100)  # Start From 100
print(f"\nSum With Initial 100: {sumWithInitial}")

# COMBINING MAP, FILTER, AND REDUCE
print("\n\n=== COMBINING MAP, FILTER, REDUCE ===")

# Example 1: Sum Of Squares Of Even Numbers
numbers = list(range(1, 11))
result = reduce(
    lambda x, y: x + y,
    map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers))
)
print(f"Numbers: {numbers}")
print(f"Sum Of Squares Of Evens: {result}")

# Example 2: Product Of Cubes Of Odd Numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = reduce(
    lambda x, y: x * y,
    map(lambda x: x ** 3, filter(lambda x: x % 2 != 0, numbers))
)
print(f"\nProduct Of Cubes Of Odds: {result}")

# Example 3: Process Student Data
students = [
    {"name": "Alice", "marks": 85},
    {"name": "Bob", "marks": 92},
    {"name": "Charlie", "marks": 78},
    {"name": "Diana", "marks": 95}
]

# Get Names Of Students With Marks >= 85
topStudents = list(
    map(
        lambda s: s["name"],
        filter(lambda s: s["marks"] >= 85, students)
    )
)
print(f"\nTop Students (Marks >= 85): {topStudents}")

# Calculate Average Of High Scores
highScores = list(map(lambda s: s["marks"], filter(lambda s: s["marks"] >= 85, students)))
averageHighScore = reduce(lambda x, y: x + y, highScores) / len(highScores)
print(f"Average Of High Scores: {averageHighScore}")

# PRACTICAL REAL-WORLD EXAMPLES
print("\n\n=== PRACTICAL REAL-WORLD EXAMPLES ===")

# Example 1: Process Sales Data
sales = [
    {"product": "Laptop", "price": 50000, "quantity": 2},
    {"product": "Mouse", "price": 500, "quantity": 5},
    {"product": "Keyboard", "price": 1500, "quantity": 3},
    {"product": "Monitor", "price": 15000, "quantity": 1}
]

# Calculate Total Revenue
totalRevenue = reduce(
    lambda x, y: x + y,
    map(lambda sale: sale["price"] * sale["quantity"], sales)
)
print(f"Total Revenue: ₹{totalRevenue}")

# Filter Expensive Items (Price > 1000)
expensiveItems = list(filter(lambda s: s["price"] > 1000, sales))
print(f"Expensive Items: {expensiveItems}")

# Example 2: Text Processing
sentences = [
    "Hello World",
    "Python Programming",
    "Map Filter Reduce",
    "Lambda Functions"
]

# Count Total Words
totalWords = reduce(
    lambda x, y: x + y,
    map(lambda s: len(s.split()), sentences)
)
print(f"\nSentences: {sentences}")
print(f"Total Words: {totalWords}")

# Get All Words In Uppercase
allWords = reduce(
    lambda x, y: x + y,
    map(lambda s: s.split(), sentences)
)
uppercaseWords = list(map(lambda w: w.upper(), allWords))
print(f"All Words Uppercase: {uppercaseWords}")

# Example 3: Grade Calculator
scores = [45, 67, 89, 34, 92, 78, 56, 83, 91, 72]

# Calculate Letter Grades
grades = list(map(
    lambda score: (
        "A" if score >= 90 else
        "B" if score >= 80 else
        "C" if score >= 70 else
        "D" if score >= 60 else
        "F"
    ),
    scores
))
print(f"\nScores: {scores}")
print(f"Grades: {grades}")

# Count Passing Students (>= 50)
passingCount = len(list(filter(lambda s: s >= 50, scores)))
print(f"Passing Students: {passingCount}")

# Calculate Average Of Passing Students
passingScores = list(filter(lambda s: s >= 50, scores))
averagePassing = reduce(lambda x, y: x + y, passingScores) / len(passingScores)
print(f"Average Of Passing Students: {averagePassing:.2f}")

print("\n--- End Of Map, Filter, Reduce Section ---")
 
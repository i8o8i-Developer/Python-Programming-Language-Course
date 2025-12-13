# Chapter 8: Functions And Recursion

"""
TABLE OF CONTENTS:
1. Function Basics
   - Defining Functions
   - Function Arguments
   - Return Values
2. Recursion
   - Basic Recursion (Factorial)
   - Advanced Recursive Functions (18+ Examples)
   - Fibonacci (Multiple Approaches)
   - Tower Of Hanoi
   - GCD And LCM
   - Palindrome Check
   - Binary Search
   - Permutations
   - Array Operations
   - String Reversal
   - List Sum
   - And More...
3. Recursion Best Practices
"""

# ========================================
# FUNCTION BASICS
# ========================================

"Sample"

# def() Is Used To Define A Functiom 
def Sample():
    H = "Hello"
    return H
    # return <value> Return The Computed Value

S = Sample() # Used To Call The Function
print(S)

"""Function With Argument / Invoking Function"""

z = 5 # Variables Defined Outside The Function Are Global Variable

def Cal(X,Y): # X & Y Are Parameter
    Sum = X + Y
    return Sum

# <function-name>(<value-to-be-passed>)

Result = Cal(1,2) # Passing Parameter
print(Result)

"""Default Parameter"""
# If We Don't Pass The Parameter, The Default Value Will Be Used
def Name(H="Hello"): # H="Hello"
    print(f"{H} , Anubhav")
Name() # Using Default Parameter When Not Specified
Name(H="Bye") # Using Passed Parameter


"""Recursion""" # When Function Call Itself

# Factorial
def Factorial(N):
    if N == 1 or N == 0:
        return 1
    else:
        return N * Factorial(N-1)
# Another Meaning :  When Function Runs In Loop Untill Finished By Calling Itself
print(Factorial(4))


"""Advanced Recursive Functions"""
print("\n--- Advanced Recursion Examples ---")

# Example 1: Fibonacci Sequence
print("\n=== Fibonacci Sequence ===")
def Fibonacci(n):
    """Return nth Fibonacci Number"""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)

print("First 10 Fibonacci Numbers:")
for i in range(10):
    print(f"Fib({i}) = {Fibonacci(i)}")

# Example 2: Fibonacci With Memoization (Optimized)
print("\n=== Fibonacci With Memoization ===")
def FibonacciMemo(n, memo={}):
    """Optimized Fibonacci Using Memoization"""
    if n in memo:
        return memo[n]
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        memo[n] = FibonacciMemo(n - 1, memo) + FibonacciMemo(n - 2, memo)
        return memo[n]

print(f"Fib(30) With Memoization: {FibonacciMemo(30)}")

# Example 3: Sum Of Natural Numbers
print("\n=== Sum Of Natural Numbers ===")
def SumOfN(n):
    """Calculate Sum Of Numbers From 1 To n"""
    if n <= 1:
        return n
    else:
        return n + SumOfN(n - 1)

print(f"Sum Of 1 To 10: {SumOfN(10)}")

# Example 4: Power Function
print("\n=== Power Function ===")
def Power(base, exponent):
    """Calculate base^exponent Using Recursion"""
    if exponent == 0:
        return 1
    elif exponent < 0:
        return 1 / Power(base, -exponent)
    else:
        return base * Power(base, exponent - 1)

print(f"2^5 = {Power(2, 5)}")
print(f"3^4 = {Power(3, 4)}")
print(f"2^-3 = {Power(2, -3)}")

# Example 5: GCD (Greatest Common Divisor) - Euclidean Algorithm
print("\n=== GCD Using Euclidean Algorithm ===")
def GCD(a, b):
    """Calculate GCD Of Two Numbers"""
    if b == 0:
        return a
    else:
        return GCD(b, a % b)

print(f"GCD(48, 18) = {GCD(48, 18)}")
print(f"GCD(100, 35) = {GCD(100, 35)}")

# Example 6: Reverse A String
print("\n=== Reverse String ===")
def ReverseString(s):
    """Reverse A String Using Recursion"""
    if len(s) <= 1:
        return s
    else:
        return ReverseString(s[1:]) + s[0]

print(f"Reverse 'Hello': {ReverseString('Hello')}")
print(f"Reverse 'Python': {ReverseString('Python')}")

# Example 7: Palindrome Check
print("\n=== Palindrome Check ===")
def IsPalindrome(s):
    """Check If String Is Palindrome"""
    s = s.lower().replace(" ", "")
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return IsPalindrome(s[1:-1])

print(f"'radar' Is Palindrome: {IsPalindrome('radar')}")
print(f"'hello' Is Palindrome: {IsPalindrome('hello')}")
print(f"'A man a plan a canal Panama' Is Palindrome: {IsPalindrome('A man a plan a canal Panama')}")

# Example 8: Sum Of Digits
print("\n=== Sum Of Digits ===")
def SumOfDigits(n):
    """Calculate Sum Of All Digits In A Number"""
    if n == 0:
        return 0
    else:
        return n % 10 + SumOfDigits(n // 10)

print(f"Sum Of Digits Of 12345: {SumOfDigits(12345)}")
print(f"Sum Of Digits Of 9876: {SumOfDigits(9876)}")

# Example 9: Count Digits
print("\n=== Count Digits ===")
def CountDigits(n):
    """Count Number Of Digits"""
    if n == 0:
        return 0
    else:
        return 1 + CountDigits(n // 10)

print(f"Number Of Digits In 12345: {CountDigits(12345)}")
print(f"Number Of Digits In 987654321: {CountDigits(987654321)}")

# Example 10: Binary Search (Recursive)
print("\n=== Binary Search ===")
def BinarySearch(arr, target, low, high):
    """Search For Target In Sorted Array"""
    if low > high:
        return -1
    
    mid = (low + high) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return BinarySearch(arr, target, low, mid - 1)
    else:
        return BinarySearch(arr, target, mid + 1, high)

sortedArray = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = 13
result = BinarySearch(sortedArray, target, 0, len(sortedArray) - 1)
print(f"Index Of {target} In Array: {result}")

# Example 11: Tower Of Hanoi
print("\n=== Tower Of Hanoi ===")
def TowerOfHanoi(n, source, destination, auxiliary):
    """
    Solve Tower Of Hanoi Puzzle
    n: Number Of Disks
    source: Source Rod
    destination: Destination Rod
    auxiliary: Auxiliary Rod
    """
    if n == 1:
        print(f"Move Disk 1 From {source} To {destination}")
        return
    
    # Move n-1 Disks From Source To Auxiliary Using Destination
    TowerOfHanoi(n - 1, source, auxiliary, destination)
    
    # Move The Largest Disk From Source To Destination
    print(f"Move Disk {n} From {source} To {destination}")
    
    # Move n-1 Disks From Auxiliary To Destination Using Source
    TowerOfHanoi(n - 1, auxiliary, destination, source)

print("Solving Tower Of Hanoi With 3 Disks:")
TowerOfHanoi(3, 'A', 'C', 'B')

# Example 12: Print Numbers In Ascending And Descending Order
print("\n=== Print Numbers ===")
def PrintAscending(n):
    """Print Numbers From 1 To n"""
    if n > 0:
        PrintAscending(n - 1)
        print(n, end=" ")

def PrintDescending(n):
    """Print Numbers From n To 1"""
    if n > 0:
        print(n, end=" ")
        PrintDescending(n - 1)

print("Ascending (1 To 10):", end=" ")
PrintAscending(10)
print("\nDescending (10 To 1):", end=" ")
PrintDescending(10)
print()

# Example 13: List Sum
print("\n=== List Sum Recursive ===")
def ListSum(lst):
    """Calculate Sum Of List Elements"""
    if not lst:
        return 0
    else:
        return lst[0] + ListSum(lst[1:])

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Sum Of {numbers}: {ListSum(numbers)}")

# Example 14: Flatten Nested List
print("\n=== Flatten Nested List ===")
def FlattenList(lst):
    """Flatten A Nested List"""
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(FlattenList(item))
        else:
            result.append(item)
    return result

nestedList = [1, [2, 3], [4, [5, 6]], 7, [8, [9, 10]]]
print(f"Nested: {nestedList}")
print(f"Flattened: {FlattenList(nestedList)}")

# Example 15: String Permutations
print("\n=== String Permutations ===")
def Permutations(string):
    """Generate All Permutations Of A String"""
    if len(string) <= 1:
        return [string]
    
    perms = []
    for i, char in enumerate(string):
        remaining = string[:i] + string[i+1:]
        for perm in Permutations(remaining):
            perms.append(char + perm)
    
    return perms

result = Permutations("ABC")
print(f"Permutations Of 'ABC': {result}")

# Example 16: Array Maximum
print("\n=== Find Maximum In Array ===")
def FindMax(arr, n):
    """Find Maximum Element In Array Using Recursion"""
    if n == 1:
        return arr[0]
    
    return max(arr[n-1], FindMax(arr, n-1))

numbers = [45, 23, 78, 12, 89, 34]
print(f"Maximum In {numbers}: {FindMax(numbers, len(numbers))}")

# Example 17: Decimal To Binary
print("\n=== Decimal To Binary ===")
def DecimalToBinary(n):
    """Convert Decimal To Binary"""
    if n == 0:
        return 0
    else:
        return n % 2 + 10 * DecimalToBinary(n // 2)

print(f"Binary Of 10: {DecimalToBinary(10)}")
print(f"Binary Of 25: {DecimalToBinary(25)}")

# Example 18: Multiplication Without * Operator
print("\n=== Multiplication Using Addition ===")
def Multiply(a, b):
    """Multiply Two Numbers Using Only Addition"""
    if b == 0:
        return 0
    if b > 0:
        return a + Multiply(a, b - 1)
    if b < 0:
        return -Multiply(a, -b)

print(f"5 * 4 = {Multiply(5, 4)}")
print(f"7 * 3 = {Multiply(7, 3)}")

# Recursion Best Practices
print("\n=== Recursion Best Practices ===")
print("1. Always Have A Base Case (Termination Condition)")
print("2. Ensure The Recursion Moves Towards The Base Case")
print("3. Be Careful Of Stack Overflow With Deep Recursion")
print("4. Consider Memoization For Optimization")
print("5. Sometimes Iteration Is More Efficient Than Recursion")
print("6. Recursion Is Great For: Tree Traversal, Divide-And-Conquer, Backtracking")


"""fUNCTIONS wITH ARGUMENTS"""


# Arbitrary Arguments, *args
# If You Do Not Know How Many Arguments That Will Be Passed Into Your Function , Add (*) Before The Parameter Name In The Function Definition.

# Example
def My_Function(*Kids):
    print("The youngest child is " + Kids[2])

My_Function("Emil", "Tobias", "Linus")


# Keyword Arguments, **kwargs

# If You Do Not Know Which Keyword Arguments That Will Be Passed Into Your Function , Add (**) Before The Parameter Name In The Function Definition.

# Example
def My_Function(**Kid):
    print("His Last Name Is " + Kid["Lname"])
    
My_Function(Fname = "Tobias", Lname = "Refsnes")


# Global Variable
X = 5
Y = 10
# Local Variable
def MyFunc():
    Z = 15
    print(X)
    print(Y)
    print(Z)

# Calling Function
MyFunc()

# TO Modify Global Variable Inside Function
X = 20
def MyFunc():
    global X
    X = 25
    print(X)
MyFunc()
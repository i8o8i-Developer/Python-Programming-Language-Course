# Chapter 7: Loops And Pattern Programming

"""
TABLE OF CONTENTS:
1. While Loop
   - Basic While Loop
   - While Loop Examples
2. For Loop
   - Range Function
   - For Loop Examples
3. Loop Control Statements
   - Break
   - Continue
4. Different Patterns With Loops (25+ Patterns)
   - Number Patterns
   - Star Patterns
   - Pyramid Patterns
   - Diamond Patterns
   - Floyd's Triangle
   - Pascal's Triangle
   - Butterfly Pattern
   - Hourglass Pattern
   - Cross Pattern
   - And More...
"""

# ========================================
# LOOP BASICS
# ========================================

# Two Types Of Loops : 
"For Loop"
"While Loop"

# While Loop
Example = 1
while Example < 10:
    print(Example)
    Example += 1 # Till Here It Will Check Upto 9 And When 10th Statement Is Checked It Passed But Not Printed Because Specified
print(Example) # It Runs Untill Execute ( False )

# Range Function
""" range( 0 , 8 , 2)"""
#          |   |   |
#         0I  LI  SS
'''
0I = First Index
LI = Last Index # (n-1) For Value Output
SS = Step Size
'''

# for i (-) Statement:
'     <---------|  ' # Putting And Comparing Direction

Example = [1,78.0,"Anubhav"]
Example1 = (95,87,65)
Example2 = "ANUBHAV"

# For List 
for i in Example:
    print(i)

# For Tuples
for i in Example1:
    print(i)

# For String
for i in Example2:
    print(i)

# For Reversing The Example2
for i in Example2[::-1]: # Going Backward
    print(i)

"For Loop With Else"

Example = [1,78.0,"Anubhav"]
for i in Example:
    print(i)
else: # When The Loop Is Over It Will Execute Else 
    print("Done")

# For Loop With Break And Continue And Pass
"Break Statement"

Example = [1,78.0,"Anubhav"]
for i in Example:
    if i == "Anubhav":
        break # Exit Loop # Come Out Of Loop When True / When Needed
    print(i)

"Continue Statement"

Example = [1,78.0,"Anubhav"]
for i in Example:
    if i == "Anubhav":
        continue # Skip Particular Iteration But Not Exit The Loop
    print(i)

"Pass Statement"

Example = [1,78.0,"Anubhav"]
for i in Example:
    if i == "Anubhav":
        pass # Null Statement / Skip The Condition / Do Nothing
    print(i)


"""Different Patterns With Loops"""
print("\n--- Pattern Printing With Loops ---")

# Pattern 1: Right-Angled Triangle (Stars)
print("\n=== Pattern 1: Right-Angled Triangle ===")
rows = 5
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
    print()

# Pattern 2: Inverted Right-Angled Triangle
print("\n=== Pattern 2: Inverted Right-Angled Triangle ===")
rows = 5
for i in range(rows, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()

# Pattern 3: Pyramid (Centered Triangle)
print("\n=== Pattern 3: Pyramid ===")
rows = 5
for i in range(1, rows + 1):
    # Print Spaces
    for j in range(rows - i):
        print(" ", end=" ")
    # Print Stars
    for k in range(2 * i - 1):
        print("*", end=" ")
    print()

# Pattern 4: Inverted Pyramid
print("\n=== Pattern 4: Inverted Pyramid ===")
rows = 5
for i in range(rows, 0, -1):
    # Print Spaces
    for j in range(rows - i):
        print(" ", end=" ")
    # Print Stars
    for k in range(2 * i - 1):
        print("*", end=" ")
    print()

# Pattern 5: Diamond
print("\n=== Pattern 5: Diamond ===")
rows = 5
# Upper Half (Pyramid)
for i in range(1, rows + 1):
    for j in range(rows - i):
        print(" ", end=" ")
    for k in range(2 * i - 1):
        print("*", end=" ")
    print()
# Lower Half (Inverted Pyramid)
for i in range(rows - 1, 0, -1):
    for j in range(rows - i):
        print(" ", end=" ")
    for k in range(2 * i - 1):
        print("*", end=" ")
    print()

# Pattern 6: Hollow Diamond
print("\n=== Pattern 6: Hollow Diamond ===")
n = 5
# Upper Half
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end=" ")
    for k in range(2 * i - 1):
        if k == 0 or k == 2 * i - 2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
# Lower Half
for i in range(n - 1, 0, -1):
    for j in range(n - i):
        print(" ", end=" ")
    for k in range(2 * i - 1):
        if k == 0 or k == 2 * i - 2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# Pattern 7: Number Pyramid
print("\n=== Pattern 7: Number Pyramid ===")
rows = 5
for i in range(1, rows + 1):
    for j in range(rows - i):
        print(" ", end=" ")
    for k in range(1, 2 * i):
        print(k, end=" ")
    print()

# Pattern 8: Floyd's Triangle
print("\n=== Pattern 8: Floyd's Triangle ===")
rows = 5
num = 1
for i in range(1, rows + 1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()

# Pattern 9: Pascal's Triangle
print("\n=== Pattern 9: Pascal's Triangle ===")
rows = 6
for i in range(rows):
    # Print Spaces
    for j in range(rows - i):
        print(" ", end=" ")
    # Calculate And Print Values
    num = 1
    for j in range(i + 1):
        print(num, end="   ")
        num = num * (i - j) // (j + 1)
    print()

# Pattern 10: Number Square
print("\n=== Pattern 10: Number Square ===")
rows = 5
for i in range(1, rows + 1):
    for j in range(1, rows + 1):
        print(i, end=" ")
    print()

# Pattern 11: Multiplication Table Pattern
print("\n=== Pattern 11: Multiplication Table Pattern ===")
rows = 5
for i in range(1, rows + 1):
    for j in range(1, rows + 1):
        print(f"{i*j:3}", end=" ")
    print()

# Pattern 12: Alphabet Pattern (A-E)
print("\n=== Pattern 12: Alphabet Pattern ===")
rows = 5
for i in range(rows):
    for j in range(i + 1):
        print(chr(65 + j), end=" ")
    print()

# Pattern 13: Continuous Alphabet Pattern
print("\n=== Pattern 13: Continuous Alphabet Pattern ===")
rows = 5
char = 65  # ASCII Value Of 'A'
for i in range(rows):
    for j in range(i + 1):
        print(chr(char), end=" ")
        char += 1
    print()

# Pattern 14: Reverse Number Triangle
print("\n=== Pattern 14: Reverse Number Triangle ===")
rows = 5
for i in range(rows, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# Pattern 15: Binary Pattern
print("\n=== Pattern 15: Binary Pattern ===")
rows = 5
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print((i + j) % 2, end=" ")
    print()

# Pattern 16: Hollow Square
print("\n=== Pattern 16: Hollow Square ===")
size = 5
for i in range(size):
    for j in range(size):
        if i == 0 or i == size - 1 or j == 0 or j == size - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# Pattern 17: Hollow Right-Angled Triangle
print("\n=== Pattern 17: Hollow Right-Angled Triangle ===")
rows = 5
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        if j == 1 or j == i or i == rows:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# Pattern 18: Butterfly Pattern
print("\n=== Pattern 18: Butterfly Pattern ===")
n = 5
# Upper Half
for i in range(1, n + 1):
    # Left Stars
    for j in range(i):
        print("*", end=" ")
    # Spaces
    for j in range(2 * (n - i)):
        print(" ", end=" ")
    # Right Stars
    for j in range(i):
        print("*", end=" ")
    print()
# Lower Half
for i in range(n, 0, -1):
    # Left Stars
    for j in range(i):
        print("*", end=" ")
    # Spaces
    for j in range(2 * (n - i)):
        print(" ", end=" ")
    # Right Stars
    for j in range(i):
        print("*", end=" ")
    print()

# Pattern 19: Sandglass/Hourglass
print("\n=== Pattern 19: Sandglass/Hourglass ===")
n = 5
# Upper Half (Inverted Pyramid)
for i in range(n, 0, -1):
    for j in range(n - i):
        print(" ", end=" ")
    for k in range(2 * i - 1):
        print("*", end=" ")
    print()
# Lower Half (Pyramid)
for i in range(2, n + 1):
    for j in range(n - i):
        print(" ", end=" ")
    for k in range(2 * i - 1):
        print("*", end=" ")
    print()

# Pattern 20: Number Pyramid With Same Number
print("\n=== Pattern 20: Number Pyramid With Same Number ===")
rows = 5
for i in range(1, rows + 1):
    for j in range(rows - i):
        print(" ", end=" ")
    for k in range(i):
        print(i, end=" ")
    print()

# Pattern 21: Cross Pattern
print("\n=== Pattern 21: Cross Pattern ===")
size = 7
for i in range(size):
    for j in range(size):
        if i == j or i + j == size - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# Pattern 22: Zigzag Pattern
print("\n=== Pattern 22: Zigzag Pattern ===")
rows = 3
cols = 20
for i in range(rows):
    for j in range(cols):
        if ((i + j) % 4 == 0) or (i == 2 and j % 4 == 0):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# Pattern 23: Rectangle With Diagonal
print("\n=== Pattern 23: Rectangle With Diagonal ===")
rows = 5
cols = 8
for i in range(rows):
    for j in range(cols):
        if i == 0 or i == rows - 1 or j == 0 or j == cols - 1 or i == j:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# Pattern 24: Heart Pattern (Advanced)
print("\n=== Pattern 24: Heart Pattern ===")
for i in range(6):
    for j in range(7):
        if (i == 0 and j % 3 != 0) or (i == 1 and j % 3 == 0) or (i - j == 2) or (i + j == 8):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# Pattern 25: Rhombus Pattern
print("\n=== Pattern 25: Rhombus Pattern ===")
rows = 5
for i in range(rows):
    for j in range(rows - i - 1):
        print(" ", end=" ")
    for j in range(rows):
        print("*", end=" ")
    print()

print("\n--- End Of Pattern Section ---")

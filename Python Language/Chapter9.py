# Chapter 9: Built-in Mathematical Functions

"""
TABLE OF CONTENTS:
1. Basic Math Functions
   - abs() - Absolute Value
   - pow() - Power
   - math.sqrt() - Square Root
   - math.factorial() - Factorial
2. Trigonometric Functions
   - sin(), cos(), tan()
   - asin(), acos(), atan()
3. Logarithmic Functions
   - log(), log10(), log2()
4. Advanced Numeric Functions
   - ceil(), floor()
   - round(), trunc()
   - min(), max()
   - divmod()
5. Complex Numbers
6. Random Module
   - random(), uniform()
   - randint(), choice()
   - shuffle(), sample()
7. Special Math Functions
   - GCD, LCM
   - Combinations, Permutations
   - copysign(), frexp(), modf()
"""

# ========================================
# BASIC MATH FUNCTIONS
# ========================================

import math

# Absolute Value / Mod Value
H = abs(-5)
print(f"Mod/Absolute Value : {H}")

# Power { pow(<int>,<power>)}
H = pow(2,3)
print(f"Power : {H} ")

# Square Root
H = math.sqrt(25)
print(f"Square Root : {H} ")

# Factorial
H = math.factorial(5)
print(f"Factorial : {H} ")

# Trignometric Functions
Z = math.sin(90)
X = math.cos(90)
C = math.tan(90)
print(f"Sin : {Z} , Cos : {X} , Tan : {C} ")

# Logarithmic Functions
Log = math.log(10)
print(f"Logs : {Log}")

#Buildit Random Module
import random

# Random Uniform
H = random.uniform(1,10)
print(f"Random Float Value From 1 To 10 : {H}")

# Random Range
J = random.randrange(1,10)
print(f"Random Value From 1 To 10 : {J}")

# Random Choice
K = random.choice([1,2,3,4,5,6,7,8,9,10])
print(f"Random Value From 1,2,3,4,5,6,7,8,9,10 : {K}")

# Random Shuffle
List = [1,2,3,4,5,6,7,8,9,10]
H = random.shuffle(List)
print(H)

# Random Sample ( sample(<list>,<Number Of Element Want To Displayed>) )
H = random.sample([1,2,3,4,5,6,7,8,9,10],5)
print(H)

# Random Int
J = random.randint(1,10)
print(J)

# Random Int Range
Random = random.randrange(1,10,2)
print(Random) # randrange(<start-range>,<end-range>,<step-size>)

# Random Int Choice
Int = random.choice([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
print(Int)

# Random Int Shuffle
List_Int = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
H = random.shuffle(List_Int)
print(H)

# Random Int Sample ( sample(<list>,<Number Of Element Want To Displayed>) )
H = random.sample([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],5)
print(H)

# Sum Function
H = sum([1,2,3,4,5,6,7,8,9,10])
print(H)

# Octal String From Given Number
H = oct(10)
print(H)

# Hexadecimal String From Given Number
H = hex(10)
print(H)

# Binary String From Given Number
H = bin(10)
print(H)

# Decimal String From Given Number
H = str(10)
print(H)

# Round Off Of Given Number
H = round(10.5)
print(H)
H = round(1.23,1) # round( <float> , <Nearest-Int>)
print(H)

# String Useful Consatnts
import string

H = string.ascii_letters
print(H) #abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ

H = string.ascii_lowercase
print(H) #abcdefghijklmnopqrstuvwxyz

H = string.ascii_uppercase
print(H) #ABCDEFGHIJKLMNOPQRSTUVWXYZ

H = string.digits
print(H) #0123456789

H = string.punctuation
print(H) #!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

H = string.printable
print(H) #0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~♂♀

H = string.whitespace
print(H) #      # 

# String Formatting
H = "{} Is Greater Than {}".format(20,10)
print(H) # 0 index , 1 Index

H = "{1},{0}".format(10,20)
print(H) # 1 index , 0 index


"""Advanced Numeric Functions"""
print("\n--- Advanced Numeric Functions ---")

# Min And Max Functions
numbers = [45, 12, 89, 34, 67]
print(f"\nMin Value : {min(numbers)}")
print(f"Max Value : {max(numbers)}")
print(f"Min Of Multiple Args : {min(5, 2, 9, 1)}")
print(f"Max Of Multiple Args : {max(5, 2, 9, 1)}")

# Divmod Function - Returns Quotient And Remainder
quotient, remainder = divmod(17, 5)
print(f"\ndivmod(17, 5) : Quotient = {quotient}, Remainder = {remainder}")

# Complex Number Operations
complexNum1 = 3 + 4j
complexNum2 = 1 + 2j
print(f"\nComplex Number 1 : {complexNum1}")
print(f"Complex Number 2 : {complexNum2}")
print(f"Addition : {complexNum1 + complexNum2}")
print(f"Multiplication : {complexNum1 * complexNum2}")
print(f"Real Part : {complexNum1.real}")
print(f"Imaginary Part : {complexNum1.imag}")
print(f"Conjugate : {complexNum1.conjugate()}")

# Absolute Value Of Complex Number
print(f"Absolute Value Of {complexNum1} : {abs(complexNum1)}")

# Math Module - Ceiling And Floor
import math

print(f"\nCeiling Of 4.3 : {math.ceil(4.3)}")  # Rounds Up
print(f"Floor Of 4.9 : {math.floor(4.9)}")    # Rounds Down
print(f"Truncate 4.9 : {math.trunc(4.9)}")    # Removes Decimal

# Exponential And Logarithm
print(f"\ne^2 : {math.exp(2)}")
print(f"Natural Log Of 10 : {math.log(10)}")
print(f"Log Base 10 Of 100 : {math.log10(100)}")
print(f"Log Base 2 Of 8 : {math.log2(8)}")

# Trigonometric Functions (In Radians)
angleInDegrees = 45
angleInRadians = math.radians(angleInDegrees)
print(f"\n{angleInDegrees} Degrees In Radians : {angleInRadians}")
print(f"Sin(45°) : {math.sin(angleInRadians)}")
print(f"Cos(45°) : {math.cos(angleInRadians)}")
print(f"Tan(45°) : {math.tan(angleInRadians)}")

# Inverse Trigonometric Functions
print(f"\nasin(0.5) In Radians : {math.asin(0.5)}")
print(f"asin(0.5) In Degrees : {math.degrees(math.asin(0.5))}")

# Hyperbolic Functions
print(f"\nsinh(1) : {math.sinh(1)}")
print(f"cosh(1) : {math.cosh(1)}")
print(f"tanh(1) : {math.tanh(1)}")

# Constants
print(f"\nPi : {math.pi}")
print(f"Euler's Number (e) : {math.e}")
print(f"Tau (2*Pi) : {math.tau}")
print(f"Infinity : {math.inf}")

# GCD And LCM
num1, num2 = 48, 18
print(f"\nGCD Of {num1} And {num2} : {math.gcd(num1, num2)}")
print(f"LCM Of {num1} And {num2} : {math.lcm(num1, num2)}")

# Factorial And Combinations
n = 5
print(f"\nFactorial Of {n} : {math.factorial(n)}")
print(f"Permutations P(5,2) : {math.perm(5, 2)}")  # 5!/(5-2)!
print(f"Combinations C(5,2) : {math.comb(5, 2)}")  # 5!/(2!*(5-2)!)

# Power And Square Root
print(f"\n2^10 : {math.pow(2, 10)}")
print(f"Square Root Of 144 : {math.sqrt(144)}")
print(f"Cube Root Of 27 : {math.pow(27, 1/3)}")

# Is Functions For Special Values
print(f"\nIs 5.0 An Integer? : {5.0.is_integer()}")
print(f"Is 5.5 An Integer? : {5.5.is_integer()}")
print(f"Is Finite? : {math.isfinite(100)}")
print(f"Is Infinite? : {math.isinf(math.inf)}")
print(f"Is NaN? : {math.isnan(float('nan'))}")

# Degrees And Radians Conversion
print(f"\n180 Degrees In Radians : {math.radians(180)}")
print(f"Pi Radians In Degrees : {math.degrees(math.pi)}")

# Distance And Hypotenuse
x, y = 3, 4
print(f"\nHypotenuse Of Triangle With Sides {x} And {y} : {math.hypot(x, y)}")
print(f"Euclidean Distance : {math.dist([0, 0], [3, 4])}")

# Sum With Higher Precision
floatList = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
print(f"\nRegular Sum : {sum(floatList)}")
print(f"Math.fsum (Higher Precision) : {math.fsum(floatList)}")

# Remainder And Modulo
print(f"\nRemainder(17, 5) : {math.remainder(17, 5)}")
print(f"Modulo 17 % 5 : {17 % 5}")

# CopySign - Copy Sign From One Number To Another
print(f"\nCopySign(5, -1) : {math.copysign(5, -1)}")  # Returns -5.0
print(f"CopySign(-5, 1) : {math.copysign(-5, 1)}")   # Returns 5.0

# Frexp And Ldexp - Mantissa And Exponent
mantissa, exponent = math.frexp(16)
print(f"\nfrexp(16) : Mantissa = {mantissa}, Exponent = {exponent}")
print(f"ldexp({mantissa}, {exponent}) : {math.ldexp(mantissa, exponent)}")

# Modf - Separate Integer And Fractional Parts
fractional, integer = math.modf(5.75)
print(f"\nmodf(5.75) : Integer = {integer}, Fractional = {fractional}")

# Random Module Advanced
import random

print("\n--- Random Module Advanced ---")

# Random Float Between 0 And 1
print(f"Random Float [0,1) : {random.random()}")

# Random With Seed (Reproducible)
random.seed(42)
print(f"Random With Seed 42 : {random.randint(1, 100)}")
random.seed(42)
print(f"Same Seed Same Result : {random.randint(1, 100)}")

# Random Choices With Weights
items = ['Apple', 'Banana', 'Cherry']
weights = [10, 5, 1]  # Apple Is 10x More Likely Than Cherry
print(f"Weighted Random Choice : {random.choices(items, weights=weights, k=5)}")

# Random Gauss (Normal Distribution)
print(f"Gaussian Random (Mean=0, Std=1) : {random.gauss(0, 1)}")

# Triangular Distribution
print(f"Triangular (Low=0, High=10, Mode=5) : {random.triangular(0, 10, 5)}")

# Beta Distribution
print(f"Beta Distribution : {random.betavariate(2, 5)}")

# Chapter Continued...
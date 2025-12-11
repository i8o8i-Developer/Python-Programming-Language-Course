# ╔═══════════════════════════════════════════════════════════════╗
# ║              CHAPTER 2: VARIABLES AND DATA TYPES              ║
# ╠═══════════════════════════════════════════════════════════════╣
# ║                                                               ║
# ║  TABLE OF CONTENTS:                                           ║
# ║  ═════════════════                                            ║
# ║                                                               ║
# ║  1. Variables (Declaration And Assignment)                    ║
# ║  2. Variable Naming Rules                                     ║
# ║  3. Data Types (int, float, str, bool, None)                  ║
# ║  4. Type Casting (int(), float(), str(), bool())              ║
# ║  5. Type Checking (type() Function)                           ║
# ║                                                               ║
# ╚═══════════════════════════════════════════════════════════════╝


# ═══════════════════════════════════════════════════════════════
#  TOPIC 1: Variables (Declaration And Assignment)
# ═══════════════════════════════════════════════════════════════

# Varialbles

Int = 1 # Int Is Storing The Value = Which Is Integer

Ft = 34.57 # Ft Is Storing The Value = Which Is In Decimal

N = "Anubhav" # N Is Storing The Value = Which Is String And Used By ""

D = True # D Is Storing The Value = Which Is Boolean True/False

E = None # E Is Storing The Value = Which Is Nothing


# ═══════════════════════════════════════════════════════════════
#  TOPIC 2: Variable Naming Rules
# ═══════════════════════════════════════════════════════════════

""" Rules : = >

1. No Space
2. Can Contain Alphabets , Digits , And UnderScore ( _ )
3. Can Start Only With An Alphabet And UnderScore
4. Variable Can't Start With Digits
5. Variable Can't Contain Special Characters

"""


# ═══════════════════════════════════════════════════════════════
#  TOPIC 3: Operaters Overview
# ═══════════════════════════════════════════════════════════════

# Operaters 

Arithmetic_Operaters = " + , - . * , / "
Assignment_Operaters = " = , += , -= , *= , /= "
Comparison_Operaters = " == , != , > , < , >= , <= "
Logical_Operaters = " and , or , not , in "

# ( in ) Is Used To Derecr That Value In Another Set Of Value 


# ═══════════════════════════════════════════════════════════════
#  TOPIC 4: Arithmetic Operaters
# ═══════════════════════════════════════════════════════════════

# Arithmetic_Operaters = > Start  

a = 2
b = 3
c = a + b
print(c)

d = a - b
print(d)

e = a * b
print(e)

f = a / b
print(f)    

g = a % b # Remainder
print(g)

h = a ** b # Power
print(h)

I = a // b # Floor Division
print(I)

" Floor Division Is An Arithmetic Operation That Divides Two Numbers And Rounds The Result Down To The Nearest Whole Number Or Integer "

# Arithmetic_Operaters = > End

# Assignment_Operaters = > Start

a = 2
b = 3
a += b # Increment The Value Of a By Value Of b And Then Assign It To a
print(a)

# Assignment_Operaters = > End

# Comparison_Operaters = > Start

a = 2
b = 3
c = a == b # Return True/False If Value Of a = Value of b
d = a<b # Return True/False If Value Of a < Value of b
e = a>b # Return True/False If Value Of a > Value of b
f = a>=b # Return True/False If Value Of a > or = Value of b
g = a<=b # Return True/False If Value Of a < or = Value of b
h = a!=b # Return True/False If Value Of a Is Not Equal To Value of b
print(c,d,e,f,g,h)

# Comparison_Operaters = > End ( They Return Always Boolean Value)

# Logical_Operaters = > Start
 
# Truth Table Of or 
print("True Or False Is ", True or False)
print("True Or True Is ", True or True)
print("False Or True Is ", False or True)
print("False Or False Is ", False or False)

# Truth Table Of and
print("True And False Is ", True and False)
print("True And True Is ", True and True)
print("False And True Is ", False and True)
print("False And False Is ", False and False)

# Truth Table Of not
print("Not True Is ", not True)
print("Not False Is ", not False)

# Logical_Operaters = > End


# Type Casting And Type() Function 

H = 31.2
I = type(H)
print(I)

J = 31
K = type(J)
print(K)

L = "Anubhav"
M = type(L)
print(M)

print(str(H)) # Convert To String
print(float(J)) # Convert To Float
print(int(H)) # Convert To Integer

print(type(str(H))) # Convert To String And Print Its Type
print(type(float(J))) # Convert To Float And Print Its Type
print(type(int(H))) # Convert To Integer And Print Its Type

# Input function ()

Helo = input("Enter Any Thing : ") # Treated As String
print(type(Helo))

Helo = int(input("Enter Any Number : ")) # Treated As Integer
print(type(Helo))

Helo = float(input("Enter Any Number : ")) # Treated As Float
print(type(Helo))

Extra = " ,%, Gives The Remainder Of 2 Numbers "
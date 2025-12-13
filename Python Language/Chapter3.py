# ╔═══════════════════════════════════════════════════════════════╗
# ║                    CHAPTER 3: STRINGS                         ║
# ╠═══════════════════════════════════════════════════════════════╣
# ║                                                               ║
# ║  TABLE OF CONTENTS:                                           ║
# ║  ═════════════════                                            ║
# ║                                                               ║
# ║  1. String Creation (Single, Double, Multi-line Quotes)       ║
# ║  2. String Indexing (Positive And Negative)                   ║
# ║  3. String Slicing [start:end:step]                           ║
# ║  4. String Length (len() Function)                            ║
# ║  5. String Methods (50+ Methods)                              ║
# ║     - count(), endswith(), startswith()                       ║
# ║     - find(), index(), replace()                              ║
# ║     - capitalize(), title(), upper(), lower()                 ║
# ║     - strip(), split(), join()                                ║
# ║     - And Many More...                                        ║
# ║  6. String Immutability                                       ║
# ║  7. String Concatenation And Repetition                       ║
# ║                                                               ║
# ╚═══════════════════════════════════════════════════════════════╝


# ═══════════════════════════════════════════════════════════════
#  TOPIC 1: String Creation
# ═══════════════════════════════════════════════════════════════

# Strings """Details"""

# Strings Are Immutable & Strings Are Enclosed In Single Or Double Quotes

a = 'Anubhav' # Single Quote
b = "Anubhav" # Double Quote
c = '''Anubhav''' # Multi-Line Quote
d = """Anubhav""" # Multi-Line Quote


# ═══════════════════════════════════════════════════════════════
#  TOPIC 2: String Indexing
# ═══════════════════════════════════════════════════════════════

# Strings Slicing
 
""" Example = Anubhav """

#  A  n  u  b  h  a  v 
#  0  1  2  3  4  5  6 = Indexing
# -7 -6 -5 -4 -3 -2 -1 = Opposite Indexing


# ═══════════════════════════════════════════════════════════════
#  TOPIC 3: String Slicing [start:end:step]
# ═══════════════════════════════════════════════════════════════

Slicing = [a]
print(Slicing)

Real_Slice = a[0:7]  # Start From Index 0 All The Way Till 7 Excluding 7
print(Real_Slice)

Negative_Real_Slice = a[-7:-1]  # Start From Index -7 All The Way Till -1 Excluding -1
print(Negative_Real_Slice)

Character_Slice = a[3] # To Extract A Particular Character
print(Character_Slice)
Negative_Character_Slice = a[-4] #To Extract A Particular Character fROM Backward Direction 
print(Negative_Character_Slice)


# ═══════════════════════════════════════════════════════════════
#  TOPIC 4: String Length
# ═══════════════════════════════════════════════════════════════

# For Length In String
Length = len(a)
print(Length)

# If Conditions

H = a[:4] # a[0:4]
K = a[3:] # a[3: One More Than Index Of Last Index (Positive)]

print(H,K)


# ═══════════════════════════════════════════════════════════════
#  TOPIC 5: String Methods (Comprehensive)
# ═══════════════════════════════════════════════════════════════

# Slicing Skip Value 

SLI = a[2:7:3] # [ First_index : Last_Index : Skip_Value ]
print(SLI)

Hello = "anubhavdhfhjfcxfgfvdfggdg"

# String Methods : Count ( Case-Sensitive )
C = Hello.count("b") # Tells How Many Times The Given Value Is Found
print(C) # Return Count Value ( Positive )

# String Methods : Ends With ( Case-Sensitive )
E = Hello.endswith("y") # Tells Where The String Ends With The Given Value Or Not
print(E) # Return Boolean Value

# String Methods : Starts With ( Case-Sensitive )
S = a.startswith("Anu") # Tells Where The String Starts With The Given Value Or Not
print(S) # Return Boolean Value

# String Methods : Find ( Case-Sensitive )
F = a.find("b") # Tells At Which Index The Given Value Is Found
print(F) # Return Integer Value And return -1 If Not Found The Occurrence

# String Methods : Index ( Case-Sensitive )
I = a.index("b") # Tells At Which Index The Given Value Is Found
print(I) # Return Index Value ( Positive )

# String Methods : Replace ( Case-Sensitive )   
R = a.replace("b","B") # Replaces The Given Value With The Given Value
print(R) # Return String Value

# String Methods : Capitalize ( Case-Sensitive )
C = a.capitalize() # Capitalizes The First Character
print(C) # Return String Value

# String Methods : Title ( Case-Sensitive )
T = a.title() # Capitalizes The First Character Of Each Word
print(T) # Return String Value

# String Methods : Lower ( Case-Sensitive )
L = a.lower() # Makes All Characters Lower
print(L) # Return String Value

# String Methods : Upper ( Case-Sensitive )
U = a.upper() # Makes All Characters Upper
print(U) # Return String Value

# String Methods : Swapcase ( Case-Sensitive )
S = a.swapcase() # Swaps Case (First Char Small )
print(S) # Return String Value

# String Methods : Isalpha ( Case-Sensitive )
I = a.isalpha() # Checks If All Characters Are Alphabets
print(I) # Return Boolean Value

# String Methods : Isdigit ( Case-Sensitive )
D = a.isdigit() # Checks If All Characters Are Digits
print(D) # Return Boolean Value

# String Methods : Isalnum ( Case-Sensitive )
A = a.isalnum() # Checks If All Characters Are Alphabets Or Digits
print(A) # Return Boolean Value

# String Methods : Islower ( Case-Sensitive )
L = a.islower() # Checks If All Characters Are Lower
print(L) # Return Boolean Value

# String Methods : Isupper ( Case-Sensitive )
U = a.isupper() # Checks If All Characters Are Upper
print(U) # Return Boolean Value

# String Methods : Isnumeric ( Case-Sensitive )
N = a.isnumeric() # Checks If All Characters Are Numeric
print(N) # Return Boolean Value

# String Methods : Isprintable ( Case-Sensitive )
P = a.isprintable() # Checks If All Characters Are Printable
print(P) # Return Boolean Value

# String Methods : Isascii ( Case-Sensitive )
A = a.isascii() # Checks If All Characters Are Ascii
print(A) # Return Boolean Value

# String Methods : Isdecimal ( Case-Sensitive )
D = a.isdecimal() # Checks If All Characters Are Decimal
print(D) # Return Boolean Value

# String Methods : Isidentifier ( Case-Sensitive )
I = a.isidentifier() # Checks If All Characters Are Identifier
print(I) # Return Boolean Value

# String Methods : Isspace
S1 = "  ".isspace() # Checks If All Characters Are Space
print(S1) # Return Boolean Value

# String Methods : Split
S2 = "You Are Mad".split() # Splits String Into List
print(S2) # Return List Value

# Example string
a = "hello123"

# Method: strip()
# Description: Removes leading and trailing whitespace characters.
# Usage: a.strip()
# Returns: String (with leading and trailing whitespace removed)
b = "   hello   "
stripped = b.strip()
print(f"strip() - Stripped '{b}' is: '{stripped}'")

# Method: replace()
# Description: Replaces occurrences of a substring with another string.
# Usage: a.replace('l', 'X')
# Returns: String (with replacements made)
replaced = a.replace('l', 'X')
print(f"replace('l', 'X') - '{a}' with 'l' replaced by 'X': '{replaced}'")

# Method: join()
# Description: Joins elements of an iterable (like a list) into a single string.
# Usage: '-'.join(['a', 'b', 'c'])
# Returns: String (joined with specified separator)
joined = '-'.join(['a', 'b', 'c'])
print(f"join(['a', 'b', 'c']) - Join with '-' separator: '{joined}'")

# Method: format()
# Description: Formats a string using placeholders.
# Usage: "Hello, {}!".format('World')
# Returns: String (formatted)
formatted = "Hello, {}!".format('World')
print(f"format('World') - Formatted string: '{formatted}'")

# Method: encode()
# Description: Encodes the string into bytes using a specified encoding.
# Usage: a.encode('utf-8')
# Returns: Bytes (encoded)
encoded = a.encode('utf-8')
print(f"encode('utf-8') - Encoded bytes of '{a}': {encoded}")

# Method: decode()
# Description: Decodes bytes into a string using a specified encoding.
# Usage: encoded.decode('utf-8')
# Returns: String (decoded)
decoded = encoded.decode('utf-8')
print(f"decode('utf-8') - Decoded string from bytes: '{decoded}'")

# Example strings
str1 = "   Hello"
str2 = "World   "
str3 = "Python"

# String Repetition with * operator
# Description: Repeats a string a specified number of times.
# Usage: str3 * 3
# Returns: String (repeated result)
Repeated = str3 * 3
print(f"String Repetition with * operator: '{str3}' * 3 = '{Repeated}'")

# lstrip() - Removes whitespace from the beginning of a string.
# Description: Removes leading whitespace characters.
# Usage: str1.lstrip()
# Returns: String (with leading whitespace removed)
lstripped = str1.lstrip()
print(f"lstrip() - Stripped '{str1}' from the left: '{lstripped}'")

# rstrip() - Removes whitespace from the end of a string.
# Description: Removes trailing whitespace characters.
# Usage: str2.rstrip()
# Returns: String (with trailing whitespace removed)
rstripped = str2.rstrip()
print(f"rstrip() - Stripped '{str2}' from the right: '{rstripped}'")

# Example string
num_str = "42"

# Pad with zeros to make the string 5 characters long
padded_str = num_str.zfill(5)
print(f"Original string: '{num_str}'")
print(f"Padded string with zeros: '{padded_str}'")


# Escape Sequence Strings
Hey = "Anubhav Is A Very Good Character \n He Is Artificial Intelligence \"Developer\""
print(Hey)

# For Double Quote = \"Developer\" = "Developer"
# For Tab Like Space = Hello \t Everyone = Hello       Everyone

# Simple animated loading spinner using \r to overwrite
import time
spinner = ['-', '\\', '|', '/']
for _ in range(10):  # Repeat 10 times
    for char in spinner:
        print(f"Loading... {char}", end='\r')
        time.sleep(0.1)  # Pause for a short time to create animation effect

print("\nLoading complete!")  # Print completion message on a new line

# Round() Function
H = round(3.14159, 2) 
# Round to 2 Decimal Places
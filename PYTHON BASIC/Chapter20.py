# Chapter 20: Advanced Topics - Threading, Regex, Network Programming

"""
TABLE OF CONTENTS:
1. Threading Module
   - Creating Threads
   - Thread Locks
   - Thread Methods

2. Note: AsyncIO Is Covered In Chapter 28

3. Multiprocessing Module

4. Note: Generators Are Covered In Chapter 25

5. Regular Expressions (Comprehensive)
   - Dot Metacharacter
   - Character Classes
   - Quantifiers
   - All Metacharacters
   - compile() Function
   - search() And match()
   - Star, Plus, Curly Braces
   - Caret Metacharacter

6. Note: JSON Is Covered In Chapter 22

7. CSV Module

8. Network Programming
   - IP Addresses
   - Ports And Sockets
   - TCP Client/Server
   - UDP Communication
   - Buffers
   - Multi-Client Server
   - Error Handling
"""

# ========================================
# THREADING AND MULTIPROCESSING
# ========================================

#Function For Threading
import time as Time
def Function(N):
    print(f" Sleeping Program For {N} Seconds")
    Time.sleep(N)

Time_1 = Time.perf_counter()
Function(5)
Function(3)
Function(6)
print("Done")
Time_2 = Time.perf_counter()
print(f"Time Taken : {Time_2 - Time_1} Seconds")

print("Now Implementing Threading ..")

# Threading Module
import threading as Threading

T1 = Threading.Thread(target=Function , args=[5])
T2 = Threading.Thread(target=Function , args=[3])
T3 = Threading.Thread(target=Function , args=[6])

Time_1 = Time.perf_counter()
T1.start()
T2.start()
T3.start()
# For Joining The Threads
T1.join()
T2.join()
T3.join()
Time_2 = Time.perf_counter()
print(f"\nTime Taken : {Time_2 - Time_1} Seconds")
print("Done")

# Locking The Single Thread At Particular part of Code
My_Lock = Threading.Lock()

def Worker():
    My_Lock.acquire()
    try:
        print("Thread", Threading.current_thread().name, "Is Executing The Critical Section")
        Time.sleep(2)
    finally:
        My_Lock.release()

Threads = []
for i in range(5):
    T = Threading.Thread(target=Worker)
    Threads.append(T)
    T.start()

for T in Threads:
    T.join()

# Threading.current_thread().name == Current Thread Name As String
# threading.active_count(): Returns The Number Of Thread Objects Currently Alive.
# threading.current_thread(): Returns The Thread Object Corresponding To The Current Thread.
# threading.main_thread(): Returns The Main Thread Object.
# threading.enumerate(): Returns A List Of All Thread Objects Currently Alive.
# thread.is_alive(): Returns Whether The Thread Is Alive.

# Note: AsyncIO Is Covered In Detail In Chapter 28

''' MULTIPROCESSING MODULE'''

import multiprocessing as MP
import requests as RQ

def DownloadImage():
    pass

# Note: Generators Are Covered In Detail In Chapter 25

'''Regular Expression'''

import re as RE

# RE.search() == Searches For A Pattern In A String
Pattern = "H"
Text = "Hello Harry The Great"

IF = RE.search(Pattern, Text)

# RE.match() == Searches For A Pattern At The Beginning Of A String
Text = "Hello, world!"
Pattern = "Hello"
Match = RE.match(Pattern, Text)


"""Advanced Regular Expressions - Very Detailed"""
print("\n--- COMPREHENSIVE REGULAR EXPRESSIONS GUIDE ---")

import re

# ========================================
# 1. DOT METACHARACTER (.)
# ========================================
print("\n=== DOT METACHARACTER (.) ===")
print("Dot (.) Matches Any Single Character Except Newline")

text = "cat bat rat mat"

# Match Any Character Followed By 'at'
pattern = r'.at'
matches = re.findall(pattern, text)
print(f"Pattern '.at' In '{text}': {matches}")  # ['cat', 'bat', 'rat', 'mat']

# Dot Can Match Letters, Digits, Spaces, Special Characters
text2 = "a1t a@t a t"
matches2 = re.findall(r'.at', text2)
print(f"Pattern '.at' In '{text2}': {matches2}")

# Multiple Dots
text3 = "hello"
pattern3 = r'h...o'  # h + any 3 chars + o
match3 = re.search(pattern3, text3)
print(f"Pattern 'h...o' In '{text3}': {match3.group() if match3 else 'Not Found'}")

# Dot Does NOT Match Newline By Default
text4 = "hello\nworld"
pattern4 = r'hello.world'
match4 = re.search(pattern4, text4)
print(f"Dot Matches Newline By Default? {bool(match4)}")  # False

# Use re.DOTALL Flag To Make Dot Match Newline
match5 = re.search(pattern4, text4, re.DOTALL)
print(f"With re.DOTALL Flag: {bool(match5)}")  # True

# Escape Dot To Match Literal Dot
text5 = "example.com"
pattern5 = r'example\.com'  # \. Matches Literal Dot
match6 = re.search(pattern5, text5)
print(f"Match Literal Dot In '{text5}': {bool(match6)}")


# ========================================
# 2. CHARACTER CLASS [ ]
# ========================================
print("\n\n=== CHARACTER CLASS [ ] ===")
print("Character Class Matches Any ONE Character From The Set")

# Basic Character Class
text = "The year is 2024"
pattern = r'[0-9]'  # Match Any Digit
matches = re.findall(pattern, text)
print(f"Pattern '[0-9]' In '{text}': {matches}")  # ['2', '0', '2', '4']

# Match Vowels
text2 = "Hello World"
pattern2 = r'[aeiouAEIOU]'
matches2 = re.findall(pattern2, text2)
print(f"Vowels In '{text2}': {matches2}")

# Range In Character Class
pattern3 = r'[a-z]'  # Lowercase Letters
pattern4 = r'[A-Z]'  # Uppercase Letters
pattern5 = r'[a-zA-Z]'  # All Letters
pattern6 = r'[0-9]'  # Digits

text3 = "Hello123"
print(f"Lowercase: {re.findall(r'[a-z]', text3)}")
print(f"Uppercase: {re.findall(r'[A-Z]', text3)}")
print(f"Digits: {re.findall(r'[0-9]', text3)}")

# Multiple Ranges
pattern7 = r'[a-zA-Z0-9]'  # Alphanumeric
matches7 = re.findall(pattern7, "Hello123!@#")
print(f"Alphanumeric Characters: {matches7}")

# Negated Character Class [^ ]
print("\n--- Negated Character Class [^ ] ---")
text4 = "Hello123!@#"
pattern8 = r'[^a-zA-Z]'  # NOT A Letter
matches8 = re.findall(pattern8, text4)
print(f"Non-Letters In '{text4}': {matches8}")

pattern9 = r'[^0-9]'  # NOT A Digit
matches9 = re.findall(pattern9, text4)
print(f"Non-Digits In '{text4}': {matches9}")

# Special Characters In Character Class
pattern10 = r'[.@#]'  # Match Dot, @, Or #
text5 = "email@example.com"
matches10 = re.findall(pattern10, text5)
print(f"Special Characters In '{text5}': {matches10}")


# ========================================
# 3. QUANTIFIERS
# ========================================
print("\n\n=== QUANTIFIERS ===")
print("Quantifiers Specify How Many Times A Pattern Should Match")

# STAR METACHARACTER (*)
print("\n--- STAR METACHARACTER (*) ---")
print("* Matches 0 Or More Occurrences")

text = "ac abc abbc abbbc"
pattern = r'ab*c'  # a + zero or more b + c
matches = re.findall(pattern, text)
print(f"Pattern 'ab*c' In '{text}': {matches}")  # ['ac', 'abc', 'abbc', 'abbbc']

text2 = "gooooogle"
pattern2 = r'go*gle'  # g + zero or more o + gle
matches2 = re.findall(pattern2, text2)
print(f"Pattern 'go*gle' In '{text2}': {matches2}")

# PLUS METACHARACTER (+)
print("\n--- PLUS METACHARACTER (+) ---")
print("+ Matches 1 Or More Occurrences")

text3 = "ac abc abbc abbbc"
pattern3 = r'ab+c'  # a + one or more b + c
matches3 = re.findall(pattern3, text3)
print(f"Pattern 'ab+c' In '{text3}': {matches3}")  # ['abc', 'abbc', 'abbbc'] (NOT 'ac')

text4 = "gooooogle"
pattern4 = r'go+gle'  # g + one or more o + gle
matches4 = re.findall(pattern4, text4)
print(f"Pattern 'go+gle' In '{text4}': {matches4}")

# QUESTION MARK (?)
print("\n--- QUESTION MARK (?) ---")
print("? Matches 0 Or 1 Occurrence (Optional)")

text5 = "color colour"
pattern5 = r'colou?r'  # colo + optional u + r
matches5 = re.findall(pattern5, text5)
print(f"Pattern 'colou?r' In '{text5}': {matches5}")  # ['color', 'colour']

text6 = "http https"
pattern6 = r'https?'  # http + optional s
matches6 = re.findall(pattern6, text6)
print(f"Pattern 'https?' In '{text6}': {matches6}")

# CURLY BRACES {n}, {n,}, {n,m}
print("\n--- CURLY BRACES QUANTIFIERS ---")
print("{n} = Exactly n Occurrences")
print("{n,} = n Or More Occurrences")
print("{n,m} = Between n And m Occurrences")

# {n} - Exactly n
text7 = "abc abbc abbbc abbbbc"
pattern7 = r'ab{2}c'  # a + exactly 2 b + c
matches7 = re.findall(pattern7, text7)
print(f"Pattern 'ab{{2}}c' In '{text7}': {matches7}")  # ['abbc']

# {n,} - n Or More
pattern8 = r'ab{2,}c'  # a + 2 or more b + c
matches8 = re.findall(pattern8, text7)
print(f"Pattern 'ab{{2,}}c' In '{text7}': {matches8}")  # ['abbc', 'abbbc', 'abbbbc']

# {n,m} - Between n And m
pattern9 = r'ab{2,3}c'  # a + 2 to 3 b + c
matches9 = re.findall(pattern9, text7)
print(f"Pattern 'ab{{2,3}}c' In '{text7}': {matches9}")  # ['abbc', 'abbbc']

# Practical Examples
text8 = "Phone: 123-456-7890"
pattern10 = r'\d{3}-\d{3}-\d{4}'  # 3 digits - 3 digits - 4 digits
match10 = re.search(pattern10, text8)
print(f"Phone Number Pattern: {match10.group() if match10 else 'Not Found'}")

text9 = "ZIP: 12345"
pattern11 = r'\d{5}'  # Exactly 5 digits
match11 = re.search(pattern11, text9)
print(f"ZIP Code: {match11.group() if match11 else 'Not Found'}")


# ========================================
# 4. ALL METACHARACTERS
# ========================================
print("\n\n=== ALL METACHARACTERS ===")

# CARET METACHARACTER (^)
print("\n--- CARET METACHARACTER (^) ---")
print("^ Matches Start Of String")

text = "Hello World"
pattern = r'^Hello'  # Starts With Hello
match = re.search(pattern, text)
print(f"'{text}' Starts With 'Hello': {bool(match)}")

pattern2 = r'^World'
match2 = re.search(pattern2, text)
print(f"'{text}' Starts With 'World': {bool(match2)}")  # False

# Multiline Mode
text2 = "Line 1\nLine 2\nLine 3"
pattern3 = r'^Line'
matches3 = re.findall(pattern3, text2)  # Only Matches Start Of String
print(f"Without MULTILINE: {matches3}")

matches4 = re.findall(pattern3, text2, re.MULTILINE)  # Matches Start Of Each Line
print(f"With MULTILINE: {matches4}")

# DOLLAR SIGN METACHARACTER ($)
print("\n--- DOLLAR SIGN METACHARACTER ($) ---")
print("$ Matches End Of String")

text3 = "Hello World"
pattern4 = r'World$'  # Ends With World
match4 = re.search(pattern4, text3)
print(f"'{text3}' Ends With 'World': {bool(match4)}")

pattern5 = r'Hello$'
match5 = re.search(pattern5, text3)
print(f"'{text3}' Ends With 'Hello': {bool(match5)}")  # False

# PIPE METACHARACTER (|)
print("\n--- PIPE METACHARACTER (|) ---")
print("| Means OR")

text4 = "I like cats and dogs"
pattern6 = r'cat|dog'  # Match cat OR dog
matches6 = re.findall(pattern6, text4)
print(f"Matches 'cat|dog' In '{text4}': {matches6}")

pattern7 = r'python|java|javascript'
text5 = "I code in python and javascript"
matches7 = re.findall(pattern7, text5)
print(f"Languages In '{text5}': {matches7}")

# PARENTHESES ( ) - Grouping
print("\n--- PARENTHESES ( ) - GROUPING ---")

text6 = "ababab"
pattern8 = r'(ab)+'  # Group 'ab' and match 1 or more
match8 = re.search(pattern8, text6)
print(f"Pattern '(ab)+' In '{text6}': {match8.group() if match8 else 'Not Found'}")

text7 = "John Doe, Jane Smith"
pattern9 = r'(\w+) (\w+)'  # Capture first and last name
matches9 = re.findall(pattern9, text7)
print(f"Names: {matches9}")  # [('John', 'Doe'), ('Jane', 'Smith')]

# BACKSLASH (\) - Escape Character
print("\n--- BACKSLASH (\\) - ESCAPE ---")

text8 = "Price: $100.50"
pattern10 = r'\$\d+\.\d{2}'  # \$ and \. for literal $ and .
match10 = re.search(pattern10, text8)
print(f"Price Pattern: {match10.group() if match10 else 'Not Found'}")


# ========================================
# 5. SPECIAL SEQUENCES
# ========================================
print("\n\n=== SPECIAL SEQUENCES ===")

# \d - Digit [0-9]
print("\\d = Digit [0-9]")
text = "Order 123 costs $45.67"
digits = re.findall(r'\d', text)
print(f"Digits: {digits}")

digitGroups = re.findall(r'\d+', text)  # One or more digits
print(f"Digit Groups: {digitGroups}")

# \D - Non-Digit
print("\n\\D = Non-Digit")
nonDigits = re.findall(r'\D', text)
print(f"Non-Digits (First 20): {nonDigits[:20]}")

# \w - Word Character [a-zA-Z0-9_]
print("\n\\w = Word Character [a-zA-Z0-9_]")
text2 = "hello_world123"
wordChars = re.findall(r'\w', text2)
print(f"Word Characters: {wordChars}")

words = re.findall(r'\w+', "Hello, World! How are you?")
print(f"Words: {words}")

# \W - Non-Word Character
print("\n\\W = Non-Word Character")
nonWordChars = re.findall(r'\W', "Hello, World!")
print(f"Non-Word Characters: {nonWordChars}")

# \s - Whitespace [ \t\n\r\f\v]
print("\n\\s = Whitespace")
text3 = "Hello\tWorld\nPython"
whitespace = re.findall(r'\s', text3)
print(f"Whitespace Characters: {whitespace}")

# \S - Non-Whitespace
print("\n\\S = Non-Whitespace")
nonWhitespace = re.findall(r'\S+', "Hello World Python")
print(f"Non-Whitespace Groups: {nonWhitespace}")

# \b - Word Boundary
print("\n\\b = Word Boundary")
text4 = "The cat in the catalog"
pattern = r'\bcat\b'  # 'cat' as whole word
matches = re.findall(pattern, text4)
print(f"Whole Word 'cat': {matches}")

pattern2 = r'cat'  # 'cat' anywhere
matches2 = re.findall(pattern2, text4)
print(f"'cat' Anywhere: {matches2}")

# \B - Not Word Boundary
print("\n\\B = Not Word Boundary")
pattern3 = r'\Bcat\B'  # 'cat' NOT at word boundaries
text5 = "concatenate scat bobcat cat"
matches3 = re.findall(pattern3, text5)
print(f"'cat' Not At Boundaries: {matches3}")


# ========================================
# 6. COMPILE FUNCTION
# ========================================
print("\n\n=== COMPILE FUNCTION ===")
print("re.compile() Creates A Reusable Pattern Object")

# Without Compile (Inefficient For Repeated Use)
text = "Contact: 123-456-7890 or 987-654-3210"
for _ in range(3):
    matches = re.findall(r'\d{3}-\d{3}-\d{4}', text)

# With Compile (Efficient For Repeated Use)
phonePattern = re.compile(r'\d{3}-\d{3}-\d{4}')
for _ in range(3):
    matches = phonePattern.findall(text)
print(f"Phone Numbers: {matches}")

# Compile With Flags
emailPattern = re.compile(r'[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}', re.IGNORECASE)
text2 = "Contact: user@EXAMPLE.COM or admin@test.org"
emails = emailPattern.findall(text2)
print(f"Emails: {emails}")

# Multiple Methods On Compiled Pattern
urlPattern = re.compile(r'https?://[\w.-]+')
text3 = "Visit https://example.com or http://test.org"

print(f"Search: {urlPattern.search(text3).group()}")
print(f"Findall: {urlPattern.findall(text3)}")
print(f"Match: {urlPattern.match(text3)}")  # None (doesn't start with pattern)


# ========================================
# 7. SEARCH AND MATCH
# ========================================
print("\n\n=== SEARCH VS MATCH ===")

text = "Hello World"

# re.search() - Finds First Match ANYWHERE In String
print("re.search() - Finds First Match Anywhere")
searchResult = re.search(r'World', text)
print(f"Search For 'World': {searchResult.group() if searchResult else 'Not Found'}")

# re.match() - Matches Only At START Of String
print("\nre.match() - Matches Only At Start")
matchResult = re.match(r'World', text)
print(f"Match 'World' At Start: {matchResult.group() if matchResult else 'Not Found'}")

matchResult2 = re.match(r'Hello', text)
print(f"Match 'Hello' At Start: {matchResult2.group() if matchResult2 else 'Not Found'}")

# re.fullmatch() - Entire String Must Match
print("\nre.fullmatch() - Entire String Must Match")
fullMatchResult = re.fullmatch(r'Hello World', text)
print(f"Full Match 'Hello World': {bool(fullMatchResult)}")

fullMatchResult2 = re.fullmatch(r'Hello', text)
print(f"Full Match 'Hello': {bool(fullMatchResult2)}")  # False

# re.findall() - Find All Matches
print("\nre.findall() - Find All Matches")
text2 = "cat bat rat mat"
allMatches = re.findall(r'\w+at', text2)
print(f"All Matches: {allMatches}")

# re.finditer() - Returns Iterator Of Match Objects
print("\nre.finditer() - Iterator Of Match Objects")
for match in re.finditer(r'\w+at', text2):
    print(f"  Found '{match.group()}' At Position {match.start()}-{match.end()}")


# ========================================
# 8. MATCH OBJECT METHODS
# ========================================
print("\n\n=== MATCH OBJECT METHODS ===")

text = "Contact: John Doe at john.doe@example.com or 123-456-7890"
pattern = r'(\w+)\.(\w+)@([\w.-]+)'
match = re.search(pattern, text)

if match:
    print(f"Full Match: {match.group()}")  # or match.group(0)
    print(f"Group 1 (First Name): {match.group(1)}")
    print(f"Group 2 (Last Name): {match.group(2)}")
    print(f"Group 3 (Domain): {match.group(3)}")
    print(f"All Groups: {match.groups()}")
    print(f"Start Position: {match.start()}")
    print(f"End Position: {match.end()}")
    print(f"Span: {match.span()}")

# Named Groups
print("\n--- Named Groups ---")
pattern2 = r'(?P<first>\w+)\.(?P<last>\w+)@(?P<domain>[\w.-]+)'
match2 = re.search(pattern2, text)

if match2:
    print(f"First Name: {match2.group('first')}")
    print(f"Last Name: {match2.group('last')}")
    print(f"Domain: {match2.group('domain')}")
    print(f"Group Dict: {match2.groupdict()}")


# ========================================
# 9. FLAGS
# ========================================
print("\n\n=== REGULAR EXPRESSION FLAGS ===")

# re.IGNORECASE (re.I)
print("re.IGNORECASE - Case-Insensitive Matching")
text = "Hello HELLO hello"
matches = re.findall(r'hello', text, re.IGNORECASE)
print(f"Case-Insensitive Matches: {matches}")

# re.MULTILINE (re.M)
print("\nre.MULTILINE - ^ And $ Match Line Boundaries")
text2 = "Line 1\nLine 2\nLine 3"
matches2 = re.findall(r'^Line \d', text2, re.MULTILINE)
print(f"Multiline Matches: {matches2}")

# re.DOTALL (re.S)
print("\nre.DOTALL - Dot Matches Newline")
text3 = "Hello\nWorld"
match3 = re.search(r'Hello.World', text3, re.DOTALL)
print(f"Dot Matches Newline: {bool(match3)}")

# re.VERBOSE (re.X)
print("\nre.VERBOSE - Allow Comments And Whitespace")
phonePattern = re.compile(r'''
    \d{3}     # Area code
    -         # Separator
    \d{3}     # First 3 digits
    -         # Separator
    \d{4}     # Last 4 digits
''', re.VERBOSE)
match4 = phonePattern.search("Call 123-456-7890")
print(f"Verbose Pattern Match: {match4.group() if match4 else 'Not Found'}")

# Combined Flags
pattern = re.compile(r'hello.*world', re.IGNORECASE | re.DOTALL)


# ========================================
# 10. PRACTICAL EXAMPLES
# ========================================
print("\n\n=== PRACTICAL REAL-WORLD EXAMPLES ===")

# Email Validation
print("\n--- Email Validation ---")
emailPattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
emails = ["user@example.com", "invalid.email", "test@test.co.uk", "@nope.com"]
for email in emails:
    isValid = bool(emailPattern.match(email))
    print(f"  {email}: {'Valid' if isValid else 'Invalid'}")

# Phone Number Extraction
print("\n--- Phone Number Extraction ---")
text = "Contact: 123-456-7890, (987) 654-3210, or 555.123.4567"
phonePattern = re.compile(r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}')
phones = phonePattern.findall(text)
print(f"  Phone Numbers: {phones}")

# URL Extraction
print("\n--- URL Extraction ---")
text = "Visit https://example.com or http://test.org for more info"
urlPattern = re.compile(r'https?://[\w.-]+(?:/[\w.-]*)*')
urls = urlPattern.findall(text)
print(f"  URLs: {urls}")

# Password Validation (8+ chars, 1 upper, 1 lower, 1 digit)
print("\n--- Password Validation ---")
passwordPattern = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$')
passwords = ["Pass123", "password", "PASSWORD123", "ValidPass1"]
for pwd in passwords:
    isValid = bool(passwordPattern.match(pwd))
    print(f"  {pwd}: {'Valid' if isValid else 'Invalid'}")

# Extract Hashtags
print("\n--- Extract Hashtags ---")
text = "Love #Python and #Regex! #Programming is fun"
hashtags = re.findall(r'#\w+', text)
print(f"  Hashtags: {hashtags}")

# Remove HTML Tags
print("\n--- Remove HTML Tags ---")
html = "<p>Hello <b>World</b>!</p>"
cleanText = re.sub(r'<[^>]+>', '', html)
print(f"  Original: {html}")
print(f"  Cleaned: {cleanText}")

# Split By Multiple Delimiters
print("\n--- Split By Multiple Delimiters ---")
text = "apple,banana;cherry:date|elderberry"
parts = re.split(r'[,;:|]', text)
print(f"  Parts: {parts}")

print("\n--- End Of Regular Expressions Section ---")


# Note: JSON Is Covered In Detail In Chapter 22

''' CSV '''

import csv as CSV

# CSV.writer() == Creates A Writer Object
# CSV.reader() == Creates A Reader Object
# CSV.DictReader() == Creates A DictReader Object
# CSV.DictWriter() == Creates A DictWriter Object


"""Network Programming In Python"""
print("\n\n" + "="*60)
print("NETWORK PROGRAMMING IN PYTHON")
print("="*60)

import socket
import threading
import time

# ========================================
# 1. IP ADDRESSES
# ========================================
print("\n--- IP ADDRESSES ---")

# IP Address Basics
print("IP Address = Unique Identifier For Devices On A Network")
print("IPv4 = 32-bit Address (e.g., 192.168.1.1)")
print("IPv6 = 128-bit Address (e.g., 2001:0db8:85a3::8a2e:0370:7334)")

# Get Hostname
hostname = socket.gethostname()
print(f"\nCurrent Hostname: {hostname}")

# Get IP Address Of Current Machine
try:
    localIP = socket.gethostbyname(hostname)
    print(f"Local IP Address: {localIP}")
except Exception as e:
    print(f"Could Not Get IP: {e}")

# Get IP Address From Hostname
print("\n--- Hostname To IP Resolution ---")
websites = ["google.com", "github.com", "python.org"]
for site in websites:
    try:
        ip = socket.gethostbyname(site)
        print(f"{site} => {ip}")
    except socket.gaierror as e:
        print(f"Could Not Resolve {site}: {e}")

# Get Detailed Host Information
print("\n--- Detailed Host Information ---")
try:
    hostInfo = socket.gethostbyname_ex("google.com")
    print(f"Hostname: {hostInfo[0]}")
    print(f"Aliases: {hostInfo[1]}")
    print(f"IP Addresses: {hostInfo[2]}")
except Exception as e:
    print(f"Error: {e}")

# Get Fully Qualified Domain Name
fqdn = socket.getfqdn()
print(f"\nFully Qualified Domain Name: {fqdn}")

# IPv4 vs IPv6
print("\n--- IPv4 vs IPv6 ---")
print("IPv4: 4 octets (0-255), e.g., 192.168.1.1")
print("IPv6: 8 groups of 4 hex digits, e.g., 2001:0db8::1")

# Check IP Address Validity
import ipaddress

print("\n--- IP Address Validation ---")
testAddresses = ["192.168.1.1", "256.1.1.1", "2001:0db8::1", "invalid"]
for addr in testAddresses:
    try:
        ipObj = ipaddress.ip_address(addr)
        print(f"{addr} => Valid ({type(ipObj).__name__})")
    except ValueError:
        print(f"{addr} => Invalid")

# Network Information
print("\n--- Network Information ---")
network = ipaddress.ip_network("192.168.1.0/24", strict=False)
print(f"Network: {network}")
print(f"Network Address: {network.network_address}")
print(f"Broadcast Address: {network.broadcast_address}")
print(f"Netmask: {network.netmask}")
print(f"Number Of Hosts: {network.num_addresses}")

# Loopback Address
print("\n--- Loopback Address ---")
print("Loopback IPv4: 127.0.0.1 (localhost)")
print("Loopback IPv6: ::1")
print("Used For Testing Network Applications On Same Machine")


# ========================================
# 2. PORTS
# ========================================
print("\n\n--- PORTS ---")

print("Port = Endpoint For Network Communication")
print("Port Number Range: 0-65535")
print("\nWell-Known Ports (0-1023):")
print("  HTTP: 80")
print("  HTTPS: 443")
print("  FTP: 21")
print("  SSH: 22")
print("  SMTP: 25")
print("  DNS: 53")
print("  Telnet: 23")
print("\nRegistered Ports (1024-49151):")
print("  MySQL: 3306")
print("  PostgreSQL: 5432")
print("  MongoDB: 27017")
print("\nDynamic/Private Ports (49152-65535):")
print("  Used For Temporary Connections")

# Get Service Name From Port
print("\n--- Port To Service Mapping ---")
commonPorts = [80, 443, 21, 22, 25, 53]
for port in commonPorts:
    try:
        service = socket.getservbyport(port)
        print(f"Port {port} => {service}")
    except OSError:
        print(f"Port {port} => Unknown Service")

# Get Port From Service Name
print("\n--- Service To Port Mapping ---")
services = ["http", "https", "ftp", "ssh"]
for service in services:
    try:
        port = socket.getservbyname(service)
        print(f"{service} => Port {port}")
    except OSError:
        print(f"{service} => Unknown Port")


# ========================================
# 3. SOCKETS
# ========================================
print("\n\n--- SOCKETS ---")

print("Socket = Endpoint For Sending/Receiving Data")
print("Types Of Sockets:")
print("  1. TCP (SOCK_STREAM) - Connection-Oriented, Reliable")
print("  2. UDP (SOCK_DGRAM) - Connectionless, Fast But Unreliable")

# Socket Address Families
print("\n--- Socket Address Families ---")
print("AF_INET = IPv4")
print("AF_INET6 = IPv6")
print("AF_UNIX = Unix Domain Sockets (Local)")

# Creating A Socket
print("\n--- Creating A Socket ---")
print("Syntax: socket.socket(family, type, protocol)")

# Create TCP Socket
tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(f"TCP Socket Created: {tcpSocket}")

# Create UDP Socket
udpSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print(f"UDP Socket Created: {udpSocket}")

# Close Sockets
tcpSocket.close()
udpSocket.close()
print("Sockets Closed")

# Socket Options
print("\n--- Socket Options ---")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# SO_REUSEADDR - Allows Reuse Of Address
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
print("SO_REUSEADDR Enabled (Address Reuse)")

# Get Socket Options
reuseAddr = sock.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR)
print(f"SO_REUSEADDR Value: {reuseAddr}")

sock.close()


# ========================================
# 4. TCP CLIENT (SENDING MESSAGES)
# ========================================
print("\n\n--- TCP CLIENT ---")

print("""
TCP Client Steps:
1. Create Socket
2. Connect To Server
3. Send Data
4. Receive Data
5. Close Connection
""")

# Example: Simple TCP Client
print("--- Simple TCP Client Example ---")
print("# Create A TCP Client That Connects To A Server")

clientCode = '''
import socket

# Create TCP Socket
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Server Address And Port
serverHost = '127.0.0.1'  # Localhost
serverPort = 12345

try:
    # Connect To Server
    clientSocket.connect((serverHost, serverPort))
    print(f"Connected To {serverHost}:{serverPort}")
    
    # Send Message
    message = "Hello Server!"
    clientSocket.send(message.encode('utf-8'))
    print(f"Sent: {message}")
    
    # Receive Response
    response = clientSocket.recv(1024)  # Buffer Size 1024 Bytes
    print(f"Received: {response.decode('utf-8')}")
    
finally:
    # Close Connection
    clientSocket.close()
    print("Connection Closed")
'''

print(clientCode)

# Practical TCP Client Example
print("\n--- Practical HTTP Client ---")
print("Fetching Data From A Website Using Sockets")

try:
    # Create Socket
    httpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Connect To Website (HTTP Port 80)
    host = "example.com"
    port = 80
    httpSocket.connect((host, port))
    
    # Send HTTP GET Request
    request = f"GET / HTTP/1.1\r\nHost: {host}\r\nConnection: close\r\n\r\n"
    httpSocket.send(request.encode('utf-8'))
    
    # Receive Response
    response = httpSocket.recv(4096).decode('utf-8')
    
    # Print First 500 Characters
    print(f"\nHTTP Response (First 500 Chars):")
    print(response[:500])
    
    httpSocket.close()
    
except Exception as e:
    print(f"Error: {e}")


# ========================================
# 5. TCP SERVER (RECEIVING MESSAGES)
# ========================================
print("\n\n--- TCP SERVER ---")

print("""
TCP Server Steps:
1. Create Socket
2. Bind To Address And Port
3. Listen For Connections
4. Accept Connections
5. Send/Receive Data
6. Close Connection
""")

# Simple TCP Server Example
print("--- Simple TCP Server Example ---")

serverCode = '''
import socket

# Create TCP Socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Enable Address Reuse
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Bind To Address And Port
host = '127.0.0.1'  # Localhost
port = 12345
serverSocket.bind((host, port))

# Listen For Connections (Backlog = 5)
serverSocket.listen(5)
print(f"Server Listening On {host}:{port}")

try:
    while True:
        # Accept Connection
        clientSocket, clientAddress = serverSocket.accept()
        print(f"Connection From {clientAddress}")
        
        # Receive Data
        data = clientSocket.recv(1024)
        print(f"Received: {data.decode('utf-8')}")
        
        # Send Response
        response = "Message Received!"
        clientSocket.send(response.encode('utf-8'))
        
        # Close Client Connection
        clientSocket.close()
        
except KeyboardInterrupt:
    print("\\nServer Shutting Down")
finally:
    serverSocket.close()
'''

print(serverCode)


# ========================================
# 6. USING BUFFERS
# ========================================
print("\n\n--- USING BUFFERS ---")

print("""
Buffer = Temporary Storage For Data Being Sent/Received

Buffer Size Considerations:
- Too Small: Multiple recv() Calls Needed
- Too Large: Memory Waste
- Common Sizes: 1024, 2048, 4096, 8192 Bytes
""")

# Buffer Example
print("--- Buffer Usage Example ---")

bufferExample = '''
import socket

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect(('127.0.0.1', 12345))

# Sending Large Data
largeData = "A" * 10000  # 10KB Of Data
clientSocket.sendall(largeData.encode('utf-8'))  # sendall() Ensures All Data Sent

# Receiving Large Data With Buffer
receivedData = b''
bufferSize = 1024

while True:
    chunk = clientSocket.recv(bufferSize)
    if not chunk:
        break  # No More Data
    receivedData += chunk

print(f"Total Data Received: {len(receivedData)} Bytes")
clientSocket.close()
'''

print(bufferExample)

# Buffer Size Impact
print("\n--- Buffer Size Impact ---")
print("Small Buffer (1024 Bytes):")
print("  + Less Memory Usage")
print("  - More recv() Calls")
print("  - Slower For Large Data")

print("\nLarge Buffer (8192 Bytes):")
print("  + Fewer recv() Calls")
print("  + Faster For Large Data")
print("  - More Memory Usage")


# ========================================
# 7. UDP CLIENT AND SERVER
# ========================================
print("\n\n--- UDP SOCKETS ---")

print("""
UDP = User Datagram Protocol
- Connectionless (No Connection Needed)
- Unreliable (No Guarantee Of Delivery)
- Faster Than TCP
- Used For: Video Streaming, Gaming, DNS
""")

# UDP Client Example
print("--- UDP Client Example ---")

udpClientCode = '''
import socket

# Create UDP Socket
udpClient = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Server Address
serverAddress = ('127.0.0.1', 12345)

# Send Data (No Connection Needed)
message = "Hello UDP Server!"
udpClient.sendto(message.encode('utf-8'), serverAddress)
print(f"Sent: {message}")

# Receive Response
data, server = udpClient.recvfrom(1024)
print(f"Received From {server}: {data.decode('utf-8')}")

udpClient.close()
'''

print(udpClientCode)

# UDP Server Example
print("\n--- UDP Server Example ---")

udpServerCode = '''
import socket

# Create UDP Socket
udpServer = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind To Address
host = '127.0.0.1'
port = 12345
udpServer.bind((host, port))

print(f"UDP Server Listening On {host}:{port}")

while True:
    # Receive Data
    data, clientAddress = udpServer.recvfrom(1024)
    print(f"Received From {clientAddress}: {data.decode('utf-8')}")
    
    # Send Response
    response = "Message Received!"
    udpServer.sendto(response.encode('utf-8'), clientAddress)
'''

print(udpServerCode)


# ========================================
# 8. MULTI-CLIENT SERVER
# ========================================
print("\n\n--- MULTI-CLIENT SERVER (THREADING) ---")

print("Handle Multiple Clients Simultaneously Using Threading")

multiClientServer = '''
import socket
import threading

def handleClient(clientSocket, clientAddress):
    """Handle Individual Client Connection"""
    print(f"New Connection: {clientAddress}")
    
    try:
        while True:
            # Receive Data
            data = clientSocket.recv(1024)
            if not data:
                break
            
            message = data.decode('utf-8')
            print(f"[{clientAddress}] {message}")
            
            # Echo Back
            response = f"Echo: {message}"
            clientSocket.send(response.encode('utf-8'))
    
    except Exception as e:
        print(f"Error With {clientAddress}: {e}")
    
    finally:
        clientSocket.close()
        print(f"Connection Closed: {clientAddress}")

# Create Server Socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

host = '127.0.0.1'
port = 12345
serverSocket.bind((host, port))
serverSocket.listen(5)

print(f"Multi-Client Server Listening On {host}:{port}")

try:
    while True:
        # Accept Connection
        clientSocket, clientAddress = serverSocket.accept()
        
        # Create Thread For Each Client
        clientThread = threading.Thread(
            target=handleClient,
            args=(clientSocket, clientAddress)
        )
        clientThread.daemon = True
        clientThread.start()

except KeyboardInterrupt:
    print("\\nServer Shutting Down")
finally:
    serverSocket.close()
'''

print(multiClientServer)


# ========================================
# 9. SOCKET TIMEOUT AND NON-BLOCKING
# ========================================
print("\n\n--- SOCKET TIMEOUT AND NON-BLOCKING ---")

# Set Timeout
print("--- Socket Timeout ---")
print("Prevents recv() From Blocking Forever")

timeoutExample = '''
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Set Timeout To 5 Seconds
sock.settimeout(5.0)

try:
    sock.connect(('example.com', 80))
    data = sock.recv(1024)  # Will Timeout After 5 Seconds
except socket.timeout:
    print("Connection Timed Out!")
finally:
    sock.close()
'''

print(timeoutExample)

# Non-Blocking Socket
print("\n--- Non-Blocking Socket ---")

nonBlockingExample = '''
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Set Non-Blocking Mode
sock.setblocking(False)

try:
    sock.connect(('example.com', 80))
except BlockingIOError:
    print("Connection In Progress...")
    
# Use select.select() To Check When Socket Is Ready
'''

print(nonBlockingExample)


# ========================================
# 10. SOCKET ERROR HANDLING
# ========================================
print("\n\n--- SOCKET ERROR HANDLING ---")

print("""
Common Socket Exceptions:
- socket.error: General Socket Error
- socket.timeout: Operation Timed Out
- socket.gaierror: Address-Related Error
- ConnectionRefusedError: Server Not Listening
- BrokenPipeError: Connection Broken
- OSError: Operating System Error
""")

errorHandlingExample = '''
import socket

def connectToServer(host, port):
    """Connect To Server With Error Handling"""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(10)
    
    try:
        print(f"Connecting To {host}:{port}...")
        sock.connect((host, port))
        print("Connected Successfully!")
        return sock
        
    except socket.gaierror:
        print(f"Error: Could Not Resolve Hostname '{host}'")
    except ConnectionRefusedError:
        print(f"Error: Connection Refused By {host}:{port}")
    except socket.timeout:
        print(f"Error: Connection Timed Out")
    except OSError as e:
        print(f"Error: {e}")
    
    return None

# Usage
sock = connectToServer('127.0.0.1', 12345)
if sock:
    # Use Socket
    sock.close()
'''

print(errorHandlingExample)


# ========================================
# 11. PRACTICAL EXAMPLES
# ========================================
print("\n\n--- PRACTICAL EXAMPLES ---")

# Example 1: Simple Chat Client
print("--- Simple Chat Client ---")

chatClient = '''
import socket
import threading

def receiveMessages(sock):
    """Receive Messages From Server"""
    while True:
        try:
            message = sock.recv(1024).decode('utf-8')
            if message:
                print(f"\\n{message}")
        except:
            break

# Connect To Chat Server
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect(('127.0.0.1', 5555))

# Start Receiving Thread
receiveThread = threading.Thread(target=receiveMessages, args=(clientSocket,))
receiveThread.daemon = True
receiveThread.start()

# Send Messages
print("Connected To Chat Server!")
while True:
    message = input()
    if message.lower() == 'quit':
        break
    clientSocket.send(message.encode('utf-8'))

clientSocket.close()
'''

print(chatClient)

# Example 2: File Transfer
print("\n--- File Transfer Example ---")

fileTransferClient = '''
import socket
import os

def sendFile(filename, host, port):
    """Send File To Server"""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    
    # Send Filename
    sock.send(filename.encode('utf-8'))
    
    # Send File Size
    fileSize = os.path.getsize(filename)
    sock.send(str(fileSize).encode('utf-8'))
    
    # Send File Data
    with open(filename, 'rb') as f:
        while True:
            data = f.read(4096)
            if not data:
                break
            sock.sendall(data)
    
    print(f"File '{filename}' Sent Successfully!")
    sock.close()

# sendFile('document.pdf', '127.0.0.1', 9999)
'''

print(fileTransferClient)


# ========================================
# 12. SUMMARY AND BEST PRACTICES
# ========================================
print("\n\n--- NETWORK PROGRAMMING BEST PRACTICES ---")

print("""
1. Always Close Sockets
   - Use 'with' Statement Or try/finally

2. Handle Exceptions
   - socket.error, timeout, ConnectionRefusedError

3. Use Timeouts
   - Prevent Indefinite Blocking

4. Buffer Size
   - Choose Appropriate Size (1024, 4096, 8192)

5. TCP vs UDP
   - TCP: Reliable, Ordered, Connection-Oriented
   - UDP: Fast, Unreliable, Connectionless

6. Multi-Client Servers
   - Use Threading Or Asyncio

7. Security
   - Use SSL/TLS For Encryption
   - Validate Input Data
   - Implement Authentication

8. Performance
   - Use sendall() For Large Data
   - Reuse Sockets When Possible
   - Consider Non-Blocking I/O

9. Testing
   - Test On Localhost First
   - Handle Network Failures Gracefully

10. Documentation
    - Document Protocol Format
    - Specify Message Structure
""")

print("\n--- Common Socket Methods ---")
print("""
Server Methods:
  socket() - Create Socket
  bind() - Bind To Address
  listen() - Listen For Connections
  accept() - Accept Connection

Client Methods:
  socket() - Create Socket
  connect() - Connect To Server

Both:
  send() - Send Data
  recv() - Receive Data
  sendall() - Send All Data
  close() - Close Socket
  
Configuration:
  settimeout() - Set Timeout
  setblocking() - Set Blocking Mode
  setsockopt() - Set Socket Options
  getsockopt() - Get Socket Options
""")

print("\n" + "="*60)
print("END OF NETWORK PROGRAMMING SECTION")
print("="*60)

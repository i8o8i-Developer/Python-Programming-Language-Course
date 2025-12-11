# ╔═══════════════════════════════════════════════════════════════╗
# ║              CHAPTER 5: DICTIONARIES AND SETS                 ║
# ╠═══════════════════════════════════════════════════════════════╣
# ║                                                               ║
# ║  TABLE OF CONTENTS:                                           ║
# ║  ═════════════════                                            ║
# ║                                                               ║
# ║  1. Dictionary Basics                                         ║
# ║     - Creating Dictionaries (3 Ways)                          ║
# ║     - Accessing Values (Key-Based)                            ║
# ║     - Dictionary Properties (Unordered, Mutable, Indexed)     ║
# ║                                                               ║
# ║  2. Dictionary Methods                                        ║
# ║     - items(), keys(), values()                               ║
# ║     - get(), update(), pop()                                  ║
# ║     - Updating And Adding Entries                             ║
# ║                                                               ║
# ║  3. Sets Basics                                               ║
# ║     - Creating Sets                                           ║
# ║     - Unique Elements (Auto Duplicate Removal)                ║
# ║     - Set Operations (Union, Intersection, Difference)        ║
# ║     - Set Methods (add, remove, discard, etc.)                ║
# ║     - Frozen Sets (Immutable Sets)                            ║
# ║                                                               ║
# ║  4. Dictionary And Set Comprehensions                         ║
# ║                                                               ║
# ╚═══════════════════════════════════════════════════════════════╝


# ═══════════════════════════════════════════════════════════════
#  TOPIC 1: Dictionary Basics
# ═══════════════════════════════════════════════════════════════

# Dictionary And Sets 

# Empty Dictionary
Dict = {}

Example = {
    "Name": "John",
    "Age": 30,
    "City": "New York",
    "HasChildren": True,
}

# For Finding Corresponding Pair 
print(Example["Name"]) # John

# It Is Unordered
print(Example) # {'Name': 'John', 'Age': 30, 'City':'New York', 'HasChildren': True}

# It Is Mutable
Example["Age"] = 31

# It Is Indexed
print(Example["Age"]) # 31

# Connot Contain Duplicate Keys

# Second Way Of Creating Dictionary
Example = {}
Example["Name"] = "John"
#  |      |         | 
# Dict   Key       Value

# Third Way Of Creating Dictionary
Example = dict(Name = "John")
#  |             |       |
" Dict          Key    Value  "
print(Example)


# ═══════════════════════════════════════════════════════════════
#  TOPIC 2: Dictionary Methods
# ═══════════════════════════════════════════════════════════════

# For Extracting Items 
print(Example.items())

# For Extracting Keys 
print(Example.keys())

# For Extracting Values 
print(Example.values())

# Updating|Adding Dictionary
Example["Age"] = 31
print(Example)


# ═══════════════════════════════════════════════════════════════
#  TOPIC 3: Sets Basics
# ═══════════════════════════════════════════════════════════════

# Sets - Unordered Collections Of Unique Elements
print("\n--- Sets ---")
# Creating Sets
SetExample = {1, 2, 3, 4, 5}
print("Set:", SetExample)

# Sets Automatically Remove Duplicates
DuplicateSet = {1, 2, 2, 3, 3, 3}
print("Set With Duplicates:", DuplicateSet)  # {1, 2, 3}

# Adding Elements
SetExample.add(6)
print("After Add(6):", SetExample)

# Removing Elements
SetExample.remove(3)  # Raises KeyError If Not Found
print("After Remove(3):", SetExample)

SetExample.discard(10)  # No Error If Not Found
print("After Discard(10):", SetExample)

# Set Operations
SetA = {1, 2, 3, 4}
SetB = {3, 4, 5, 6}
print("SetA:", SetA)
print("SetB:", SetB)
print("Union (A | B):", SetA | SetB)  # {1, 2, 3, 4, 5, 6}
print("Intersection (A & B):", SetA & SetB)  # {3, 4}
print("Difference (A - B):", SetA - SetB)  # {1, 2}
print("Symmetric Difference (A ^ B):", SetA ^ SetB)  # {1, 2, 5, 6}

# Frozenset - Immutable Set
FrozenSet = frozenset([1, 2, 3])
print("Frozenset:", FrozenSet)
# FrozenSet.add(4)  # AttributeError: 'frozenset' Object Does Not Have Attribute 'add'

# Use Cases: Removing Duplicates From Lists, Membership Testing (Fast), Mathematical Operations
Example.update({"Age":30})
print(Example)
Example.update({"City": "New York"})
print(Example)

# Using get() Fuctions
print(Example.get("Name")) # John
# Its Gives None When Its Not Available

# Using Len() Function
print(len(Example)) # 4 

# Using fromkeys() Function
Example = dict.fromkeys(["Name", "Age", "City"], "Unknown")
#  |         |
# Dict      Key

print(Example) # {'Name': 'Unknown', 'Age': 'Unknown', 'City': 'Unknown'}

# Using Pop Function
Example = {"Name": "John", "Age": 31, "City": "New York"}
print(Example.pop("Age")) # 31
print(Example) # {'Name': 'John', 'City': 'New York'} 

# Using popitems() Functions
Example = {"Name": "John", "Age": 31, "City": "New York"}
print(Example.popitem()) # ('City', 'New York') # It Will Remove The Last Value And Ke Pair
print(Example) # {'Name': 'John', 'Age': 31}

# Using clear() Functions
Example = {"Name": "John", "Age": 31, "City": "New York"}
print(Example.clear()) # None

# Using Sorted() Function
Example = {"Name": "John", "Age": 31, "City": "New York"}
print(sorted(Example)) # ['Age', 'City', 'Name']

# Using Reverse=? In Sorted() Function
Example = {"Name": "John", "Age": 31, "City": "New York"}
print(sorted(Example, reverse=True)) # ['Name', 'Age', 'City']

# Using Copy() Function
Example = {"Name": "John", "Age": 31, "City": "New York"}
Example2 = Example.copy()
print(Example2) # {'Name': 'John', 'Age': 31, 'City': 'New York'}

# Nested Dictionary
Example = {
    "Name": "John",
    "Age": 31,
    "Hometown": {
        "City": "New York",
        "Country": "USA"
    }
} 
print(Example["Hometown"]["City"])


# Full Sets Explanation And Details 
Set = {1,2,3}
print(type(Set))

# For Empty Sets 
Set = set()
print(type(Set))

# Rules
# 1. No Repeatation Is Allowed 
# 2. Sets Are Written With Curly Brackets.
# 3. Sets Are Unchangeable, Meaning That We Cannot Change The Items After The Set Has Been Created.
# 4. Sets Are Unordered, Meaning That The Items Will Appear In A Random Order.
# 5. Sets Are Unindexed, Meaning That We Cannot Access The Items By Their Index Number
# 6. Sets Are Unchangeable, Meaning That We Cannot Change The Items After The Set
"Methods"

# Using add() Function
Set = {1,2,3,4,5,6,7,8,9}
Set.add(10)
print(Set) # {1, 2, 3, 4, 5,...

# Using update() Function
Set = {1,2,3,4,5,6,7,8,9}
Set.update([10,11,12,13,14,15,16,17,18])
print(Set) # {1, 2, 3, 4, 5,.....

# Using remove() Method
Set = {1,2,3,4,5,6,7,8,9}
Set.remove(1)
print(Set) # {2, 3, 4, 5, 6,.....

# Using Len() Fuction
Set = {1,2,3,4,5,6,7,8,9}
print(len(Set)) # 9

# Using Pop() Function
Set = {1,2,3,4,5,6,7,8,9}
Set.pop() # Removes Random Element
print(Set) # {1, 2, 3, 4, 5,.....

# Using Clear() Function
Set = {1,2,3,4,5,6,7,8,9}
Set.clear()
print(Set) # set()



"""Sets Union Intersection"""

Set1 = {1,2,4,5}
Set2 = {1,2,3,4,5,6,7,8}

H = Set1.union(Set2)
print(H) # Joining Two Sets 

"""Sets Intersection"""

Set1 = {1,2,4,5}
Set2 = {1,2,3,4,5,6,7,8}
# Used To Identify Repeated Value By Comparing Given Sets
print(Set1.intersection(Set2))

# Using difference() Function : To Identify The Value Of Set 1 Which Is Not Present In Set 2
Set1 = {1,2,4,5,12}
Set2 = {1,2,3,4,5,6,7,8}
Difference_Set = Set1.difference(Set2)
print(Difference_Set)  # Output: {12}


# Define two sets : To Identufy The Elements Present In Their Own Set But Not In Another Set (Both Set)
Set1 = {1, 2, 3, 4}
Set2 = {3, 4, 5, 6}
# Compute Symmetric Difference Using symmetric_difference() Method
Result_Set = Set1.symmetric_difference(Set2)
print(Result_Set)  # Output: {1, 2, 5, 6}


"""IsSubset And IssuperSet"""
Set1 = {1, 2, 3}
Set2 = {1, 2, 3, 4, 5}
print(Set1.issubset(Set2))  # True, Because Set1 Is A Subset Of Set2
print(Set2.issubset(Set1))  # False, Because Set2 Is Not A Subset Of Set1


Set1 = {1, 2, 3}
Set2 = {1, 2}
print(Set1.issuperset(Set2))  # True, Because Set1 Is A Superset Of Set2
print(Set2.issuperset(Set1))  # False, Because Set2 Is Not A Superset Of Set1

"Extra"
# In Set Certain Things Are Same Like : 1 & 1.0 (Because Numeric Value Is Equal)
# But In Dict 1 & 1.0 Are Different
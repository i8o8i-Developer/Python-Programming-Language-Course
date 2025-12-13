# ╔═══════════════════════════════════════════════════════════════╗
# ║          CHAPTER 16: ADVANCED PYTHON FEATURES                 ║
# ╠═══════════════════════════════════════════════════════════════╣
# ║                                                               ║
# ║  TABLE OF CONTENTS:                                           ║
# ║  ═════════════════                                            ║
# ║                                                               ║
# ║  1. List Comprehension (Advanced)                             ║
# ║     - With If Condition                                       ║
# ║     - With If-Else                                            ║
# ║     - Nested Conditions                                       ║
# ║                                                               ║
# ║  2. Walrus Operator (:=)                                      ║
# ║     - Assignment Expressions                                  ║
# ║     - Use In Conditionals                                     ║
# ║                                                               ║
# ║  3. Type Annotations And Hints                                ║
# ║     - Variable Type Hints                                     ║
# ║     - Function Return Types                                   ║
# ║     - Type Aliases (List, Tuple, Dict, Union)                 ║
# ║                                                               ║
# ║  4. Match-Case Statement (Python 3.10+)                       ║
# ║                                                               ║
# ╚═══════════════════════════════════════════════════════════════╝


# ═══════════════════════════════════════════════════════════════
#  TOPIC 1: List Comprehension (Advanced)
# ═══════════════════════════════════════════════════════════════

# Advanced Python With Newly Added Features 

"""List Comprehension"""

'==> Syntax  [ <Expression> For <Item=Expression> In <List> <Conditions> ]'
'==> Syntax  [ <Expression> <Conditions> For <Item=Expression> In <List> ]'

Example = [i for i in range(1,11)]
H = Example

# List Comprehension With If Condition

Example = [i for i in range(1,11) if i%2==0]
H = Example

# List Comprehension With If And Else Condition

Example = [i if i%2==0 else "Anubhav" for i in range(1,11)]
H = Example

# List Comprehension With Nested If Condition

Example = [i if i%2==0 else i**2 if i%3==0 else i**3 for i in range(1,11)]
H = Example

# List Comprehension With Nested If And Else Condition

Example = [i if i%2==0 else i**2 if i%3==0 else i**3 if i%4==0 else "Anubhav" for i in range(1,11)]
H = Example

"""Walrus Operater"""

# Walrus = (:=) Is Used To Assign The Value Of Walrus To The Variable
if ( N := len([1,2,3,4,5,6,7,8,9,0])) > 6 :
    H = (f" List Is Too Long ( {N} Elements Detected In List )")
    

# Type Definition 

Number : int = 5 # Type Annotation
String : str = "Anubhav" # Type Annotation
 
def Sum(A : int , B : int) -> int :
    return A+B
# ( - > int ) = Will Return The Value In Int

# Type Aliases


from typing import List , Tuple , Dict , Union

Example : List[int] = [1,2,3,4,5]

Example : Tuple[int,str] = (1,"Anubhav")

Example : Dict[int,str] = {1:"Anubhav"}

Example : Union[int,str] = "1AD"
Example = 12345 # Also Vali:

""" Match Case """

def HTTP_STATUS(STATUS):
    match STATUS:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:
            return "Unknown Status"

H = HTTP_STATUS(5004)

# Dictionary Merge And Update Operaters 

Dict1 = { 'A' : 1 , 'B' : 2}
Dict2 = { 'B' : 3 , 'D' : 4}
Merging = Dict1 | Dict2

# Multiple Context Managers

with (
    open("OuputFolder/Text.txt") as F,
    open("OuputFolder/Output.txt") as F2
):
    pass

# __name__ == '__main__'

def TestFunction():
    print("Hello Learner")

if __name__ == '__main__':
    # If This Code Is Executed By Running Its Main File
    TestFunction()

# Enumerate

L = [1,2,3,4,5,6,7,8]
# Built-In Function That Adds A Counter To An Iterable And Returns It

for Index , Item in enumerate(L):
    print(Index,Item)

"""
Used Instead Of:
Index = 0
for Index in L:
    print(Index,L[Index])
    index += 1

"""
# Chapter 10: File Input/Output (I/O)

"""
TABLE OF CONTENTS:
1. File Types
   - Text Files
   - Binary Files
2. File Operations
   - Reading Files (read, readline, readlines)
   - Writing Files (write, writelines)
   - Appending To Files
3. Context Manager (with Statement)
   - Auto-Closing Files
   - Error Handling
4. File Methods
   - seek(), tell()
   - flush()
5. Working With Directories
   - os.path Module
6. Note: JSON Is Covered In Chapter 22
"""

# ========================================
# FILE BASICS
# ========================================

'There Are Two Types Of Files'
'Text File'
'Binary File'

# Best Practice: Using 'with' Statement (Context Manager)
# Automatically Closes File, Even If Errors Occur
# No Need To Call .close() Manually

# Reading With 'with'
print("--- Reading With 'with' ---")
with open("OuputFolder/Text.txt", "r") as file:
    content = file.read()
    print("File content:", content)

# Writing With 'with'
print("--- Writing With 'with' ---")
with open("OuputFolder/Text.txt", "w") as file:
    file.write("Hello From 'with' Statement!\n")
    file.write("This Is Safer File Handling.")

# Appending With 'with'
with open("OuputFolder/Text.txt", "a") as file:
    file.write("\nAppended Text.")

# Reading line By line
print("--- Reading line By line ---")
with open("OuputFolder/Text.txt", "r") as file:
    for line in file:
        print("Line:", line.strip())

# Old Way (Manual Close) - Prone To Errors If Exceptions Occur
print("--- Old Way (For Comparison) ---")
File = open("OuputFolder/Text.txt","r") # "r" = Read
# File Must Exist Already OtherWise Error Will Raise
# <Variable> = open(<FileName>)
# <Variable> = open(<FileName>,<mode>)

Content = File.read()
print("Read Content:", Content)
File.close() # Must Remember To Close!

# Text File ( Open And Write )
File = open("OuputFolder/Text.txt","w") # "w" = Write
File.write("Hello Everyone My Name Is Anubhav Chaurasia")
File.close() # If File Is Non Existed It Will Be Created 
# If File Exist It Will Over Write It 

# Text File ( Open And Append )
File = open("OuputFolder/Text.txt","a") # "a" = Append
File.write(" Hello Everyone My Name Is Anubhav Chaurasia")
File.close() # If File Is Non Existed It Will Be Created 
# If File Exist It Will Write Data At End

# Text File ( Open And Read + Write )
File = open("OuputFolder/Text.txt","r+") # "r+" = Read + Write
H = File.read()
File.write("Hello Everyone My Name Is Anubhav Chaurasia")
File.close() # File Must Exist Already OtherWise Error Will Raise

# Text File ( Open And Read + Append )
File = open("OuputFolder/Text.txt","a+") # "a+" = Append + Read
H = File.read()
File.write("Hello Everyone My Name Is Anubhav Chaurasia")
File.close() # If File Is Non Existed It Will Be Created 
# If File Exist It Will Write Data At End

# Text File ( Open And Write + Read )
File = open("OuputFolder/Text.txt","w+") # "w+" = Write + Read
File.write("Hello Everyone My Name Is Anubhav Chaurasia")
H = File.read()
File.close() # If File Is Non Existed It Will Be Created 
# If File Exist It Will Over Write It

# Binary File (Open And Read )
File = open("OuputFolder/Text.bin","rb") # "rb" = Read
File.read()
File.close()

# Binary File (Open And Write )
File = open("OuputFolder/Text.bin","wb") # "wb" = Write
File.write("Hello Everyone My Name Is Anubhav Chaurasia".encode())
File.close() # .encode()  For Converting Into Str


''' Or Use b"Hello Everyone My Name Is Anubhav Chaurasia "'''


# Binary File (Open And Append )
File = open("OuputFolder/Text.bin","ab") # "ab" = Append
File.write("Hello Everyone My Name Is Anubhav Chaurasia".encode())
File.close()

# Binary File (Open And Read + Write )
File = open("OuputFolder/Text.bin","rb+") # "rb+" = Read + Write
H = File.read()
File.write("Hello Everyone My Name Is Anubhav Chaurasia".encode())
File.close()

# Binary File (Open And Read + Append )
File = open("OuputFolder/Text.bin","ab+") # "ab+" = Append + Read
H = File.read()
File.write("Hello Everyone My Name Is Anubhav Chaurasia".encode())
File.close()

# Binary File (Open And Write + Read )
File = open("OuputFolder/Text.bin","wb+") # "wb+" = Write + Read
File.write("Hello Everyone My Name Is Anubhav Chaurasia".encode())
H = File.read()
File.close()

'''
with open(<FileName> , <FileMode>) as <FileHandle>:
    <FileHandle>.<FileOperation>()
'''

# Writing To A Binary File
with open('OuputFolder/BinaryFile.bin', 'wb') as File:
    data = b'\x48\x65\x6c\x6c\x6f'  # Example Binary Data (Hello in ASCII)
    File.write(data)

# Telling Current Position
File = open("OuputFolder/Text.txt","r")
File.tell()
File.close() # Use Indexing Of Current Cursor

with open('OuputFolder/Example.bin', 'rb') as File:
    File.tell()  # Output: 0 (initial position)
    
    Data = File.read(10)  # Read 10 bytes
    File.tell() # Output: 10 (position after reading)

    Data = File.seek(5, 0)  # Move Pointer 5 bytes from the beginning <Offset>,<Whence>  or <mode> Which Indicate Pointer Ahead Or BackWard Direction According To Offset(+,-) 
    File.tell()  # Output: 5 (new position after seeking)

# Auto Closing A File
with open("OuputFolder/Text.txt","r") as File:
    File.read()

# Read-Line Method
File = open("OuputFolder/Text01.txt","r")
File.readline()
File.close()

# File.readline() will read the first line from "OuputFolder/Text.txt", which is "Hello, This Is Line 1.\n".
# The newline character (\n) represents the end of the line in the file.

# Read-Lines Method
File = open("OuputFolder/Text01.txt","r")
File.readlines()
File.close()

# File.readlines() will read all the lines from "OuputFolder/Text.txt"
# and return them as a list of strings, where each string represents a line in the file.
# .\n Represents New Line In That File

# Write-Lines Method
Lines = [
    "First line.\n",
    "Second line.\n",
    "Third line.\n"
]

with open("OuputFolder/Output.txt", "w") as File:
    File.writelines(Lines)

# Append-Lines Method
File = open("OuputFolder/Text01.txt","a")
File.writelines(Lines)
File.close()

# Flush Function
File = open("OuputFolder/Text02.txt","w")
File.write("Hello, This Is Line 1.\n")
File.write("This Is Line 2.\n")
File.write("And Here Comes Line 3.\n")
File.flush()
File.close()

''' Normally, Python buffers file I/O operations (writing to file in memory first for efficiency). flush() forces these buffered data to be written to disk immediately.
# File.flush(): Ensures that all the data written to the file so far is physically stored in the file  '''

# Strip Method
# Lstrip Method
File = open("OuputFolder/Text01.txt","r")
File.readline().lstrip()
File.close() # Removing Leading WhiteSpace From Line

# Rstrip Method
File = open("OuputFolder/Text01.txt","r")
File.readline().rstrip('.\n')
File.close() # Removing EOL '.\n' For Line Or Whitespace .rstrip()

# Split Method
File = open("OuputFolder/Text01.txt","r")
File.readline().split()
File.close() # Splitting String Into List

# Strip Method strip()
File = open("OuputFolder/Text01.txt","r")
File.readline().strip()
File.close() # Remove Leading And Trailing WhiteSpace


# Pickling And Unpickling
import pickle 

# Pickling (.Any Extension)
File = open("Text.durgaai","wb")
pickle.dump("Hello Everyone My Name Is Anubhav Chaurasia",File)
File.close()

# Unpickling
File = open("Text.durgaai","rb")
H = pickle.load(File)
File.close()


# Note: JSON Is Covered In Detail In Chapter 22

# Standard Input , Output And Error Streams In Python
import sys

sys.stdout.write("Hello Everyone My Name Is Anubhav Chaurasia\n")
# Instead Of Print Statement : print("Hello Everyone My Name Is Anubhav Chaurasia")

sys.stdout.write("Hello Everyone My Name Is Anubhav Chaurasia")
# Instead Of Print Statement : print("Hello Everyone My Name Is Anubhav Chaurasia" , end='')
print("")
sys.stderr.write('This Is An Error\n')
# Instead Of Print Statement : print('This Is An Error', end="" , file=sys.stderr)
# Used To Print Error Before Anything
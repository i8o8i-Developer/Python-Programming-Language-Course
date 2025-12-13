# ╔═══════════════════════════════════════════════════════════════╗
# ║                    CHAPTER 1: PYTHON BASICS                   ║
# ╠═══════════════════════════════════════════════════════════════╣
# ║                                                               ║
# ║  TABLE OF CONTENTS:                                           ║
# ║  ═════════════════                                            ║
# ║                                                               ║
# ║  1. Comments And Multi-line Strings                           ║
# ║  2. Input Function                                            ║
# ║  3. F-strings (Formatted String Literals)                     ║
# ║  4. Print Statement (end Parameter)                           ║
# ║  5. Data Types / Literals                                     ║
# ║                                                               ║
# ╚═══════════════════════════════════════════════════════════════╝


# ═══════════════════════════════════════════════════════════════
#  TOPIC 1: Comments And Multi-line Strings
# ═══════════════════════════════════════════════════════════════

# For Comments We Use "#" = Infront Of Text
# Shortcut For Comments = Ctrl+/

# Multiline Prints/Strings = """" """ or ''' ''' 


# ═══════════════════════════════════════════════════════════════
#  TOPIC 2: Input Function
# ═══════════════════════════════════════════════════════════════

Name = input("Enter Your Name : ")

print(f"Hello {Name}")


# ═══════════════════════════════════════════════════════════════
#  TOPIC 3: F-strings (Formatted String Literals)
# ═══════════════════════════════════════════════════════════════

# f Is Used In Puting "Name Variable" In Quoted Text


# ═══════════════════════════════════════════════════════════════
#  TOPIC 4: Print Statement (end Parameter)
# ═══════════════════════════════════════════════════════════════

"""Print Statement Gives New Line By Default"""
print("Hello")
print("Anubhav")

# To Fix This Error We Use 
print("Hello",end="")
print("Anubhav")

# Now Both Statements Will Be Printed In Same Line
# You Can Use Any Character In End Parameter

print("Hello",end="---")
print("Anubhav")

# Now Both Statements Will Be Printed With "---" In Between


# ═══════════════════════════════════════════════════════════════
#  TOPIC 5: Data Types / Literals
# ═══════════════════════════════════════════════════════════════

# Data Types In Python Are Also Called Literals
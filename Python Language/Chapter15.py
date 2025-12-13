# ╔═══════════════════════════════════════════════════════════════╗
# ║         CHAPTER 15: SPECIAL METHODS (MAGIC METHODS)           ║
# ╠═══════════════════════════════════════════════════════════════╣
# ║                                                               ║
# ║  TABLE OF CONTENTS:                                           ║
# ║  ═════════════════                                            ║
# ║                                                               ║
# ║  1. Operator Overloading (__add__, __sub__, __mul__)          ║
# ║  2. String Representation (__str__, __repr__)                 ║
# ║  3. Comparison Operators (__eq__, __lt__, __gt__)             ║
# ║  4. Container Methods (__len__, __getitem__, __setitem__)     ║
# ║  5. Callable Objects (__call__)                               ║
# ║  6. Context Managers (__enter__, __exit__)                    ║
# ║  7. All Dunder Methods Reference                              ║
# ║                                                               ║
# ╚═══════════════════════════════════════════════════════════════╝

"""
╔════════════════════════════════════════════════════════╗
║           MAGIC METHODS (DUNDER METHODS)               ║
╠════════════════════════════════════════════════════════╣
║                                                        ║
║  __init__    Constructor                               ║
║  __str__     String Representation (User-Friendly)     ║
║  __repr__    Official Representation (Dev-Friendly)    ║
║  __add__     + Operator                                ║
║  __sub__     - Operator                                ║
║  __mul__     * Operator                                ║
║  __len__     len() Function                            ║
║  __getitem__ Indexing []                               ║
║  __call__    Make Object Callable ()                   ║
║                                                        ║
╚════════════════════════════════════════════════════════╝
"""


# ═══════════════════════════════════════════════════════════════
#  TOPIC 1: Operator Overloading
# ═══════════════════════════════════════════════════════════════

# Operator Overloading and Dunder/Magic Functions

class AddingComplexNumber:
    """
    A class to represent complex numbers and perform addition.

    Attributes:
        Real (int): The real part of the complex number.
        Img (int): The imaginary part of the complex number.

    Methods:
        __init__: Initializes the complex number with real and imaginary parts.
        __add__: Adds two complex numbers.
        __str__: Converts the complex number to a string representation.
    """

    def __init__(self, RealNumber, ImaginaryNumber):
        """
        Initializes the complex number with real and imaginary parts.

        Args:
            RealNumber (int): The real part of the complex number.
            ImaginaryNumber (int): The imaginary part of the complex number.

        Example:
            >>> A = AddingComplexNumber(1, 2)
            >>> A.Real
            1
            >>> A.Img
            2
        """
        self.Real = RealNumber
        self.Img = ImaginaryNumber

    def __add__(self, Other):
        """
        Adds two complex numbers.

        Args:
            Other (AddingComplexNumber): The other complex number to add.

        Returns:
            AddingComplexNumber: The result of the addition.

        Example:
            >>> A = AddingComplexNumber(1, 2)
            >>> B = AddingComplexNumber(3, 4)
            >>> H = A + B
            >>> H.Real
            4
            >>> H.Img
            6
        """
        return AddingComplexNumber(self.Real + Other.Real, self.Img + Other.Img)

    def __str__(self):
        """
        Converts the complex number to a string representation.

        Returns:
            str: The string representation of the complex number.

        Example:
            >>> A = AddingComplexNumber(1, 2)
            >>> print(A)
            1 + 2j
        """
        return f"{self.Real} + {self.Img}j"

# Example usage
A = AddingComplexNumber(1, 2)
B = AddingComplexNumber(3, 4)
H = A + B
print(H)  # Output: 4 + 6j

# List of all dunder/magic functions in operator overloading

# Unary Operators
# __pos__() = Unary positive
# Example: +A
# __neg__() = Unary negative
# Example: -A
# __invert__() = Unary invert
# Example: ~A

# Binary Operators
# __add__() = Adding two numbers/string
# Example: A + B
# __sub__() = Subtracting two numbers
# Example: A - B
# __mul__() = Multiplying two numbers
# Example: A * B
# __truediv__() = Dividing two numbers
# Example: A / B
# __floordiv__() = Floor division
# Example: A // B
# __pow__() = Power
# Example: A ** B
# __lshift__() = Left shift
# Example: A << B
# __rshift__() = Right shift
# Example: A >> B
# __and__() = Bitwise AND
# Example: A & B
# __or__() = Bitwise OR
# Example: A | B
# __xor__() = Bitwise XOR
# Example: A ^ B

# Comparison Operators
# __eq__() = Equal
# Example: A == B
# __ne__() = Not equal
# Example: A != B
# __lt__() = Less than
# Example: A < B
# __le__() = Less than or equal
# Example: A <= B
# __gt__() = Greater than
# Example: A > B
# __ge__() = Greater than or equal
# Example: A >= B

# Container Emulation
# __len__() = Length
# Example: len(A)
# __getitem__() = Get item
# Example: A[0]
# __setitem__() = Set item
# Example: A[0] = 1
# __delitem__() = Delete item
# Example: del A[0]
# __iter__() = Iterator
# Example: for item in A:
# __contains__() = Contains
# Example: 1 in A

# Attribute Access
# __getattr__() = Get attribute
# Example: A.attr
# __setattr__() = Set attribute
# Example: A.attr = 1
# __delattr__() = Delete attribute
# Example: del A.attr

# Callable Objects
# __call__() = Callable object
# Example: A()

# Context Managers
# __enter__() = Enter context
# Example: with A:
# __exit__() = Exit context
# Example: with A:

# Descriptor Objects
# __get__() = Get descriptor
# Example: A.descriptor
# __set__() = Set descriptor
# Example: A.descriptor = 1
# __delete__() = Delete descriptor
# Example: del A.descriptor

# Pickling
# __getstate__() = Get state
# Example: pickle.dumps(A)
# __setstate__() = Set state
# Example: pickle.loads(A)

# Representation
# __repr__() = Representation
# Example: repr(A)
# __str__() = String representation
# Example: str(A)

class AddingComplexNumber:
    def __init__(self, RealNumber, ImaginaryNumber):
        self.Real = RealNumber
        self.Img = ImaginaryNumber

    def __repr__(self):
        return f"AddingComplexNumber({self.Real}, {self.Img})"

A = AddingComplexNumber(1, 2)
H = repr(A)  # Output: AddingComplexNumber(1, 2)
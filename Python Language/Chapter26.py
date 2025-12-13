# ╔═══════════════════════════════════════════════════════════════╗
# ║               CHAPTER 26: TESTING BASICS                      ║
# ╠═══════════════════════════════════════════════════════════════╣
# ║                                                               ║
# ║  TABLE OF CONTENTS:                                           ║
# ║  ═════════════════                                            ║
# ║                                                               ║
# ║  1. Simple Assert Testing                                     ║
# ║     - assert Statement                                        ║
# ║     - Basic Test Functions                                    ║
# ║                                                               ║
# ║  2. Testing With Error Handling                               ║
# ║     - try-except In Tests                                     ║
# ║     - Validating Exceptions                                   ║
# ║                                                               ║
# ║  3. unittest Module (Structured Testing)                      ║
# ║     - TestCase Class                                          ║
# ║     - Test Methods (test_*)                                   ║
# ║     - setUp() And tearDown()                                  ║
# ║                                                               ║
# ║  4. Assertion Methods                                         ║
# ║     - assertEqual, assertNotEqual                             ║
# ║     - assertTrue, assertFalse                                 ║
# ║     - assertRaises                                            ║
# ║                                                               ║
# ║  5. Running Tests (unittest.main())                           ║
# ║  6. Test-Driven Development (TDD) Basics                      ║
# ║                                                               ║
# ╚═══════════════════════════════════════════════════════════════╝

"""
╔════════════════════════════════════════════════════════╗
║         TEST-DRIVEN DEVELOPMENT (TDD) CYCLE            ║
╠════════════════════════════════════════════════════════╣
║                                                        ║
║   1. Write Test ────────> FAIL (Red)                   ║
║         │                                              ║
║         ├─> 2. Write Code ────> PASS (Green)           ║
║         │                           │                  ║
║         │                           │                  ║
║         └───<───── 3. Refactor <────┘                  ║
║                       │                                ║
║                       └──> REPEAT                      ║
║                                                        ║
╚════════════════════════════════════════════════════════╝
"""

# Chapter 26: Testing Basics
"""
Python's Built-In 'assert' Statement Checks Conditions.
For More Advanced Testing, Use the 'unittest' Module.

How It Works:
- assert Condition: Raises AssertionError If False
- Use For Validating Function Outputs, Edge Cases
- Write Tests Before Or After Implementing Features
"""

# Simple Assert Tests
def add(a, b):
    return a + b

def Test_Add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    print("All Add Tests Passed!")

Test_Add()

# Testing With Error Handling
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot Divide By Zero")
    return a / b

def Test_Divide():
    assert divide(10, 2) == 5
    assert divide(9, 3) == 3
    try:
        divide(5, 0)
        assert False, "Should Have Raised ValueError"
    except ValueError:
        pass  # Expected
    print("All Divide Tests Passed!")

Test_Divide()

# Using unittest Module (More Structured)
import unittest

class TestMathFunctions(unittest.TestCase):
    def Test_Add_Positive(self):
        self.assertEqual(add(2, 3), 5)

    def Test_Add_Negative(self):
        self.assertEqual(add(-2, -3), -5)

    def Test_Divide_Normal(self):
        self.assertEqual(divide(10, 2), 5)

    def Test_Divide_By_Zero(self):
        with self.assertRaises(ValueError):
            divide(5, 0)

if __name__ == '__main__':
    unittest.main()
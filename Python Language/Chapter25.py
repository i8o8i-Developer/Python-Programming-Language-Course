# ╔═══════════════════════════════════════════════════════════════╗
# ║            CHAPTER 25: GENERATORS AND ITERATORS               ║
# ╠═══════════════════════════════════════════════════════════════╣
# ║                                                               ║
# ║  TABLE OF CONTENTS:                                           ║
# ║  ═════════════════                                            ║
# ║                                                               ║
# ║  1. What Are Iterators?                                       ║
# ║     - iter() And next() Functions                             ║
# ║     - Iterator Protocol (__iter__, __next__)                  ║
# ║                                                               ║
# ║  2. Creating Custom Iterators                                 ║
# ║     - Iterator Class Example                                  ║
# ║     - StopIteration Exception                                 ║
# ║                                                               ║
# ║  3. Generator Functions                                       ║
# ║     - yield Keyword                                           ║
# ║     - Generator State Management                              ║
# ║     - yield vs return                                         ║
# ║                                                               ║
# ║  4. Generator Expressions                                     ║
# ║     - Syntax: (expr for item in iterable)                     ║
# ║     - Memory Efficiency                                       ║
# ║     - vs List Comprehensions                                  ║
# ║                                                               ║
# ║  5. Advanced Generator Techniques                             ║
# ║     - Infinite Generators                                     ║
# ║     - Generator Pipelines                                     ║
# ║     - send() Method                                           ║
# ║     - throw() And close() Methods                             ║
# ║                                                               ║
# ║  6. Practical Examples                                        ║
# ║     - Reading Large Files                                     ║
# ║     - Fibonacci Generator                                     ║
# ║     - Prime Number Generator                                  ║
# ║                                                               ║
# ╚═══════════════════════════════════════════════════════════════╝

"""
╔════════════════════════════════════════════════════════╗
║         GENERATOR VS REGULAR FUNCTION                  ║
╠════════════════════════════════════════════════════════╣
║                                                        ║
║  Regular Function      Generator Function              ║
║  ────────────────      ─────────────────               ║
║                                                        ║
║  def func():           def gen():                      ║
║      return [1,2,3]        yield 1                     ║
║                            yield 2                     ║
║  Returns: List             yield 3                     ║
║  Memory: Stores All                                    ║
║                        Returns: Generator Object       ║
║                        Memory: Generates On-The-Fly    ║
║                                                        ║
╚════════════════════════════════════════════════════════╝
"""

# Chapter 25: Generators and Iterators
"""
Iterators Are Objects That Can Be Iterated Over (e.g., Lists, Strings).
Generators Are Special Iterators Created With 'Yield' Instead Of 'Return'.

How It Works:
- iter() Creates An Iterator From An Iterable
- next() Gets The Next Item From An Iterator
- Generators Use 'Yield' To Produce Values One At A Time
- Memory Efficient For Large Datasets
- Can Only Be Consumed Once
"""

# Basic Iterator
My_List = [1, 2, 3, 4, 5]
My_Iter = iter(My_List)  # Create Iterator

print("Manual Iteration:")
print(next(My_Iter))  # 1
print(next(My_Iter))  # 2

# For Loop Uses Iterators Internally
for item in My_List:
    print(f"For Loop: {item}")

# Custom Iterator Class
class Countdown:
    """Iterator That Counts Down From A Number"""
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self  # Iterator Is Itself

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        self.current -= 1
        return self.current + 1

CountDown = Countdown(5)
for num in CountDown:
    print(f"CountDown : {num}")

# Generator Function
def Simple_Generator():
    """Generator That Yields Numbers"""
    yield 1
    yield 2
    yield 3

gen = Simple_Generator()
print("Generator Values:")
print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3
# next(gen) Would Raise StopIteration

# Generator With Loop
def Fibonacci_Generator(n):
    """Generate First n Fibonacci Numbers"""
    a, b = 0, 1
    Count = 0
    while Count < n:
        yield a
        a, b = b, a + b
        Count += 1

for Num in Fibonacci_Generator(10):
    print(f"Fib: {Num}", end=" ")
print()

# Generator Expressions (Like List Comprehensions)
Gen_Expr = (x**2 for x in range(5))
print("Generator Expression:", list(Gen_Expr))  # Convert To List To See Values

# Memory Comparison
import sys

# List Comprehension (Creates All At Once)
Big_List = [x for x in range(100000)]
print(f"List Memory: {sys.getsizeof(Big_List)} Bytes")

# Generator Expression (Creates On Demand)
Big_Gen = (x for x in range(100000))
print(f"Generator Memory: {sys.getsizeof(Big_Gen)} Bytes")

# Infinite Generator
def Infinite_Counter():
    """Generator That Counts Forever"""
    num = 0
    while True:
        yield num
        num += 1

Counter = Infinite_Counter()
for _ in range(5):
    print(f"Infinite: {next(Counter)}")

# Generator With Send() - Advanced
def Accumulator():
    """Generator That Accumulates Values"""
    Total = 0
    while True:
        value = (yield Total)  # Receive Value Via send()
        if value is not None:
            Total += value

Acc = Accumulator()
next(Acc)  # Prime The Generator
print(f"Total: {Acc.send(10)}")  # Send 10, Get Total
print(f"Total: {Acc.send(5)}")   # Send 5, Get Total

# Use Cases:
# - Processing Large Files Line By Line
# - Generating Infinite Sequences
# - Memory-Efficient Data Processing
# - Implementing Coroutines

print("\nGenerators Provide Lazy Evaluation And Memory Efficiency.")
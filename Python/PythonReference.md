# Python Reference Sheet

## Variables & Data Types

```python
# Variables (no declaration needed)
name = "Alice"          # String
age = 25                # Integer
price = 19.99           # Float
is_active = True        # Boolean
items = None            # NoneType

# Check type
type(name)              # <class 'str'>
```

## Strings

```python
text = "Hello, World!"

# Common methods
text.lower()            # "hello, world!"
text.upper()            # "HELLO, WORLD!"
text.strip()            # Remove whitespace from ends
text.split(",")         # ["Hello", " World!"]
text.replace("H", "J")  # "Jello, World!"
text.find("World")      # 7 (index where found)
len(text)               # 13

# String formatting
name = "Alice"
f"Hello, {name}!"       # f-strings (recommended)
"Hello, {}!".format(name)

# Slicing
text[0]                 # "H" (first character)
text[-1]                # "!" (last character)
text[0:5]               # "Hello" (index 0 to 4)
text[7:]                # "World!" (index 7 to end)
```

## Input/Output

```python
# Output
print("Hello")
print("Value:", x)
print(f"Name: {name}, Age: {age}")

# Input (always returns string)
name = input("Enter your name: ")
age = int(input("Enter age: "))     # Convert to int
price = float(input("Enter price: "))  # Convert to float
```

## Operators

```python
# Arithmetic
+   # Addition
-   # Subtraction
*   # Multiplication
/   # Division (returns float)
//  # Floor division (returns int)
%   # Modulus (remainder)
**  # Exponent

# Comparison (return True/False)
==  # Equal
!=  # Not equal
>   # Greater than
<   # Less than
>=  # Greater than or equal
<=  # Less than or equal

# Logical
and  # Both must be True
or   # At least one True
not  # Inverts True/False
```

## Conditionals

```python
if condition:
    # code
elif another_condition:
    # code
else:
    # code

# Example
age = 18
if age >= 21:
    print("Adult")
elif age >= 13:
    print("Teen")
else:
    print("Child")
```

## Loops

```python
# For loop
for i in range(5):          # 0, 1, 2, 3, 4
    print(i)

for i in range(2, 6):       # 2, 3, 4, 5
    print(i)

for i in range(0, 10, 2):   # 0, 2, 4, 6, 8 (step by 2)
    print(i)

for item in my_list:        # Loop through list
    print(item)

# While loop
count = 0
while count < 5:
    print(count)
    count += 1

# Loop control
break       # Exit loop entirely
continue    # Skip to next iteration
```

## Lists

```python
fruits = ["apple", "banana", "cherry"]

# Access
fruits[0]               # "apple"
fruits[-1]              # "cherry" (last item)

# Modify
fruits[0] = "orange"    # Replace first item
fruits.append("grape")  # Add to end
fruits.insert(1, "kiwi")  # Insert at index 1
fruits.remove("banana") # Remove by value
fruits.pop()            # Remove & return last item
fruits.pop(0)           # Remove & return item at index

# Other methods
len(fruits)             # Length
fruits.sort()           # Sort in place
fruits.reverse()        # Reverse in place
"apple" in fruits       # True/False (check membership)
fruits.index("cherry")  # Find index of item
fruits.count("apple")   # Count occurrences
```

## Dictionaries

```python
person = {
    "name": "Alice",
    "age": 25,
    "city": "NYC"
}

# Access
person["name"]          # "Alice"
person.get("name")      # "Alice" (safer, returns None if missing)

# Modify
person["age"] = 26      # Update value
person["job"] = "Dev"   # Add new key
del person["city"]      # Delete key

# Methods
person.keys()           # All keys
person.values()         # All values
person.items()          # Key-value pairs
"name" in person        # Check if key exists

# Loop through
for key in person:
    print(key, person[key])

for key, value in person.items():
    print(key, value)
```

## Functions

```python
# Define a function
def greet(name):
    return f"Hello, {name}!"

# Call a function
message = greet("Alice")

# Default parameters
def greet(name="World"):
    return f"Hello, {name}!"

# Multiple parameters
def add(a, b):
    return a + b

# Return multiple values
def get_stats(numbers):
    return min(numbers), max(numbers)

low, high = get_stats([1, 2, 3, 4, 5])
```

## Common Built-in Functions

```python
len(x)          # Length of string, list, etc.
range(n)        # Numbers 0 to n-1
range(a, b)     # Numbers a to b-1
range(a, b, s)  # Numbers a to b-1, step s

int(x)          # Convert to integer
float(x)        # Convert to float
str(x)          # Convert to string
bool(x)         # Convert to boolean
list(x)         # Convert to list

max(list)       # Maximum value
min(list)       # Minimum value
sum(list)       # Sum of all values
abs(x)          # Absolute value
round(x, n)     # Round to n decimal places

sorted(list)    # Return sorted copy
reversed(list)  # Return reversed iterator
enumerate(list) # Returns index and value pairs
```

## File Handling

```python
# Read file
with open("file.txt", "r") as f:
    content = f.read()          # Read entire file
    # or
    lines = f.readlines()       # Read as list of lines

# Write file
with open("file.txt", "w") as f:
    f.write("Hello, World!")

# Append to file
with open("file.txt", "a") as f:
    f.write("New line\n")
```

## Error Handling

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
except Exception as e:
    print(f"Error: {e}")
finally:
    print("This always runs")
```

## List Comprehensions

```python
# Basic
squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]

# With condition
evens = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]
```

## Useful Shortcuts

```python
# Swap variables
a, b = b, a

# Multiple assignment
x, y, z = 1, 2, 3

# Check if string is number
"123".isdigit()     # True

# Join list to string
", ".join(["a", "b", "c"])  # "a, b, c"

# Random
import random
random.randint(1, 10)       # Random int 1-10
random.choice(my_list)      # Random item from list
random.shuffle(my_list)     # Shuffle list in place
```

## Tuples

```python
# Tuples are like lists but immutable (can't change after creation)
coords = (10, 20)
rgb = (255, 128, 0)

# Access (same as lists)
coords[0]               # 10
coords[-1]              # 20

# Unpack
x, y = coords           # x=10, y=20

# Single element tuple (need trailing comma)
single = (42,)

# Useful for returning multiple values from functions
# and as dictionary keys (lists can't be dict keys)
```

## Sets

```python
# Unordered collection of unique items
colors = {"red", "green", "blue"}

# Add/remove
colors.add("yellow")
colors.remove("red")        # Error if not found
colors.discard("red")       # No error if not found

# Set operations
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

a | b       # Union: {1, 2, 3, 4, 5, 6}
a & b       # Intersection: {3, 4}
a - b       # Difference: {1, 2}
a ^ b       # Symmetric difference: {1, 2, 5, 6}

# Remove duplicates from a list
nums = [1, 2, 2, 3, 3, 3]
unique = list(set(nums))    # [1, 2, 3]
```

## Ternary Operator

```python
# One-line if/else
age = 18
status = "adult" if age >= 18 else "minor"

# Works in assignments, return statements, etc.
print("even" if x % 2 == 0 else "odd")
```

## Dictionary & Set Comprehensions

```python
# Dictionary comprehension
squares = {x: x**2 for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# With condition
even_sq = {x: x**2 for x in range(10) if x % 2 == 0}

# Set comprehension
unique_lengths = {len(word) for word in ["hi", "hey", "hello"]}
# {2, 3, 5}
```

## Lambda Functions

```python
# Anonymous (unnamed) one-line functions
square = lambda x: x ** 2
square(5)               # 25

add = lambda a, b: a + b
add(3, 4)               # 7

# Useful with sort, map, filter
students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]
students.sort(key=lambda s: s[1])  # Sort by score
```

## Map, Filter, Zip

```python
# map - apply function to every item
nums = [1, 2, 3, 4]
doubled = list(map(lambda x: x * 2, nums))   # [2, 4, 6, 8]

# filter - keep items that return True
evens = list(filter(lambda x: x % 2 == 0, nums))  # [2, 4]

# zip - pair up items from multiple lists
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]
paired = list(zip(names, scores))
# [("Alice", 85), ("Bob", 92), ("Charlie", 78)]

for name, score in zip(names, scores):
    print(f"{name}: {score}")
```

## *args and **kwargs

```python
# *args - accept any number of positional arguments
def add_all(*args):
    return sum(args)

add_all(1, 2, 3)         # 6
add_all(1, 2, 3, 4, 5)   # 15

# **kwargs - accept any number of keyword arguments
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25)

# Can combine both
def func(a, b, *args, **kwargs):
    pass
```

## Classes (OOP Basics)

```python
class Dog:
    # Class variable (shared by all instances)
    species = "Canis familiaris"

    # Constructor
    def __init__(self, name, age):
        self.name = name        # Instance variable
        self.age = age

    # Method
    def bark(self):
        return f"{self.name} says Woof!"

    # String representation
    def __str__(self):
        return f"{self.name}, age {self.age}"

# Create objects
my_dog = Dog("Rex", 5)
print(my_dog.name)          # "Rex"
print(my_dog.bark())        # "Rex says Woof!"
print(my_dog)               # "Rex, age 5"

# Inheritance
class Puppy(Dog):
    def __init__(self, name, age, toy):
        super().__init__(name, age)
        self.toy = toy

    def play(self):
        return f"{self.name} plays with {self.toy}"
```

## Modules & Imports

```python
# Import entire module
import math
math.sqrt(16)               # 4.0

# Import specific items
from math import sqrt, pi
sqrt(16)                     # 4.0

# Import with alias
import numpy as np

# Common standard library modules
import os               # File system operations
import sys              # System-specific parameters
import math             # Math functions
import random           # Random numbers
import datetime         # Date and time
import json             # JSON encoding/decoding
import re               # Regular expressions
import collections      # Specialized containers
```

## Working with Dates & Times

```python
from datetime import datetime, date, timedelta

# Current date/time
now = datetime.now()
today = date.today()

# Create specific date
birthday = date(2000, 5, 15)

# Format dates
now.strftime("%Y-%m-%d")       # "2026-02-10"
now.strftime("%B %d, %Y")      # "February 10, 2026"
now.strftime("%I:%M %p")       # "03:30 PM"

# Date math
tomorrow = today + timedelta(days=1)
next_week = today + timedelta(weeks=1)
diff = date(2026, 12, 25) - today   # timedelta object
print(diff.days)                     # days until Christmas
```

## JSON

```python
import json

# Python dict to JSON string
data = {"name": "Alice", "age": 25}
json_str = json.dumps(data)              # '{"name": "Alice", "age": 25}'
json_pretty = json.dumps(data, indent=2) # Pretty-printed

# JSON string to Python dict
parsed = json.loads(json_str)
parsed["name"]                            # "Alice"

# Read/write JSON files
with open("data.json", "r") as f:
    data = json.load(f)

with open("data.json", "w") as f:
    json.dump(data, f, indent=2)
```

## Regular Expressions

```python
import re

text = "My email is alice@example.com and bob@test.org"

# Search for pattern
match = re.search(r"\d+", "There are 42 apples")
if match:
    print(match.group())        # "42"

# Find all matches
emails = re.findall(r"[\w.]+@[\w.]+", text)
# ["alice@example.com", "bob@test.org"]

# Replace
cleaned = re.sub(r"\d+", "X", "abc123def456")
# "abcXdefX"

# Common patterns
r"\d"       # Digit (0-9)
r"\w"       # Word character (a-z, A-Z, 0-9, _)
r"\s"       # Whitespace
r"."        # Any character except newline
r"+"        # One or more
r"*"        # Zero or more
r"?"        # Zero or one
r"[abc]"    # Character class (a, b, or c)
r"^"        # Start of string
r"$"        # End of string
```

## Decorators

```python
# A decorator wraps a function to add behavior
def timer(func):
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.2f}s")
        return result
    return wrapper

@timer
def slow_function():
    import time
    time.sleep(1)

slow_function()     # "slow_function took 1.00s"
```

## Generators

```python
# Generators produce values one at a time (memory efficient)
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for num in countdown(5):
    print(num)              # 5, 4, 3, 2, 1

# Generator expression (like list comp but with parentheses)
squares = (x**2 for x in range(1000000))  # Doesn't store all in memory
```

## Useful String Methods

```python
# Checking content
"hello123".isalnum()    # True  (letters and numbers only)
"hello".isalpha()       # True  (letters only)
"12345".isdigit()       # True  (digits only)
"hello".islower()       # True
"HELLO".isupper()       # True
"  ".isspace()          # True

# Padding/alignment
"hi".ljust(10)          # "hi        "
"hi".rjust(10)          # "        hi"
"hi".center(10)         # "    hi    "
"42".zfill(5)           # "00042"

# Starts/ends with
"hello.py".endswith(".py")    # True
"hello.py".startswith("he")   # True

# Multi-line strings
text = """
This is a
multi-line string
"""
```

## Unpacking & Advanced Assignment

```python
# List/tuple unpacking
first, *rest = [1, 2, 3, 4, 5]
# first = 1, rest = [2, 3, 4, 5]

first, *middle, last = [1, 2, 3, 4, 5]
# first = 1, middle = [2, 3, 4], last = 5

# Dictionary merging (Python 3.9+)
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
merged = dict1 | dict2     # {"a": 1, "b": 3, "c": 4}

# Walrus operator (Python 3.8+) - assign and use in one step
if (n := len("hello")) > 3:
    print(f"Length {n} is greater than 3")
```

## Common Patterns

```python
# Counting items
from collections import Counter
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
counts = Counter(words)
# Counter({"apple": 3, "banana": 2, "cherry": 1})
counts.most_common(2)       # [("apple", 3), ("banana", 2)]

# Default dictionary
from collections import defaultdict
grouped = defaultdict(list)
for name, score in [("Alice", 85), ("Bob", 92), ("Alice", 90)]:
    grouped[name].append(score)
# {"Alice": [85, 90], "Bob": [92]}

# Enumerate with start index
for i, item in enumerate(["a", "b", "c"], start=1):
    print(f"{i}. {item}")   # 1. a, 2. b, 3. c

# any() and all()
nums = [2, 4, 6, 8]
all(x % 2 == 0 for x in nums)   # True (all even)
any(x > 5 for x in nums)        # True (at least one > 5)
```

## Virtual Environments & pip

```bash
# Create a virtual environment
python -m venv myenv

# Activate it
myenv\Scripts\activate          # Windows
source myenv/bin/activate       # Mac/Linux

# Install packages
pip install requests
pip install requests==2.28.0    # Specific version
pip install -r requirements.txt # From file

# Save current packages
pip freeze > requirements.txt

# Deactivate
deactivate
```
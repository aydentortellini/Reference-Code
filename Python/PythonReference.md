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

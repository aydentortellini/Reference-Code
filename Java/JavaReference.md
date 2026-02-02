# Java Quick Reference Guide

## Basic Structure

```java
public class ClassName {
    public static void main(String[] args) {
        // Entry point of the program
    }
}
```

## Output

```java
System.out.println("text");   // Print with newline
System.out.print("text");     // Print without newline
System.out.printf("%s", x);   // Formatted print (like C)
```

## Variables & Data Types

```java
int x = 10;           // Integer (whole numbers)
double y = 3.14;      // Decimal numbers
float z = 3.14f;      // Smaller decimal (needs 'f')
boolean flag = true;  // true or false
char c = 'A';         // Single character
String s = "Hello";   // Text (note: capital S)
long big = 100000L;   // Large integers (needs 'L')
```

## Input (Scanner)

```java
import java.util.Scanner;

Scanner sc = new Scanner(System.in);
String text = sc.nextLine();    // Read entire line
String word = sc.next();        // Read single word
int num = sc.nextInt();         // Read integer
double dec = sc.nextDouble();   // Read decimal
sc.close();                     // Close when done
```

## Arrays

```java
int[] nums = new int[5];              // Create array of size 5
int[] nums = {1, 2, 3, 4, 5};         // Create with values
nums[0] = 10;                         // Set first element
int len = nums.length;                // Get array length
```

## Conditionals

```java
if (condition) {
    // code
} else if (otherCondition) {
    // code
} else {
    // code
}

// Comparison operators
==    // equals
!=    // not equals
>     // greater than
<     // less than
>=    // greater or equal
<=    // less or equal
&&    // AND
||    // OR
!     // NOT
```

## Loops

```java
// For loop
for (int i = 0; i < 10; i++) {
    // runs 10 times (0-9)
}

// For-each loop (arrays/collections)
for (int num : nums) {
    // iterates through each element
}

// While loop
while (condition) {
    // runs while condition is true
}

// Do-while loop
do {
    // runs at least once
} while (condition);

break;      // Exit loop immediately
continue;   // Skip to next iteration
```

## Methods (Functions)

```java
// Method with return value
public static int add(int a, int b) {
    return a + b;
}

// Method with no return (void)
public static void sayHello(String name) {
    System.out.println("Hello " + name);
}
```

## String Methods

```java
String s = "Hello World";

s.length()              // Get length: 11
s.charAt(0)             // Get char at index: 'H'
s.substring(0, 5)       // Get substring: "Hello"
s.toLowerCase()         // Convert to lowercase
s.toUpperCase()         // Convert to uppercase
s.trim()                // Remove leading/trailing spaces
s.contains("World")     // Check if contains: true
s.equals("Hello")       // Compare strings (use this, not ==)
s.equalsIgnoreCase()    // Compare ignoring case
s.split(" ")            // Split into array: ["Hello", "World"]
s.replace("o", "0")     // Replace chars: "Hell0 W0rld"
s.indexOf("W")          // Find index: 6 (-1 if not found)
```

## Math Operations

```java
Math.abs(-5)            // Absolute value: 5
Math.max(3, 7)          // Maximum: 7
Math.min(3, 7)          // Minimum: 3
Math.pow(2, 3)          // Power: 8.0 (2^3)
Math.sqrt(16)           // Square root: 4.0
Math.round(3.7)         // Round: 4
Math.random()           // Random 0.0 to 1.0
(int)(Math.random()*10) // Random int 0-9
```

## Type Conversion

```java
// String to number
int i = Integer.parseInt("123");
double d = Double.parseDouble("3.14");

// Number to String
String s = String.valueOf(123);
String s = Integer.toString(123);

// Casting between number types
int i = (int) 3.14;     // Truncates to 3
double d = (double) 5;  // Becomes 5.0
```

## ArrayList (Dynamic Array)

```java
import java.util.ArrayList;

ArrayList<String> list = new ArrayList<>();
list.add("item");           // Add to end
list.add(0, "first");       // Add at index
list.get(0);                // Get element
list.set(0, "new");         // Replace element
list.remove(0);             // Remove by index
list.remove("item");        // Remove by value
list.size();                // Get size
list.contains("item");      // Check if exists
list.clear();               // Remove all
```

## Common Errors & Fixes

| Error | Meaning |
|-------|---------|
| `NullPointerException` | Using a variable that is null |
| `ArrayIndexOutOfBoundsException` | Accessing invalid array index |
| `cannot find symbol` | Variable/method doesn't exist or typo |
| `incompatible types` | Wrong data type assignment |
| `missing return statement` | Method needs to return something |

## Quick Tips

- Class names start with uppercase: `MyClass`
- Variable/method names start with lowercase: `myVariable`
- Use `equals()` to compare Strings, not `==`
- Arrays start at index 0
- `length` for arrays, `length()` for Strings, `size()` for ArrayList

---

# Advanced Java Concepts

## Object-Oriented Programming (OOP)

### Classes & Objects

```java
public class Dog {
    // Instance variables (fields)
    private String name;
    private int age;

    // Constructor
    public Dog(String name, int age) {
        this.name = name;
        this.age = age;
    }

    // Getter
    public String getName() {
        return name;
    }

    // Setter
    public void setName(String name) {
        this.name = name;
    }

    // Method
    public void bark() {
        System.out.println(name + " says woof!");
    }
}

// Using the class
Dog myDog = new Dog("Buddy", 3);
myDog.bark();
```

### Inheritance

```java
// Parent class (superclass)
public class Animal {
    protected String name;

    public void eat() {
        System.out.println(name + " is eating");
    }
}

// Child class (subclass)
public class Cat extends Animal {
    public Cat(String name) {
        this.name = name;  // inherited from Animal
    }

    public void meow() {
        System.out.println(name + " says meow!");
    }
}
```

### Method Overriding

```java
public class Animal {
    public void makeSound() {
        System.out.println("Some sound");
    }
}

public class Dog extends Animal {
    @Override
    public void makeSound() {
        System.out.println("Woof!");
    }
}
```

### Abstract Classes

```java
public abstract class Shape {
    // Abstract method (no body, must be implemented)
    public abstract double getArea();

    // Regular method
    public void printInfo() {
        System.out.println("I am a shape");
    }
}

public class Circle extends Shape {
    private double radius;

    public Circle(double radius) {
        this.radius = radius;
    }

    @Override
    public double getArea() {
        return Math.PI * radius * radius;
    }
}
```

### Interfaces

```java
public interface Drawable {
    void draw();  // implicitly public abstract

    // Default method (Java 8+)
    default void print() {
        System.out.println("Printing...");
    }
}

public class Rectangle implements Drawable {
    @Override
    public void draw() {
        System.out.println("Drawing rectangle");
    }
}

// A class can implement multiple interfaces
public class Square implements Drawable, Comparable<Square> {
    // must implement all methods
}
```

## Access Modifiers

```java
public      // Accessible from anywhere
private     // Accessible only within the class
protected   // Accessible within package and subclasses
(default)   // Accessible only within package (no keyword)
```

## Static Keyword

```java
public class Counter {
    // Shared by all instances
    private static int count = 0;

    // Can be called without creating object
    public static int getCount() {
        return count;
    }

    // Static block - runs once when class loads
    static {
        System.out.println("Class loaded");
    }
}

// Usage
Counter.getCount();  // No need to create instance
```

## Final Keyword

```java
final int MAX = 100;           // Constant (can't change)
final class Utility { }        // Can't be extended
final void method() { }        // Can't be overridden
```

## Exception Handling

```java
try {
    int result = 10 / 0;  // Risky code
} catch (ArithmeticException e) {
    System.out.println("Cannot divide by zero!");
} catch (Exception e) {
    System.out.println("Something went wrong: " + e.getMessage());
} finally {
    // Always runs (cleanup code)
    System.out.println("Done");
}

// Throwing exceptions
public void checkAge(int age) throws IllegalArgumentException {
    if (age < 0) {
        throw new IllegalArgumentException("Age cannot be negative");
    }
}
```

## HashMap (Key-Value Pairs)

```java
import java.util.HashMap;

HashMap<String, Integer> scores = new HashMap<>();
scores.put("Alice", 95);            // Add entry
scores.put("Bob", 87);
scores.get("Alice");                // Get value: 95
scores.getOrDefault("Eve", 0);      // Get or default if missing
scores.containsKey("Bob");          // Check key exists: true
scores.containsValue(87);           // Check value exists: true
scores.remove("Bob");               // Remove entry
scores.size();                      // Number of entries
scores.keySet();                    // Get all keys
scores.values();                    // Get all values

// Iterate through HashMap
for (String key : scores.keySet()) {
    System.out.println(key + ": " + scores.get(key));
}

// Or using entrySet
for (Map.Entry<String, Integer> entry : scores.entrySet()) {
    System.out.println(entry.getKey() + ": " + entry.getValue());
}
```

## HashSet (Unique Values)

```java
import java.util.HashSet;

HashSet<String> names = new HashSet<>();
names.add("Alice");
names.add("Bob");
names.add("Alice");     // Ignored (duplicate)
names.size();           // 2 (only unique values)
names.contains("Bob");  // true
names.remove("Bob");
names.isEmpty();
```

## Generics

```java
// Generic class
public class Box<T> {
    private T content;

    public void set(T content) {
        this.content = content;
    }

    public T get() {
        return content;
    }
}

Box<String> stringBox = new Box<>();
stringBox.set("Hello");

Box<Integer> intBox = new Box<>();
intBox.set(123);

// Generic method
public static <T> void printArray(T[] array) {
    for (T element : array) {
        System.out.println(element);
    }
}
```

## Lambda Expressions (Java 8+)

```java
// Old way with anonymous class
Runnable r1 = new Runnable() {
    @Override
    public void run() {
        System.out.println("Running");
    }
};

// Lambda way
Runnable r2 = () -> System.out.println("Running");

// Lambda with parameters
Comparator<String> comp = (a, b) -> a.length() - b.length();

// Common functional interfaces
Consumer<String> printer = s -> System.out.println(s);
Predicate<Integer> isEven = n -> n % 2 == 0;
Function<String, Integer> length = s -> s.length();
Supplier<Double> random = () -> Math.random();
```

## Stream API (Java 8+)

```java
import java.util.stream.*;
import java.util.Arrays;
import java.util.List;

List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);

// Filter - keep elements matching condition
List<Integer> evens = numbers.stream()
    .filter(n -> n % 2 == 0)
    .collect(Collectors.toList());  // [2, 4, 6, 8, 10]

// Map - transform each element
List<Integer> doubled = numbers.stream()
    .map(n -> n * 2)
    .collect(Collectors.toList());  // [2, 4, 6, 8, ...]

// Reduce - combine to single value
int sum = numbers.stream()
    .reduce(0, (a, b) -> a + b);    // 55

// Chaining operations
int result = numbers.stream()
    .filter(n -> n > 5)
    .map(n -> n * 2)
    .reduce(0, Integer::sum);       // 80

// Other useful operations
numbers.stream().count();           // Count elements
numbers.stream().min(Integer::compare);  // Find min
numbers.stream().max(Integer::compare);  // Find max
numbers.stream().sorted();          // Sort
numbers.stream().distinct();        // Remove duplicates
numbers.stream().limit(5);          // Take first 5
numbers.stream().skip(3);           // Skip first 3
numbers.stream().anyMatch(n -> n > 5);   // true if any match
numbers.stream().allMatch(n -> n > 0);   // true if all match
numbers.stream().forEach(System.out::println);  // Print each
```

## File I/O

```java
import java.io.*;
import java.nio.file.*;

// Reading a file (modern way)
String content = Files.readString(Path.of("file.txt"));
List<String> lines = Files.readAllLines(Path.of("file.txt"));

// Writing a file (modern way)
Files.writeString(Path.of("file.txt"), "Hello World");
Files.write(Path.of("file.txt"), lines);

// Reading with BufferedReader (traditional)
try (BufferedReader reader = new BufferedReader(new FileReader("file.txt"))) {
    String line;
    while ((line = reader.readLine()) != null) {
        System.out.println(line);
    }
}

// Writing with PrintWriter (traditional)
try (PrintWriter writer = new PrintWriter(new FileWriter("file.txt"))) {
    writer.println("Hello World");
}
```

## Multithreading Basics

```java
// Method 1: Extend Thread
class MyThread extends Thread {
    @Override
    public void run() {
        System.out.println("Thread running");
    }
}

MyThread t = new MyThread();
t.start();

// Method 2: Implement Runnable
class MyRunnable implements Runnable {
    @Override
    public void run() {
        System.out.println("Runnable running");
    }
}

Thread t2 = new Thread(new MyRunnable());
t2.start();

// Method 3: Lambda (easiest)
Thread t3 = new Thread(() -> {
    System.out.println("Lambda thread running");
});
t3.start();

// Useful thread methods
Thread.sleep(1000);     // Pause for 1 second (throws InterruptedException)
t.join();               // Wait for thread to finish
t.isAlive();            // Check if thread is running
```

## Enum Types

```java
public enum Day {
    MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY
}

Day today = Day.MONDAY;

// Enum with values
public enum Size {
    SMALL("S"), MEDIUM("M"), LARGE("L");

    private String abbrev;

    Size(String abbrev) {
        this.abbrev = abbrev;
    }

    public String getAbbrev() {
        return abbrev;
    }
}

// Using enum in switch
switch (today) {
    case MONDAY -> System.out.println("Start of week");
    case FRIDAY -> System.out.println("Almost weekend!");
    default -> System.out.println("Regular day");
}
```

## Optional (Java 8+)

```java
import java.util.Optional;

// Avoid null pointer exceptions
Optional<String> name = Optional.of("Alice");
Optional<String> empty = Optional.empty();
Optional<String> nullable = Optional.ofNullable(possiblyNull);

name.isPresent();                  // true
name.get();                        // "Alice" (throws if empty)
name.orElse("Default");            // Value or default
name.orElseGet(() -> "Computed");  // Value or computed default
name.ifPresent(n -> System.out.println(n));
```

## Records (Java 16+)

```java
// Compact way to create data classes
public record Person(String name, int age) { }

// Automatically generates constructor, getters, equals, hashCode, toString
Person p = new Person("Alice", 25);
p.name();    // "Alice" (getter)
p.age();     // 25
```

## Switch Expressions (Java 14+)

```java
// Modern switch with arrow syntax
String result = switch (day) {
    case MONDAY, FRIDAY -> "Work day";
    case SATURDAY, SUNDAY -> "Weekend";
    default -> "Midweek";
};

// With code blocks
int numLetters = switch (day) {
    case MONDAY, FRIDAY, SUNDAY -> 6;
    case TUESDAY -> 7;
    default -> {
        String s = day.toString();
        yield s.length();  // yield instead of return
    }
};
```

## Common Design Patterns

### Singleton

```java
public class Database {
    private static Database instance;

    private Database() { }  // Private constructor

    public static Database getInstance() {
        if (instance == null) {
            instance = new Database();
        }
        return instance;
    }
}
```

### Builder Pattern

```java
public class Pizza {
    private String size;
    private boolean cheese;
    private boolean pepperoni;

    private Pizza(Builder builder) {
        this.size = builder.size;
        this.cheese = builder.cheese;
        this.pepperoni = builder.pepperoni;
    }

    public static class Builder {
        private String size;
        private boolean cheese = false;
        private boolean pepperoni = false;

        public Builder(String size) {
            this.size = size;
        }

        public Builder cheese() {
            this.cheese = true;
            return this;
        }

        public Builder pepperoni() {
            this.pepperoni = true;
            return this;
        }

        public Pizza build() {
            return new Pizza(this);
        }
    }
}

// Usage
Pizza pizza = new Pizza.Builder("Large")
    .cheese()
    .pepperoni()
    .build();
```

## Annotations

```java
@Override           // Marks method as overriding parent
@Deprecated         // Marks as outdated
@SuppressWarnings("unchecked")  // Suppress compiler warnings
@FunctionalInterface  // Marks interface for lambda use

// Custom annotation
@interface MyAnnotation {
    String value() default "";
}
```

## Useful Utility Classes

```java
// Arrays class
import java.util.Arrays;
Arrays.sort(arr);                    // Sort array
Arrays.binarySearch(arr, key);       // Search sorted array
Arrays.fill(arr, value);             // Fill with value
Arrays.copyOf(arr, newLength);       // Copy array
Arrays.equals(arr1, arr2);           // Compare arrays
Arrays.toString(arr);                // Array to string

// Collections class
import java.util.Collections;
Collections.sort(list);              // Sort list
Collections.reverse(list);           // Reverse list
Collections.shuffle(list);           // Randomize order
Collections.max(list);               // Find max
Collections.min(list);               // Find min
Collections.frequency(list, obj);    // Count occurrences

// Objects class
import java.util.Objects;
Objects.equals(a, b);                // Null-safe equals
Objects.hash(a, b, c);               // Generate hash
Objects.requireNonNull(obj);         // Throw if null

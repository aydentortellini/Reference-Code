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
```

---

## StringBuilder (Efficient String Building)

```java
// String concatenation in a loop is slow — use StringBuilder instead
StringBuilder sb = new StringBuilder();
sb.append("Hello");         // Add to end
sb.append(", ");
sb.append("World");
sb.insert(5, "!");          // Insert at index
sb.delete(5, 6);            // Delete chars from 5 to 6
sb.reverse();               // Reverse the contents
sb.replace(0, 5, "Hi");     // Replace range
sb.length();                // Current length
sb.charAt(0);               // Get char at index
String result = sb.toString();  // Convert back to String

// Chaining (each method returns the StringBuilder)
String s = new StringBuilder()
    .append("Hello")
    .append(" ")
    .append("World")
    .toString();  // "Hello World"

// String.format and String.join (alternatives)
String formatted = String.format("Name: %s, Age: %d", "Alice", 25);
String joined = String.join(", ", "Alice", "Bob", "Charlie");  // "Alice, Bob, Charlie"
String joined2 = String.join("-", List.of("a", "b", "c"));     // "a-b-c"
```

---

## 2D Arrays

```java
// Declare a 2D array (3 rows, 4 columns)
int[][] grid = new int[3][4];

// Initialize with values
int[][] matrix = {
    {1, 2, 3},
    {4, 5, 6},
    {7, 8, 9}
};

// Access elements
matrix[0][0] = 10;       // First row, first column
int val = matrix[1][2];  // Second row, third column: 6

// Dimensions
int rows = matrix.length;         // 3
int cols = matrix[0].length;      // 3

// Loop through 2D array
for (int i = 0; i < matrix.length; i++) {
    for (int j = 0; j < matrix[i].length; j++) {
        System.out.print(matrix[i][j] + " ");
    }
    System.out.println();
}

// For-each equivalent
for (int[] row : matrix) {
    for (int val2 : row) {
        System.out.print(val2 + " ");
    }
}

// Jagged array (rows of different sizes)
int[][] jagged = new int[3][];
jagged[0] = new int[2];
jagged[1] = new int[4];
jagged[2] = new int[1];
```

---

## Varargs (Variable-Length Arguments)

```java
// Accept any number of arguments of the same type
public static int sum(int... numbers) {
    int total = 0;
    for (int n : numbers) {
        total += n;
    }
    return total;
}

sum(1, 2, 3);          // 6
sum(10, 20);           // 30
sum();                 // 0

// Varargs must be the last parameter
public static void log(String label, int... values) {
    System.out.print(label + ": ");
    for (int v : values) System.out.print(v + " ");
}

log("scores", 90, 85, 78);  // scores: 90 85 78

// Internally treated as an array
public static void printAll(String... items) {
    System.out.println(items.length);  // works like array
}
```

---

## Autoboxing & Wrapper Types

```java
// Each primitive has a wrapper class
// int -> Integer,  double -> Double,  boolean -> Boolean,
// char -> Character,  long -> Long,  float -> Float, etc.

// Autoboxing: primitive -> wrapper (automatic)
Integer boxed = 42;           // same as Integer.valueOf(42)
Double d = 3.14;

// Unboxing: wrapper -> primitive (automatic)
int unboxed = boxed;          // same as boxed.intValue()

// Useful wrapper methods
Integer.parseInt("123");      // String to int
Integer.toBinaryString(10);   // "1010"
Integer.toHexString(255);     // "ff"
Integer.MAX_VALUE;            // 2147483647
Integer.MIN_VALUE;            // -2147483648

Double.isNaN(0.0 / 0.0);     // true
Double.isInfinite(1.0 / 0.0);// true

// Collections require wrapper types (not primitives)
List<Integer> ints = new ArrayList<>();
ints.add(5);    // autoboxed to Integer
int x = ints.get(0);  // unboxed to int
```

---

## Nested & Inner Classes

```java
// Static nested class — does NOT need an outer instance
public class Outer {
    private static int count = 0;

    public static class StaticNested {
        public void show() {
            System.out.println("count = " + count);  // can access static fields
        }
    }
}
Outer.StaticNested nested = new Outer.StaticNested();

// Inner class — requires an outer instance, can access all outer members
public class Outer {
    private String name = "Outer";

    public class Inner {
        public void show() {
            System.out.println(name);  // accesses outer's private field
        }
    }
}
Outer outer = new Outer();
Outer.Inner inner = outer.new Inner();

// Anonymous class — one-off implementation of an interface or abstract class
Runnable r = new Runnable() {
    @Override
    public void run() {
        System.out.println("Anonymous runnable");
    }
};

// Local class — defined inside a method
public void doSomething() {
    class LocalHelper {
        void help() { System.out.println("Helping"); }
    }
    new LocalHelper().help();
}
```

---

## More Collections

```java
import java.util.*;

// LinkedList — doubly linked list, good for frequent insert/remove
LinkedList<String> ll = new LinkedList<>();
ll.addFirst("first");    // Add to front
ll.addLast("last");      // Add to back
ll.peekFirst();          // View front without removing
ll.pollFirst();          // Remove and return front
ll.pollLast();           // Remove and return back

// Deque (double-ended queue) — stack + queue operations
Deque<Integer> deque = new ArrayDeque<>();
deque.push(1);           // Push to front (stack)
deque.pop();             // Pop from front (stack)
deque.offer(2);          // Add to back (queue)
deque.poll();            // Remove from front (queue)

// PriorityQueue — min-heap by default
PriorityQueue<Integer> pq = new PriorityQueue<>();
pq.add(5);
pq.add(1);
pq.add(3);
pq.peek();   // 1  (smallest, without removing)
pq.poll();   // 1  (removes smallest)

// Max-heap using comparator
PriorityQueue<Integer> maxPQ = new PriorityQueue<>(Comparator.reverseOrder());

// TreeMap — sorted HashMap (sorted by key)
TreeMap<String, Integer> treeMap = new TreeMap<>();
treeMap.put("banana", 2);
treeMap.put("apple", 5);
treeMap.put("cherry", 1);
treeMap.firstKey();         // "apple" (alphabetically first)
treeMap.lastKey();          // "cherry"
treeMap.headMap("cherry");  // entries before "cherry"
treeMap.tailMap("banana");  // entries from "banana" onward

// TreeSet — sorted HashSet (no duplicates, sorted order)
TreeSet<Integer> treeSet = new TreeSet<>();
treeSet.add(5);
treeSet.add(1);
treeSet.add(3);
treeSet.first();            // 1
treeSet.last();             // 5
treeSet.headSet(3);         // [1] (elements < 3)
treeSet.tailSet(3);         // [3, 5] (elements >= 3)
```

---

## Comparable & Comparator (Custom Sorting)

```java
// Comparable — class defines its own natural ordering
public class Student implements Comparable<Student> {
    String name;
    int grade;

    public Student(String name, int grade) {
        this.name = name;
        this.grade = grade;
    }

    @Override
    public int compareTo(Student other) {
        return this.grade - other.grade;  // sort by grade ascending
        // return other.grade - this.grade;  // descending
        // return this.name.compareTo(other.name);  // by name
    }
}

List<Student> students = new ArrayList<>();
students.add(new Student("Alice", 90));
students.add(new Student("Bob", 75));
Collections.sort(students);   // uses compareTo

// Comparator — external comparison logic (more flexible)
Comparator<Student> byName = Comparator.comparing(s -> s.name);
Comparator<Student> byGrade = Comparator.comparingInt(s -> s.grade);
Comparator<Student> byGradeDesc = Comparator.comparingInt((Student s) -> s.grade).reversed();

// Chaining comparators
Comparator<Student> byGradeThenName = Comparator
    .comparingInt((Student s) -> s.grade)
    .thenComparing(s -> s.name);

students.sort(byGradeThenName);
students.sort((a, b) -> a.name.compareTo(b.name));  // inline lambda
```

---

## Method References

```java
// Shorthand for lambdas that just call a method
// Syntax: ClassName::methodName  or  instance::methodName

// Static method reference
Function<String, Integer> parser = Integer::parseInt;
parser.apply("123");   // 123

// Instance method reference on a type
Function<String, String> upper = String::toUpperCase;
upper.apply("hello");  // "HELLO"

// Instance method reference on a specific object
String prefix = "Hello, ";
Function<String, String> greeter = prefix::concat;
greeter.apply("Alice");  // "Hello, Alice"

// Constructor reference
Supplier<ArrayList<String>> listFactory = ArrayList::new;
ArrayList<String> list = listFactory.get();

// Common usage in streams
List<String> names = List.of("alice", "bob", "charlie");
names.stream()
    .map(String::toUpperCase)           // method ref instead of s -> s.toUpperCase()
    .forEach(System.out::println);      // method ref instead of s -> System.out.println(s)

List<String> strings = List.of("3", "1", "4", "1", "5");
List<Integer> ints = strings.stream()
    .map(Integer::parseInt)             // static method ref
    .collect(Collectors.toList());
```

---

## Custom Exceptions

```java
// Checked exception (must be declared or caught)
public class InsufficientFundsException extends Exception {
    private double amount;

    public InsufficientFundsException(double amount) {
        super("Insufficient funds. Short by: " + amount);
        this.amount = amount;
    }

    public double getAmount() {
        return amount;
    }
}

// Unchecked exception (extends RuntimeException, no need to declare)
public class InvalidAgeException extends RuntimeException {
    public InvalidAgeException(String message) {
        super(message);
    }
}

// Throwing and catching
public void withdraw(double amount) throws InsufficientFundsException {
    if (amount > balance) {
        throw new InsufficientFundsException(amount - balance);
    }
    balance -= amount;
}

try {
    account.withdraw(1000);
} catch (InsufficientFundsException e) {
    System.out.println(e.getMessage());
    System.out.println("Short by: " + e.getAmount());
}

// Multi-catch (Java 7+)
try {
    // risky code
} catch (IOException | SQLException e) {
    System.out.println("IO or SQL error: " + e.getMessage());
}
```

---

## try-with-resources

```java
// Automatically closes resources that implement AutoCloseable
// No need for finally block to close

// Single resource
try (Scanner sc = new Scanner(new File("data.txt"))) {
    while (sc.hasNextLine()) {
        System.out.println(sc.nextLine());
    }
}  // sc.close() called automatically

// Multiple resources (closed in reverse order)
try (
    FileReader fr = new FileReader("input.txt");
    BufferedReader br = new BufferedReader(fr);
    PrintWriter pw = new PrintWriter("output.txt")
) {
    String line;
    while ((line = br.readLine()) != null) {
        pw.println(line.toUpperCase());
    }
}  // pw, then br, then fr all closed automatically

// Custom AutoCloseable class
public class DatabaseConnection implements AutoCloseable {
    public DatabaseConnection() { System.out.println("Connected"); }

    @Override
    public void close() { System.out.println("Disconnected"); }
}

try (DatabaseConnection conn = new DatabaseConnection()) {
    // use connection
}  // "Disconnected" printed automatically
```

---

## var Keyword (Java 10+)

```java
// Local variable type inference — compiler infers the type
var message = "Hello";          // String
var count = 42;                 // int
var price = 9.99;               // double
var list = new ArrayList<String>();  // ArrayList<String>

// Useful in for loops
for (var name : List.of("Alice", "Bob")) {
    System.out.println(name);
}

// Useful with long generic types
var map = new HashMap<String, List<Integer>>();

// Limitations — var cannot be used for:
// - fields, method parameters, or return types
// - without initialization (var x;  is invalid)
// - null initialization (var x = null;  is invalid)
```

---

## Text Blocks (Java 15+)

```java
// Multi-line strings without escape sequences
String json = """
        {
            "name": "Alice",
            "age": 25
        }
        """;

String html = """
        <html>
            <body>
                <p>Hello, World!</p>
            </body>
        </html>
        """;

// Indentation is stripped based on the closing """
// Trailing newline is included unless """ is on the same line as content

// Works with String methods
String query = """
        SELECT *
        FROM users
        WHERE age > 18
        """.strip();

// Formatted text blocks
String greeting = """
        Hello, %s!
        You are %d years old.
        """.formatted("Alice", 25);
```

---

## Pattern Matching instanceof (Java 16+)

```java
// Old way
Object obj = "Hello";
if (obj instanceof String) {
    String s = (String) obj;   // explicit cast needed
    System.out.println(s.length());
}

// New way — cast happens automatically
if (obj instanceof String s) {
    System.out.println(s.length());  // s is already a String
}

// Works in conditions too
if (obj instanceof String s && s.length() > 3) {
    System.out.println("Long string: " + s);
}

// Useful in polymorphic scenarios
public String describe(Object shape) {
    if (shape instanceof Circle c) {
        return "Circle with radius " + c.getRadius();
    } else if (shape instanceof Rectangle r) {
        return "Rectangle " + r.getWidth() + "x" + r.getHeight();
    } else {
        return "Unknown shape";
    }
}

// Pattern matching in switch (Java 21+)
String result = switch (obj) {
    case Integer i -> "int: " + i;
    case String s  -> "string: " + s;
    case null      -> "null";
    default        -> "other";
};
```

---

## Sealed Classes (Java 17+)

```java
// Restricts which classes can extend or implement this type
public sealed class Shape permits Circle, Rectangle, Triangle { }

public final class Circle extends Shape {
    private double radius;
    public Circle(double radius) { this.radius = radius; }
    public double getRadius() { return radius; }
}

public final class Rectangle extends Shape {
    private double width, height;
    public Rectangle(double w, double h) { this.width = w; this.height = h; }
}

public non-sealed class Triangle extends Shape {
    // non-sealed means Triangle itself can be extended further
}

// Sealed interfaces work the same way
public sealed interface Result<T> permits Success, Failure { }

public record Success<T>(T value) implements Result<T> { }
public record Failure<T>(String error) implements Result<T> { }

// Benefit: exhaustive switch (compiler knows all cases)
double area = switch (shape) {
    case Circle c    -> Math.PI * c.getRadius() * c.getRadius();
    case Rectangle r -> r.width * r.height;
    case Triangle t  -> 0.5 * t.base * t.height;
    // no default needed — compiler knows all subtypes
};
```

---

## More Stream API

```java
import java.util.stream.*;
import java.util.*;

List<List<Integer>> nested = List.of(List.of(1, 2), List.of(3, 4), List.of(5));

// flatMap — flatten nested collections
List<Integer> flat = nested.stream()
    .flatMap(Collection::stream)
    .collect(Collectors.toList());  // [1, 2, 3, 4, 5]

// Collectors.groupingBy — group elements by a classifier
List<String> words = List.of("ant", "bear", "apple", "bat", "cherry");
Map<Integer, List<String>> byLength = words.stream()
    .collect(Collectors.groupingBy(String::length));
// {3=[ant, bat], 4=[bear], 5=[apple], 6=[cherry]}

// groupingBy with a downstream collector
Map<Integer, Long> countByLength = words.stream()
    .collect(Collectors.groupingBy(String::length, Collectors.counting()));

// partitioningBy — split into two groups (true/false)
List<Integer> numbers = List.of(1, 2, 3, 4, 5, 6);
Map<Boolean, List<Integer>> evenOdd = numbers.stream()
    .collect(Collectors.partitioningBy(n -> n % 2 == 0));
// {false=[1, 3, 5], true=[2, 4, 6]}

// Collectors.toMap
Map<String, Integer> nameLengths = words.stream()
    .collect(Collectors.toMap(w -> w, String::length));
// {ant=3, bear=4, apple=5, bat=3, cherry=6}

// Collectors.joining
String sentence = words.stream()
    .collect(Collectors.joining(", ", "[", "]"));  // "[ant, bear, apple, bat, cherry]"

// Statistics
IntSummaryStatistics stats = numbers.stream()
    .mapToInt(Integer::intValue)
    .summaryStatistics();
stats.getMin();    // 1
stats.getMax();    // 6
stats.getSum();    // 21
stats.getAverage(); // 3.5
stats.getCount();  // 6

// takeWhile / dropWhile (Java 9+)
List<Integer> taken = numbers.stream()
    .takeWhile(n -> n < 4)
    .collect(Collectors.toList());  // [1, 2, 3]

List<Integer> dropped = numbers.stream()
    .dropWhile(n -> n < 4)
    .collect(Collectors.toList());  // [4, 5, 6]
```

---

## ExecutorService & CompletableFuture (Modern Concurrency)

```java
import java.util.concurrent.*;

// ExecutorService — manage a thread pool
ExecutorService executor = Executors.newFixedThreadPool(4);

// Submit a task (Runnable — no return value)
executor.submit(() -> System.out.println("Task running"));

// Submit a task (Callable — returns a value)
Future<Integer> future = executor.submit(() -> {
    Thread.sleep(1000);
    return 42;
});

int result = future.get();      // Blocks until result is ready
future.get(2, TimeUnit.SECONDS); // Timeout version

executor.shutdown();             // Gracefully stop accepting new tasks
executor.awaitTermination(5, TimeUnit.SECONDS);  // Wait for all tasks to finish

// CompletableFuture — non-blocking async operations (Java 8+)
CompletableFuture<String> cf = CompletableFuture.supplyAsync(() -> {
    // runs in ForkJoinPool.commonPool()
    return "Hello";
});

// Chain operations
cf.thenApply(s -> s + " World")         // transform result
  .thenApply(String::toUpperCase)
  .thenAccept(System.out::println);     // consume result (no return)

// Combine two futures
CompletableFuture<String> cf1 = CompletableFuture.supplyAsync(() -> "Hello");
CompletableFuture<String> cf2 = CompletableFuture.supplyAsync(() -> "World");

CompletableFuture<String> combined = cf1.thenCombine(cf2, (a, b) -> a + " " + b);
combined.thenAccept(System.out::println);  // "Hello World"

// Run multiple and wait for all
CompletableFuture.allOf(cf1, cf2).join();  // wait for all

// Error handling
cf.exceptionally(ex -> {
    System.out.println("Error: " + ex.getMessage());
    return "default";
});

// synchronized — prevent race conditions
public synchronized void increment() {
    count++;  // only one thread at a time
}

// volatile — ensure visibility across threads
private volatile boolean running = true;
```

---

## More Design Patterns

### Factory Pattern

```java
// Interface for product
public interface Animal {
    void speak();
}

public class Dog implements Animal {
    public void speak() { System.out.println("Woof!"); }
}

public class Cat implements Animal {
    public void speak() { System.out.println("Meow!"); }
}

// Factory creates the right object
public class AnimalFactory {
    public static Animal create(String type) {
        return switch (type.toLowerCase()) {
            case "dog" -> new Dog();
            case "cat" -> new Cat();
            default -> throw new IllegalArgumentException("Unknown: " + type);
        };
    }
}

Animal a = AnimalFactory.create("dog");
a.speak();  // "Woof!"
```

### Observer Pattern

```java
import java.util.*;

// Subject (notifies observers)
public class EventSource {
    private List<Observer> observers = new ArrayList<>();

    public void subscribe(Observer o) { observers.add(o); }
    public void unsubscribe(Observer o) { observers.remove(o); }

    public void notifyObservers(String event) {
        for (Observer o : observers) {
            o.onEvent(event);
        }
    }
}

// Observer interface
public interface Observer {
    void onEvent(String event);
}

// Concrete observers
EventSource source = new EventSource();
source.subscribe(event -> System.out.println("Observer 1: " + event));
source.subscribe(event -> System.out.println("Observer 2: " + event));
source.notifyObservers("click");  // both observers notified
```

### Strategy Pattern

```java
// Define interchangeable algorithms
public interface SortStrategy {
    void sort(int[] arr);
}

public class BubbleSort implements SortStrategy {
    public void sort(int[] arr) { /* bubble sort logic */ }
}

public class QuickSort implements SortStrategy {
    public void sort(int[] arr) { /* quicksort logic */ }
}

// Context uses strategy
public class Sorter {
    private SortStrategy strategy;

    public Sorter(SortStrategy strategy) {
        this.strategy = strategy;
    }

    public void setStrategy(SortStrategy strategy) {
        this.strategy = strategy;
    }

    public void sort(int[] arr) {
        strategy.sort(arr);
    }
}

Sorter sorter = new Sorter(new BubbleSort());
sorter.sort(new int[]{5, 1, 3});
sorter.setStrategy(new QuickSort());  // swap algorithm at runtime
sorter.sort(new int[]{5, 1, 3});
```

---

## More Error Types

| Error | Meaning | Common Cause |
|-------|---------|--------------|
| `StackOverflowError` | Call stack exceeded limit | Infinite recursion |
| `OutOfMemoryError` | Heap memory exhausted | Huge data, memory leak |
| `ClassCastException` | Invalid type cast | `(Dog) new Cat()` |
| `NumberFormatException` | Invalid number string | `Integer.parseInt("abc")` |
| `ConcurrentModificationException` | List modified while iterating | Remove in for-each loop |
| `UnsupportedOperationException` | Operation not allowed | Modifying `List.of(...)` |

## Immutable Collections (Java 9+)

```java
// These collections cannot be modified after creation
List<String> names = List.of("Alice", "Bob", "Charlie");
Set<Integer> primes = Set.of(2, 3, 5, 7, 11);
Map<String, Integer> scores = Map.of("Alice", 95, "Bob", 87);

// Map.ofEntries for larger maps
Map<String, Integer> bigMap = Map.ofEntries(
    Map.entry("Alice", 95),
    Map.entry("Bob", 87),
    Map.entry("Charlie", 92)
);

// Attempting to modify throws UnsupportedOperationException
// names.add("Dave");  // throws!

// To get a mutable copy:
List<String> mutable = new ArrayList<>(names);
mutable.add("Dave");  // works
```

## Interface Advanced Features

```java
// Static methods in interfaces (Java 8+)
public interface Validator {
    boolean validate(String input);

    static Validator notNull() {
        return input -> input != null;
    }

    static Validator minLength(int min) {
        return input -> input != null && input.length() >= min;
    }

    // Combine validators
    default Validator and(Validator other) {
        return input -> this.validate(input) && other.validate(input);
    }
}

Validator check = Validator.notNull().and(Validator.minLength(3));
check.validate("Hi");     // false (too short)
check.validate("Hello");  // true

// Functional interface (exactly one abstract method — usable as lambda)
@FunctionalInterface
public interface Transformer<T, R> {
    R transform(T input);

    // Can have default and static methods
    default <V> Transformer<T, V> andThen(Transformer<R, V> after) {
        return input -> after.transform(this.transform(input));
    }
}

Transformer<String, Integer> length = String::length;
Transformer<String, String> lengthStr = length.andThen(n -> "Length: " + n);
lengthStr.transform("Hello");  // "Length: 5"
```

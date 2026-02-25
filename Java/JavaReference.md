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

Java has two categories of types: **primitives** (stored directly in memory) and **reference types** (store a reference/address to an object). `String` is a reference type; everything else below is a primitive.

```java
int x = 10;           // Integer (whole numbers), range: -2,147,483,648 to 2,147,483,647
double y = 3.14;      // 64-bit decimal, most common for floating point
float z = 3.14f;      // 32-bit decimal, less precise (needs 'f' suffix)
boolean flag = true;  // Only true or false — no 1/0 like in C
char c = 'A';         // Single character (16-bit Unicode), use single quotes
String s = "Hello";   // Text (reference type, note: capital S), use double quotes
long big = 100000L;   // 64-bit integer for large numbers (needs 'L' suffix)
byte b = 127;         // 8-bit integer, range: -128 to 127
short sh = 30000;     // 16-bit integer, range: -32,768 to 32,767
```

**Key concepts:**
- **Integer division truncates**: `5 / 2 = 2`, not 2.5. Use `5.0 / 2` or `(double) 5 / 2` to get 2.5.
- **Integer overflow wraps silently**: `Integer.MAX_VALUE + 1` wraps to `Integer.MIN_VALUE` — no error!
- **Uninitialized local variables** cause a compile error. Class fields default to `0`, `false`, or `null`.
- **`String` is immutable** — every operation like `s + " world"` creates a new String object.
- **Use `double` over `float`** unless memory is critical — `float` loses precision quickly.

```java
// Integer division gotcha
int a = 5, bv = 2;
System.out.println(a / bv);        // 2 (not 2.5!)
System.out.println((double) a / bv); // 2.5

// Overflow — no error thrown
int max = Integer.MAX_VALUE;  // 2147483647
System.out.println(max + 1);  // -2147483648 (wraps around!)

// Field default values (only for class fields, NOT local variables)
// int -> 0, double -> 0.0, boolean -> false, char -> '\u0000', Object -> null
```

## Input (Scanner)

`Scanner` reads tokens from input. A **token** is a chunk of text separated by whitespace. `nextLine()` reads the whole line including spaces; `next()` / `nextInt()` etc. read one token at a time and **leave the newline character in the buffer**.

```java
import java.util.Scanner;

Scanner sc = new Scanner(System.in);
String text = sc.nextLine();    // Read entire line (including spaces)
String word = sc.next();        // Read one word (stops at whitespace)
int num = sc.nextInt();         // Read integer token
double dec = sc.nextDouble();   // Read decimal token
sc.close();                     // Close when done (releases the resource)
```

**Critical gotcha — mixing `nextInt()` and `nextLine()`:**
```java
// BROKEN — nextLine() reads the leftover newline, not actual input
int age = sc.nextInt();
String name = sc.nextLine();  // Gets "" because '\n' is still in the buffer!

// FIX — consume the leftover newline first
int age = sc.nextInt();
sc.nextLine();                // discard leftover newline
String name = sc.nextLine();  // now reads correctly

// ALTERNATIVE FIX — use nextLine() for everything and parse manually
int age = Integer.parseInt(sc.nextLine());
String name = sc.nextLine();
```

**Checking if input exists:**
```java
while (sc.hasNextInt()) {
    System.out.println(sc.nextInt());
}
// sc.hasNext(), sc.hasNextDouble(), sc.hasNextLine() also exist
```

## Arrays

Arrays are **fixed-size** and **zero-indexed**. Once created, the size cannot change — use `ArrayList` if you need a resizable collection. Arrays are reference types, so assigning one array to another variable doesn't copy the data.

```java
int[] nums = new int[5];              // Create array of size 5, all values default to 0
int[] nums2 = {1, 2, 3, 4, 5};        // Create and initialize with values
nums[0] = 10;                         // Set first element (index 0)
int len = nums.length;                // Get array length (property, not method — no parentheses!)
```

**Default values after `new`:**
- `int[]` → all `0`
- `double[]` → all `0.0`
- `boolean[]` → all `false`
- `String[]` → all `null`

**Common operations:**
```java
import java.util.Arrays;

int[] arr = {5, 2, 8, 1, 9};

Arrays.sort(arr);                     // Sort in place: [1, 2, 5, 8, 9]
Arrays.fill(arr, 0);                  // Fill all with 0: [0, 0, 0, 0, 0]
int[] copy = Arrays.copyOf(arr, 3);   // Copy first 3 elements: [0, 0, 0]
System.out.println(Arrays.toString(arr)); // Print as string: "[0, 0, 0, 0, 0]"
Arrays.equals(arr, copy);             // Compare element-by-element: false

// Arrays are passed by reference — the method can modify the original
void doubleAll(int[] a) {
    for (int i = 0; i < a.length; i++) a[i] *= 2;
}
// After calling doubleAll(arr), arr is modified!

// To copy without sharing: use Arrays.copyOf or clone()
int[] safeCopy = arr.clone();
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
==    // equals (for primitives; use .equals() for objects!)
!=    // not equals
>     // greater than
<     // less than
>=    // greater or equal
<=    // less or equal
&&    // AND (short-circuits — stops if left side is false)
||    // OR  (short-circuits — stops if left side is true)
!     // NOT
```

**Ternary operator** — compact if/else for a single value:
```java
// condition ? valueIfTrue : valueIfFalse
int max = (a > b) ? a : b;
String label = (score >= 60) ? "Pass" : "Fail";
```

**Short-circuit evaluation** — Java stops evaluating as soon as the result is known:
```java
// If s is null, s.length() is never called (avoids NullPointerException)
if (s != null && s.length() > 3) { ... }

// If list is non-empty, second condition only runs when needed
if (list.isEmpty() || list.get(0).equals("start")) { ... }
```

**`==` vs `.equals()` for objects:**
```java
String a = new String("hello");
String b = new String("hello");

a == b          // false — compares memory address (different objects)
a.equals(b)     // true  — compares content

// String literals are pooled — this can be misleading:
String x = "hello";
String y = "hello";
x == y   // true (same pool entry) — but don't rely on this!
```

**switch statement** (use for many discrete values):
```java
switch (day) {
    case "Monday":
    case "Friday":
        System.out.println("Work day");
        break;          // IMPORTANT: without break, falls through to next case!
    case "Saturday":
        System.out.println("Weekend");
        break;
    default:
        System.out.println("Other");
}
```

## Loops

```java
// For loop — use when you know the number of iterations in advance
for (int i = 0; i < 10; i++) {
    // runs 10 times (i goes 0, 1, 2, ... 9)
}

// Counting down
for (int i = 10; i > 0; i--) { }

// Stepping by 2
for (int i = 0; i < 20; i += 2) { }

// For-each loop — cleanest way to iterate, but no index access
for (int num : nums) {
    // iterates through each element — cannot modify the array through 'num'
}

// While loop — use when you don't know how many iterations in advance
while (condition) {
    // runs 0 or more times
}

// Do-while loop — guaranteed to run at least once (rare, useful for input validation)
do {
    // runs at least once, then repeats while condition is true
} while (condition);

break;      // Exit the current loop immediately
continue;   // Skip the rest of this iteration, jump to next one
```

**Modifying a collection while iterating** is a common bug — use an iterator or index loop instead:
```java
// BROKEN — throws ConcurrentModificationException
for (String s : list) {
    if (s.isEmpty()) list.remove(s);  // don't do this!
}

// FIX — use Iterator
Iterator<String> it = list.iterator();
while (it.hasNext()) {
    if (it.next().isEmpty()) it.remove();  // safe
}

// OR use removeIf (Java 8+, cleanest)
list.removeIf(String::isEmpty);
```

**Labeled break/continue** — break out of nested loops:
```java
outer:
for (int i = 0; i < 5; i++) {
    for (int j = 0; j < 5; j++) {
        if (i == 2 && j == 2) break outer;  // exits BOTH loops
        if (j == 3) continue outer;          // skips to next i
    }
}
```

## Methods (Functions)

A method is a reusable block of code. The signature includes the name and parameter types — this is what makes two methods distinct.

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

**Method Overloading** — same name, different parameter types or count. Java picks the right one at compile time:
```java
public static int multiply(int a, int b) { return a * b; }
public static double multiply(double a, double b) { return a * b; }
public static int multiply(int a, int b, int c) { return a * b * c; }

multiply(2, 3);        // calls int version
multiply(2.0, 3.0);    // calls double version
multiply(2, 3, 4);     // calls 3-param version
```

**Pass by value** — Java always passes a copy:
```java
// Primitives: method gets a copy, original is unaffected
void addTen(int n) { n += 10; }
int x = 5;
addTen(x);
System.out.println(x);  // still 5

// Objects: the reference is copied, but both point to the same object
// So you CAN modify the object's contents, but NOT reassign the variable
void addItem(ArrayList<String> list) {
    list.add("new item");  // modifies the actual list — caller sees this
}
void reassign(ArrayList<String> list) {
    list = new ArrayList<>();  // only changes local copy — caller unaffected
}
```

**Returning early** — `return` in a void method exits immediately:
```java
public static void printPositive(int n) {
    if (n <= 0) return;  // early exit
    System.out.println(n);
}
```

## String Methods

**Strings are immutable** — every method returns a NEW string. The original is never modified.

```java
String s = "Hello World";

s.length()                  // Get length: 11
s.charAt(0)                 // Get char at index: 'H'
s.substring(0, 5)           // Get substring (start inclusive, end exclusive): "Hello"
s.substring(6)              // Substring from index to end: "World"
s.toLowerCase()             // New string, all lowercase: "hello world"
s.toUpperCase()             // New string, all uppercase: "HELLO WORLD"
s.trim()                    // Remove leading/trailing whitespace: "Hello World"
s.strip()                   // Like trim() but handles Unicode whitespace (Java 11+)
s.contains("World")         // Check if contains substring: true
s.startsWith("Hello")       // Check prefix: true
s.endsWith("World")         // Check suffix: true
s.equals("Hello")           // Compare content (use this, NEVER ==): false
s.equalsIgnoreCase("hello world") // Compare ignoring case: true
s.split(" ")                // Split into array: ["Hello", "World"]
s.split(",", 3)             // Split into at most 3 parts
s.replace("o", "0")         // Replace all occurrences: "Hell0 W0rld"
s.replaceAll("\\s+", "-")   // Replace with regex: "Hello-World"
s.indexOf("W")              // First index of substring: 6 (-1 if not found)
s.lastIndexOf("l")          // Last index of: 9
s.isEmpty()                 // True if length == 0: ""
s.isBlank()                 // True if empty or only whitespace (Java 11+)
```

**String concatenation with `+`:**
```java
// In a loop, + creates many temporary String objects (slow!)
String result = "";
for (int i = 0; i < 1000; i++) {
    result += i;   // slow — use StringBuilder instead (see that section)
}

// Outside loops, + is fine and readable
String name = "Alice";
String greeting = "Hello, " + name + "!";  // fine
```

**Useful String extras:**
```java
String.valueOf(42)          // Convert anything to String: "42"
String.format("%s is %d", "Alice", 25)  // "Alice is 25"
"  hello  ".strip()         // "hello"
"a,b,c".split(",")          // ["a", "b", "c"]
String.join("-", "a","b","c")  // "a-b-c"

// Convert String <-> char array
char[] chars = s.toCharArray();   // ['H','e','l','l','o',' ','W','o','r','l','d']
String back = new String(chars);  // back to String
```

## Math Operations

All `Math` methods are static — call them directly as `Math.methodName()`. Most return `double`.

```java
Math.abs(-5)            // Absolute value: 5
Math.max(3, 7)          // Maximum: 7
Math.min(3, 7)          // Minimum: 3
Math.pow(2, 3)          // Power: 8.0 (2^3) — always returns double
Math.sqrt(16)           // Square root: 4.0
Math.cbrt(27)           // Cube root: 3.0
Math.round(3.7)         // Round to nearest int: 4  (rounds .5 UP)
Math.floor(3.9)         // Round DOWN to nearest whole: 3.0
Math.ceil(3.1)          // Round UP to nearest whole: 4.0
Math.random()           // Random double in [0.0, 1.0)
(int)(Math.random()*10) // Random int 0-9
Math.log(Math.E)        // Natural log (ln): 1.0
Math.log10(100)         // Base-10 log: 2.0
Math.PI                 // 3.141592653589793
Math.E                  // 2.718281828459045
```

**Random number recipes:**
```java
// Random int between min and max (inclusive)
int min = 5, max = 10;
int rand = (int)(Math.random() * (max - min + 1)) + min;  // 5–10

// Better: use java.util.Random
import java.util.Random;
Random rng = new Random();
int r1 = rng.nextInt(10);      // 0-9
int r2 = rng.nextInt(6) + 1;   // 1-6 (like a die)
double d = rng.nextDouble();   // 0.0 to 1.0
boolean b = rng.nextBoolean(); // true or false

// Java 17+ — cleaner
int r3 = rng.nextInt(1, 7);    // 1-6, bounds inclusive/exclusive like substring
```

**Integer math gotcha:**
```java
Math.pow(2, 10)          // 1024.0 (double, not int!)
(int) Math.pow(2, 10)    // 1024 (cast needed if you want int)
```

## Type Conversion

There are two kinds of casting: **widening** (safe, automatic) and **narrowing** (manual, can lose data).

```java
// String to number — throws NumberFormatException if input is invalid
int i = Integer.parseInt("123");
double d = Double.parseDouble("3.14");
long l = Long.parseLong("9999999999");
boolean b = Boolean.parseBoolean("true");  // case-insensitive: "True", "TRUE" all work

// Number to String
String s1 = String.valueOf(123);        // works for any type
String s2 = Integer.toString(123);      // same result
String s3 = 123 + "";                   // works but style is debated

// Widening — smaller to larger type, AUTOMATIC (no cast needed)
int x = 100;
long xl = x;       // int -> long (automatic)
double xd = x;     // int -> double (automatic)

// Narrowing — larger to smaller, REQUIRES EXPLICIT CAST (may lose data!)
double pi = 3.99;
int truncated = (int) pi;    // 3 — truncates (NOT rounds!) toward zero

long big = 5000000000L;
int narrowed = (int) big;    // data loss — result is unpredictable

// Safe integer parsing (avoid exceptions with a helper)
try {
    int num = Integer.parseInt(userInput);
} catch (NumberFormatException e) {
    System.out.println("Not a valid number!");
}

// Useful number conversions
Integer.toBinaryString(10)   // "1010"
Integer.toHexString(255)     // "ff"
Integer.toOctalString(8)     // "10"
Integer.parseInt("1010", 2)  // Parse binary string: 10
Integer.parseInt("ff", 16)   // Parse hex string: 255
```

## ArrayList (Dynamic Array)

`ArrayList` is a resizable array. It can only hold objects, not primitives — use `Integer`, `Double`, etc. (Java autoboxes automatically). It preserves insertion order and allows duplicates.

```java
import java.util.ArrayList;
import java.util.Collections;

ArrayList<String> list = new ArrayList<>();
list.add("item");               // Add to end
list.add(0, "first");           // Insert at index (shifts others right — O(n))
list.get(0);                    // Get element by index — O(1)
list.set(0, "new");             // Replace element at index
list.remove(0);                 // Remove by index (shifts others — O(n))
list.remove("item");            // Remove first occurrence by value
list.size();                    // Number of elements
list.contains("item");          // Linear search — O(n)
list.indexOf("item");           // First index, or -1 if not found
list.clear();                   // Remove all elements
list.isEmpty();                 // true if size == 0
```

**Sorting and utilities:**
```java
ArrayList<Integer> nums = new ArrayList<>();
nums.add(3); nums.add(1); nums.add(4);

Collections.sort(nums);                   // [1, 3, 4] ascending
Collections.sort(nums, Collections.reverseOrder()); // [4, 3, 1] descending
Collections.reverse(nums);               // reverse order in place
Collections.shuffle(nums);               // randomize order
Collections.min(nums);                   // find minimum
Collections.max(nums);                   // find maximum

// Converting between arrays and ArrayList
String[] arr = {"a", "b", "c"};
ArrayList<String> fromArray = new ArrayList<>(Arrays.asList(arr));  // array -> list
String[] backToArray = list.toArray(new String[0]);                  // list -> array

// Iterating (prefer for-each when you don't need index)
for (String item : list) { System.out.println(item); }
for (int i = 0; i < list.size(); i++) { System.out.println(list.get(i)); }
```

**ArrayList vs Array — when to use which:**
| | Array | ArrayList |
|---|---|---|
| Size | Fixed | Dynamic |
| Primitives | Yes (`int[]`) | No (use `Integer`) |
| Performance | Slightly faster | More flexible |
| Sorting built-in | `Arrays.sort()` | `Collections.sort()` |

## Common Errors & Fixes

| Error | Meaning | Common Cause & Fix |
|-------|---------|---------------------|
| `NullPointerException` | Calling a method or accessing a field on `null` | Check for null before use; use `Optional`; use `Objects.requireNonNull` to find source |
| `ArrayIndexOutOfBoundsException` | Accessing index ≥ array length or < 0 | Use `i < arr.length` in loop; check off-by-one errors |
| `StringIndexOutOfBoundsException` | Same but for String index | Ensure index < s.length() |
| `cannot find symbol` | Variable/method doesn't exist or wrong scope | Typo? Wrong class? Forgot import? Not declared in this scope? |
| `incompatible types` | Assigning wrong type | Add cast `(int) x` for narrowing; use correct type |
| `missing return statement` | Non-void method doesn't always return | Ensure every code path returns a value (even inside if/else) |
| `unreachable statement` | Code after `return` / `break` that can never run | Remove dead code |
| `variable might not have been initialized` | Local variable used before assignment | Assign a default value when declaring |
| `non-static method cannot be referenced from a static context` | Calling instance method from `main` or static method | Create an object first, or make the method static |
| `reached end of file while parsing` | Missing closing `}` | Count braces; use IDE auto-format |

## Quick Tips

**Naming conventions:**
- Classes & Interfaces: `PascalCase` → `MyClass`, `Runnable`
- Variables & Methods: `camelCase` → `myVariable`, `getCount()`
- Constants (`static final`): `ALL_CAPS` → `MAX_SIZE`, `PI`
- Packages: `all.lowercase` → `com.example.app`

**Common gotchas:**
- Use `equals()` to compare Strings, not `==` (which compares references)
- Arrays start at index **0** — last element is `arr[arr.length - 1]`
- `length` for arrays (property), `length()` for Strings (method), `size()` for ArrayList (method)
- `int / int` = integer division — use `(double)` cast or `1.0 *` to get decimal result
- Scanner's `nextInt()` leaves a newline in the buffer — call `nextLine()` after to consume it
- `for (x : list)` loop — don't call `list.remove()` inside, use `removeIf()` or an Iterator
- `ArrayList<int>` doesn't work — use `ArrayList<Integer>` (primitives need wrapper types)
- `Math.random()` returns `[0.0, 1.0)` — multiply and cast for a range: `(int)(Math.random() * 6) + 1`
- `switch` without `break` falls through to the next case — modern arrow syntax avoids this

---

# Advanced Java Concepts

## Object-Oriented Programming (OOP)

### Classes & Objects

A **class** is a blueprint; an **object** is an instance of that blueprint. Each object has its own copy of instance variables (fields). `this` refers to the current object.

```java
public class Dog {
    // Instance variables (fields) — each Dog object has its own copy
    private String name;
    private int age;

    // No-arg constructor (if you define any constructor, Java no longer auto-provides this)
    public Dog() {
        this.name = "Unknown";
        this.age = 0;
    }

    // Parameterized constructor
    public Dog(String name, int age) {
        this.name = name;   // 'this.name' = field, 'name' = parameter
        this.age = age;
    }

    // Constructor chaining — one constructor calls another with this()
    public Dog(String name) {
        this(name, 0);      // calls the 2-param constructor above
    }

    // Getter (accessor) — allows read access to private field
    public String getName() { return name; }
    public int getAge() { return age; }

    // Setter (mutator) — allows controlled write access
    public void setName(String name) { this.name = name; }

    // Method
    public void bark() {
        System.out.println(name + " says woof!");
    }

    // Override toString for readable output
    @Override
    public String toString() {
        return "Dog{name='" + name + "', age=" + age + "}";
    }
}

// Using the class
Dog myDog = new Dog("Buddy", 3);
myDog.bark();
System.out.println(myDog);   // calls toString(): Dog{name='Buddy', age=3}

// Objects are reference types — two variables can point to the same object
Dog a = new Dog("Rex", 5);
Dog b = a;              // b points to SAME object as a
b.setName("Max");
System.out.println(a.getName()); // "Max" — a was affected!
```

### Inheritance

A subclass **inherits** all non-private fields and methods from its parent. Use `super` to call the parent's constructor or methods. Java only supports **single inheritance** (one parent class), but a class can implement multiple interfaces.

```java
// Parent class (superclass)
public class Animal {
    protected String name;   // protected = accessible in subclasses

    public Animal(String name) {
        this.name = name;
    }

    public void eat() {
        System.out.println(name + " is eating");
    }
}

// Child class (subclass) — inherits Animal's fields and methods
public class Cat extends Animal {
    private String color;

    public Cat(String name, String color) {
        super(name);           // MUST call parent constructor first if parent has no no-arg constructor
        this.color = color;
    }

    public void meow() {
        System.out.println(name + " says meow!");  // 'name' inherited from Animal
    }

    // Calling parent method from child
    public void describe() {
        super.eat();           // calls Animal.eat()
        System.out.println("And I'm " + color);
    }
}

// Polymorphism — parent type can hold child objects
Animal a = new Cat("Whiskers", "orange");  // Animal reference, Cat object
a.eat();    // works — eat() is from Animal
// a.meow() — compile error! Animal reference doesn't know about meow()
```

### Method Overriding

Overriding replaces a parent method's behavior in the subclass. **Polymorphism** means the actual object type determines which method runs at runtime — even through a parent-type reference.

```java
public class Animal {
    public void makeSound() {
        System.out.println("Some sound");
    }
}

public class Dog extends Animal {
    @Override               // tells compiler to verify this actually overrides something
    public void makeSound() {
        System.out.println("Woof!");
    }
}

public class Cat extends Animal {
    @Override
    public void makeSound() {
        System.out.println("Meow!");
    }
}

// Polymorphism in action — runtime type determines which method runs
Animal[] animals = { new Dog(), new Cat(), new Dog() };
for (Animal a : animals) {
    a.makeSound();  // prints Woof!, Meow!, Woof! — Java picks the right version
}

// Rules for overriding:
// - Same method name and parameters
// - Return type must be same or a subtype (covariant return)
// - Cannot reduce visibility (e.g., public -> private is illegal)
// - Cannot override final or static methods
```

### Abstract Classes

An **abstract class** cannot be instantiated directly — it exists to be extended. Use it when subclasses share common behavior but each must implement certain specific methods. It can have both abstract and concrete methods, as well as fields and constructors.

```java
public abstract class Shape {
    protected String color;   // shared field

    public Shape(String color) {  // constructor — called by subclasses via super()
        this.color = color;
    }

    // Abstract method — NO body, subclass MUST implement or be abstract itself
    public abstract double getArea();
    public abstract double getPerimeter();

    // Concrete method — shared by all subclasses, not overridden
    public void printInfo() {
        System.out.printf("%s area=%.2f%n", color, getArea());
    }
}

public class Circle extends Shape {
    private double radius;

    public Circle(double radius, String color) {
        super(color);         // call Shape's constructor
        this.radius = radius;
    }

    @Override
    public double getArea() { return Math.PI * radius * radius; }

    @Override
    public double getPerimeter() { return 2 * Math.PI * radius; }
}

// Cannot instantiate: Shape s = new Shape();  // compile error!
Shape s = new Circle(5, "red");  // OK — using parent type
s.printInfo();                   // calls Circle.getArea() via polymorphism

// Abstract vs Interface:
// - Abstract class: use when subclasses share STATE (fields) or common code
// - Interface: use when you want to define a contract multiple unrelated classes can fulfill
```

### Interfaces

An **interface** is a pure contract — it defines what a class must do, not how. A class can implement multiple interfaces, enabling a form of multiple inheritance in Java. All methods are implicitly `public abstract` unless marked `default` or `static`.

```java
public interface Drawable {
    void draw();  // implicitly public abstract — every implementor must define this

    // Default method (Java 8+) — provides a default implementation
    // Implementing classes inherit this but can override it
    default void print() {
        System.out.println("Printing...");
    }

    // Static method (Java 8+) — called on the interface itself, not instances
    static Drawable noop() {
        return () -> {};  // lambda returning an empty implementation
    }
}

public interface Resizable {
    void resize(double factor);
}

// A class can implement MULTIPLE interfaces (unlike extends — only one class)
public class Rectangle implements Drawable, Resizable {
    private double width, height;

    public Rectangle(double w, double h) { this.width = w; this.height = h; }

    @Override
    public void draw() { System.out.println("Drawing rectangle"); }

    @Override
    public void resize(double factor) { width *= factor; height *= factor; }
}

// Interface as a type — powerful for polymorphism
Drawable d = new Rectangle(3, 4);
d.draw();
d.print();  // uses default implementation

// Interface variables are implicitly public static final (constants)
public interface Config {
    int MAX_RETRIES = 3;       // same as: public static final int MAX_RETRIES = 3;
}
```

## Access Modifiers

Access modifiers control **visibility** — who can see and use a field, method, or class.

```java
public      // Accessible from anywhere
private     // Accessible only within the same class
protected   // Accessible within same package AND subclasses (even different package)
(default)   // No keyword — accessible only within the same package
```

| Modifier | Same Class | Same Package | Subclass | Everywhere |
|----------|-----------|--------------|----------|------------|
| `private` | ✓ | | | |
| (default) | ✓ | ✓ | | |
| `protected` | ✓ | ✓ | ✓ | |
| `public` | ✓ | ✓ | ✓ | ✓ |

**Best practices:**
- Make fields `private` by default — expose them through getters/setters if needed
- Make methods `public` only if they're part of the class's intended interface
- Use `protected` for methods meant to be used or overridden by subclasses
- Prefer the most restrictive modifier that works — it keeps code flexible to change

## Static Keyword

`static` means "belongs to the class, not to any instance." There's one copy of a static field regardless of how many objects you create. Static methods can't use `this` or access instance fields directly.

```java
public class Counter {
    private static int count = 0;   // ONE shared copy across all Counter objects
    private int id;                 // each instance has its own 'id'

    public Counter() {
        count++;
        this.id = count;
    }

    // Static method — call via ClassName.method(), not instance.method()
    public static int getCount() {
        return count;          // OK — accessing static field
        // return id;          // ERROR — can't access instance field from static method
    }

    // Static constant — convention is ALL_CAPS
    public static final double PI = 3.14159;

    // Static block — runs ONCE when the class is first loaded by the JVM
    static {
        System.out.println("Counter class loaded");
        // useful for complex static initialization
    }

    // Static nested class (see Nested Classes section)
    public static class Helper { }
}

// Usage — no object needed
Counter.getCount();
System.out.println(Counter.PI);

// When to use static:
// - Utility/helper methods that don't need object state (Math.abs, Arrays.sort)
// - Constants shared across all instances (MAX_SIZE, VERSION)
// - Factory methods (Integer.valueOf, List.of)
// Avoid: making everything static just to avoid passing objects around
```

## Final Keyword

`final` means "cannot be changed after initial assignment." It applies to variables, methods, and classes, each with different effects.

```java
// final variable — must be assigned exactly once, never changed
final int MAX = 100;           // compile-time constant
final List<String> list = new ArrayList<>();
list.add("item");              // OK — modifying the list is fine
// list = new ArrayList<>();   // ERROR — can't reassign the reference

// final field — must be set in constructor, never changed after
public class Circle {
    private final double radius;    // set once, then immutable
    public Circle(double radius) { this.radius = radius; }
}

// final parameter — cannot be reassigned inside the method
public void process(final String input) {
    // input = "other";  // ERROR
}

// final method — subclasses cannot override it
public class Base {
    public final void template() { /* fixed behavior */ }
}

// final class — cannot be extended at all
public final class String { }   // that's why you can't extend String!
public final class Integer { }

// When to use final:
// - Constants: public static final int MAX = 100;
// - Immutable fields that shouldn't change after construction
// - Methods that are security-critical and shouldn't be overridden
```

## Exception Handling

Exceptions are objects that represent errors. Java has two types:
- **Checked exceptions** — must be declared with `throws` or caught (e.g., `IOException`, `SQLException`)
- **Unchecked exceptions** — extend `RuntimeException`, no need to declare (e.g., `NullPointerException`, `ArrayIndexOutOfBoundsException`)

```java
try {
    int result = 10 / 0;  // throws ArithmeticException
} catch (ArithmeticException e) {
    System.out.println("Cannot divide by zero!");
    System.out.println(e.getMessage());    // "/ by zero"
    e.printStackTrace();                   // full stack trace to stderr
} catch (Exception e) {
    // Catches any exception — put more specific catches BEFORE this
    System.out.println("Something went wrong: " + e.getMessage());
} finally {
    // ALWAYS runs, even if exception thrown or return executed — use for cleanup
    System.out.println("Done");
}
```

**Exception hierarchy** (simplified):
```
Throwable
├── Error         (don't catch — JVM problems like OutOfMemoryError)
└── Exception
    ├── IOException         (checked)
    ├── SQLException        (checked)
    └── RuntimeException    (unchecked)
        ├── NullPointerException
        ├── ArrayIndexOutOfBoundsException
        ├── ClassCastException
        └── IllegalArgumentException
```

**Throwing exceptions:**
```java
// Declaring a checked exception — callers must handle or declare it too
public void readFile(String path) throws IOException {
    // ...
}

// Throwing — stops the method and unwinds the call stack
public void checkAge(int age) {
    if (age < 0) {
        throw new IllegalArgumentException("Age cannot be negative: " + age);
    }
}

// Re-throwing — catch, do something, then throw again
try {
    readFile("data.txt");
} catch (IOException e) {
    System.out.println("Logging: " + e.getMessage());
    throw e;   // re-throw the same exception
}
```

## HashMap (Key-Value Pairs)

A `HashMap` maps keys to values. Keys must be unique — putting a value for an existing key **overwrites** the old value. `HashMap` does NOT guarantee any order. Keys are found using `hashCode()` and `equals()`, so those must be correctly implemented for custom key types.

```java
import java.util.HashMap;
import java.util.Map;

HashMap<String, Integer> scores = new HashMap<>();
scores.put("Alice", 95);            // Add or overwrite entry
scores.put("Bob", 87);
scores.put("Alice", 100);           // Overwrites Alice's previous value!

scores.get("Alice");                // Get value: 100 (null if key missing)
scores.getOrDefault("Eve", 0);      // Get or default if missing: 0
scores.containsKey("Bob");          // Check key exists: true
scores.containsValue(87);           // Check value exists: true (slower — O(n))
scores.remove("Bob");               // Remove entry, returns old value
scores.size();                      // Number of entries: 1 (only Alice left)
scores.keySet();                    // Set<String> of all keys
scores.values();                    // Collection<Integer> of all values
scores.isEmpty();                   // true if no entries
```

**Iterating — prefer `entrySet` for efficiency:**
```java
// entrySet — most efficient, gives key and value together
for (Map.Entry<String, Integer> entry : scores.entrySet()) {
    System.out.println(entry.getKey() + ": " + entry.getValue());
}

// keySet — simpler but calls get() for each key (slightly slower)
for (String key : scores.keySet()) {
    System.out.println(key + ": " + scores.get(key));
}

// forEach with lambda (Java 8+)
scores.forEach((key, val) -> System.out.println(key + "=" + val));
```

**Useful operations:**
```java
// putIfAbsent — only adds if key not already present
scores.putIfAbsent("Charlie", 70);

// computeIfAbsent — add and compute value if missing (great for counting)
HashMap<String, Integer> wordCount = new HashMap<>();
String[] words = {"apple", "banana", "apple"};
for (String w : words) {
    wordCount.put(w, wordCount.getOrDefault(w, 0) + 1);
}
// wordCount = {apple=2, banana=1}

// merge — combine value if key exists
wordCount.merge("apple", 1, Integer::sum);  // adds 1 to apple's count
```

## HashSet (Unique Values)

`HashSet` stores unique elements with no guaranteed order. Internally it's a `HashMap` where the element is the key. It uses `hashCode()` and `equals()` to determine uniqueness — for custom objects, override both.

```java
import java.util.HashSet;

HashSet<String> names = new HashSet<>();
names.add("Alice");         // returns true (added)
names.add("Bob");
names.add("Alice");         // returns false (duplicate — ignored)
names.size();               // 2
names.contains("Bob");      // O(1) average — very fast!
names.remove("Bob");        // returns true if removed
names.isEmpty();            // false

// Iterating (order is not guaranteed!)
for (String name : names) {
    System.out.println(name);
}
```

**Set operations (useful for math-style set logic):**
```java
HashSet<Integer> setA = new HashSet<>(Arrays.asList(1, 2, 3, 4));
HashSet<Integer> setB = new HashSet<>(Arrays.asList(3, 4, 5, 6));

// Union — all elements from both
HashSet<Integer> union = new HashSet<>(setA);
union.addAll(setB);           // [1, 2, 3, 4, 5, 6]

// Intersection — only elements in both
HashSet<Integer> intersection = new HashSet<>(setA);
intersection.retainAll(setB); // [3, 4]

// Difference — in setA but not setB
HashSet<Integer> difference = new HashSet<>(setA);
difference.removeAll(setB);   // [1, 2]

// Common use case — removing duplicates from a list
List<Integer> withDupes = Arrays.asList(1, 2, 2, 3, 3, 3);
Set<Integer> unique = new HashSet<>(withDupes);  // {1, 2, 3}
```

## Generics

Generics let you write type-safe code that works with any type, without casting. The type parameter (`<T>`) is a placeholder replaced at compile time with a real type. This eliminates `ClassCastException` and removes the need for ugly casts.

```java
// Generic class — T is replaced by a real type when you use the class
public class Box<T> {
    private T content;

    public void set(T content) { this.content = content; }
    public T get() { return content; }
}

Box<String> stringBox = new Box<>();
stringBox.set("Hello");
String s = stringBox.get();  // no cast needed!

Box<Integer> intBox = new Box<>();
intBox.set(123);

// Generic method — type is inferred from the argument
public static <T> void printArray(T[] array) {
    for (T element : array) {
        System.out.println(element);
    }
}
printArray(new String[]{"a", "b"});   // T inferred as String
printArray(new Integer[]{1, 2, 3});   // T inferred as Integer
```

**Bounded type parameters — restrict what types are allowed:**
```java
// T must be a Number or subclass (Integer, Double, Long, etc.)
public static <T extends Number> double sum(T[] arr) {
    double total = 0;
    for (T t : arr) total += t.doubleValue();
    return total;
}

// Multiple bounds
public static <T extends Comparable<T> & Cloneable> T findMax(T[] arr) {
    T max = arr[0];
    for (T t : arr) if (t.compareTo(max) > 0) max = t;
    return max;
}
```

**Wildcards — for flexible method parameters:**
```java
// ? extends T — read-only (upper bound) — "some subtype of Number"
public static double total(List<? extends Number> list) {
    double sum = 0;
    for (Number n : list) sum += n.doubleValue();
    return sum;
}
total(List.of(1, 2, 3));       // works with List<Integer>
total(List.of(1.1, 2.2));      // works with List<Double>

// ? super T — write-only (lower bound) — "some supertype of Integer"
public static void addNumbers(List<? super Integer> list) {
    list.add(1);
    list.add(2);
}
```

## Lambda Expressions (Java 8+)

A lambda is a concise way to write a **functional interface** implementation — an interface with exactly one abstract method. The lambda body IS that method's implementation. Lambdas make code shorter and more readable, especially when working with streams, sorting, and event handling.

```java
// Old way — anonymous class (verbose)
Runnable r1 = new Runnable() {
    @Override
    public void run() { System.out.println("Running"); }
};

// Lambda — concise equivalent
Runnable r2 = () -> System.out.println("Running");
// ()  = parameters (none here)
// ->  = "arrow" separating params from body
// ... = body (expression or {} block)

// Multi-line lambda body
Runnable r3 = () -> {
    System.out.println("Step 1");
    System.out.println("Step 2");
};

// Lambda with parameters
Comparator<String> byLength = (a, b) -> a.length() - b.length();
List<String> names = Arrays.asList("Charlie", "Alice", "Bob");
names.sort(byLength);  // [Bob, Alice, Charlie]
```

**Built-in functional interfaces** (`java.util.function`):
```java
// Consumer<T>     — takes T, returns nothing
Consumer<String> printer = s -> System.out.println(s);
printer.accept("Hello");

// Predicate<T>    — takes T, returns boolean (used in filter)
Predicate<Integer> isEven = n -> n % 2 == 0;
isEven.test(4);    // true
isEven.test(3);    // false

// Combining predicates
Predicate<Integer> isPositive = n -> n > 0;
Predicate<Integer> isEvenAndPositive = isEven.and(isPositive);
Predicate<Integer> isEvenOrNegative = isEven.or(isPositive.negate());

// Function<T, R>  — takes T, returns R (used in map)
Function<String, Integer> length = s -> s.length();
length.apply("Hello");  // 5

// Chaining functions
Function<Integer, Integer> doubleIt = x -> x * 2;
Function<Integer, String> toStr = x -> "Value: " + x;
Function<Integer, String> combined = doubleIt.andThen(toStr);
combined.apply(5);  // "Value: 10"

// Supplier<T>     — takes nothing, returns T
Supplier<Double> random = () -> Math.random();
random.get();

// BiFunction<T, U, R> — takes two params, returns R
BiFunction<String, Integer, String> repeat = (s, n) -> s.repeat(n);
repeat.apply("ha", 3);  // "hahaha"
```

## Stream API (Java 8+)

A `Stream` is a pipeline of operations applied to a sequence of elements. Streams are **lazy** — intermediate operations (filter, map, sorted) don't run until a **terminal operation** (collect, forEach, reduce) is called. Streams do NOT modify the original collection.

Three phases: **source → intermediate operations → terminal operation**

```java
import java.util.stream.*;
import java.util.Arrays;
import java.util.List;

List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);

// filter — keep elements that match the predicate (intermediate)
List<Integer> evens = numbers.stream()
    .filter(n -> n % 2 == 0)
    .collect(Collectors.toList());  // [2, 4, 6, 8, 10]

// map — transform each element to something else (intermediate)
List<Integer> doubled = numbers.stream()
    .map(n -> n * 2)
    .collect(Collectors.toList());  // [2, 4, 6, 8, ...]

// map to a different type
List<String> strs = numbers.stream()
    .map(n -> "num" + n)
    .collect(Collectors.toList());  // ["num1", "num2", ...]

// reduce — combine all elements into a single value (terminal)
int sum = numbers.stream()
    .reduce(0, (a, b) -> a + b);    // 55  (0 is the identity/starting value)

// Chaining operations — the power of streams
int result = numbers.stream()
    .filter(n -> n > 5)             // [6, 7, 8, 9, 10]
    .map(n -> n * 2)                // [12, 14, 16, 18, 20]
    .reduce(0, Integer::sum);       // 80

// Terminal operations
numbers.stream().count();                      // 10
numbers.stream().min(Integer::compare);        // Optional[1]
numbers.stream().max(Integer::compare);        // Optional[10]
numbers.stream().sum();                        // only for IntStream/LongStream/DoubleStream
numbers.stream().findFirst();                  // Optional[1]
numbers.stream().anyMatch(n -> n > 5);         // true (stops at first match)
numbers.stream().allMatch(n -> n > 0);         // true (must check all)
numbers.stream().noneMatch(n -> n > 100);      // true
numbers.stream().forEach(System.out::println); // print each (no return value)

// Intermediate operations
numbers.stream().sorted();                     // natural order (new sorted stream)
numbers.stream().sorted(Comparator.reverseOrder()); // reverse order
numbers.stream().distinct();                   // remove duplicates
numbers.stream().limit(5);                     // take first 5: [1,2,3,4,5]
numbers.stream().skip(3);                      // skip first 3: [4,5,...,10]
numbers.stream().peek(n -> System.out.println("Processing: " + n)); // debug without consuming

// Primitive streams — avoid autoboxing overhead
int sumDirect = numbers.stream()
    .mapToInt(Integer::intValue)   // IntStream
    .sum();                         // built-in sum, no reduce needed

IntStream.range(0, 5)              // 0, 1, 2, 3, 4 (exclusive end)
IntStream.rangeClosed(1, 5)        // 1, 2, 3, 4, 5 (inclusive end)
```

## File I/O

Java's `java.nio.file` package (NIO.2, Java 7+) is the modern API. Prefer it over the older `java.io` classes. **Always use try-with-resources** when working with streams and readers to guarantee files are closed.

```java
import java.io.*;
import java.nio.file.*;
import java.util.List;

Path path = Path.of("file.txt");   // Represents a file path (doesn't need to exist yet)

// Reading — modern NIO.2 (best for small/medium files)
String content = Files.readString(path);               // Entire file as one String (Java 11+)
List<String> lines = Files.readAllLines(path);         // One String per line
byte[] bytes = Files.readAllBytes(path);               // Raw bytes

// Writing — modern NIO.2
Files.writeString(path, "Hello World");                // Write String (overwrites)
Files.writeString(path, "More", StandardOpenOption.APPEND); // Append instead
Files.write(path, lines);                              // Write list of lines

// Checking and managing files/directories
Files.exists(path);              // true if file exists
Files.isDirectory(path);         // true if it's a directory
Files.size(path);                // file size in bytes
Files.delete(path);              // delete (throws if not found)
Files.deleteIfExists(path);      // delete if exists (no exception if missing)
Files.copy(path, Path.of("copy.txt"));   // copy file
Files.move(path, Path.of("new.txt"));    // move/rename file
Files.createDirectory(Path.of("myDir")); // create a directory
Files.createDirectories(Path.of("a/b/c")); // create nested dirs

// Listing files in a directory
Files.list(Path.of("."))                          // Stream<Path> of directory contents
    .filter(p -> p.toString().endsWith(".java"))
    .forEach(System.out::println);

// Streaming large files line by line (efficient — doesn't load everything at once)
try (var stream = Files.lines(path)) {
    stream.filter(line -> !line.isBlank())
          .forEach(System.out::println);
}

// Traditional BufferedReader (still useful, slightly faster for large files)
try (BufferedReader reader = new BufferedReader(new FileReader("file.txt"))) {
    String line;
    while ((line = reader.readLine()) != null) {
        System.out.println(line);
    }
}  // reader closed automatically

// Traditional PrintWriter (fine for writing)
try (PrintWriter writer = new PrintWriter(new FileWriter("file.txt", true))) {
    // true = append mode
    writer.println("Hello World");
    writer.printf("Value: %d%n", 42);
}
```

## Multithreading Basics

A **thread** is an independent path of execution. The JVM runs multiple threads concurrently. The `main` method itself runs on the main thread. Use threads to do work in parallel (e.g., background tasks while the UI stays responsive).

```java
// Method 1: Extend Thread (less flexible — can't extend anything else)
class MyThread extends Thread {
    @Override
    public void run() {
        System.out.println("Thread running on: " + Thread.currentThread().getName());
    }
}
MyThread t = new MyThread();
t.start();   // starts a new thread — do NOT call run() directly (that runs on current thread)

// Method 2: Implement Runnable (preferred — separates task from threading)
class MyRunnable implements Runnable {
    @Override
    public void run() { System.out.println("Runnable running"); }
}
Thread t2 = new Thread(new MyRunnable());
t2.start();

// Method 3: Lambda (cleanest for simple tasks)
Thread t3 = new Thread(() -> System.out.println("Lambda thread running"));
t3.start();

// Useful thread methods
Thread.sleep(1000);         // Pause current thread for 1000ms (throws InterruptedException)
t.join();                   // Current thread waits until t finishes
t.join(500);                // Wait at most 500ms
t.isAlive();                // true if thread hasn't finished
Thread.currentThread();     // Reference to the currently running thread
t.setName("worker-1");      // Give the thread a readable name (helpful for debugging)
```

**The race condition problem:**
```java
// UNSAFE — two threads modifying same variable simultaneously
class Counter {
    int count = 0;
    void increment() { count++; }  // NOT atomic! (read, add, write = 3 steps)
}

// FIX 1: synchronized — only one thread can enter at a time
class SafeCounter {
    private int count = 0;
    public synchronized void increment() { count++; }
    public synchronized int getCount() { return count; }
}

// FIX 2: AtomicInteger — lock-free, fast
import java.util.concurrent.atomic.AtomicInteger;
AtomicInteger atomicCount = new AtomicInteger(0);
atomicCount.incrementAndGet();  // thread-safe increment
atomicCount.get();              // read current value
```

## Enum Types

An `enum` defines a fixed set of named constants. Enums are full classes in Java — they can have fields, constructors, and methods. They're type-safe (unlike using plain `int` or `String` constants) and work great with `switch`.

```java
public enum Day {
    MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY
}

Day today = Day.MONDAY;
System.out.println(today);           // "MONDAY"
System.out.println(today.name());    // "MONDAY" (same as toString)
System.out.println(today.ordinal()); // 0 (index in declaration order)

// Enum built-in methods
Day[] days = Day.values();           // All values as array
Day d = Day.valueOf("FRIDAY");       // Parse string to enum (throws if invalid)

// Enum with fields and methods
public enum Planet {
    MERCURY(3.303e+23, 2.4397e6),
    VENUS(4.869e+24, 6.0518e6),
    EARTH(5.976e+24, 6.37814e6);

    private final double mass;    // kg
    private final double radius;  // meters

    Planet(double mass, double radius) {
        this.mass = mass;
        this.radius = radius;
    }

    double surfaceGravity() {
        final double G = 6.67300E-11;
        return G * mass / (radius * radius);
    }
}

Planet.EARTH.surfaceGravity();  // 9.80...

// Enum in switch (best use case for enums)
switch (today) {
    case MONDAY -> System.out.println("Start of week");
    case FRIDAY -> System.out.println("Almost weekend!");
    case SATURDAY, SUNDAY -> System.out.println("Weekend!");
    default -> System.out.println("Midweek");
}

// EnumSet and EnumMap — efficient collections for enums
import java.util.*;
EnumSet<Day> weekend = EnumSet.of(Day.SATURDAY, Day.SUNDAY);
EnumSet<Day> weekdays = EnumSet.complementOf(weekend);
EnumMap<Day, String> schedule = new EnumMap<>(Day.class);
schedule.put(Day.MONDAY, "Meeting");
```

## Optional (Java 8+)

`Optional<T>` is a container that either holds a value or is empty. It forces you to explicitly handle the "no value" case instead of silently returning `null` and risking `NullPointerException`. Use `Optional` as a **return type** when a method might not find a result — don't use it for fields or parameters.

```java
import java.util.Optional;

// Creating Optional values
Optional<String> name = Optional.of("Alice");         // must be non-null (throws if null)
Optional<String> empty = Optional.empty();            // explicitly empty
Optional<String> nullable = Optional.ofNullable(possiblyNull);  // null -> empty

// Checking and getting the value
name.isPresent();                      // true (value exists)
name.isEmpty();                        // false (Java 11+)
name.get();                            // "Alice" — throws NoSuchElementException if empty!

// Safe alternatives to get() — prefer these:
name.orElse("Default");                // return value or a default
name.orElseGet(() -> computeDefault()); // return value or lazily compute a default
name.orElseThrow(() -> new RuntimeException("No name!")); // throw custom exception if empty

// Performing actions
name.ifPresent(n -> System.out.println(n));           // only runs if present
name.ifPresentOrElse(                                  // Java 9+
    n -> System.out.println("Found: " + n),
    () -> System.out.println("Not found")
);

// Transforming — Optional chains work like streams
Optional<Integer> nameLength = name
    .filter(n -> n.length() > 3)        // empty if name too short
    .map(String::length);               // transform to length

nameLength.orElse(0);   // 5

// Real-world example — searching a list
Optional<String> found = names.stream()
    .filter(n -> n.startsWith("A"))
    .findFirst();

found.ifPresent(System.out::println);
String result = found.orElse("None found");
```

## Records (Java 16+)

A `record` is a compact, immutable data class. Java auto-generates the constructor, getters (named after the fields), `equals()`, `hashCode()`, and `toString()`. Records are **immutable** — fields are `final` and there are no setters.

```java
// Compact way to create immutable data classes
public record Person(String name, int age) { }

// Equivalent to a class with:
// - private final String name; private final int age;
// - public Person(String name, int age) { this.name = name; this.age = age; }
// - public String name() { return name; }   // NOTE: no "get" prefix!
// - public int age() { return age; }
// - equals(), hashCode(), toString() all auto-generated

Person p = new Person("Alice", 25);
p.name();    // "Alice"
p.age();     // 25
System.out.println(p);  // Person[name=Alice, age=25]

// Records can have custom methods
public record Point(double x, double y) {
    // Compact canonical constructor — for validation
    public Point {
        if (x < 0 || y < 0) throw new IllegalArgumentException("Negative coordinates");
    }

    // Custom method
    public double distanceTo(Point other) {
        return Math.sqrt(Math.pow(x - other.x, 2) + Math.pow(y - other.y, 2));
    }

    // Static factory method
    public static Point origin() { return new Point(0, 0); }
}

// Records are great for:
// - DTOs (Data Transfer Objects)
// - Returning multiple values from a method
// - Map keys (equals/hashCode are value-based)
// - Pattern matching targets with sealed interfaces

// Records implement equals by value (not reference)
Person a = new Person("Alice", 25);
Person b = new Person("Alice", 25);
a.equals(b);  // true (compares field values)
a == b;       // false (different objects)
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

Annotations are metadata attached to code elements (classes, methods, fields). They don't change behavior by themselves — but tools, frameworks, and the compiler can read and act on them.

```java
// Built-in Java annotations
@Override                         // Tells compiler: verify this actually overrides a parent method
@Deprecated                       // Marks as outdated — callers get a warning
@SuppressWarnings("unchecked")    // Suppress specific compiler warnings
@SuppressWarnings({"unchecked", "rawtypes"})  // Multiple warnings
@FunctionalInterface              // Verifies interface has exactly one abstract method

// Where to use @Override: always use it when overriding — catches typos at compile time
public class Dog extends Animal {
    @Override
    public void makeSound() { }   // compiler confirms Animal has makeSound()
}

// @Deprecated — also add Javadoc explaining what to use instead
/**
 * @deprecated Use {@link #newMethod()} instead
 */
@Deprecated(since = "2.0", forRemoval = true)
public void oldMethod() { }

// Custom annotation — rarely needed but useful in frameworks
@interface Validate {
    int min() default 0;
    int max() default Integer.MAX_VALUE;
    String message() default "Invalid value";
}

// Using custom annotation
public class User {
    @Validate(min = 0, max = 150, message = "Age out of range")
    private int age;
}

// Common framework annotations you'll encounter:
// Spring:  @Component, @Service, @Autowired, @RequestMapping
// JUnit:   @Test, @BeforeEach, @AfterEach
// Jackson: @JsonProperty, @JsonIgnore
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

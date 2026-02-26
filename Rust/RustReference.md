# Rust Quick Reference Guide

A practical, code-focused reference for Rust — from basics to advanced concepts.

---

## Table of Contents

- [Getting Started](#getting-started)
- [Variables & Constants](#variables--constants)
- [Data Types](#data-types)
- [Operators](#operators)
- [Control Flow](#control-flow)
- [Functions](#functions)
- [Ownership & Borrowing](#ownership--borrowing)
- [Strings](#strings)
- [Collections](#collections)
- [Structs](#structs)
- [Enums](#enums)
- [Pattern Matching](#pattern-matching)
- [Traits & Generics](#traits--generics)
- [Error Handling](#error-handling)
- [Closures](#closures)
- [Iterators](#iterators)
- [Lifetimes](#lifetimes)
- [Concurrency](#concurrency)
- [File I/O](#file-io)
- [Modules & Crates](#modules--crates)
- [Smart Pointers](#smart-pointers)
- [Macros](#macros)
- [Testing](#testing)
- [Common Errors & Tips](#common-errors--tips)
- [Useful Crates](#useful-crates)

---

<!-- TIER 1 — GETTING STARTED -->

## Getting Started

### Installation

Rust is installed via **rustup**, which manages the Rust toolchain.

```bash
# Install rustup (macOS/Linux)
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

# Check version
rustc --version
cargo --version

# Update Rust
rustup update
```

### Creating a Project

Rust projects are managed with **Cargo**, Rust's build system and package manager.

```bash
# Create a new project (binary)
cargo new my_project

# Create a library project
cargo new my_library --lib

# Project structure:
# my_project/
# ├── Cargo.toml      # Project config & dependencies
# └── src/
#     └── main.rs      # Entry point (binary) or lib.rs (library)
```

### Compiling & Running

```bash
cargo build           # Compile (debug mode)
cargo build --release # Compile (optimized release mode)
cargo run             # Compile and run
cargo check           # Check for errors without building (fastest)
```

### Hello, World!

```rust
fn main() {
    println!("Hello, world!");
}
```

### Comments

```rust
// Single-line comment

/*
   Multi-line
   comment
*/

/// Doc comment (generates documentation for the item below)
/// Supports **Markdown** formatting
fn documented_function() {}

//! Inner doc comment (documents the enclosing item, e.g. a module or crate)
```

### Printing

```rust
fn main() {
    println!("Hello!");             // Print with newline
    print!("No newline ");          // Print without newline
    eprintln!("Error message");     // Print to stderr

    let name = "Rust";
    let version = 2021;
    println!("Language: {}", name);              // Positional placeholder
    println!("Edition: {version}");              // Inline variable (Rust 1.58+)
    println!("{0} is {0}, {1} is {1}", "a", "b"); // Indexed placeholders

    // Debug printing (works with types that implement Debug)
    println!("{:?}", vec![1, 2, 3]);             // Debug format
    println!("{:#?}", vec![1, 2, 3]);            // Pretty debug format

    // Formatting
    println!("{:>10}", "right");     // Right-align, width 10
    println!("{:<10}", "left");      // Left-align, width 10
    println!("{:^10}", "center");    // Center-align, width 10
    println!("{:0>5}", 42);          // Zero-pad: 00042
    println!("{:.2}", 3.14159);      // 2 decimal places: 3.14
    println!("{:b}", 255);           // Binary: 11111111
    println!("{:x}", 255);           // Hex lowercase: ff
    println!("{:X}", 255);           // Hex uppercase: FF
    println!("{:o}", 255);           // Octal: 377
}
```

---

<!-- TIER 2 — CORE FUNDAMENTALS -->

## Variables & Constants

```rust
fn main() {
    // Variables are immutable by default
    let x = 5;
    // x = 6;  // ERROR: cannot assign twice to immutable variable

    // Use `mut` to make a variable mutable
    let mut y = 5;
    y = 6;  // OK

    // Type annotation
    let z: i32 = 10;

    // Constants — must have a type annotation, always immutable
    // Naming convention: SCREAMING_SNAKE_CASE
    const MAX_POINTS: u32 = 100_000;

    // Static variables — similar to constants but have a fixed memory address
    static LANGUAGE: &str = "Rust";

    // Shadowing — re-declare a variable with the same name
    let x = 5;
    let x = x + 1;      // x is now 6
    let x = "hello";    // x is now a &str — type can change with shadowing!
}
```

**Key difference: `mut` vs shadowing**
- `mut` lets you change the value but NOT the type
- Shadowing creates a new variable — the type CAN change

---

## Data Types

### Scalar Types

| Type | Size | Range / Description |
|------|------|---------------------|
| `i8` | 1 byte | -128 to 127 |
| `i16` | 2 bytes | -32,768 to 32,767 |
| `i32` | 4 bytes | -2,147,483,648 to 2,147,483,647 (default integer) |
| `i64` | 8 bytes | -9.2×10¹⁸ to 9.2×10¹⁸ |
| `i128` | 16 bytes | Very large range |
| `isize` | arch | Pointer-sized signed integer |
| `u8` | 1 byte | 0 to 255 |
| `u16` | 2 bytes | 0 to 65,535 |
| `u32` | 4 bytes | 0 to 4,294,967,295 |
| `u64` | 8 bytes | 0 to 1.8×10¹⁹ |
| `u128` | 16 bytes | Very large range |
| `usize` | arch | Pointer-sized unsigned integer (used for indexing) |
| `f32` | 4 bytes | Single-precision float |
| `f64` | 8 bytes | Double-precision float (default float) |
| `bool` | 1 byte | `true` or `false` |
| `char` | 4 bytes | Unicode scalar value (e.g. `'a'`, `'🦀'`) |

```rust
fn main() {
    // Integer literals
    let decimal = 98_222;       // Underscores for readability
    let hex = 0xff;
    let octal = 0o77;
    let binary = 0b1111_0000;
    let byte = b'A';            // u8 only

    // Floats
    let f1 = 2.0;              // f64 (default)
    let f2: f32 = 3.0;         // f32

    // Bool
    let t = true;
    let f: bool = false;

    // Char — uses single quotes, supports Unicode
    let c = 'z';
    let heart = '❤';
    let crab = '🦀';
}
```

### Compound Types

```rust
fn main() {
    // Tuples — fixed-length, can hold different types
    let tup: (i32, f64, u8) = (500, 6.4, 1);
    let (x, y, z) = tup;            // Destructuring
    let first = tup.0;              // Access by index
    let second = tup.1;

    // Unit type — empty tuple, represents "no value"
    let unit: () = ();

    // Arrays — fixed-length, same type, stack-allocated
    let arr = [1, 2, 3, 4, 5];
    let first = arr[0];             // Access by index
    let len = arr.len();            // Length: 5

    let zeros = [0; 5];             // [0, 0, 0, 0, 0] — repeat syntax
    let arr: [i32; 5] = [1, 2, 3, 4, 5];  // Explicit type & length

    // Slices — a view into an array or Vec
    let slice = &arr[1..3];         // [2, 3] — elements at index 1 and 2
    let slice = &arr[..2];          // [1, 2] — from start
    let slice = &arr[3..];          // [4, 5] — to end
    let slice = &arr[..];           // [1, 2, 3, 4, 5] — full slice
}
```

### Type Casting

```rust
fn main() {
    let x: i32 = 42;
    let y: f64 = x as f64;          // Cast i32 to f64
    let z: u8 = x as u8;            // Cast i32 to u8 (may truncate!)

    let c: char = 65u8 as char;     // 'A'
    let n: u8 = 'A' as u8;          // 65
}
```

> **Gotcha:** Rust has no implicit type coercion. You must explicitly cast with `as`. This is intentional — it prevents subtle bugs from unexpected conversions.

---

## Operators

### Arithmetic

| Operator | Description | Example |
|----------|-------------|---------|
| `+` | Addition | `5 + 3` → `8` |
| `-` | Subtraction | `5 - 3` → `2` |
| `*` | Multiplication | `5 * 3` → `15` |
| `/` | Division | `7 / 2` → `3` (integer division) |
| `%` | Remainder | `7 % 2` → `1` |

> **Note:** Integer division truncates toward zero. For float division, at least one operand must be a float: `7.0 / 2.0` → `3.5`

### Comparison

| Operator | Description |
|----------|-------------|
| `==` | Equal to |
| `!=` | Not equal to |
| `<` | Less than |
| `>` | Greater than |
| `<=` | Less than or equal to |
| `>=` | Greater than or equal to |

### Logical

| Operator | Description |
|----------|-------------|
| `&&` | Logical AND (short-circuit) |
| `\|\|` | Logical OR (short-circuit) |
| `!` | Logical NOT |

### Bitwise

| Operator | Description |
|----------|-------------|
| `&` | Bitwise AND |
| `\|` | Bitwise OR |
| `^` | Bitwise XOR |
| `!` | Bitwise NOT (for integers) |
| `<<` | Left shift |
| `>>` | Right shift |

### Compound Assignment

```rust
let mut x = 10;
x += 5;   // x = x + 5
x -= 3;   // x = x - 3
x *= 2;   // x = x * 2
x /= 4;   // x = x / 4
x %= 3;   // x = x % 3
```

> **Note:** Rust does NOT have `++` or `--` operators. Use `x += 1` and `x -= 1` instead.

---

<!-- TIER 3 — CONTROL FLOW -->

## Control Flow

### If Expressions

```rust
fn main() {
    let number = 7;

    // Basic if/else
    if number > 5 {
        println!("Greater than 5");
    } else if number > 0 {
        println!("Between 1 and 5");
    } else {
        println!("Zero or negative");
    }

    // if is an expression — it returns a value!
    let result = if number > 5 { "big" } else { "small" };

    // No parentheses needed around the condition (unlike C/Java)
    // The condition MUST be a bool — no truthy/falsy values
    // if 1 { ... }  // ERROR: expected bool, found integer
}
```

### Loops

```rust
fn main() {
    // loop — infinite loop (like while true)
    let mut counter = 0;
    let result = loop {
        counter += 1;
        if counter == 10 {
            break counter * 2;  // `break` can return a value!
        }
    };
    // result is 20

    // Loop labels — for nested loops
    'outer: loop {
        'inner: loop {
            break 'outer;  // Break out of the outer loop
        }
    }

    // while loop
    let mut n = 3;
    while n != 0 {
        println!("{n}");
        n -= 1;
    }

    // for loop — iterate over a range or collection
    for i in 0..5 {
        println!("{i}");       // 0, 1, 2, 3, 4
    }

    for i in 0..=5 {
        println!("{i}");       // 0, 1, 2, 3, 4, 5 (inclusive)
    }

    // Iterate over an array
    let arr = [10, 20, 30];
    for element in arr {
        println!("{element}");
    }

    // With index
    for (index, value) in arr.iter().enumerate() {
        println!("{index}: {value}");
    }

    // Reverse
    for i in (1..4).rev() {
        println!("{i}");       // 3, 2, 1
    }
}
```

> **Gotcha:** `0..5` is exclusive (0 to 4). Use `0..=5` for inclusive (0 to 5).

### While Let

```rust
fn main() {
    let mut stack = vec![1, 2, 3];

    // Loop while the pattern matches
    while let Some(top) = stack.pop() {
        println!("{top}");     // 3, 2, 1
    }
}
```

---

<!-- TIER 4 — FUNCTIONS -->

## Functions

```rust
// Basic function
fn greet() {
    println!("Hello!");
}

// With parameters — types are required
fn add(a: i32, b: i32) -> i32 {
    a + b    // No semicolon = implicit return (this is an expression)
}

// Explicit return (use for early returns)
fn absolute(x: i32) -> i32 {
    if x < 0 {
        return -x;    // Early return needs `return` keyword
    }
    x                 // Last expression is returned implicitly
}

// Multiple return values via tuple
fn swap(a: i32, b: i32) -> (i32, i32) {
    (b, a)
}

fn main() {
    greet();
    let sum = add(3, 5);               // 8
    let (x, y) = swap(1, 2);           // x=2, y=1
}
```

**Key points:**
- Function names use `snake_case`
- Parameter types are always required
- Return type is specified with `-> Type`
- Functions that don't return a value implicitly return `()` (the unit type)
- The last expression (without semicolon) is the return value
- Adding a semicolon turns an expression into a statement (returns `()`)

---

<!-- TIER 5 — OWNERSHIP & BORROWING -->

## Ownership & Borrowing

This is Rust's most unique feature. It enables memory safety without a garbage collector.

### Ownership Rules

1. Each value has exactly **one owner**
2. When the owner goes out of scope, the value is **dropped** (freed)
3. There can only be one owner at a time

```rust
fn main() {
    // Strings are heap-allocated — ownership matters
    let s1 = String::from("hello");
    let s2 = s1;              // s1 is MOVED to s2 — s1 is no longer valid!
    // println!("{s1}");      // ERROR: value used after move

    // Clone for a deep copy
    let s3 = s2.clone();     // s2 is still valid
    println!("{s2} {s3}");   // OK

    // Copy types (stack-allocated: integers, floats, bool, char, tuples of Copy types)
    let x = 5;
    let y = x;               // x is COPIED (not moved) — both are valid
    println!("{x} {y}");     // OK
}
```

### Borrowing (References)

Instead of transferring ownership, you can **borrow** a value with references.

```rust
fn main() {
    let s = String::from("hello");

    // Immutable reference (&) — can have many at once
    let len = calculate_length(&s);    // Borrow s
    println!("{s} has length {len}");  // s is still valid!

    // Mutable reference (&mut) — only ONE at a time
    let mut s = String::from("hello");
    change(&mut s);
    println!("{s}");                   // "hello, world"
}

fn calculate_length(s: &String) -> usize {
    s.len()
    // s goes out of scope but doesn't drop the value — it's just a reference
}

fn change(s: &mut String) {
    s.push_str(", world");
}
```

### Borrowing Rules

1. You can have **either** (not both at the same time):
   - Any number of immutable references (`&T`)
   - Exactly ONE mutable reference (`&mut T`)
2. References must always be valid (no dangling references)

```rust
fn main() {
    let mut s = String::from("hello");

    let r1 = &s;        // OK — immutable borrow
    let r2 = &s;        // OK — another immutable borrow
    // let r3 = &mut s;  // ERROR: can't borrow as mutable while immutable borrows exist
    println!("{r1} {r2}");
    // r1 and r2 are no longer used after this point (NLL — Non-Lexical Lifetimes)

    let r3 = &mut s;    // OK — no immutable borrows are active
    println!("{r3}");
}
```

> **Why?** These rules prevent data races at compile time. If someone is reading data, no one can change it. If someone is changing data, no one else can access it.

---

## Strings

Rust has two main string types:

| Type | Description | Where | Mutable |
|------|-------------|-------|---------|
| `String` | Owned, growable string | Heap | Yes |
| `&str` | Borrowed string slice (view) | Stack/Heap/Static | No |

```rust
fn main() {
    // String — owned, heap-allocated, growable
    let mut s = String::new();                    // Empty String
    let s = String::from("hello");                // From a literal
    let s = "hello".to_string();                  // Same thing

    // &str — borrowed string slice
    let slice: &str = "hello";                    // String literal (stored in binary)
    let slice: &str = &s[0..3];                   // Slice of a String: "hel"
    let slice: &str = &s;                         // Whole String as a slice

    // String operations
    let mut s = String::from("hello");
    s.push(' ');                                  // Append a char
    s.push_str("world");                          // Append a &str
    println!("{s}");                              // "hello world"

    // Concatenation
    let s1 = String::from("hello ");
    let s2 = String::from("world");
    let s3 = s1 + &s2;                           // s1 is moved! s2 is borrowed
    // println!("{s1}");                          // ERROR: s1 was moved

    // format! macro — doesn't take ownership
    let s1 = String::from("hello");
    let s2 = String::from("world");
    let s3 = format!("{s1} {s2}");               // Both still valid

    // Common methods
    let s = String::from("Hello, World!");
    println!("{}", s.len());                      // 13 (byte length)
    println!("{}", s.is_empty());                 // false
    println!("{}", s.contains("World"));          // true
    println!("{}", s.starts_with("Hello"));       // true
    println!("{}", s.ends_with("!"));             // true
    println!("{}", s.to_uppercase());             // "HELLO, WORLD!"
    println!("{}", s.to_lowercase());             // "hello, world!"
    println!("{}", s.trim());                     // Remove leading/trailing whitespace
    println!("{}", s.replace("World", "Rust"));   // "Hello, Rust!"

    // Iterating over characters
    for c in "hello".chars() {
        println!("{c}");
    }

    // Split
    let parts: Vec<&str> = "a,b,c".split(',').collect();  // ["a", "b", "c"]

    // Parse string to number
    let n: i32 = "42".parse().unwrap();           // 42
    let n: f64 = "3.14".parse().unwrap();         // 3.14
}
```

> **Gotcha:** Rust strings are UTF-8 encoded. You cannot index into a String with `s[0]` because characters can be multi-byte. Use `.chars()` or `.bytes()` to iterate.

---

<!-- TIER 6 — COLLECTIONS -->

## Collections

### Vec (Vector)

A growable array — the most commonly used collection.

```rust
fn main() {
    // Creating vectors
    let v: Vec<i32> = Vec::new();           // Empty vector with type annotation
    let v = vec![1, 2, 3];                  // vec! macro with initial values
    let v = vec![0; 5];                     // [0, 0, 0, 0, 0]

    // Adding elements
    let mut v = Vec::new();
    v.push(1);
    v.push(2);
    v.push(3);

    // Accessing elements
    let third = v[2];                       // Panics if out of bounds!
    let third = v.get(2);                   // Returns Option<&T> — safe

    match v.get(2) {
        Some(value) => println!("Third: {value}"),
        None => println!("No third element"),
    }

    // Common methods
    v.len();                                // Length
    v.is_empty();                           // Check if empty
    v.contains(&2);                         // Check if contains value
    v.pop();                                // Remove and return last element (Option<T>)
    v.remove(0);                            // Remove at index (shifts elements)
    v.insert(0, 10);                        // Insert at index (shifts elements)
    v.sort();                               // Sort in place
    v.reverse();                            // Reverse in place
    v.dedup();                              // Remove consecutive duplicates

    // Iterating
    let v = vec![1, 2, 3];
    for val in &v {                         // Immutable borrow
        println!("{val}");
    }

    let mut v = vec![1, 2, 3];
    for val in &mut v {                     // Mutable borrow
        *val += 10;                         // Dereference to modify
    }

    // Slicing
    let slice = &v[1..3];                   // &[i32] slice
}
```

### HashMap

```rust
use std::collections::HashMap;

fn main() {
    // Creating
    let mut scores = HashMap::new();
    scores.insert(String::from("Alice"), 100);
    scores.insert(String::from("Bob"), 85);

    // From iterators
    let keys = vec!["Alice", "Bob"];
    let values = vec![100, 85];
    let scores: HashMap<_, _> = keys.into_iter().zip(values.into_iter()).collect();

    // Accessing
    let score = scores.get("Alice");        // Returns Option<&V>
    let score = scores["Alice"];            // Panics if key missing!

    // Check if key exists
    if scores.contains_key("Alice") {
        println!("Found Alice");
    }

    // Insert only if key doesn't exist
    scores.entry("Charlie".to_string()).or_insert(90);

    // Update based on old value
    let text = "hello world hello rust";
    let mut word_count = HashMap::new();
    for word in text.split_whitespace() {
        let count = word_count.entry(word).or_insert(0);
        *count += 1;
    }

    // Iterating
    for (key, value) in &scores {
        println!("{key}: {value}");
    }

    // Remove
    scores.remove("Bob");

    // Length
    println!("{}", scores.len());
}
```

### HashSet

```rust
use std::collections::HashSet;

fn main() {
    let mut set = HashSet::new();
    set.insert(1);
    set.insert(2);
    set.insert(3);
    set.insert(2);                          // Duplicate — ignored

    println!("{}", set.len());              // 3
    println!("{}", set.contains(&2));       // true

    set.remove(&2);

    // Set operations
    let a: HashSet<i32> = [1, 2, 3].into();
    let b: HashSet<i32> = [2, 3, 4].into();

    let union: HashSet<_> = a.union(&b).collect();              // {1, 2, 3, 4}
    let intersection: HashSet<_> = a.intersection(&b).collect(); // {2, 3}
    let difference: HashSet<_> = a.difference(&b).collect();     // {1}
}
```

---

<!-- TIER 7 — STRUCTS & ENUMS -->

## Structs

```rust
// Define a struct
struct User {
    username: String,
    email: String,
    active: bool,
    sign_in_count: u64,
}

fn main() {
    // Create an instance
    let user1 = User {
        username: String::from("alice"),
        email: String::from("alice@example.com"),
        active: true,
        sign_in_count: 1,
    };

    // Access fields
    println!("{}", user1.username);

    // Mutable instance — entire struct must be mut (not individual fields)
    let mut user2 = User {
        username: String::from("bob"),
        email: String::from("bob@example.com"),
        active: true,
        sign_in_count: 1,
    };
    user2.email = String::from("new@example.com");

    // Struct update syntax — create from another instance
    let user3 = User {
        email: String::from("charlie@example.com"),
        ..user1    // Remaining fields come from user1 (user1 may be partially moved!)
    };
}

// Field init shorthand — if variable name matches field name
fn build_user(username: String, email: String) -> User {
    User {
        username,           // shorthand for username: username
        email,              // shorthand for email: email
        active: true,
        sign_in_count: 1,
    }
}
```

### Tuple Structs & Unit Structs

```rust
// Tuple structs — named tuples
struct Color(i32, i32, i32);
struct Point(f64, f64, f64);

let black = Color(0, 0, 0);
let origin = Point(0.0, 0.0, 0.0);
println!("{}", black.0);    // Access by index

// Unit struct — no fields (useful for traits)
struct AlwaysEqual;
```

### Methods (impl blocks)

```rust
struct Rectangle {
    width: f64,
    height: f64,
}

impl Rectangle {
    // Associated function (like a static method) — no &self
    fn new(width: f64, height: f64) -> Self {
        Self { width, height }
    }

    fn square(size: f64) -> Self {
        Self { width: size, height: size }
    }

    // Method — takes &self (immutable borrow of the instance)
    fn area(&self) -> f64 {
        self.width * self.height
    }

    fn perimeter(&self) -> f64 {
        2.0 * (self.width + self.height)
    }

    // Method that takes &mut self (mutable borrow)
    fn scale(&mut self, factor: f64) {
        self.width *= factor;
        self.height *= factor;
    }

    // Method that takes self (consumes the instance)
    fn into_square(self) -> Rectangle {
        let side = self.width.max(self.height);
        Rectangle { width: side, height: side }
    }
}

fn main() {
    let r = Rectangle::new(10.0, 5.0);      // Associated function call
    println!("Area: {}", r.area());          // Method call
    println!("Perimeter: {}", r.perimeter());

    let mut r = Rectangle::new(10.0, 5.0);
    r.scale(2.0);                            // Mutable method

    let sq = Rectangle::square(5.0);
}
```

### Deriving Traits

```rust
#[derive(Debug, Clone, PartialEq)]
struct Point {
    x: f64,
    y: f64,
}

fn main() {
    let p = Point { x: 1.0, y: 2.0 };
    println!("{:?}", p);             // Debug printing
    println!("{:#?}", p);            // Pretty debug printing

    let p2 = p.clone();             // Clone
    println!("{}", p == p2);        // PartialEq comparison: true
}
```

---

## Enums

```rust
// Basic enum
enum Direction {
    North,
    South,
    East,
    West,
}

// Enum with data — each variant can hold different types
enum Message {
    Quit,                          // No data
    Move { x: i32, y: i32 },      // Named fields (struct-like)
    Write(String),                 // Single value (tuple-like)
    ChangeColor(i32, i32, i32),   // Multiple values
}

fn main() {
    let dir = Direction::North;
    let msg = Message::Write(String::from("hello"));
    let msg = Message::Move { x: 10, y: 20 };
}

// Enums can have methods too
impl Message {
    fn call(&self) {
        // ...
    }
}
```

### Option — Rust's Null Alternative

Rust has no `null`. Instead, it uses `Option<T>` to represent values that might not exist.

```rust
enum Option<T> {
    Some(T),    // A value exists
    None,       // No value
}

fn main() {
    let some_number: Option<i32> = Some(5);
    let no_number: Option<i32> = None;

    // You MUST handle the None case to use the value
    // This prevents null pointer exceptions at compile time!

    // Using match
    match some_number {
        Some(n) => println!("Got: {n}"),
        None => println!("Got nothing"),
    }

    // Using if let (for when you only care about one variant)
    if let Some(n) = some_number {
        println!("Got: {n}");
    }

    // Common Option methods
    let x: Option<i32> = Some(5);
    x.unwrap();              // 5 — panics if None!
    x.unwrap_or(0);          // 5 — returns default if None
    x.unwrap_or_default();   // 5 — uses type's Default if None
    x.is_some();             // true
    x.is_none();             // false
    x.map(|n| n * 2);       // Some(10)

    let y: Option<i32> = None;
    y.unwrap_or(0);          // 0
    y.unwrap_or_else(|| compute_default());  // Lazy default
}
```

---

## Pattern Matching

### match

The `match` expression is like a supercharged switch statement. It must be **exhaustive** — every possible value must be handled.

```rust
fn main() {
    let x = 5;

    match x {
        1 => println!("one"),
        2 => println!("two"),
        3 | 4 => println!("three or four"),     // Multiple patterns with |
        5..=10 => println!("five through ten"),  // Range pattern
        _ => println!("something else"),         // Wildcard (catch-all)
    }

    // match is an expression — returns a value
    let text = match x {
        1 => "one",
        2 => "two",
        _ => "other",
    };

    // Matching enums
    enum Coin {
        Penny,
        Nickel,
        Dime,
        Quarter(String),  // Quarter with state name
    }

    fn value_in_cents(coin: &Coin) -> u32 {
        match coin {
            Coin::Penny => 1,
            Coin::Nickel => 5,
            Coin::Dime => 10,
            Coin::Quarter(state) => {
                println!("Quarter from {state}");
                25
            }
        }
    }

    // Destructuring structs in match
    struct Point { x: i32, y: i32 }
    let p = Point { x: 0, y: 7 };

    match p {
        Point { x: 0, y } => println!("On y-axis at {y}"),
        Point { x, y: 0 } => println!("On x-axis at {x}"),
        Point { x, y } => println!("At ({x}, {y})"),
    }

    // Match guards — additional conditions
    let num = Some(4);
    match num {
        Some(x) if x < 5 => println!("Less than 5: {x}"),
        Some(x) => println!("{x}"),
        None => (),
    }
}
```

### if let / let else

```rust
fn main() {
    let value: Option<i32> = Some(42);

    // if let — shorthand when you only care about one pattern
    if let Some(n) = value {
        println!("Got {n}");
    } else {
        println!("Got nothing");
    }

    // let else — bind or diverge (Rust 1.65+)
    let Some(n) = value else {
        println!("Got nothing");
        return;   // Must diverge: return, break, continue, or panic
    };
    println!("Got {n}");    // n is available here
}
```

---

<!-- TIER 8 — TRAITS & GENERICS -->

## Traits & Generics

### Traits

Traits define shared behavior — similar to interfaces in other languages.

```rust
// Define a trait
trait Summary {
    // Required method — implementors must define this
    fn summarize(&self) -> String;

    // Default method — can be overridden
    fn preview(&self) -> String {
        format!("Read more: {}", self.summarize())
    }
}

struct Article {
    title: String,
    content: String,
}

struct Tweet {
    username: String,
    text: String,
}

// Implement the trait for a type
impl Summary for Article {
    fn summarize(&self) -> String {
        format!("{}: {}", self.title, &self.content[..50])
    }
}

impl Summary for Tweet {
    fn summarize(&self) -> String {
        format!("@{}: {}", self.username, self.text)
    }
}
```

### Generics

```rust
// Generic function
fn largest<T: PartialOrd>(list: &[T]) -> &T {
    let mut largest = &list[0];
    for item in &list[1..] {
        if item > largest {
            largest = item;
        }
    }
    largest
}

// Generic struct
struct Wrapper<T> {
    value: T,
}

impl<T> Wrapper<T> {
    fn new(value: T) -> Self {
        Self { value }
    }
}

// Generic enum (Option and Result are built-in examples)
enum MyResult<T, E> {
    Ok(T),
    Err(E),
}
```

### Trait Bounds

```rust
// Trait bound syntax
fn notify<T: Summary>(item: &T) {
    println!("Breaking: {}", item.summarize());
}

// impl Trait syntax (shorthand for simple cases)
fn notify(item: &impl Summary) {
    println!("Breaking: {}", item.summarize());
}

// Multiple trait bounds
fn notify<T: Summary + std::fmt::Display>(item: &T) { }

// where clause — cleaner for complex bounds
fn some_function<T, U>(t: &T, u: &U) -> i32
where
    T: Summary + Clone,
    U: std::fmt::Debug,
{
    // ...
    0
}

// Returning impl Trait
fn make_summary() -> impl Summary {
    Tweet {
        username: String::from("bot"),
        text: String::from("hello"),
    }
}
```

### Common Standard Library Traits

| Trait | Purpose | Derivable |
|-------|---------|-----------|
| `Debug` | `{:?}` formatting | Yes |
| `Display` | `{}` formatting | No — must implement manually |
| `Clone` | Explicit deep copy (`.clone()`) | Yes |
| `Copy` | Implicit bitwise copy (stack only) | Yes |
| `PartialEq` / `Eq` | `==` and `!=` comparison | Yes |
| `PartialOrd` / `Ord` | `<`, `>`, `<=`, `>=` comparison + sorting | Yes |
| `Hash` | Hashing (for HashMap keys) | Yes |
| `Default` | Default value (`Default::default()`) | Yes |
| `From` / `Into` | Type conversion | No |
| `Iterator` | Iteration protocol | No |
| `Drop` | Custom cleanup when value is dropped | No |

```rust
use std::fmt;

// Manually implementing Display
struct Point { x: f64, y: f64 }

impl fmt::Display for Point {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "({}, {})", self.x, self.y)
    }
}

// From/Into conversion
impl From<(f64, f64)> for Point {
    fn from((x, y): (f64, f64)) -> Self {
        Point { x, y }
    }
}

let p: Point = (1.0, 2.0).into();
let p = Point::from((1.0, 2.0));
```

---

<!-- TIER 9 — ERROR HANDLING -->

## Error Handling

### Result Type

```rust
enum Result<T, E> {
    Ok(T),    // Success with value
    Err(E),   // Failure with error
}
```

```rust
use std::fs;
use std::io;
use std::num::ParseIntError;

fn main() {
    // Functions that can fail return Result
    let content: Result<String, io::Error> = fs::read_to_string("hello.txt");

    // Handle with match
    match content {
        Ok(text) => println!("File: {text}"),
        Err(e) => println!("Error: {e}"),
    }

    // unwrap — get the value or panic
    let text = fs::read_to_string("hello.txt").unwrap();

    // expect — like unwrap but with a custom panic message
    let text = fs::read_to_string("hello.txt").expect("Failed to read file");

    // unwrap_or — provide a default
    let text = fs::read_to_string("hello.txt").unwrap_or(String::from("default"));

    // unwrap_or_else — lazy default
    let text = fs::read_to_string("hello.txt").unwrap_or_else(|e| {
        eprintln!("Warning: {e}");
        String::from("default")
    });
}
```

### The `?` Operator

Shorthand for propagating errors up to the caller. If the Result is `Err`, it returns the error early. If `Ok`, it unwraps the value.

```rust
use std::fs;
use std::io;

fn read_username_from_file() -> Result<String, io::Error> {
    let content = fs::read_to_string("username.txt")?;  // Return Err early if it fails
    Ok(content.trim().to_string())
}

// Can chain ? calls
fn read_and_parse() -> Result<i32, Box<dyn std::error::Error>> {
    let content = fs::read_to_string("number.txt")?;
    let number = content.trim().parse::<i32>()?;
    Ok(number)
}
```

> **Note:** `?` can only be used in functions that return `Result` or `Option`.

### Custom Error Types

```rust
use std::fmt;

#[derive(Debug)]
enum AppError {
    IoError(std::io::Error),
    ParseError(String),
    NotFound(String),
}

impl fmt::Display for AppError {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        match self {
            AppError::IoError(e) => write!(f, "IO error: {e}"),
            AppError::ParseError(msg) => write!(f, "Parse error: {msg}"),
            AppError::NotFound(item) => write!(f, "Not found: {item}"),
        }
    }
}

impl From<std::io::Error> for AppError {
    fn from(e: std::io::Error) -> Self {
        AppError::IoError(e)
    }
}
```

### panic!

For unrecoverable errors — crashes the program.

```rust
fn main() {
    panic!("Something went terribly wrong!");

    // Common panics:
    // - Indexing out of bounds: vec[100]
    // - unwrap() on None/Err
    // - Integer overflow in debug mode
}
```

> **Rule of thumb:** Use `Result` for expected failures (file not found, invalid input). Use `panic!` for bugs and truly unrecoverable situations.

---

<!-- TIER 10 — CLOSURES & ITERATORS -->

## Closures

Closures are anonymous functions that capture variables from their environment.

```rust
fn main() {
    // Basic closure syntax
    let add = |a, b| a + b;
    let result = add(3, 5);         // 8

    // With type annotations
    let add = |a: i32, b: i32| -> i32 { a + b };

    // Multi-line closure
    let complex = |x: i32| {
        let y = x * 2;
        y + 1
    };

    // Closures capture variables from the enclosing scope
    let name = String::from("Rust");
    let greet = || println!("Hello, {name}!");
    greet();                         // "Hello, Rust!"

    // Move closure — takes ownership of captured variables
    let name = String::from("Rust");
    let greet = move || println!("Hello, {name}!");
    // name is no longer available here — it was moved into the closure

    // Closures as parameters
    fn apply<F: Fn(i32) -> i32>(f: F, x: i32) -> i32 {
        f(x)
    }
    let double = |x| x * 2;
    println!("{}", apply(double, 5));   // 10
}
```

**Closure trait bounds:**
| Trait | Description | Use when |
|-------|-------------|----------|
| `Fn` | Borrows captured values immutably | Closure only reads captured values |
| `FnMut` | Borrows captured values mutably | Closure modifies captured values |
| `FnOnce` | Takes ownership of captured values | Closure consumes captured values |

---

## Iterators

Iterators are lazy — they do nothing until consumed.

```rust
fn main() {
    let v = vec![1, 2, 3, 4, 5];

    // Creating iterators
    let iter = v.iter();           // Immutable references (&T)
    let iter = v.iter_mut();       // Mutable references (&mut T) — needs mut v
    let iter = v.into_iter();      // Owned values (T) — consumes v

    // Consuming adaptors — consume the iterator
    let v = vec![1, 2, 3, 4, 5];
    let sum: i32 = v.iter().sum();                        // 15
    let count = v.iter().count();                          // 5
    let min = v.iter().min();                              // Some(&1)
    let max = v.iter().max();                              // Some(&5)
    let found = v.iter().find(|&&x| x == 3);              // Some(&3)
    let any_even = v.iter().any(|&x| x % 2 == 0);        // true
    let all_positive = v.iter().all(|&x| x > 0);         // true
    let collected: Vec<_> = v.iter().collect();            // Collect into collection

    // Iterator adaptors — transform iterators (lazy!)
    let v = vec![1, 2, 3, 4, 5];

    let doubled: Vec<i32> = v.iter()
        .map(|&x| x * 2)                                  // [2, 4, 6, 8, 10]
        .collect();

    let evens: Vec<&i32> = v.iter()
        .filter(|&&x| x % 2 == 0)                         // [&2, &4]
        .collect();

    // Chaining — this is where iterators shine
    let result: Vec<i32> = (1..=10)
        .filter(|x| x % 2 == 0)       // Keep even numbers
        .map(|x| x * x)               // Square them
        .take(3)                       // Take first 3
        .collect();                    // [4, 16, 36]

    // Other useful adaptors
    let v = vec![1, 2, 3];
    v.iter().enumerate();              // (index, &value) pairs
    v.iter().zip(v.iter());            // Pair up two iterators
    v.iter().skip(1);                  // Skip first N
    v.iter().take(2);                  // Take first N
    v.iter().chain(v.iter());          // Concatenate two iterators
    v.iter().flat_map(|x| vec![x, x]); // Map and flatten
    v.iter().peekable();               // Peek at next without consuming
    v.iter().cloned();                 // Clone each element

    // fold — like reduce in other languages
    let sum = v.iter().fold(0, |acc, &x| acc + x);        // 6
}
```

---

<!-- TIER 11 — LIFETIMES -->

## Lifetimes

Lifetimes ensure references are valid for as long as they're used. Most of the time the compiler infers them, but sometimes you need to annotate them.

```rust
// The compiler can't tell which reference the return value borrows from
// Lifetime 'a says: the returned reference lives at least as long as both inputs
fn longest<'a>(x: &'a str, y: &'a str) -> &'a str {
    if x.len() > y.len() { x } else { y }
}

fn main() {
    let string1 = String::from("long string");
    let result;
    {
        let string2 = String::from("xyz");
        result = longest(&string1, &string2);
        println!("{result}");   // OK — both string1 and string2 are still alive
    }
    // println!("{result}");    // ERROR if uncommented: string2 is dropped
}

// Lifetime in structs — the struct can't outlive the reference it holds
struct Excerpt<'a> {
    part: &'a str,
}

impl<'a> Excerpt<'a> {
    fn level(&self) -> i32 {
        3
    }
}

// 'static lifetime — lives for the entire program
let s: &'static str = "I live forever";
```

**Lifetime elision rules** (when you don't need to annotate):
1. Each input reference gets its own lifetime
2. If there's exactly one input lifetime, it's assigned to all output lifetimes
3. If `&self` or `&mut self` is an input, its lifetime is assigned to all output lifetimes

---

<!-- TIER 12 — CONCURRENCY -->

## Concurrency

### Threads

```rust
use std::thread;
use std::time::Duration;

fn main() {
    // Spawn a thread
    let handle = thread::spawn(|| {
        for i in 1..5 {
            println!("Spawned thread: {i}");
            thread::sleep(Duration::from_millis(1));
        }
    });

    for i in 1..3 {
        println!("Main thread: {i}");
        thread::sleep(Duration::from_millis(1));
    }

    // Wait for the thread to finish
    handle.join().unwrap();

    // Move data into a thread
    let data = vec![1, 2, 3];
    let handle = thread::spawn(move || {
        println!("Data: {:?}", data);
    });
    // data is no longer available here
    handle.join().unwrap();
}
```

### Message Passing (Channels)

```rust
use std::sync::mpsc;  // Multiple Producer, Single Consumer
use std::thread;

fn main() {
    let (tx, rx) = mpsc::channel();

    // Clone tx for multiple producers
    let tx2 = tx.clone();

    thread::spawn(move || {
        tx.send(String::from("hello from thread 1")).unwrap();
    });

    thread::spawn(move || {
        tx2.send(String::from("hello from thread 2")).unwrap();
    });

    // Receive messages
    for received in rx {
        println!("Got: {received}");
    }
}
```

### Shared State (Arc & Mutex)

```rust
use std::sync::{Arc, Mutex};
use std::thread;

fn main() {
    // Arc = Atomic Reference Counted (thread-safe Rc)
    // Mutex = Mutual Exclusion (thread-safe interior mutability)
    let counter = Arc::new(Mutex::new(0));
    let mut handles = vec![];

    for _ in 0..10 {
        let counter = Arc::clone(&counter);
        let handle = thread::spawn(move || {
            let mut num = counter.lock().unwrap();
            *num += 1;
        });
        handles.push(handle);
    }

    for handle in handles {
        handle.join().unwrap();
    }

    println!("Result: {}", *counter.lock().unwrap());  // 10
}
```

---

<!-- TIER 13 — FILE I/O -->

## File I/O

```rust
use std::fs;
use std::io::{self, Read, Write, BufRead, BufReader, BufWriter};
use std::path::Path;

fn main() -> Result<(), Box<dyn std::error::Error>> {
    // Read entire file to string
    let content = fs::read_to_string("file.txt")?;

    // Read entire file to bytes
    let bytes = fs::read("file.txt")?;

    // Write string to file (creates or overwrites)
    fs::write("output.txt", "Hello, world!")?;

    // Append to file
    use std::fs::OpenOptions;
    let mut file = OpenOptions::new()
        .append(true)
        .create(true)
        .open("log.txt")?;
    writeln!(file, "New log entry")?;

    // Read file line by line (memory efficient for large files)
    let file = fs::File::open("file.txt")?;
    let reader = BufReader::new(file);
    for line in reader.lines() {
        let line = line?;
        println!("{line}");
    }

    // Buffered writing
    let file = fs::File::create("output.txt")?;
    let mut writer = BufWriter::new(file);
    writeln!(writer, "Line 1")?;
    writeln!(writer, "Line 2")?;

    // Check if file exists
    if Path::new("file.txt").exists() {
        println!("File exists");
    }

    // Create directory
    fs::create_dir_all("path/to/dir")?;

    // Remove file/directory
    fs::remove_file("file.txt")?;
    fs::remove_dir_all("path/to/dir")?;

    // List directory contents
    for entry in fs::read_dir(".")? {
        let entry = entry?;
        println!("{}", entry.path().display());
    }

    Ok(())
}
```

---

<!-- TIER 14 — MODULES & CRATES -->

## Modules & Crates

### Module System

```rust
// In src/main.rs or src/lib.rs

// Inline module
mod math {
    pub fn add(a: i32, b: i32) -> i32 { a + b }

    fn private_helper() { }  // Private by default

    pub mod advanced {
        pub fn factorial(n: u64) -> u64 {
            (1..=n).product()
        }
    }
}

fn main() {
    // Use full path
    let sum = math::add(1, 2);
    let fact = math::advanced::factorial(5);

    // Or bring into scope with `use`
    use math::add;
    let sum = add(1, 2);

    use math::advanced::factorial;
    let fact = factorial(5);
}
```

### File-based Modules

```
src/
├── main.rs
├── math.rs           // mod math
└── math/
    └── advanced.rs   // mod math::advanced
```

```rust
// src/main.rs
mod math;   // Loads from src/math.rs or src/math/mod.rs

fn main() {
    math::add(1, 2);
    math::advanced::factorial(5);
}

// src/math.rs
pub mod advanced;   // Loads from src/math/advanced.rs

pub fn add(a: i32, b: i32) -> i32 { a + b }

// src/math/advanced.rs
pub fn factorial(n: u64) -> u64 {
    (1..=n).product()
}
```

### Visibility

```rust
mod outer {
    pub fn public_fn() {}          // Accessible outside the module
    fn private_fn() {}             // Only accessible within this module

    pub(crate) fn crate_fn() {}    // Accessible within the crate
    pub(super) fn parent_fn() {}   // Accessible by parent module

    pub struct MyStruct {
        pub public_field: i32,     // Public field
        private_field: i32,        // Private field (even if struct is pub)
    }
}
```

### use & Paths

```rust
// Absolute path (from crate root)
use crate::math::add;

// Relative path
use self::math::add;
use super::something;    // Parent module

// Re-export
pub use crate::math::add;

// Glob import (generally avoid — pollutes namespace)
use std::collections::*;

// Nested use
use std::io::{self, Read, Write};
use std::collections::{HashMap, HashSet};

// Aliasing
use std::collections::HashMap as Map;
```

### Adding Dependencies (Cargo.toml)

```toml
[package]
name = "my_project"
version = "0.1.0"
edition = "2021"

[dependencies]
serde = { version = "1.0", features = ["derive"] }
tokio = { version = "1", features = ["full"] }
rand = "0.8"
```

```bash
# Add a dependency via command line
cargo add serde --features derive
cargo add tokio --features full
```

---

<!-- TIER 15 — SMART POINTERS -->

## Smart Pointers

### Box — Heap Allocation

```rust
fn main() {
    // Box puts data on the heap
    let b = Box::new(5);
    println!("{b}");     // Derefs automatically

    // Useful for recursive types
    enum List {
        Cons(i32, Box<List>),
        Nil,
    }

    let list = List::Cons(1, Box::new(List::Cons(2, Box::new(List::Nil))));
}
```

### Rc — Reference Counted

```rust
use std::rc::Rc;

fn main() {
    // Rc allows multiple owners (single-threaded only)
    let a = Rc::new(vec![1, 2, 3]);
    let b = Rc::clone(&a);          // Increment reference count (cheap!)
    let c = Rc::clone(&a);

    println!("Count: {}", Rc::strong_count(&a));  // 3
    println!("{:?}", a);
}
// All clones dropped → data is freed
```

### RefCell — Interior Mutability

```rust
use std::cell::RefCell;

fn main() {
    // RefCell allows mutable borrows checked at RUNTIME (not compile time)
    let data = RefCell::new(vec![1, 2, 3]);

    data.borrow_mut().push(4);           // Mutable borrow at runtime
    println!("{:?}", data.borrow());     // Immutable borrow at runtime

    // Common pattern: Rc<RefCell<T>> — multiple owners with interior mutability
    use std::rc::Rc;
    let shared = Rc::new(RefCell::new(0));
    let clone1 = Rc::clone(&shared);
    let clone2 = Rc::clone(&shared);

    *clone1.borrow_mut() += 10;
    *clone2.borrow_mut() += 20;
    println!("{}", shared.borrow());     // 30
}
```

> **When to use what:**
> - `Box<T>` — Single owner, heap allocation
> - `Rc<T>` — Multiple owners, single-threaded, immutable
> - `Arc<T>` — Multiple owners, multi-threaded (see Concurrency section)
> - `RefCell<T>` — Interior mutability, runtime borrow checking
> - `Mutex<T>` — Interior mutability, multi-threaded (see Concurrency section)

---

<!-- TIER 16 — MACROS -->

## Macros

### Common Built-in Macros

```rust
fn main() {
    println!("Print with newline: {}", 42);
    print!("Print without newline");
    eprintln!("Print to stderr");
    format!("Returns a String: {}", 42);

    dbg!(42);                    // Debug print with file/line info

    vec![1, 2, 3];              // Create a Vec
    todo!();                    // Mark code as unfinished (panics at runtime)
    unimplemented!();           // Similar to todo!
    unreachable!();             // Mark code that should never be reached

    assert!(true);              // Panics if false
    assert_eq!(1, 1);           // Panics if not equal
    assert_ne!(1, 2);           // Panics if equal

    include_str!("file.txt");   // Include file contents as &str at compile time
    include_bytes!("img.png");  // Include file contents as &[u8]

    cfg!(target_os = "linux");  // Check compile-time configuration
}
```

### Declarative Macros (macro_rules!)

```rust
// Simple macro
macro_rules! say_hello {
    () => {
        println!("Hello!");
    };
}

// Macro with arguments
macro_rules! create_vec {
    ( $( $x:expr ),* ) => {
        {
            let mut v = Vec::new();
            $( v.push($x); )*
            v
        }
    };
}

fn main() {
    say_hello!();                           // Hello!
    let v = create_vec![1, 2, 3, 4, 5];    // Vec with elements
}
```

---

<!-- TIER 17 — TESTING -->

## Testing

```rust
// In any .rs file
#[cfg(test)]
mod tests {
    use super::*;   // Import items from parent module

    #[test]
    fn it_works() {
        assert_eq!(2 + 2, 4);
    }

    #[test]
    fn test_with_result() -> Result<(), String> {
        if 2 + 2 == 4 {
            Ok(())
        } else {
            Err(String::from("two plus two does not equal four"))
        }
    }

    #[test]
    #[should_panic]
    fn test_panic() {
        panic!("This should panic");
    }

    #[test]
    #[should_panic(expected = "specific message")]
    fn test_specific_panic() {
        panic!("specific message here");
    }

    #[test]
    #[ignore]   // Skip this test unless specifically requested
    fn expensive_test() {
        // Long-running test...
    }
}
```

```bash
cargo test                     # Run all tests
cargo test test_name           # Run specific test
cargo test -- --ignored        # Run ignored tests
cargo test -- --show-output    # Show println! output
cargo test -- --test-threads=1 # Run tests sequentially
```

### Integration Tests

```
my_project/
├── src/
│   └── lib.rs
└── tests/                     # Integration tests directory
    └── integration_test.rs
```

```rust
// tests/integration_test.rs
use my_project;   // Import your crate

#[test]
fn test_from_outside() {
    assert_eq!(my_project::add(1, 2), 3);
}
```

---

<!-- TIER 18 — REFERENCE -->

## Common Errors & Tips

### Common Compiler Errors

| Error | Cause | Fix |
|-------|-------|-----|
| `E0382: use of moved value` | Value was moved | Use `.clone()`, borrow with `&`, or restructure |
| `E0502: cannot borrow as mutable` | Already borrowed as immutable | Ensure immutable borrows end before mutable borrow |
| `E0499: cannot borrow as mutable more than once` | Two `&mut` at same time | Restructure to avoid overlapping mutable borrows |
| `E0106: missing lifetime specifier` | Compiler can't infer lifetime | Add lifetime annotations |
| `E0308: mismatched types` | Wrong type | Check expected vs actual type, use `as` or `.into()` |
| `E0277: trait not satisfied` | Type doesn't implement a trait | Derive or implement the trait |
| `E0599: no method named X` | Method doesn't exist on type | Check type, import trait, or implement method |

### Best Practices

- **Prefer `&str` over `String` in function parameters** — accepts both `String` and `&str`
- **Use `Result` over `panic!`** — let the caller decide how to handle errors
- **Use `clippy`** — `cargo clippy` catches common mistakes and suggests improvements
- **Use `rustfmt`** — `cargo fmt` formats your code consistently
- **Use `.iter()` methods over manual loops** — more idiomatic and often faster
- **Prefer `collect()` with type annotation** — `let v: Vec<_> = iter.collect();`
- **Use `if let` for single-pattern matches** — cleaner than a full `match`
- **Avoid `.unwrap()` in production code** — use `?`, `unwrap_or`, or proper error handling

### Useful Commands

```bash
cargo fmt              # Format code
cargo clippy           # Lint code
cargo doc --open       # Generate and open documentation
cargo bench            # Run benchmarks
cargo update           # Update dependencies
cargo tree             # Show dependency tree
```

---

## Useful Crates

| Crate | Purpose |
|-------|---------|
| `serde` + `serde_json` | Serialization/deserialization (JSON, TOML, etc.) |
| `tokio` | Async runtime |
| `reqwest` | HTTP client |
| `clap` | Command-line argument parsing |
| `anyhow` | Simplified error handling |
| `thiserror` | Custom error types with derive macros |
| `rand` | Random number generation |
| `regex` | Regular expressions |
| `log` + `env_logger` | Logging |
| `chrono` | Date and time |
| `rayon` | Data parallelism (parallel iterators) |
| `itertools` | Extra iterator methods |

```rust
// Example: serde JSON
use serde::{Deserialize, Serialize};

#[derive(Serialize, Deserialize, Debug)]
struct User {
    name: String,
    age: u32,
}

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let user = User { name: "Alice".into(), age: 30 };

    // Serialize to JSON string
    let json = serde_json::to_string(&user)?;
    println!("{json}");   // {"name":"Alice","age":30}

    // Deserialize from JSON string
    let parsed: User = serde_json::from_str(&json)?;
    println!("{:?}", parsed);

    Ok(())
}
```

---

*Happy coding with Rust!* 🦀

# Rust Quick Reference Guide

A practical, code-focused reference for Rust — from basics to advanced concepts. Written for beginners and those new to systems programming.

**What is Rust?** Rust is a systems programming language focused on three goals: speed, safety, and concurrency. Unlike C/C++, Rust prevents entire categories of bugs (null pointer dereferences, buffer overflows, data races) at compile time — meaning the compiler catches them *before* your program ever runs. Unlike Java or Python, Rust does this without a garbage collector, giving you full control over memory without sacrificing safety.

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

Rust is installed via **rustup**, a command-line tool that manages your Rust installation. Think of rustup like an app store just for Rust toolchains — it lets you install, update, and switch between Rust versions easily.

```bash
# Install rustup (macOS/Linux)
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

# Check version
rustc --version
cargo --version

# Update Rust
rustup update
```

**What each tool does:**
- `rustup` = The installer and version manager — you use this to manage Rust itself
- `rustc` = The Rust Compiler — turns your `.rs` source code into an executable
- `cargo` = Rust's build system and package manager — you'll use this for almost everything

> **Note for Windows users:** Download and run `rustup-init.exe` from [rustup.rs](https://rustup.rs) instead of the curl command above.

---

### Creating a Project

In Rust, almost every project uses **Cargo** — Rust's build system and package manager. Cargo handles compiling your code, downloading libraries (called "crates"), running tests, and more. You rarely call `rustc` directly.

```bash
# Create a new project (binary — a runnable program)
cargo new my_project

# Create a library project (code other programs can use)
cargo new my_library --lib

# Project structure:
# my_project/
# ├── Cargo.toml      # Project config & dependencies (like package.json in JS)
# └── src/
#     └── main.rs      # Entry point (binary) or lib.rs (library)
```

**What each file does:**
- `Cargo.toml` = Your project's configuration file — name, version, and what libraries you depend on
- `src/main.rs` = Where your program starts running — contains the `main` function
- `Cargo.lock` = Auto-generated file that locks exact dependency versions (commit this for binaries, ignore for libraries)

---

### Compiling & Running

```bash
cargo build           # Compile (debug mode — fast compile, slow runtime, extra checks)
cargo build --release # Compile (release mode — slow compile, fast runtime, optimized)
cargo run             # Compile and run in one step (most common during development)
cargo check           # Check for errors WITHOUT building (fastest — great for quick feedback)
```

**When to use each:**
- Day-to-day development: `cargo run`
- Just want to check for errors quickly: `cargo check`
- Shipping your program: `cargo build --release`

**Common first-time errors:**
```
error: could not find `Cargo.toml` in ... or any parent directory
→ You're not inside a Cargo project. Run `cargo new my_project` first,
  then `cd my_project` before running cargo commands.

error[E0425]: cannot find value `x` in this scope
→ You used a variable that hasn't been declared yet, or you made a typo.
```

---

### Hello, World!

Every Rust program starts from the `main` function. The `fn` keyword declares a function. `println!` is a **macro** (notice the `!` — that's what distinguishes macros from regular functions in Rust).

```rust
fn main() {
    println!("Hello, world!");
}
```

---

### Comments

Comments are notes for humans — the compiler ignores them completely. Write comments to explain *why* something is done, not just *what* it does (the code itself shows what).

```rust
// This is a single-line comment

/*
   Multi-line
   comment
*/

/// Doc comment — generates HTML documentation for the item below it.
/// Supports **Markdown** formatting. Put this above functions, structs, enums, etc.
fn documented_function() {}

//! Inner doc comment — documents the enclosing module or crate itself.
//! Put this at the TOP of a file to describe the whole file/module.
```

**When to comment:**
- Explain *why* you made a decision, not *what* the code does: `// Using BufReader here because the file can be gigabytes`
- Warn about non-obvious gotchas: `// Note: this intentionally truncates — values above 255 wrap around`
- Mark unfinished work: `// TODO: handle the error case here`
- Don't comment obvious things: `x += 1; // increment x` adds noise, not value

---

### Printing

In Rust, `println!` is the main way to print to the screen. The `!` means it's a macro, not a regular function. Macros are code that writes code — they're more powerful than functions and can accept a variable number of arguments with special formatting syntax.

```rust
fn main() {
    println!("Hello!");             // Print with newline
    print!("No newline ");          // Print without newline (cursor stays on same line)
    eprintln!("Error message");     // Print to stderr (standard error — for error messages)

    let name = "Rust";
    let version = 2021;
    println!("Language: {}", name);              // {} is a placeholder — replaced by the variable
    println!("Edition: {version}");              // Inline variable (Rust 1.58+) — cleaner syntax
    println!("{0} is {0}, {1} is {1}", "a", "b"); // Indexed placeholders (reuse arguments)

    // Debug printing — works with most types, useful for development
    println!("{:?}", vec![1, 2, 3]);             // [1, 2, 3]  — debug format (compact)
    println!("{:#?}", vec![1, 2, 3]);            // Pretty debug format (indented, one item per line)

    // Number formatting
    println!("{:>10}", "right");     // Right-align in a field of width 10: "     right"
    println!("{:<10}", "left");      // Left-align:  "left      "
    println!("{:^10}", "center");    // Center:      "  center  "
    println!("{:0>5}", 42);          // Zero-pad to width 5: "00042"
    println!("{:.2}", 3.14159);      // 2 decimal places: "3.14"
    println!("{:b}", 255);           // Binary:  "11111111"
    println!("{:x}", 255);           // Hex lowercase: "ff"
    println!("{:X}", 255);           // Hex uppercase: "FF"
    println!("{:o}", 255);           // Octal: "377"
}
```

**Common first-time errors:**
```
error: 1 positional argument in format string, but no arguments were given
→ You wrote {} but forgot to pass the variable: println!("{}", my_var)

error[E0277]: `MyStruct` doesn't implement `std::fmt::Display`
→ Your custom type can't be printed with {}. Use {:?} for debug printing,
  or implement the Display trait (see Traits section).
```

---

<!-- TIER 2 — CORE FUNDAMENTALS -->

## Variables & Constants

In most languages, variables are mutable by default (you can change them anytime). **Rust flips this** — variables are **immutable by default**. You have to explicitly opt in to mutability with `mut`. This forces you to think about what data actually needs to change, which prevents a whole class of bugs.

```rust
fn main() {
    // Variables are immutable by default
    let x = 5;
    // x = 6;  // ERROR: cannot assign twice to immutable variable

    // Use `mut` to make a variable mutable
    let mut y = 5;
    y = 6;  // OK — we declared it mutable

    // Type annotation — Rust usually infers the type, but you can be explicit
    let z: i32 = 10;

    // Constants — must ALWAYS have a type, always immutable, can be in global scope
    // Use SCREAMING_SNAKE_CASE by convention
    const MAX_POINTS: u32 = 100_000;   // Underscores in numbers are just for readability

    // Static variables — like constants but have a fixed memory address
    // Useful when you need to pass a reference that lives forever
    static LANGUAGE: &str = "Rust";

    // Shadowing — re-declare a variable with the same name using `let`
    let x = 5;
    let x = x + 1;      // x is now 6 — a BRAND NEW variable that shadows the old one
    let x = "hello";    // x is now a &str — the type can change with shadowing!
}
```

**`mut` vs shadowing — what's the difference?**
- `let mut x = 5; x = 6;` — same variable, same type, value changes
- `let x = 5; let x = x + 1;` — brand new variable each time, type CAN change

**Why immutable by default?**
- Prevents accidental modification of data you didn't intend to change
- Makes it easier to reason about your code — if something is `let`, it never changes
- Enables compiler optimizations (the compiler knows the value won't change)

**Key concepts:**
- `let` = declares a variable (immutable by default)
- `let mut` = declares a mutable variable
- `const` = compile-time constant (value must be known at compile time)
- `static` = a value that lives for the entire program's lifetime

---

## Data Types

Rust is **statically typed** — every variable's type must be known at compile time. But Rust is smart: it can usually *infer* the type from how you use the variable, so you don't always have to write it explicitly.

### Scalar Types

A **scalar** type represents a single value. Rust has four primary scalar types.

| Type | Size | Range / Description |
|------|------|---------------------|
| `i8` | 1 byte | -128 to 127 |
| `i16` | 2 bytes | -32,768 to 32,767 |
| `i32` | 4 bytes | -2,147,483,648 to 2,147,483,647 **(default integer)** |
| `i64` | 8 bytes | -9.2×10¹⁸ to 9.2×10¹⁸ |
| `i128` | 16 bytes | Very large range |
| `isize` | arch | Pointer-sized signed integer (32-bit on 32-bit systems, 64-bit on 64-bit systems) |
| `u8` | 1 byte | 0 to 255 |
| `u16` | 2 bytes | 0 to 65,535 |
| `u32` | 4 bytes | 0 to 4,294,967,295 |
| `u64` | 8 bytes | 0 to 1.8×10¹⁹ |
| `u128` | 16 bytes | Very large range |
| `usize` | arch | Pointer-sized unsigned integer **(used for collection indexing)** |
| `f32` | 4 bytes | Single-precision float (less precise) |
| `f64` | 8 bytes | Double-precision float **(default float)** |
| `bool` | 1 byte | `true` or `false` |
| `char` | 4 bytes | A single Unicode character — `'a'`, `'Z'`, `'🦀'` |

**How to pick an integer type:**
- Use `i32` for most whole numbers — it's the default and works for almost everything
- Use `usize` when indexing into collections (it's what Rust expects)
- Use `u8` for raw byte data (e.g., file contents)
- Use `i64` or `u64` for very large numbers (timestamps, file sizes)
- The `i` prefix = signed (can be negative), `u` prefix = unsigned (0 and positive only)

```rust
fn main() {
    // Integer literals — multiple ways to write them
    let decimal = 98_222;       // Underscores are ignored — just for readability: 98222
    let hex = 0xff;             // Hexadecimal: 255
    let octal = 0o77;           // Octal: 63
    let binary = 0b1111_0000;  // Binary: 240
    let byte = b'A';            // Byte literal (u8 only): 65

    // Floats — always use f64 unless you have a specific reason for f32
    let f1 = 2.0;              // f64 (default)
    let f2: f32 = 3.0;         // f32 — less precise, avoid unless memory-critical

    // Bool — strictly true or false (no "truthy" values like in Python/JS)
    let t = true;
    let f: bool = false;

    // Char — uses single quotes, NOT double quotes (double quotes are for strings)
    let c = 'z';
    let heart = '❤';
    let crab = '🦀';           // Full Unicode support — emojis are valid chars!
}
```

**Key concepts:**
- **Integer overflow in debug mode:** In debug builds, Rust panics (crashes) if you overflow an integer. In release mode it wraps around silently. This is intentional — Rust catches it for you during development.
- **No implicit type coercion:** `let x: i32 = 5; let y: i64 = x;` is an **ERROR** in Rust. Unlike C or Java, you must explicitly convert types. This prevents subtle bugs.
- **Prefer `f64` over `f32`:** `f32` loses precision very quickly — use `f64` unless you have a good reason not to.

---

### Compound Types

**Compound types** group multiple values into one type.

```rust
fn main() {
    // Tuples — fixed-length, can hold different types
    // Think of a tuple as a lightweight struct where fields are accessed by position
    let tup: (i32, f64, u8) = (500, 6.4, 1);
    let (x, y, z) = tup;            // Destructuring — unpack all at once
    let first = tup.0;              // Access by index (0-based)
    let second = tup.1;

    // Unit type — empty tuple (), represents "no value" / "void"
    // Functions that don't explicitly return anything return ()
    let unit: () = ();

    // Arrays — fixed-length, same type, stored on the STACK (not the heap)
    // Arrays in Rust are NOT growable — use Vec if you need dynamic size
    let arr = [1, 2, 3, 4, 5];
    let first = arr[0];             // Access by index (panics if out of bounds!)
    let len = arr.len();            // Length: 5

    let zeros = [0; 5];             // [0, 0, 0, 0, 0] — repeat syntax: [value; count]
    let arr: [i32; 5] = [1, 2, 3, 4, 5];  // Explicit type [element_type; length]

    // Slices — a view (window) into an array or Vec — doesn't own the data
    let slice = &arr[1..3];         // [2, 3] — elements at index 1 and 2 (exclusive end)
    let slice = &arr[..2];          // [1, 2] — from start up to (not including) index 2
    let slice = &arr[3..];          // [4, 5] — from index 3 to end
    let slice = &arr[..];           // [1, 2, 3, 4, 5] — everything (full slice)
}
```

**Arrays vs Vec:**
- **Array** (`[T; N]`) = fixed size, stack-allocated, size known at compile time. Use when you know exactly how many elements you'll have.
- **Vec** (`Vec<T>`) = growable, heap-allocated. Use when the size might change or isn't known at compile time. (See Collections section.)

---

### Type Casting

Rust has **no implicit type conversion**. You must explicitly cast with the `as` keyword. This is a deliberate design choice — silent conversions in C and Java have caused countless bugs.

```rust
fn main() {
    let x: i32 = 42;
    let y: f64 = x as f64;          // Widen: i32 → f64 (always safe, no data loss)
    let z: u8 = x as u8;            // Narrow: i32 → u8 (may TRUNCATE if value > 255!)

    let c: char = 65u8 as char;     // 65 → 'A' (ASCII)
    let n: u8 = 'A' as u8;          // 'A' → 65

    // Gotcha: narrowing can lose data silently with `as`
    let big: i32 = 300;
    let small: u8 = big as u8;      // 300 % 256 = 44 — wraps around!
    println!("{small}");             // Prints 44, not 300!
}
```

> **Gotcha:** Rust has no implicit type coercion. You must explicitly cast with `as`. This is intentional — it prevents subtle bugs from unexpected conversions. Be careful with narrowing casts (going to a smaller type) — they silently truncate.

---

## Operators

### Arithmetic

| Operator | Description | Example |
|----------|-------------|---------|
| `+` | Addition | `5 + 3` → `8` |
| `-` | Subtraction | `5 - 3` → `2` |
| `*` | Multiplication | `5 * 3` → `15` |
| `/` | Division | `7 / 2` → `3` (integer division — truncates!) |
| `%` | Remainder (modulo) | `7 % 2` → `1` |

**Integer division truncates toward zero** — it throws away the decimal part. `7 / 2` is `3`, not `3.5`. For float division, at least one operand must be a float: `7.0 / 2.0` → `3.5`.

**Common uses of the `%` (modulo) operator:**
```rust
n % 2 == 0      // Check if n is even
n % 10          // Get the last digit of n
index % len     // Wrap an index around (cycle through a list)
```

> **Note:** Rust does **NOT** have `++` or `--` operators like C/Java. Use `x += 1` and `x -= 1` instead.

---

### Comparison

| Operator | Description |
|----------|-------------|
| `==` | Equal to |
| `!=` | Not equal to |
| `<` | Less than |
| `>` | Greater than |
| `<=` | Less than or equal to |
| `>=` | Greater than or equal to |

> **Important:** You can only compare values of the **same type**. `5 == 5.0` is a **compile error** in Rust — you'd need to cast first: `5 as f64 == 5.0`.

---

### Logical

| Operator | Description |
|----------|-------------|
| `&&` | Logical AND — true only if BOTH sides are true (short-circuits: stops at first false) |
| `\|\|` | Logical OR — true if EITHER side is true (short-circuits: stops at first true) |
| `!` | Logical NOT — flips true to false and vice versa |

**Short-circuit evaluation** means the right side is NOT evaluated if the left side already determines the result. This is useful: `if list.len() > 0 && list[0] == 5` — the second part is only checked if the first is true.

---

### Bitwise

| Operator | Description |
|----------|-------------|
| `&` | Bitwise AND — each bit is 1 only if both bits are 1 |
| `\|` | Bitwise OR — each bit is 1 if either bit is 1 |
| `^` | Bitwise XOR — each bit is 1 if exactly one bit is 1 |
| `!` | Bitwise NOT (for integers) — flips every bit |
| `<<` | Left shift — multiply by powers of 2 |
| `>>` | Right shift — divide by powers of 2 |

Bitwise operators work on the individual bits of integers. Commonly used in low-level programming, flags/bitmasks, and graphics.

---

### Compound Assignment

```rust
let mut x = 10;
x += 5;   // x = x + 5  →  15
x -= 3;   // x = x - 3  →  12
x *= 2;   // x = x * 2  →  24
x /= 4;   // x = x / 4  →   6
x %= 3;   // x = x % 3  →   0
```

---

### Operator Precedence (high to low)

```
()                          // Parentheses — always evaluated first
- ! (unary)                 // Unary minus, logical NOT
* / %                       // Multiply, divide, remainder
+ -                         // Add, subtract
<< >>                       // Bit shifts
&                           // Bitwise AND
^                           // Bitwise XOR
|                           // Bitwise OR
== != < > <= >=             // Comparison
&&                          // Logical AND
||                          // Logical OR
= += -= *= /= %=            // Assignment (right to left)
```

```rust
// Examples:
2 + 3 * 4        // 14, not 20 (* before +)
(2 + 3) * 4      // 20 (parentheses first)
true || false && false  // true (&&  before ||)
```

> **Tip:** When in doubt, use parentheses to make the intent clear. `(a + b) * c` is always clearer than relying on precedence rules.

---

<!-- TIER 3 — CONTROL FLOW -->

## Control Flow

### If Expressions

`if` in Rust works like other languages but with two key differences: **no parentheses** around the condition, and **`if` is an expression** — it returns a value.

```rust
fn main() {
    let number = 7;

    // Basic if/else — no parentheses around the condition (unlike C/Java)
    if number > 5 {
        println!("Greater than 5");
    } else if number > 0 {
        println!("Between 1 and 5");
    } else {
        println!("Zero or negative");
    }

    // if is an EXPRESSION — it returns a value (like a ternary operator in other languages)
    // Both branches must return the same type
    let result = if number > 5 { "big" } else { "small" };

    // The condition MUST be a bool — Rust has no "truthy" values
    // if 1 { ... }  // ERROR: expected bool, found integer
    // if "hello" { ... }  // ERROR: expected bool, found &str
}
```

**Common first-time errors:**
```
error[E0308]: mismatched types
→ if true { 1 } else { "hello" }
  Both arms of an if expression must return the same type.

error[E0308]: expected `bool`, found integer
→ if 1 { ... }
  Rust requires an actual bool condition. Use: if x != 0 { ... }
```

---

### Loops

Rust has three loop types: `loop` (infinite), `while` (condition-based), and `for` (iterator-based). **`for` is the most idiomatic** and should be your default choice.

```rust
fn main() {
    // loop — infinite loop (like `while true` but cleaner)
    // Can return a value using `break value`
    let mut counter = 0;
    let result = loop {
        counter += 1;
        if counter == 10 {
            break counter * 2;  // `break` with a value — result gets this value
        }
    };
    // result is 20

    // Loop labels — name a loop so you can break/continue an OUTER loop from inside a nested one
    'outer: loop {
        'inner: loop {
            break 'outer;  // Break out of the outer loop, not just the inner one
        }
    }

    // while loop — repeat as long as condition is true
    let mut n = 3;
    while n != 0 {
        println!("{n}");
        n -= 1;
    }

    // for loop — the most common and safest loop in Rust
    // Ranges: 0..5 means 0, 1, 2, 3, 4 (exclusive end)
    for i in 0..5 {
        println!("{i}");       // 0, 1, 2, 3, 4
    }

    // 0..=5 means 0, 1, 2, 3, 4, 5 (inclusive end — note the =)
    for i in 0..=5 {
        println!("{i}");       // 0, 1, 2, 3, 4, 5
    }

    // Iterate over a collection — Rust automatically borrows it
    let arr = [10, 20, 30];
    for element in arr {
        println!("{element}");
    }

    // With index — use .enumerate() to get (index, value) pairs
    for (index, value) in arr.iter().enumerate() {
        println!("{index}: {value}");
    }

    // Reverse — use .rev() on a range
    for i in (1..4).rev() {
        println!("{i}");       // 3, 2, 1
    }
}
```

**When to use which loop:**
- `for` — when you know the collection or range to iterate over (use this 90% of the time)
- `while` — when you want to loop until a condition changes
- `loop` — when you need an infinite loop or want to return a value from the loop

> **Gotcha:** `0..5` is exclusive (0 to 4). Use `0..=5` for inclusive (0 to 5). This trips up many beginners coming from other languages.

---

### While Let

`while let` is a convenient way to loop while a pattern matches — commonly used with `Option` and iterators.

```rust
fn main() {
    let mut stack = vec![1, 2, 3];

    // Loop while pop() returns Some(value) — stops when the Vec is empty (returns None)
    while let Some(top) = stack.pop() {
        println!("{top}");     // 3, 2, 1
    }
    // Equivalent to a while loop that manually checks if pop() returned Some
}
```

---

<!-- TIER 4 — FUNCTIONS -->

## Functions

Functions are reusable blocks of code. In Rust, the `fn` keyword declares a function. All function and variable names use `snake_case` by convention (no camelCase).

```rust
// Basic function — no parameters, no return value
fn greet() {
    println!("Hello!");
}

// With parameters — types MUST be specified (Rust doesn't infer parameter types)
fn add(a: i32, b: i32) -> i32 {
    a + b    // No semicolon = this is an EXPRESSION, and its value is returned implicitly
}

// Explicit return — use `return` keyword for early exits
fn absolute(x: i32) -> i32 {
    if x < 0 {
        return -x;    // Early return — exits the function immediately
    }
    x                 // Last expression (no semicolon) is returned implicitly
}

// Multiple return values — use a tuple
fn swap(a: i32, b: i32) -> (i32, i32) {
    (b, a)
}

fn main() {
    greet();
    let sum = add(3, 5);               // 8
    let (x, y) = swap(1, 2);           // x=2, y=1
}
```

**Key concepts:**
- Parameter types are **always required** — Rust won't infer them
- Return type is written after `->`: `fn name(params) -> ReturnType`
- Functions that don't return a value implicitly return `()` (the unit type — Rust's version of "void")
- **Last expression = return value:** The final expression in a function body is automatically returned if there's NO semicolon at the end
- **Semicolon turns an expression into a statement:** Adding `;` makes it return `()` instead of the value

```rust
fn returns_five() -> i32 {
    5           // Returns 5 (expression — no semicolon)
}

fn returns_nothing() -> i32 {
    // 5;       // ERROR: this returns () but the function expects i32
    5           // Correct
}

// The semicolon rule in action:
fn add(a: i32, b: i32) -> i32 {
    a + b       // ✓ returns a + b
    // a + b;   // ✗ would return (), causing a type error
}
```

**Common first-time errors:**
```
error[E0308]: mismatched types — expected `i32`, found `()`
→ You likely added a semicolon to the last expression, turning it into a statement.
  Remove the semicolon from the last line.

error[E0425]: cannot find function `myFunction`
→ Rust uses snake_case. Try `my_function` instead.
```

---

<!-- TIER 5 — OWNERSHIP & BORROWING -->

## Ownership & Borrowing

This is Rust's most unique and important feature. It's what makes Rust both safe AND fast — no garbage collector needed. It takes time to get used to, but once it clicks, it makes complete sense.

**The problem Rust solves:** In languages like C, you manually manage memory (easy to forget, causing leaks or crashes). In languages like Java/Python, a garbage collector manages memory for you (safe, but adds overhead and pauses). Rust takes a third approach: the **ownership system** enforces memory safety at compile time with zero runtime cost.

---

### Ownership Rules

These three rules are the entire ownership system:

1. Each value has exactly **one owner** (a variable)
2. When the owner goes **out of scope**, the value is **automatically freed** (no manual `free()`)
3. There can only be **one owner at a time** — ownership can be transferred (moved)

```rust
fn main() {
    // Simple types (integers, bools, chars) live on the STACK — they're COPIED automatically
    let x = 5;
    let y = x;               // x is COPIED — both x and y are valid
    println!("{x} {y}");     // OK: 5 5

    // String lives on the HEAP — it's MOVED, not copied
    let s1 = String::from("hello");
    let s2 = s1;              // s1 is MOVED to s2 — s1 is no longer valid!
    // println!("{s1}");      // ERROR: value used after move
    println!("{s2}");         // OK

    // Clone for a deep copy (explicit and intentional — this costs memory)
    let s3 = String::from("hello");
    let s4 = s3.clone();     // s3 is still valid — we made a full copy
    println!("{s3} {s4}");   // OK: both are valid
}
```

**Why move semantics?**

Think of it like a physical contract for a house. When you "assign" a String to a new variable, you're transferring the ownership contract. The old variable can't use the house anymore — there's only one owner at a time. This guarantees that memory is only freed once, preventing double-free bugs.

**Stack vs Heap:**
- **Stack:** Fast, fixed-size values (integers, booleans, chars, arrays). Automatically cleaned up.
- **Heap:** Dynamic-size values (Strings, Vecs). Must be explicitly freed. Rust does this automatically when the owner goes out of scope.

**Types that are Copy (live on stack):** `i32`, `u8`, `f64`, `bool`, `char`, tuples of Copy types. These are always copied, not moved.

---

### Borrowing (References)

Moving ownership all the time would be tedious. Instead, you can **borrow** a value temporarily using **references** (`&`). A reference lets you use a value without taking ownership — like borrowing a book from a friend; you give it back when you're done.

```rust
fn main() {
    let s = String::from("hello");

    // Immutable reference (&) — borrow without taking ownership
    let len = calculate_length(&s);    // Pass a reference (borrow s)
    println!("{s} has length {len}");  // s is STILL valid! We only borrowed it

    // Mutable reference (&mut) — borrow and allow modification
    let mut s = String::from("hello");
    change(&mut s);
    println!("{s}");                   // "hello, world"
}

fn calculate_length(s: &String) -> usize {
    s.len()
    // s goes out of scope here, but since it's just a reference,
    // the actual String is NOT freed — the original owner still has it
}

fn change(s: &mut String) {
    s.push_str(", world");
}
```

---

### Borrowing Rules

These rules prevent data races at compile time:

1. You can have **either** (not both simultaneously):
   - Any number of **immutable** references (`&T`) — multiple readers is fine
   - Exactly **ONE mutable** reference (`&mut T`) — exclusive writer access
2. References must **always be valid** — you cannot have a reference to a value that's been freed

```rust
fn main() {
    let mut s = String::from("hello");

    let r1 = &s;        // OK — immutable borrow
    let r2 = &s;        // OK — another immutable borrow (multiple readers allowed)
    // let r3 = &mut s;  // ERROR: can't borrow as mutable while immutable borrows exist
    println!("{r1} {r2}");
    // r1 and r2 are no longer used after this line (NLL — Non-Lexical Lifetimes)
    // So now we CAN create a mutable borrow:

    let r3 = &mut s;    // OK — no immutable borrows are active anymore
    println!("{r3}");
}
```

> **Why these rules?** They prevent **data races** — a class of bug where two parts of code access the same memory simultaneously, one of them writing. These bugs are notoriously hard to find. Rust eliminates them entirely at compile time. The rule: if someone is reading data, nobody can be changing it at the same time.

**Common first-time errors:**
```
error[E0382]: borrow of moved value
→ You moved a value (e.g., passed it to a function) and then tried to use it again.
  Fix: use & to borrow instead of move, or .clone() to make a copy.

error[E0596]: cannot borrow `x` as mutable, as it is not declared as mutable
→ You tried to modify a variable declared with `let` instead of `let mut`.
```

---

## Strings

Rust has two string types, which confuses beginners at first. Understanding when to use each is important.

| Type | Description | Where stored | Mutable | Owned? |
|------|-------------|--------------|---------|--------|
| `String` | Owned, growable string | Heap | Yes | Yes |
| `&str` | Borrowed string slice (view into string data) | Stack/Heap/Binary | No | No |

**Simple rule:** Use `String` when you need to build, grow, or own a string. Use `&str` in function parameters (accepts both). String literals like `"hello"` are `&str`.

```rust
fn main() {
    // String — owned, heap-allocated, growable
    let mut s = String::new();                    // Empty String
    let s = String::from("hello");                // From a literal
    let s = "hello".to_string();                  // Same thing

    // &str — borrowed string slice
    let slice: &str = "hello";                    // String literal (stored in program binary)
    let slice: &str = &s[0..3];                   // Slice of a String: "hel"
    let slice: &str = &s;                         // Whole String as a slice

    // Building strings
    let mut s = String::from("hello");
    s.push(' ');                                  // Append a single char
    s.push_str("world");                          // Append a &str
    println!("{s}");                              // "hello world"

    // Concatenation with + — takes ownership of left side (s1 is moved!)
    let s1 = String::from("hello ");
    let s2 = String::from("world");
    let s3 = s1 + &s2;                           // s1 is MOVED, s2 is borrowed
    // println!("{s1}");                          // ERROR: s1 was moved into s3

    // format! macro — cleaner, doesn't take ownership of anything
    let s1 = String::from("hello");
    let s2 = String::from("world");
    let s3 = format!("{s1} {s2}");               // Both s1 and s2 are still valid

    // Common methods
    let s = String::from("Hello, World!");
    println!("{}", s.len());                      // 13 (byte length, NOT character count!)
    println!("{}", s.is_empty());                 // false
    println!("{}", s.contains("World"));          // true
    println!("{}", s.starts_with("Hello"));       // true
    println!("{}", s.ends_with("!"));             // true
    println!("{}", s.to_uppercase());             // "HELLO, WORLD!"
    println!("{}", s.to_lowercase());             // "hello, world!"
    println!("{}", s.trim());                     // Removes leading and trailing whitespace
    println!("{}", s.replace("World", "Rust"));   // "Hello, Rust!"

    // Iterating over characters
    for c in "hello".chars() {
        println!("{c}");
    }

    // Split into a collection
    let parts: Vec<&str> = "a,b,c".split(',').collect();  // ["a", "b", "c"]

    // Parse string to number
    let n: i32 = "42".parse().unwrap();           // 42
    let n: f64 = "3.14".parse().unwrap();         // 3.14
}
```

**Key concepts:**
- **`.len()` returns BYTES, not characters.** For ASCII text this is the same, but "hello🦀".len() is 9, not 6 (the crab emoji is 4 bytes).
- **You cannot index a String** with `s[0]` — this is a compile error. Rust prevents this because characters can be multi-byte. Use `.chars()` to iterate, or `s.chars().nth(0)` to get a specific character.
- **`&str` is just a view** into string data that lives somewhere else. It's always borrowed. You can't keep it alive longer than the data it points to.

**Common first-time errors:**
```
error[E0308]: mismatched types — expected `&str`, found `String`
→ Use &my_string to convert a String to &str, or call my_string.as_str()

error[E0277]: the type `String` cannot be indexed by `{integer}`
→ s[0] is not allowed. Use s.chars().nth(0) or s.as_bytes()[0] for bytes.
```

---

<!-- TIER 6 — COLLECTIONS -->

## Collections

### Vec (Vector)

A `Vec<T>` is a growable array — the most commonly used collection in Rust. It stores elements of the same type on the heap and automatically grows when you add more elements.

```rust
fn main() {
    // Creating vectors
    let v: Vec<i32> = Vec::new();           // Empty vector (type annotation required since it's empty)
    let v = vec![1, 2, 3];                  // vec! macro with initial values — most common
    let v = vec![0; 5];                     // [0, 0, 0, 0, 0] — five zeros

    // Adding elements (Vec must be mutable)
    let mut v = Vec::new();
    v.push(1);
    v.push(2);
    v.push(3);

    // Accessing elements
    let third = v[2];                       // Direct index — panics if out of bounds!
    let third = v.get(2);                   // Returns Option<&T> — safe, returns None if missing

    // Safe access pattern using match
    match v.get(2) {
        Some(value) => println!("Third: {value}"),
        None => println!("No third element"),
    }

    // Common methods
    v.len();                                // Number of elements
    v.is_empty();                           // true if len() == 0
    v.contains(&2);                         // true if value exists in Vec
    v.pop();                                // Remove AND return last element (Option<T>)
    v.remove(0);                            // Remove at index (shifts all later elements left — slow!)
    v.insert(0, 10);                        // Insert at index (shifts all later elements right — slow!)
    v.sort();                               // Sort in place (ascending)
    v.reverse();                            // Reverse order in place
    v.dedup();                              // Remove consecutive duplicates (sort first for all duplicates)

    // Iterating — use & to borrow the Vec (so you don't consume it)
    let v = vec![1, 2, 3];
    for val in &v {                         // Immutable borrow — v is still usable after
        println!("{val}");
    }

    let mut v = vec![1, 2, 3];
    for val in &mut v {                     // Mutable borrow — can modify elements
        *val += 10;                         // * = dereference (reach through the reference to modify)
    }
    // v is now [11, 12, 13]

    // Slicing — a &[T] slice of part of a Vec
    let slice = &v[1..3];                   // &[i32] — elements at index 1 and 2
}
```

**`v[i]` vs `v.get(i)` — which to use?**
- `v[i]` — panics (crashes) if `i` is out of bounds. Use when you're certain the index is valid.
- `v.get(i)` — returns `Option<&T>`, never panics. Use when the index might be invalid.

---

### HashMap

A `HashMap<K, V>` stores key-value pairs. Looking up a value by key is very fast (O(1) on average). Think of it like a dictionary: you look up a definition (value) by its word (key).

```rust
use std::collections::HashMap;

fn main() {
    // Creating — note: you must `use` it at the top (not in std::prelude)
    let mut scores = HashMap::new();
    scores.insert(String::from("Alice"), 100);
    scores.insert(String::from("Bob"), 85);

    // From two parallel iterators using zip
    let keys = vec!["Alice", "Bob"];
    let values = vec![100, 85];
    let scores: HashMap<_, _> = keys.into_iter().zip(values.into_iter()).collect();

    // Accessing — returns Option<&V>
    let score = scores.get("Alice");        // Some(&100) or None
    let score = scores["Alice"];            // Panics if key missing! (like Vec indexing)

    // Check if key exists
    if scores.contains_key("Alice") {
        println!("Found Alice");
    }

    // Insert only if key doesn't exist — very common pattern
    scores.entry("Charlie".to_string()).or_insert(90);
    // If "Charlie" doesn't exist, inserts 90. If it does exist, does nothing.

    // Count word frequencies — a classic HashMap pattern
    let text = "hello world hello rust";
    let mut word_count = HashMap::new();
    for word in text.split_whitespace() {
        let count = word_count.entry(word).or_insert(0);  // Get or create with default 0
        *count += 1;                                        // Increment through the mutable reference
    }
    // word_count: {"hello": 2, "world": 1, "rust": 1}

    // Iterating — order is NOT guaranteed (HashMap is unordered)
    for (key, value) in &scores {
        println!("{key}: {value}");
    }

    // Remove
    scores.remove("Bob");

    // Length
    println!("{}", scores.len());
}
```

**Key concepts:**
- **Ownership:** When you insert a `String` key or value into a HashMap, ownership is moved in — the original variable is no longer valid. Use references or `.clone()` if you need to keep using them.
- **Order:** HashMap does NOT preserve insertion order. Use `BTreeMap` if you need sorted keys, or `IndexMap` (external crate) for insertion order.
- **`entry()` API:** The `.entry().or_insert()` pattern is the idiomatic way to update-or-insert without doing two lookups.

---

### HashSet

A `HashSet<T>` stores unique values — no duplicates allowed. It's like a HashMap but with only keys and no values. Use it when you only care about membership (is this value in the set?).

```rust
use std::collections::HashSet;

fn main() {
    let mut set = HashSet::new();
    set.insert(1);
    set.insert(2);
    set.insert(3);
    set.insert(2);                          // Duplicate — silently ignored

    println!("{}", set.len());              // 3 (not 4, because 2 was a duplicate)
    println!("{}", set.contains(&2));       // true

    set.remove(&2);

    // Mathematical set operations
    let a: HashSet<i32> = [1, 2, 3].into();
    let b: HashSet<i32> = [2, 3, 4].into();

    let union: HashSet<_> = a.union(&b).collect();              // {1, 2, 3, 4} — everything
    let intersection: HashSet<_> = a.intersection(&b).collect(); // {2, 3} — only in both
    let difference: HashSet<_> = a.difference(&b).collect();     // {1} — in a but not b
    let sym_diff: HashSet<_> = a.symmetric_difference(&b).collect(); // {1, 4} — in one but not both
}
```

**When to use which collection:**
- `Vec<T>` — ordered list, fast random access by index, allows duplicates. Your default choice.
- `HashMap<K, V>` — key-value lookup, unordered. Use when you need to find things by a key.
- `HashSet<T>` — unique values, fast membership check. Use when duplicates don't make sense.
- `BTreeMap<K, V>` / `BTreeSet<T>` — like HashMap/HashSet but keys are always sorted.
- `VecDeque<T>` — fast push/pop from both ends (queue/deque).

---

<!-- TIER 7 — STRUCTS & ENUMS -->

## Structs

A **struct** groups related pieces of data together under one name. It's like a custom data type you define yourself. If you've used classes in Java/Python, think of structs as the data part of a class (without methods yet — those come in `impl` blocks).

```rust
// Define a struct — each field has a name and type
struct User {
    username: String,
    email: String,
    active: bool,
    sign_in_count: u64,
}

fn main() {
    // Create an instance — must initialize ALL fields
    let user1 = User {
        username: String::from("alice"),
        email: String::from("alice@example.com"),
        active: true,
        sign_in_count: 1,
    };

    // Access fields with dot notation
    println!("{}", user1.username);

    // Mutable instance — in Rust, the ENTIRE struct is either mutable or not
    // (you can't make individual fields mutable separately)
    let mut user2 = User {
        username: String::from("bob"),
        email: String::from("bob@example.com"),
        active: true,
        sign_in_count: 1,
    };
    user2.email = String::from("new@example.com");  // OK — user2 is mut

    // Struct update syntax — create a new struct from an existing one
    // Changes only what you specify, copies the rest from user1
    let user3 = User {
        email: String::from("charlie@example.com"),
        ..user1    // All remaining fields come from user1
        // NOTE: if any of those fields are String (not Copy), user1 is partially moved!
    };
}

// Field init shorthand — when the variable name matches the field name, you can omit the field name
fn build_user(username: String, email: String) -> User {
    User {
        username,           // shorthand for username: username
        email,              // shorthand for email: email
        active: true,
        sign_in_count: 1,
    }
}
```

---

### Tuple Structs & Unit Structs

```rust
// Tuple structs — a struct with no named fields, just types
// Useful when you want distinct types for similar data (prevents mixing them up)
struct Color(i32, i32, i32);
struct Point(f64, f64, f64);

// Even though both hold 3 numbers, Color and Point are DIFFERENT types
// You can't accidentally pass a Color where a Point is expected
let black = Color(0, 0, 0);
let origin = Point(0.0, 0.0, 0.0);
println!("{}", black.0);    // Access by position index

// Unit struct — no fields at all. Useful for implementing traits on a type with no data
struct AlwaysEqual;
```

---

### Methods (impl blocks)

Methods are functions attached to a struct. You define them inside an `impl` block. The first parameter is always `self` (the instance) — this is what makes it a method instead of a regular function.

```rust
struct Rectangle {
    width: f64,
    height: f64,
}

impl Rectangle {
    // Associated function (like a "static method" in Java) — no &self parameter
    // Called with Rectangle::new(...) syntax, NOT on an instance
    fn new(width: f64, height: f64) -> Self {
        Self { width, height }   // Self = Rectangle (the type you're implementing)
    }

    fn square(size: f64) -> Self {
        Self { width: size, height: size }
    }

    // Method — &self means "borrow the instance immutably" (just reading)
    fn area(&self) -> f64 {
        self.width * self.height
    }

    fn perimeter(&self) -> f64 {
        2.0 * (self.width + self.height)
    }

    // &mut self — "borrow the instance mutably" (modifying fields)
    fn scale(&mut self, factor: f64) {
        self.width *= factor;
        self.height *= factor;
    }

    // self — "consume the instance" (take ownership, the original is gone after this call)
    fn into_square(self) -> Rectangle {
        let side = self.width.max(self.height);
        Rectangle { width: side, height: side }
    }
}

fn main() {
    let r = Rectangle::new(10.0, 5.0);      // Associated function — called with ::
    println!("Area: {}", r.area());          // Method — called with .
    println!("Perimeter: {}", r.perimeter());

    let mut r = Rectangle::new(10.0, 5.0);
    r.scale(2.0);                            // Mutable method — r must be `mut`

    let sq = Rectangle::square(5.0);        // Another associated function
}
```

**`&self` vs `&mut self` vs `self` — when to use each:**
- `&self` — reading only, most common. The instance is still usable after the call.
- `&mut self` — modifying the instance. The instance must be declared `mut`.
- `self` — consuming the instance. Rare. The instance is gone after the call (transforms into something else).

---

### Deriving Traits

The `#[derive(...)]` attribute automatically implements common traits for your struct. This is how you give your struct the ability to be printed, cloned, compared, etc.

```rust
#[derive(Debug, Clone, PartialEq)]
struct Point {
    x: f64,
    y: f64,
}

fn main() {
    let p = Point { x: 1.0, y: 2.0 };
    println!("{:?}", p);             // Debug printing: Point { x: 1.0, y: 2.0 }
    println!("{:#?}", p);            // Pretty debug: formatted with newlines and indentation

    let p2 = p.clone();             // Clone: make a copy (requires #[derive(Clone)])
    println!("{}", p == p2);        // PartialEq comparison: true (requires #[derive(PartialEq)])
}
```

**Common derivable traits:**
- `Debug` — enables `{:?}` printing. **Derive this on almost every struct you make.**
- `Clone` — enables `.clone()` for deep copies
- `PartialEq` — enables `==` and `!=` comparison
- `PartialOrd` — enables `<`, `>`, `<=`, `>=` comparison
- `Hash` — enables using the struct as a HashMap key
- `Default` — provides `Struct::default()` with zero/empty values

---

## Enums

An **enum** (enumeration) defines a type that can be one of several variants. Unlike enums in C or Java, Rust enums can carry data inside each variant — making them extremely powerful. Rust's enums are what many languages call "algebraic data types" or "tagged unions."

```rust
// Basic enum — each variant is just a name (no data)
enum Direction {
    North,
    South,
    East,
    West,
}

// Enum with data — each variant can hold different types and amounts of data
enum Message {
    Quit,                          // No data
    Move { x: i32, y: i32 },      // Named fields (like a struct)
    Write(String),                 // Single value (like a tuple struct)
    ChangeColor(i32, i32, i32),   // Multiple values
}

fn main() {
    let dir = Direction::North;
    let msg = Message::Write(String::from("hello"));
    let msg = Message::Move { x: 10, y: 20 };
}

// Enums can have methods too, just like structs
impl Message {
    fn call(&self) {
        // Use match to handle each variant differently (see Pattern Matching)
    }
}
```

**Why are Rust enums so powerful?**

Instead of having a separate `null` value that can sneak in anywhere, Rust uses enums to explicitly model "this might not have a value" or "this operation might fail." You're forced to handle all cases.

---

### Option — Rust's Null Alternative

Rust has **no `null`**. Instead, it uses `Option<T>` to represent values that might not exist. This eliminates null pointer exceptions entirely — the compiler forces you to handle the "no value" case before you can use the value.

```rust
// Option is defined in the standard library as:
enum Option<T> {
    Some(T),    // A value exists — holds the value
    None,       // No value — like null, but safe
}

fn main() {
    let some_number: Option<i32> = Some(5);
    let no_number: Option<i32> = None;

    // You CANNOT use an Option<i32> directly as an i32
    // let x: i32 = some_number;  // ERROR — you must "unwrap" it first

    // Method 1: match — explicitly handle both cases
    match some_number {
        Some(n) => println!("Got: {n}"),
        None => println!("Got nothing"),
    }

    // Method 2: if let — when you only care about the Some case
    if let Some(n) = some_number {
        println!("Got: {n}");
    }

    // Method 3: Common Option methods
    let x: Option<i32> = Some(5);
    x.unwrap();              // 5 — extracts the value, PANICS if None! (avoid in production)
    x.unwrap_or(0);          // 5 — if None, returns 0 instead of panicking
    x.unwrap_or_default();   // 5 — if None, uses the type's default value (0 for i32)
    x.is_some();             // true — check without unwrapping
    x.is_none();             // false
    x.map(|n| n * 2);       // Some(10) — transform the inner value if it exists

    let y: Option<i32> = None;
    y.unwrap_or(0);                          // 0 — safe fallback
    y.unwrap_or_else(|| compute_default());  // Lazy fallback — only calls the closure if None
}
```

> **Key insight:** `Option<T>` forces you to consciously decide what to do when there's no value. In Java, a `null` can silently cause a NullPointerException anywhere. In Rust, the compiler won't let you use an `Option<T>` as a `T` — you must handle both cases.

---

<!-- TIER 8 — PATTERN MATCHING -->

## Pattern Matching

### match

`match` is Rust's most powerful control flow construct. It's like a `switch` statement on steroids — it works on any type, can destructure values, must handle every possible case (it's **exhaustive**), and is an expression that returns a value.

```rust
fn main() {
    let x = 5;

    match x {
        1 => println!("one"),
        2 => println!("two"),
        3 | 4 => println!("three or four"),     // | means "or" — match multiple patterns
        5..=10 => println!("five through ten"),  // Range pattern (inclusive)
        _ => println!("something else"),         // _ is the wildcard — matches everything else
        // If you remove this line, the compiler gives an error: "non-exhaustive patterns"
    }

    // match is an EXPRESSION — you can use its result directly
    let text = match x {
        1 => "one",
        2 => "two",
        _ => "other",
    };

    // Matching enums with data — extracts the data from each variant
    enum Coin {
        Penny,
        Nickel,
        Dime,
        Quarter(String),  // Quarter has an associated state name
    }

    fn value_in_cents(coin: &Coin) -> u32 {
        match coin {
            Coin::Penny => 1,
            Coin::Nickel => 5,
            Coin::Dime => 10,
            Coin::Quarter(state) => {     // Bind the inner String to `state`
                println!("Quarter from {state}");
                25
            }
        }
    }

    // Destructuring structs in match
    struct Point { x: i32, y: i32 }
    let p = Point { x: 0, y: 7 };

    match p {
        Point { x: 0, y } => println!("On y-axis at {y}"),   // x must be 0, y is bound
        Point { x, y: 0 } => println!("On x-axis at {x}"),   // y must be 0, x is bound
        Point { x, y } => println!("At ({x}, {y})"),          // Anything else
    }

    // Match guards — add extra conditions with `if` after the pattern
    let num = Some(4);
    match num {
        Some(x) if x < 5 => println!("Less than 5: {x}"),
        Some(x) => println!("{x}"),
        None => (),
    }
}
```

**Why exhaustiveness matters:** If you add a new variant to an enum, every `match` on that enum will fail to compile until you handle the new variant. This means you can never accidentally forget to handle a new case — the compiler reminds you everywhere that needs to be updated.

---

### if let / let else

When you only care about ONE variant of an enum (not all of them), a full `match` is verbose. `if let` is the shorthand.

```rust
fn main() {
    let value: Option<i32> = Some(42);

    // if let — "if this pattern matches, do this"
    // Equivalent to a match with one arm and a catch-all
    if let Some(n) = value {
        println!("Got {n}");
    } else {
        println!("Got nothing");
    }

    // let else — "bind this pattern or exit" (Rust 1.65+)
    // Useful for early returns when a value isn't what you expect
    let Some(n) = value else {
        println!("Got nothing");
        return;   // Must diverge: return, break, continue, or panic!
    };
    println!("Got {n}");    // n is available here — this code only runs if value was Some
}
```

**`if let` vs `match`:**
- Use `match` when you need to handle multiple variants differently
- Use `if let` when you only care about one specific variant and want to skip the rest
- Use `let else` when a binding failure should cause the function/loop to exit early

---

<!-- TIER 8 — TRAITS & GENERICS -->

## Traits & Generics

### Traits

A **trait** defines shared behavior — a set of methods that a type must implement. Traits are similar to interfaces in Java or abstract base classes in Python, but more flexible.

Think of a trait as a contract: "any type that implements this trait guarantees it has these methods."

```rust
// Define a trait — this describes what types that implement it CAN do
trait Summary {
    // Required method — any type implementing this trait MUST define this
    fn summarize(&self) -> String;

    // Default method — implementors CAN override this, but don't have to
    // Uses the required method internally
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

// Implement the trait for Article — "Article fulfills the Summary contract"
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

fn main() {
    let tweet = Tweet { username: "rustacean".to_string(), text: "hello!".to_string() };
    println!("{}", tweet.summarize());  // Uses the impl for Tweet
    println!("{}", tweet.preview());    // Uses the default implementation
}
```

---

### Generics

**Generics** let you write code that works for multiple types without duplicating it. Instead of writing `add_i32`, `add_f64`, `add_i64` separately, you write `add<T>` once and it works for any type `T` that supports the operation.

```rust
// Generic function — <T: PartialOrd> means "T must support comparison (< and >)"
fn largest<T: PartialOrd>(list: &[T]) -> &T {
    let mut largest = &list[0];
    for item in &list[1..] {
        if item > largest {
            largest = item;
        }
    }
    largest
}

fn main() {
    let numbers = vec![34, 50, 25, 100, 65];
    println!("Largest: {}", largest(&numbers));   // Works with i32

    let chars = vec!['y', 'm', 'a', 'q'];
    println!("Largest: {}", largest(&chars));     // Also works with char!
}

// Generic struct — Wrapper<T> works for any type T
struct Wrapper<T> {
    value: T,
}

impl<T> Wrapper<T> {
    fn new(value: T) -> Self {
        Self { value }
    }
    fn get(&self) -> &T {
        &self.value
    }
}
```

**`T` is just a name** — you could call it anything, but single uppercase letters like `T`, `U`, `E` are convention. `T` = Type, `E` = Error, `K` = Key, `V` = Value.

---

### Trait Bounds

Trait bounds constrain what types a generic can accept. They say "T must implement this trait."

```rust
// Trait bound syntax — <T: Summary> means T must implement Summary
fn notify<T: Summary>(item: &T) {
    println!("Breaking: {}", item.summarize());
}

// impl Trait syntax — shorthand, cleaner for simple cases
fn notify(item: &impl Summary) {
    println!("Breaking: {}", item.summarize());
}

// Multiple trait bounds — T must implement BOTH Summary AND Display
fn notify<T: Summary + std::fmt::Display>(item: &T) { }

// where clause — cleaner syntax when bounds get complex
fn some_function<T, U>(t: &T, u: &U) -> i32
where
    T: Summary + Clone,
    U: std::fmt::Debug,
{
    0
}

// Returning impl Trait — "returns some type that implements Summary, I won't say which"
fn make_summary() -> impl Summary {
    Tweet {
        username: String::from("bot"),
        text: String::from("hello"),
    }
}
```

---

### Common Standard Library Traits

| Trait | Purpose | Derivable? | Notes |
|-------|---------|-----------|-------|
| `Debug` | `{:?}` formatting | Yes | Derive on almost everything |
| `Display` | `{}` formatting | No — must implement manually | For user-facing output |
| `Clone` | Explicit deep copy (`.clone()`) | Yes | For heap types |
| `Copy` | Implicit bitwise copy | Yes | Only for small stack types |
| `PartialEq` / `Eq` | `==` and `!=` | Yes | Eq requires PartialEq |
| `PartialOrd` / `Ord` | `<`, `>`, `<=`, `>=` and sorting | Yes | Ord requires PartialOrd + Eq |
| `Hash` | For HashMap/HashSet keys | Yes | |
| `Default` | `Default::default()` | Yes | Returns zero/empty values |
| `From` / `Into` | Type conversion | No | Implement From, get Into for free |
| `Iterator` | Iteration protocol | No | Enables `for` loops and iterator methods |
| `Drop` | Custom cleanup when value is freed | No | Like a destructor |

```rust
use std::fmt;

// Manually implementing Display — for {} formatting
struct Point { x: f64, y: f64 }

impl fmt::Display for Point {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "({}, {})", self.x, self.y)   // write! is like println! but to a formatter
    }
}

// From/Into conversion — implement From and Into comes for free
impl From<(f64, f64)> for Point {
    fn from((x, y): (f64, f64)) -> Self {
        Point { x, y }
    }
}

fn main() {
    let p = Point { x: 3.0, y: 4.0 };
    println!("{p}");                    // (3, 4) — uses our Display impl

    let p: Point = (1.0, 2.0).into();  // Uses our From impl (Into is automatic)
    let p = Point::from((1.0, 2.0));   // Explicit From call
}
```

---

<!-- TIER 9 — ERROR HANDLING -->

## Error Handling

Rust's approach to error handling is to make errors **explicit and impossible to ignore**. There's no hidden exception mechanism — if something can fail, the return type reflects that.

Rust has two categories of errors:
- **Recoverable errors** (`Result<T, E>`) — file not found, invalid input, network failure. Handle these gracefully.
- **Unrecoverable errors** (`panic!`) — bugs, index out of bounds, logic violations. Crash the program.

---

### Result Type

`Result<T, E>` is an enum with two variants: `Ok(T)` for success and `Err(E)` for failure. Any function that can fail returns a `Result` — you cannot accidentally use the value without checking for errors first.

```rust
// Result is defined in the standard library as:
enum Result<T, E> {
    Ok(T),    // Success — holds the value of type T
    Err(E),   // Failure — holds the error of type E
}
```

```rust
use std::fs;
use std::io;

fn main() {
    // fs::read_to_string returns Result<String, io::Error>
    // You MUST handle both cases before you can use the content
    let content: Result<String, io::Error> = fs::read_to_string("hello.txt");

    // Method 1: match — explicit, handles both cases
    match content {
        Ok(text) => println!("File: {text}"),
        Err(e) => println!("Error: {e}"),
    }

    // Method 2: unwrap — get the value or PANIC (only use in prototypes/tests)
    let text = fs::read_to_string("hello.txt").unwrap();

    // Method 3: expect — like unwrap but with a better panic message
    let text = fs::read_to_string("hello.txt").expect("Failed to read file");

    // Method 4: unwrap_or — provide a default value on error
    let text = fs::read_to_string("hello.txt").unwrap_or(String::from("(file not found)"));

    // Method 5: unwrap_or_else — lazy default (closure only runs on error)
    let text = fs::read_to_string("hello.txt").unwrap_or_else(|e| {
        eprintln!("Warning: {e}");
        String::from("(default content)")
    });
}
```

---

### The `?` Operator

The `?` operator is shorthand for "if this is an error, return the error immediately; otherwise, give me the success value." It makes error propagation clean and readable.

```rust
use std::fs;
use std::io;

// Without ? — verbose
fn read_file_manual() -> Result<String, io::Error> {
    let content = match fs::read_to_string("file.txt") {
        Ok(c) => c,
        Err(e) => return Err(e),
    };
    Ok(content.trim().to_string())
}

// With ? — clean and idiomatic
fn read_username_from_file() -> Result<String, io::Error> {
    let content = fs::read_to_string("username.txt")?;  // If Err, return Err immediately
    Ok(content.trim().to_string())
}

// Chain multiple ? calls — each one propagates errors up if they fail
fn read_and_parse() -> Result<i32, Box<dyn std::error::Error>> {
    let content = fs::read_to_string("number.txt")?;
    let number = content.trim().parse::<i32>()?;
    Ok(number)
}
```

> **Note:** `?` can only be used inside functions that return `Result` or `Option`. Using it in `main` requires changing `main`'s signature to `fn main() -> Result<(), Box<dyn std::error::Error>>`.

---

### Custom Error Types

For real applications, you'll want your own error types to represent what went wrong in your specific domain.

```rust
use std::fmt;

#[derive(Debug)]
enum AppError {
    IoError(std::io::Error),
    ParseError(String),
    NotFound(String),
}

// Implement Display so the error can be printed with {}
impl fmt::Display for AppError {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        match self {
            AppError::IoError(e) => write!(f, "IO error: {e}"),
            AppError::ParseError(msg) => write!(f, "Parse error: {msg}"),
            AppError::NotFound(item) => write!(f, "Not found: {item}"),
        }
    }
}

// Implement std::error::Error trait to make it a proper error type
impl std::error::Error for AppError {}

// Implement From so ? can automatically convert io::Error into AppError
impl From<std::io::Error> for AppError {
    fn from(e: std::io::Error) -> Self {
        AppError::IoError(e)
    }
}

// Now ? will automatically convert io::Error → AppError using the From impl
fn read_config() -> Result<String, AppError> {
    let content = std::fs::read_to_string("config.txt")?;  // io::Error auto-converts to AppError
    Ok(content)
}
```

> **Tip for beginners:** Use the `anyhow` crate for easy error handling in applications, and `thiserror` for library error types. Both are listed in Useful Crates at the end.

---

### panic!

For unrecoverable errors — bugs in your code that should never happen. Using `panic!` crashes the program with a message and a stack trace.

```rust
fn main() {
    panic!("Something went terribly wrong!");

    // Common sources of panics (don't need explicit panic! call):
    let v = vec![1, 2, 3];
    v[99];           // Index out of bounds — panics automatically

    let x: Option<i32> = None;
    x.unwrap();      // Called unwrap() on None — panics

    let bad: i32 = "abc".parse().unwrap();  // parse failed, then unwrap — panics
}
```

> **Rule of thumb:** Use `Result` for expected failures (file not found, invalid input, network errors). Use `panic!` for bugs — situations that should never happen if your code is correct (violated invariants, programming errors).

---

<!-- TIER 10 — CLOSURES & ITERATORS -->

## Closures

Closures are anonymous functions (functions without a name) that can **capture variables from the surrounding scope**. They're like lambda expressions in Java/Python, but more powerful because they interact with Rust's ownership system.

```rust
fn main() {
    // Basic closure syntax: |parameters| body
    // Type annotations are optional — Rust infers them from usage
    let add = |a, b| a + b;
    let result = add(3, 5);         // 8

    // With explicit type annotations
    let add = |a: i32, b: i32| -> i32 { a + b };

    // Multi-line closure — use a block
    let complex = |x: i32| {
        let y = x * 2;
        y + 1           // Last expression is returned (no semicolon)
    };

    // Closures CAPTURE variables from the enclosing scope — this is what makes them powerful
    let name = String::from("Rust");
    let greet = || println!("Hello, {name}!");    // name is borrowed by the closure
    greet();                         // "Hello, Rust!"
    println!("{name}");              // name is still usable — it was only borrowed

    // Move closure — the closure TAKES OWNERSHIP of captured variables
    // Required when passing closures to threads (data must outlive the current scope)
    let name = String::from("Rust");
    let greet = move || println!("Hello, {name}!");
    // println!("{name}");           // ERROR: name was moved into the closure
    greet();

    // Closures as function parameters — use trait bounds Fn, FnMut, or FnOnce
    fn apply<F: Fn(i32) -> i32>(f: F, x: i32) -> i32 {
        f(x)
    }
    let double = |x| x * 2;
    println!("{}", apply(double, 5));   // 10
}
```

**Closure trait bounds — which one to use:**

| Trait | What it allows the closure to do | Example |
|-------|----------------------------------|---------|
| `Fn` | Borrow captured values immutably | Reading a config value |
| `FnMut` | Borrow captured values mutably | Incrementing a counter |
| `FnOnce` | Take ownership of captured values | Moving data into a new thread |

Use `Fn` as your default. The compiler will tell you if you need `FnMut` or `FnOnce`.

> **Closures vs functions:** Use a closure when you need to capture variables from the surrounding scope or when the logic is short and only used in one place. Use a named function when the logic is reusable or complex.

---

## Iterators

Iterators are a lazy abstraction over sequences of values. **Lazy** means no computation happens until you actually consume the iterator. You can chain many transformations together and they're all executed in a single pass.

```rust
fn main() {
    let v = vec![1, 2, 3, 4, 5];

    // Creating iterators — three kinds depending on ownership
    let iter = v.iter();           // Yields immutable references (&T) — v is still usable
    let iter = v.iter_mut();       // Yields mutable references (&mut T) — v must be mut
    let iter = v.into_iter();      // Yields owned values (T) — CONSUMES v (v is gone)

    // Consuming adaptors — trigger the iteration and produce a final result
    let v = vec![1, 2, 3, 4, 5];
    let sum: i32 = v.iter().sum();                        // 15
    let count = v.iter().count();                          // 5
    let min = v.iter().min();                              // Some(&1)
    let max = v.iter().max();                              // Some(&5)
    let found = v.iter().find(|&&x| x == 3);              // Some(&3) or None
    let any_even = v.iter().any(|&x| x % 2 == 0);        // true — is there ANY even number?
    let all_positive = v.iter().all(|&x| x > 0);         // true — are ALL numbers positive?
    let collected: Vec<i32> = v.iter().cloned().collect(); // Collect into a Vec

    // Iterator adaptors — transform the iterator (LAZY — nothing happens until consumed)
    let v = vec![1, 2, 3, 4, 5];

    let doubled: Vec<i32> = v.iter()
        .map(|&x| x * 2)           // Transform each element: [2, 4, 6, 8, 10]
        .collect();                 // Consume by collecting into Vec

    let evens: Vec<&i32> = v.iter()
        .filter(|&&x| x % 2 == 0) // Keep only elements where closure returns true: [&2, &4]
        .collect();

    // Chaining — where iterators really shine: readable, efficient, one pass
    let result: Vec<i32> = (1..=10)
        .filter(|x| x % 2 == 0)   // Keep even numbers: [2, 4, 6, 8, 10]
        .map(|x| x * x)            // Square them: [4, 16, 36, 64, 100]
        .take(3)                   // Take only the first 3: [4, 16, 36]
        .collect();                // [4, 16, 36]

    // Other useful adaptors
    let v = vec![1, 2, 3];
    v.iter().enumerate();              // Pairs of (index, &value): (0, &1), (1, &2)...
    v.iter().zip(v.iter());            // Pair up two iterators side by side
    v.iter().skip(1);                  // Skip the first N elements
    v.iter().take(2);                  // Yield only the first N elements
    v.iter().chain(v.iter());          // Concatenate two iterators
    v.iter().flat_map(|x| vec![x, x]); // Map then flatten (for returning multiple per element)
    v.iter().peekable();               // Peek at next element without consuming it
    v.iter().cloned();                 // Clone each &T to get T

    // fold — the most general consuming adaptor (like reduce in other languages)
    // Starts with initial value (0) and applies the closure to accumulate
    let sum = v.iter().fold(0, |accumulator, &x| accumulator + x);  // 6
}
```

**Key concepts:**
- **Iterators are lazy:** `v.iter().map(|x| x * 2)` does nothing until you call `.collect()`, `.sum()`, or another consuming adaptor.
- **No performance cost:** Chained iterators compile to the same efficient loop as hand-written code. Zero overhead.
- **`iter()` vs `into_iter()`:** Use `iter()` to borrow and keep the original collection. Use `into_iter()` when you want to move/consume the collection.
- **The `&&x` pattern:** When you have `v.iter()` (which gives `&&i32` in closures like `filter`), you often write `|&&x|` to double-dereference. Alternatively, write `|x| **x % 2 == 0` — both work.

---

<!-- TIER 11 — LIFETIMES -->

## Lifetimes

Lifetimes ensure that references are always valid — you can never hold a reference to data that has been freed. Most of the time the compiler infers lifetimes for you (called "lifetime elision"). You only need to annotate them when the compiler can't figure it out.

**The core concept:** A lifetime annotation (`'a`) isn't creating a lifetime — it's describing relationships between lifetimes that already exist. It tells the compiler: "the reference I return will be valid for at least as long as this input reference."

Think of it like this: if you have a function that takes two string slices and returns one of them, the compiler needs to know how long the returned reference is valid. Lifetime annotations answer that question.

```rust
// The compiler can't tell which reference the return value comes from (x or y?)
// Without a lifetime annotation, it can't determine how long the result is valid.
// 'a says: "the returned reference lives at least as long as BOTH inputs"
fn longest<'a>(x: &'a str, y: &'a str) -> &'a str {
    if x.len() > y.len() { x } else { y }
}

fn main() {
    let string1 = String::from("long string");
    let result;
    {
        let string2 = String::from("xyz");
        result = longest(&string1, &string2);
        println!("{result}");   // OK — both string1 and string2 are still alive here
    }
    // println!("{result}");    // ERROR if uncommented: string2 was dropped above
    // The compiler caught this! result might point to the now-freed string2.
}

// Lifetime in structs — the struct cannot outlive the data it references
struct Excerpt<'a> {
    part: &'a str,   // This struct holds a reference — it can't live longer than what it references
}

impl<'a> Excerpt<'a> {
    fn level(&self) -> i32 {
        3
    }
}

// 'static lifetime — the reference is valid for the entire program duration
// String literals are always 'static (they're baked into the binary)
let s: &'static str = "I live for the whole program";
```

**Lifetime elision rules — when you DON'T need to annotate:**

The compiler automatically infers lifetimes using these rules (in order):
1. Each reference parameter gets its own lifetime: `fn foo(x: &T, y: &U)` → `fn foo<'a, 'b>(x: &'a T, y: &'b U)`
2. If there's exactly one input reference, all output references get that lifetime
3. If one of the inputs is `&self` or `&mut self`, all output references get `self`'s lifetime

If these rules determine all output lifetimes, no annotation needed. If not — the compiler asks you to annotate.

> **Tip for beginners:** Don't stress about lifetimes early on. The compiler's error messages for lifetime issues are very descriptive. Most code doesn't need explicit lifetime annotations — you'll only need them for specific patterns like storing references in structs or writing functions that return references.

---

<!-- TIER 12 — CONCURRENCY -->

## Concurrency

Rust's ownership and type system make concurrent programming much safer. Many concurrency bugs (data races, use-after-free across threads) are caught at compile time. Rust's slogan here: **"fearless concurrency."**

### Threads

A **thread** is an independent unit of execution. Your program starts with one thread (the main thread) and can spawn additional threads to do work in parallel. Each thread has its own stack.

```rust
use std::thread;
use std::time::Duration;

fn main() {
    // Spawn a new thread with a closure
    let handle = thread::spawn(|| {
        for i in 1..5 {
            println!("Spawned thread: {i}");
            thread::sleep(Duration::from_millis(1));  // Pause for 1ms
        }
    });

    for i in 1..3 {
        println!("Main thread: {i}");
        thread::sleep(Duration::from_millis(1));
    }

    // join() waits for the thread to finish — without this, the thread might be killed
    // when main() exits, before it has a chance to finish
    handle.join().unwrap();

    // Moving data into a thread — must use `move` closure
    // Because the thread might outlive the current scope, it can't borrow — it must own
    let data = vec![1, 2, 3];
    let handle = thread::spawn(move || {
        println!("Data: {:?}", data);   // data was MOVED into this thread
    });
    // data is no longer available here — it belongs to the thread now
    handle.join().unwrap();
}
```

---

### Message Passing (Channels)

Channels let threads communicate by sending messages. One thread sends, another receives. **"Don't communicate by sharing memory; share memory by communicating."** This is the safe approach.

```rust
use std::sync::mpsc;  // mpsc = Multiple Producer, Single Consumer
use std::thread;

fn main() {
    // Create a channel: tx = transmitter (sender), rx = receiver
    let (tx, rx) = mpsc::channel();

    // Clone tx to have multiple senders
    let tx2 = tx.clone();

    thread::spawn(move || {
        tx.send(String::from("hello from thread 1")).unwrap();
    });

    thread::spawn(move || {
        tx2.send(String::from("hello from thread 2")).unwrap();
    });

    // rx acts like an iterator — receives messages until all senders are dropped
    for received in rx {
        println!("Got: {received}");
    }
    // Loop ends when tx and tx2 are both dropped (both threads finished)
}
```

---

### Shared State (Arc & Mutex)

When threads need to share and MODIFY the same data, you need `Arc` (shared ownership) and `Mutex` (exclusive access).

- **`Arc<T>`** (Atomic Reference Counted) = Like `Rc<T>` but thread-safe. Lets multiple threads own the same data.
- **`Mutex<T>`** (Mutual Exclusion) = Only one thread can access the inner data at a time. Like a lock on a bathroom — you lock it when you go in, others wait, you unlock when you leave.

```rust
use std::sync::{Arc, Mutex};
use std::thread;

fn main() {
    // Wrap the counter in Arc (shared ownership) and Mutex (exclusive access)
    let counter = Arc::new(Mutex::new(0));
    let mut handles = vec![];

    for _ in 0..10 {
        let counter = Arc::clone(&counter);  // Cheap clone — increments reference count
        let handle = thread::spawn(move || {
            let mut num = counter.lock().unwrap();  // Acquire the lock (blocks if another thread has it)
            *num += 1;
            // Lock is automatically released when `num` goes out of scope
        });
        handles.push(handle);
    }

    for handle in handles {
        handle.join().unwrap();  // Wait for all threads to finish
    }

    println!("Result: {}", *counter.lock().unwrap());  // 10
}
```

**Rust prevents data races at compile time:**
- Can't send non-`Send` types to other threads (the `Send` trait marks thread-safe types)
- Can't share non-`Sync` types between threads (the `Sync` trait marks types safe to reference from multiple threads)
- `Arc<Mutex<T>>` is both `Send` and `Sync` — that's why it's the go-to pattern

---

<!-- TIER 13 — FILE I/O -->

## File I/O

File operations can fail (file not found, permission denied, disk full), so all file functions return `Result`. Use the `?` operator to propagate errors cleanly.

```rust
use std::fs;
use std::io::{self, Read, Write, BufRead, BufReader, BufWriter};
use std::path::Path;

fn main() -> Result<(), Box<dyn std::error::Error>> {
    // Read entire file to a String — simple, but loads the whole file into memory
    let content = fs::read_to_string("file.txt")?;

    // Read entire file to bytes (Vec<u8>) — for binary files
    let bytes = fs::read("file.txt")?;

    // Write string to file — creates the file if it doesn't exist, OVERWRITES if it does
    fs::write("output.txt", "Hello, world!")?;

    // Append to file — adds to the end instead of overwriting
    use std::fs::OpenOptions;
    let mut file = OpenOptions::new()
        .append(true)    // Open in append mode
        .create(true)    // Create if it doesn't exist
        .open("log.txt")?;
    writeln!(file, "New log entry")?;

    // Read file line by line — memory efficient for large files (doesn't load everything at once)
    let file = fs::File::open("file.txt")?;
    let reader = BufReader::new(file);        // BufReader = buffered reader (reads in chunks, faster)
    for line in reader.lines() {
        let line = line?;                     // Each line() call returns Result<String>
        println!("{line}");
    }

    // Buffered writing — faster than writing one byte at a time (writes to buffer, flushes in chunks)
    let file = fs::File::create("output.txt")?;
    let mut writer = BufWriter::new(file);
    writeln!(writer, "Line 1")?;
    writeln!(writer, "Line 2")?;
    // Buffer is automatically flushed when writer is dropped

    // Check if a path exists
    if Path::new("file.txt").exists() {
        println!("File exists");
    }

    // Create directory (and all parent directories — like mkdir -p)
    fs::create_dir_all("path/to/dir")?;

    // Remove file or directory
    fs::remove_file("file.txt")?;
    fs::remove_dir_all("path/to/dir")?;    // Removes directory and all contents

    // List directory contents
    for entry in fs::read_dir(".")? {
        let entry = entry?;
        println!("{}", entry.path().display());
    }

    Ok(())
}
```

**When to use buffered vs unbuffered I/O:**
- `BufReader` / `BufWriter` — for any file you're reading/writing frequently (most cases). Reads/writes in chunks, much faster than one byte at a time.
- `fs::read_to_string` / `fs::write` — convenience functions for small files. Loads entire file at once.
- `BufReader::lines()` — line-by-line reading for large files where you don't want to load everything into memory.

---

<!-- TIER 14 — MODULES & CRATES -->

## Modules & Crates

Rust's module system controls how code is organized and what's accessible from where. Understanding it is key for any project larger than a single file.

**Three levels of organization:**
- **Module** (`mod`) — a namespace within a file or spanning files
- **Crate** — a single compilation unit (your project, or a dependency)
- **Package** — a Cargo project that contains one or more crates

### Module System

```rust
// In src/main.rs or src/lib.rs

// Inline module — defined directly in the same file
mod math {
    pub fn add(a: i32, b: i32) -> i32 { a + b }

    fn private_helper() { }     // private by default — only accessible within this module

    pub mod advanced {
        pub fn factorial(n: u64) -> u64 {
            (1..=n).product()
        }
    }
}

fn main() {
    // Use full path — always works
    let sum = math::add(1, 2);
    let fact = math::advanced::factorial(5);

    // Or bring into scope with `use` — less typing
    use math::add;
    let sum = add(1, 2);

    use math::advanced::factorial;
    let fact = factorial(5);
}
```

---

### File-based Modules

For larger projects, each module can live in its own file. The file name IS the module name.

```
src/
├── main.rs           ← declares: mod math;
├── math.rs           ← the math module (OR src/math/mod.rs)
└── math/
    └── advanced.rs   ← the math::advanced submodule
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

---

### Visibility

By default, everything in Rust is **private** — only accessible within the module it's defined in. Use `pub` to make things accessible from outside.

```rust
mod outer {
    pub fn public_fn() {}          // Accessible from anywhere outside this module
    fn private_fn() {}             // Only accessible within `outer`

    pub(crate) fn crate_fn() {}    // Accessible anywhere in this crate, but not from other crates
    pub(super) fn parent_fn() {}   // Accessible only by the parent module

    pub struct MyStruct {
        pub public_field: i32,     // Public — accessible outside
        private_field: i32,        // Private — even though the struct itself is pub!
    }
}
```

> **Rule of thumb:** Keep things private by default, and only make public what external code actually needs. This gives you freedom to change implementation details later without breaking users of your code.

---

### use & Paths

```rust
// Absolute path (from crate root — your project's root module)
use crate::math::add;

// Relative path
use self::math::add;           // self = current module
use super::something;          // super = parent module

// Re-export — bring something into scope AND make it public for your users
pub use crate::math::add;

// Glob import — imports everything public (generally avoid — pollutes namespace)
use std::collections::*;

// Nested use — group related imports
use std::io::{self, Read, Write};              // self = std::io itself, plus Read and Write
use std::collections::{HashMap, HashSet};

// Aliasing — rename to avoid conflicts or improve clarity
use std::collections::HashMap as Map;
```

---

### Adding Dependencies (Cargo.toml)

External libraries in Rust are called **crates**. You add them to `Cargo.toml` and Cargo downloads them automatically from [crates.io](https://crates.io).

```toml
[package]
name = "my_project"
version = "0.1.0"
edition = "2021"

[dependencies]
serde = { version = "1.0", features = ["derive"] }   # features = optional functionality to enable
tokio = { version = "1", features = ["full"] }
rand = "0.8"                                          # Just the version is fine for simple crates
```

```bash
# Add a dependency via command line (updates Cargo.toml automatically)
cargo add serde --features derive
cargo add tokio --features full
```

---

<!-- TIER 15 — SMART POINTERS -->

## Smart Pointers

Smart pointers are data structures that act like pointers but have additional capabilities. They're how Rust handles scenarios where the simple ownership rules aren't flexible enough.

### Box — Heap Allocation

`Box<T>` puts a value on the heap instead of the stack. The `Box` itself lives on the stack and automatically frees the heap data when it goes out of scope.

**When to use `Box<T>`:**
- Data is large and you don't want to copy it
- You have a recursive type (like a linked list) — without Box, the size would be infinite
- You need to store a trait object (`Box<dyn Trait>`)

```rust
fn main() {
    // Box puts data on the heap — b is on the stack, the 5 is on the heap
    let b = Box::new(5);
    println!("{b}");     // Rust auto-derefs Box, so this works like a regular i32

    // Useful for recursive types — without Box, the compiler can't know the size
    enum List {
        Cons(i32, Box<List>),   // Box breaks the infinite size problem
        Nil,
    }

    let list = List::Cons(1, Box::new(List::Cons(2, Box::new(List::Nil))));
}
```

---

### Rc — Reference Counted

`Rc<T>` (Reference Counted) allows **multiple owners** of the same data. It keeps a count of how many `Rc` values point to the data; when the count reaches zero, the data is freed. **Single-threaded only** — use `Arc<T>` for multithreading.

```rust
use std::rc::Rc;

fn main() {
    // Multiple variables own the SAME data
    let a = Rc::new(vec![1, 2, 3]);
    let b = Rc::clone(&a);          // Rc::clone increments the reference count (very cheap!)
    let c = Rc::clone(&a);

    println!("Count: {}", Rc::strong_count(&a));  // 3 — three owners
    println!("{:?}", a);            // [1, 2, 3]
}
// When a, b, c all go out of scope, count drops to 0 and vec is freed
```

> **Note:** `Rc<T>` only allows **immutable** access. For mutable access with multiple owners, use `Rc<RefCell<T>>`.

---

### RefCell — Interior Mutability

`RefCell<T>` allows you to mutate data even when you only have an immutable reference to the `RefCell`. Borrow rules are enforced at **runtime** instead of compile time — if you break them, the program panics instead of failing to compile.

```rust
use std::cell::RefCell;

fn main() {
    // RefCell allows mutable access through an immutable reference
    let data = RefCell::new(vec![1, 2, 3]);

    data.borrow_mut().push(4);           // Mutable borrow at runtime
    println!("{:?}", data.borrow());     // Immutable borrow at runtime: [1, 2, 3, 4]

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
> - `Box<T>` — Single owner, need heap allocation or recursive type
> - `Rc<T>` — Multiple owners, single-threaded, immutable access
> - `Arc<T>` — Multiple owners, multi-threaded (see Concurrency section)
> - `RefCell<T>` — Interior mutability, borrow checking at runtime
> - `Rc<RefCell<T>>` — Multiple owners + mutation, single-threaded
> - `Arc<Mutex<T>>` — Multiple owners + mutation, multi-threaded

---

<!-- TIER 16 — MACROS -->

## Macros

Macros are code that generates code. They look like function calls but with a `!` at the end. Unlike functions, macros can accept a variable number of arguments, work with types at compile time, and generate arbitrary code. You'll use built-in macros constantly in Rust.

### Common Built-in Macros

```rust
fn main() {
    println!("Print with newline: {}", 42);    // Most common output macro
    print!("Print without newline");
    eprintln!("Print to stderr");              // For error messages and diagnostics
    format!("Returns a String: {}", 42);       // Like println! but returns a String instead of printing

    dbg!(42);                    // Debug print with FILE NAME and LINE NUMBER — great for debugging
                                 // Also returns the value, so dbg!(x + 1) works in expressions

    vec![1, 2, 3];              // Create a Vec — equivalent to Vec::new() + multiple pushes
    todo!();                    // Marks unfinished code — PANICS at runtime with "not yet implemented"
    unimplemented!();           // Similar to todo! — use when a feature is intentionally not done
    unreachable!();             // Marks code paths that should never execute — panics if they do

    assert!(true);              // Panics if the condition is false — use in tests
    assert_eq!(1, 1);           // Panics if the values are not equal — better error message than assert!
    assert_ne!(1, 2);           // Panics if the values ARE equal

    include_str!("file.txt");   // Embeds file contents as &str at COMPILE time (not runtime)
    include_bytes!("img.png");  // Embeds file contents as &[u8] at compile time

    cfg!(target_os = "linux");  // Check compile-time configuration (returns bool)
}
```

**`dbg!` is your best debugging friend:**
```rust
let x = 5;
let y = dbg!(x * 2) + 1;  // Prints: [src/main.rs:2] x * 2 = 10
                            // And y = 11 (dbg! returns the value)
```

---

### Declarative Macros (macro_rules!)

You can define your own macros with `macro_rules!`. These are pattern-matching rules that transform one piece of code into another at compile time.

```rust
// Simple macro — like a function but runs at compile time
macro_rules! say_hello {
    () => {                 // () = match no arguments
        println!("Hello!");
    };
}

// Macro with arguments — $x:expr matches any expression
macro_rules! create_vec {
    ( $( $x:expr ),* ) => {   // $( ... ),* = match zero or more comma-separated expressions
        {
            let mut v = Vec::new();
            $( v.push($x); )*  // For each matched expression, generate a push statement
            v
        }
    };
}

fn main() {
    say_hello!();                           // Hello!
    let v = create_vec![1, 2, 3, 4, 5];   // Creates a Vec<i32> with those values
}
```

> **Note for beginners:** You don't need to write your own macros early on. Focus on using the built-in ones. Macro writing is an advanced topic — come back to it when you need something that functions can't do.

---

<!-- TIER 17 — TESTING -->

## Testing

Rust has built-in testing support — no external test framework needed. Tests live right next to the code they test.

```rust
// In any .rs file — the #[cfg(test)] attribute means this module is only compiled when testing
#[cfg(test)]
mod tests {
    use super::*;   // Import everything from the parent module (the code we're testing)

    #[test]          // Mark a function as a test
    fn it_works() {
        assert_eq!(2 + 2, 4);   // Fails with helpful message if not equal
    }

    #[test]
    fn test_with_result() -> Result<(), String> {
        // Tests can return Result — Err fails the test, Ok passes
        if 2 + 2 == 4 {
            Ok(())
        } else {
            Err(String::from("two plus two does not equal four"))
        }
    }

    #[test]
    #[should_panic]   // This test PASSES if the code panics (for testing error conditions)
    fn test_panic() {
        panic!("This should panic");
    }

    #[test]
    #[should_panic(expected = "specific message")]   // Panics must contain this message
    fn test_specific_panic() {
        panic!("specific message here");
    }

    #[test]
    #[ignore]   // Skip this test unless specifically requested with `cargo test -- --ignored`
    fn expensive_test() {
        // Long-running test that you don't want to run every time
    }
}
```

```bash
cargo test                     # Run all tests
cargo test test_name           # Run tests whose name contains "test_name"
cargo test -- --ignored        # Run ignored tests
cargo test -- --show-output    # Show println! output (normally suppressed during tests)
cargo test -- --test-threads=1 # Run tests one at a time (instead of in parallel)
```

---

### Integration Tests

Integration tests are in a separate `tests/` directory and test your code as an external user would — they can only call `pub` functions.

```
my_project/
├── src/
│   └── lib.rs              ← your library code
└── tests/                  ← integration tests directory
    └── integration_test.rs ← automatically run with `cargo test`
```

```rust
// tests/integration_test.rs
// Each file here is a separate "test crate" that imports your library
use my_project;   // Import your crate by name

#[test]
fn test_from_outside() {
    assert_eq!(my_project::add(1, 2), 3);
}
```

**Unit tests vs integration tests:**
- **Unit tests** (`#[cfg(test)]` inside the source file) — test individual functions in isolation, can access private code
- **Integration tests** (`tests/` directory) — test the public API as a whole, from a user's perspective

---

<!-- TIER 18 — REFERENCE -->

## Common Errors & Tips

### Common Compiler Errors

Rust's compiler errors are famously helpful — they usually tell you exactly what's wrong and often suggest a fix. Don't fear them!

| Error | Cause | Fix |
|-------|-------|-----|
| `E0382: use of moved value` | You used a value after moving it elsewhere | Use `&` to borrow instead of move, or `.clone()` to copy |
| `E0502: cannot borrow as mutable` | Already borrowed as immutable in this scope | End the immutable borrow before taking a mutable one |
| `E0499: cannot borrow as mutable more than once` | Two `&mut` at the same time | Restructure so only one `&mut` exists at a time |
| `E0106: missing lifetime specifier` | Compiler can't infer which lifetime the return borrows | Add lifetime annotations like `<'a>` |
| `E0308: mismatched types` | Wrong type — e.g., semicolon on last expression | Check expected vs actual type; use `as` or `.into()`; check for stray semicolons |
| `E0277: trait not satisfied` | Type doesn't implement a required trait | `#[derive(Trait)]` or implement it manually |
| `E0599: no method named X` | Method doesn't exist on type | Check spelling; check that you imported the right trait with `use` |
| `E0596: cannot borrow as mutable` | Variable declared with `let`, not `let mut` | Change `let` to `let mut` |
| `E0425: cannot find value/function X` | Typo, wrong scope, or missing `use` | Check spelling, add `use`, or check module path |

---

### Best Practices

- **Prefer `&str` over `String` in function parameters** — `&str` accepts both `&String` and string literals; `String` only accepts `String`
- **Use `Result` over `panic!`** — let the caller decide how to handle failures; only panic for bugs
- **Use the `?` operator** — propagate errors cleanly instead of nesting match statements
- **Use `clippy`** — `cargo clippy` catches common mistakes and suggests idiomatic alternatives (think of it as a code reviewer)
- **Use `rustfmt`** — `cargo fmt` formats code consistently; no more arguing about style
- **Prefer iterator methods over manual loops** — `.iter().map().filter().collect()` is idiomatic and often clearer
- **Prefer `collect()` with type annotation** — `let v: Vec<_> = iter.collect();` tells Rust what to collect into
- **Use `if let` for single-pattern matches** — cleaner than a full `match` when you only care about one variant
- **Avoid `.unwrap()` in production code** — use `?`, `unwrap_or`, `unwrap_or_else`, or proper error handling
- **Derive `Debug` on all your types** — makes debugging much easier with `dbg!` and `{:?}` printing
- **Use `cargo check` during development** — it's much faster than `cargo build` and catches all compile errors

---

### Useful Commands

```bash
cargo fmt              # Format all code (run before committing!)
cargo clippy           # Lint code — catch common mistakes and bad patterns
cargo doc --open       # Generate HTML documentation and open it in your browser
cargo bench            # Run benchmarks (for performance measurement)
cargo update           # Update all dependencies to their latest compatible versions
cargo tree             # Show the full dependency tree
cargo test             # Run all tests
cargo build --release  # Build optimized binary for distribution
```

---

## Useful Crates

These are the most commonly used third-party crates. Add them to `Cargo.toml` under `[dependencies]`.

| Crate | Purpose | Beginner-friendly? |
|-------|---------|-------------------|
| `serde` + `serde_json` | Serialize/deserialize data (JSON, TOML, etc.) | Yes — add `#[derive(Serialize, Deserialize)]` |
| `tokio` | Async runtime for non-blocking I/O | Intermediate |
| `reqwest` | HTTP client (make web requests) | Yes |
| `clap` | Command-line argument parsing | Yes |
| `anyhow` | Simplified error handling for applications | Yes — use instead of `Box<dyn Error>` |
| `thiserror` | Custom error types with `#[derive(Error)]` | Yes |
| `rand` | Random number generation | Yes |
| `regex` | Regular expressions | Yes |
| `log` + `env_logger` | Logging framework | Yes |
| `chrono` | Date and time handling | Yes |
| `rayon` | Data parallelism (parallel iterators — easy speedup!) | Yes |
| `itertools` | Extra iterator methods not in std | Yes |

```rust
// Example: serde JSON — serializing and deserializing data
use serde::{Deserialize, Serialize};

#[derive(Serialize, Deserialize, Debug)]
struct User {
    name: String,
    age: u32,
}

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let user = User { name: "Alice".into(), age: 30 };

    // Serialize: Rust struct → JSON string
    let json = serde_json::to_string(&user)?;
    println!("{json}");   // {"name":"Alice","age":30}

    // Deserialize: JSON string → Rust struct
    let parsed: User = serde_json::from_str(&json)?;
    println!("{:?}", parsed);   // User { name: "Alice", age: 30 }

    Ok(())
}
```

---

*Happy coding with Rust!* 🦀

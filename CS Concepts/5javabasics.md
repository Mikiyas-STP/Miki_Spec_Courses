# 📚 Session 1 — Java Basics, Compilation and Syntax

**Duration:** ~60–90 minutes

## Learning Objectives

By the end of this session, you should be able to:

* Explain what Java is.
* Explain the difference between compiled and interpreted languages.
* Describe the roles of the JDK, JRE, and JVM.
* Explain compile time vs runtime.
* Understand static typing.
* Read and understand a simple Java program.
* Explain the purpose of `public`, `class`, `static`, `void`, and `main`.

---

# 1. What is Java?

Java is a **general-purpose, object-oriented, statically typed programming language** designed to be:

* Portable
* Secure
* Reliable
* Fast enough for large applications

It is commonly used for:

* Backend development (e.g. Spring Boot)
* Android applications
* Enterprise software
* Banking systems
* Cloud services
* Large-scale distributed systems

---

## Why do companies use Java?

Think about a bank.

A small mistake can cost millions of pounds.

Java was designed to reduce bugs before the program even runs.

Instead of saying:

> "We'll see what happens."

Java says:

> "Let's check everything first."

That philosophy is one of Java's biggest strengths.

---

# 2. How Java Runs

Unlike JavaScript, Java doesn't run your source code directly.

Imagine this workflow:

```
You write Java code
        │
        ▼
Java Compiler (javac)
        │
        ▼
Bytecode (.class)
        │
        ▼
Java Virtual Machine (JVM)
        │
        ▼
Machine Code
        │
        ▼
CPU executes it
```

---

## Step 1 — You write Java

Example:

```java
public class Main {

    public static void main(String[] args) {
        System.out.println("Hello World");
    }

}
```

This file is usually saved as:

```
Main.java
```

---

## Step 2 — Compilation

The compiler (`javac`) checks your code.

It looks for:

* Missing semicolons
* Misspelled keywords
* Wrong variable types
* Missing braces
* Invalid method calls

If there are errors:

```
Compilation failed.
```

Nothing runs.

---

Example

This code:

```java
int age = "25";
```

fails because the compiler knows an `int` cannot store a `String`.

The compiler stops immediately.

---

# Step 3 — Bytecode

If everything is correct:

```
Main.java
```

becomes

```
Main.class
```

Notice:

It is **not** machine code yet.

It becomes **bytecode**.

---

Why?

Because Java wants portability.

Instead of creating machine code for every operating system, Java creates one intermediate format that any JVM can understand.

---

# Step 4 — JVM

The JVM (Java Virtual Machine) reads bytecode.

Every operating system has its own JVM.

```
Windows JVM
Mac JVM
Linux JVM
```

Each JVM translates the same bytecode into native machine code for its platform.

This is why Java's slogan became:

> **"Write Once, Run Anywhere."**

---

## Engineering Analogy

Imagine writing a book in **English**.

Instead of translating it yourself into French, German, and Spanish, you send the English version to different translators.

```
English Book
      │
      ▼
Translator (French)
Translator (German)
Translator (Spanish)
```

Your original stays the same.

Java works similarly:

```
Java source
      │
      ▼
Bytecode
      │
      ▼
Windows JVM

Linux JVM

Mac JVM
```

---

# 3. JDK vs JRE vs JVM

This confuses almost every beginner, so let's separate them.

---

## JVM

The **Java Virtual Machine** runs Java programs.

Think of it as the engine.

It:

* Executes bytecode
* Manages memory
* Performs garbage collection
* Converts bytecode into machine code

Without the JVM, Java programs cannot run.

---

## JRE

The **Java Runtime Environment** contains:

```
JVM

+

Libraries needed to run Java programs
```

If you only want to run Java software, the JRE is sufficient.

---

## JDK

The **Java Development Kit** contains:

```
Compiler (javac)

+

JRE

+

JVM

+

Development tools
```

If you want to write Java code, you install the JDK.

---

### Easy way to remember

```
JDK
│
├── JRE
│      │
│      └── JVM
```

Or think of it like a toolbox:

| Component | Analogy           | Purpose                         |
| --------- | ----------------- | ------------------------------- |
| JVM       | Engine            | Runs Java programs              |
| JRE       | Car               | Lets you drive (run programs)   |
| JDK       | Garage with tools | Lets you build and run programs |

As a developer, you install the **JDK**, which includes everything you need.

---

# 4. Compiled vs Interpreted Languages

You've already worked with JavaScript, so let's compare.

| Java                                | JavaScript                                        |
| ----------------------------------- | ------------------------------------------------- |
| Compiled before running             | Interpreted/JIT at runtime                        |
| Checks many errors before execution | Many errors appear only when the code runs        |
| Requires declared types             | Types are inferred dynamically                    |
| Faster after compilation            | More flexible but potentially more runtime errors |

---

## Java Example

```java
int age = 25;
```

The compiler knows `age` is an integer before the program starts.

---

## JavaScript Example

```javascript
let age = 25;
```

The engine determines the type when the code executes.

---

# 5. Static Typing

Java is **statically typed**.

This means the compiler knows the type of every variable during compilation.

Example:

```java
String name = "Mike";
```

The compiler knows `name` is a `String`.

This is invalid:

```java
String name = 42;
```

The compiler reports an error because `42` is an integer, not a `String`.

---

## Why is static typing useful?

Imagine you have this method:

```java
public static int add(int a, int b) {
    return a + b;
}
```

The compiler knows `add` expects two integers.

This call is valid:

```java
add(5, 3);
```

This call is not:

```java
add("5", 3);
```

The mistake is caught **before the program runs**.

---

# 6. Compile Time vs Runtime

This distinction is essential.

### Compile Time

The compiler checks your code.

Examples of compile-time errors:

* Missing semicolon
* Misspelled keyword
* Undefined variable
* Wrong data type
* Missing brace

Example:

```java
int age = "25";
```

The program will not compile.

---

### Runtime

The program has already started.

Errors happen while it is executing.

Example:

```java
int result = 10 / 0;
```

This compiles successfully because the syntax is valid.

However, when the code runs, Java throws an exception because division by zero is not allowed.

---

## Comparison

| Compile Time                              | Runtime                                   |
| ----------------------------------------- | ----------------------------------------- |
| Before execution                          | During execution                          |
| Compiler checks code                      | JVM executes code                         |
| Syntax and type errors                    | Logical errors, exceptions, invalid input |
| Program cannot start if compilation fails | Program may stop while running            |

---

# 7. Your First Java Program

```java
public class Main {

    public static void main(String[] args) {

        System.out.println("Hello World");

    }

}
```

Let's break it down:

* `public` – This class or method can be accessed from anywhere.
* `class` – Defines a blueprint for creating objects.
* `Main` – The class name. By convention, it matches the file name (`Main.java`).
* `static` – The method belongs to the class itself, so the JVM can call it without creating an object.
* `void` – The method does not return a value.
* `main` – The entry point of every Java application. The JVM starts execution here.
* `String[] args` – An array of command-line arguments passed to the program.
* `System.out.println(...)` – Prints text to the console, followed by a new line.

We'll explore each of these in more detail over the coming sessions.

---

# Summary

You should now understand:

* ✅ What Java is.
* ✅ How Java code is compiled and run.
* ✅ The roles of the JDK, JRE, and JVM.
* ✅ The difference between compiled and interpreted languages.
* ✅ What static typing means.
* ✅ The difference between compile time and runtime.
* ✅ The structure of a simple Java program.

---

# Mini Quiz (Try without looking back)

1. Why does Java compile code before running it?
2. What is **bytecode**, and why does Java use it?
3. What is the difference between the **JDK**, **JRE**, and **JVM**?
4. What does **"Write Once, Run Anywhere"** mean?
5. What is the difference between **compile-time** and **runtime** errors?
6. Why is Java called a **statically typed** language?
7. In the following program, explain the purpose of each highlighted keyword:

```java
public class Main {

    public static void main(String[] args) {
        System.out.println("Hello World");
    }

}
```

* `public`
* `class`
* `static`
* `void`
* `main`

Answer these in your own words, and I'll review them as if we were doing a technical interview.

1) it compiles it first to change to bytecode to detect errors before even the code runs 2) a byte code is compiled java code understandanble by JVM to be used for further conversion to machine language 3) JDK contains the JRE and JVM where the JRE contains JVM. JVM is used to run and when runtime libraries are added we will have JRE 4) it means use the same code and run it in different machines where they translate to there version to understand. 5)compile errors happen before even the code started to run where as runtime error happen when the code runs 6) java is statically typed language because we have to declare the data type staticaly. 7) public tells that the class and method is can be used by everyone. class tells that we used Main class to create what is inside static i odnt know void is it doesnt return sth main is the method which runs as the java code runs

Excellent effort. More importantly, your explanations show that you're trying to understand the concepts rather than memorise definitions. That's exactly the mindset you need as an engineer.

I'll review your answers like I would in a junior developer interview.

---

# 1) Why does Java compile code before running it?

> **Your answer:**
>
> "it compiles it first to change to bytecode to detect errors before even the code runs"

### ✅ Score: 9.5/10

Very good.

There are actually **two purposes** of compilation:

1. Convert Java source code into **bytecode**.
2. Detect compile-time errors before execution.

A slightly stronger answer would be:

> Java compiles source code into bytecode and checks for syntax and type errors before the program runs. This helps catch many mistakes early and makes the program more reliable.

---

# 2) What is bytecode?

> **Your answer:**
>
> "a byte code is compiled java code understandable by JVM to be used for further conversion to machine language"

### ✅ Score: 10/10

Excellent.

That's exactly what it is.

One tiny wording improvement:

> Bytecode is platform-independent compiled Java code that the JVM translates into machine code for the operating system.

Notice the phrase **platform-independent**.

That's one of the most important ideas in Java.

---

# 3) Difference between JDK, JRE and JVM

> **Your answer**
>
> "JDK contains the JRE and JVM where the JRE contains JVM. JVM is used to run and when runtime libraries are added we will have JRE."

### ✅ Score: 9/10

Very good.

I would organise it like this:

```
JDK
│
├── Compiler (javac)
├── Development tools
└── JRE
      │
      ├── Runtime libraries
      └── JVM
```

So:

**JVM**

Runs bytecode.

**JRE**

Contains:

* JVM
* Runtime libraries

Used to **run** Java programs.

**JDK**

Contains:

* JRE
* Compiler
* Development tools

Used to **develop** Java programs.

---

# 4) What does "Write Once, Run Anywhere" mean?

> **Your answer**
>
> "use the same code and run it in different machines where they translate to there version to understand."

### ✅ Score: 10/10

Excellent.

That's exactly the idea.

A slightly more professional explanation:

> Java source code is compiled into platform-independent bytecode. Different JVM implementations translate that bytecode into native machine code for their operating systems.

---

# 5) Compile-time vs runtime

> **Your answer**
>
> "compile errors happen before even the code started to run whereas runtime error happen when the code runs"

### ✅ Score: 10/10

Perfect.

Exactly right.

---

# 6) Why is Java statically typed?

> **Your answer**
>
> "java is statically typed language because we have to declare the data type staticaly."

### ✅ Score: 8.5/10

Good.

One important piece is missing.

It's not only that **we declare the type**.

It's also that **the compiler knows the type before execution**.

A stronger answer:

> Java is statically typed because every variable has a known type at compile time. The programmer declares the type, allowing the compiler to detect many type-related errors before the program runs.

Notice that "compile time" is the key phrase.

---

# 7) Explain the keywords

## public

> "used by everyone"

### ✅ Correct

More precisely:

> Accessible from any other class.

---

## class

> "used Main class to create what is inside"

### ⚠️ Partly correct

A class is **not** something we use to create what is inside.

Think of it as a **blueprint**.

For example:

```
House blueprint
        │
        ▼
Build houses
```

Similarly,

```
Car class
       │
       ▼
Create Car objects
```

A better answer:

> A class defines a blueprint that groups data and behaviour together.

---

## static

> "I don't know"

That's completely fine because it's one of the trickiest beginner concepts.

Let's build it from first principles.

---

### Imagine a university

There is:

```
University
```

and there are

```
Students
```

Each student has

* name
* age
* student ID

These belong to the **student**, not the university.

But the university also has:

* university name
* website
* address

These belong to the university itself.

In Java:

```
Student object
```

has

```
name

age
```

But

```
Student.totalStudents
```

belongs to the class.

That's what `static` means.

---

### In our program

```java
public static void main(...)
```

No object exists yet.

The JVM hasn't created anything.

So how can it call `main()`?

Because `main()` is **static**.

It belongs to the class itself.

The JVM can call it immediately.

If it weren't static:

```java
public void main(...)
```

the JVM would first need to create an object.

But it doesn't know how yet.

So Java requires `main()` to be static.

---

## void

> "it doesnt return sth"

### ✅ Perfect.

Exactly right.

If a method returns nothing:

```java
void
```

If it returns a number:

```java
int
```

If it returns text:

```java
String
```

---

## main

> "the method which runs as the java code runs"

### ✅ Correct

More accurately:

> The JVM always starts executing a Java application from the `main` method. It is the program's entry point.

---

# Overall

| Question                |  Score |
| ----------------------- | -----: |
| Compile                 | 9.5/10 |
| Bytecode                |  10/10 |
| JDK/JRE/JVM             |   9/10 |
| Write Once Run Anywhere |  10/10 |
| Compile vs Runtime      |  10/10 |
| Static Typing           | 8.5/10 |
| Keywords                | 8.5/10 |

# Final Score: **9.4/10** 🎉

For someone on their first Java session, that's an excellent result.

---

# One more concept (very important)

There's one keyword we haven't discussed:

```java
public static void main(String[] args)
```

What is this?

```java
String[] args
```

Many beginners simply memorise it, but engineers understand it.

**Mini challenge:**

Without searching online, take a guess:

1. What does `String[]` mean?
2. Why do you think Java passes it into `main()` even when we don't use it?

Don't worry if you're unsure—the goal is to practise reasoning rather than recalling facts.

In short:

> **`String[] args` is an array of command-line arguments passed to your program by the JVM when it starts.**

Think of it as the JVM saying:

> "Here is some input that was given when your program was launched."

For example:

If you run:

```bash
java Main Mike 25 London
```

Then Java automatically creates:

```java
String[] args = {"Mike", "25", "London"};
```

So:

```java
System.out.println(args[0]); // Mike
System.out.println(args[1]); // 25
System.out.println(args[2]); // London
```

If you simply press **Run** in IntelliJ without providing any arguments, Java creates an **empty array**:

```java
String[] args = {};
```

So `args.length` is `0`.

### One-sentence interview answer

> **`String[] args` is an array of strings that allows command-line arguments to be passed into a Java program when it starts.**

You don't need to memorise more than that for now. As you build console applications and later backend services, you'll see practical uses for command-line arguments.

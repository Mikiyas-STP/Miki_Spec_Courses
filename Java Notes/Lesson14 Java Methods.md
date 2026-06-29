Excellent. From this point on, we'll follow your resources **exactly**. I'll explain everything they contain, but I won't add new topics beyond what's needed to understand them.

---

# ☕ Java Methods – Lesson 1

## Introduction to Methods

**Based on:**

* W3Schools – Java Methods
* "Introduction to methods in Java"
* Your learning objectives

---

# 🎯 Learning Objectives

By the end of this lesson, you should be able to:

* Explain what a method is.
* Explain why methods are useful.
* Create a simple method.
* Call a method.
* Explain the difference between declaring and calling a method.

---

# 1. What is a Method?

The W3Schools definition says:

> **A method is a block of code which only runs when it is called.**

Let's break that down.

### **A block of code**

A block of code is simply a group of statements enclosed in curly braces `{}`.

Example:

```java
{
    System.out.println("Hello");
    System.out.println("World");
}
```

Everything inside the braces belongs together.

---

### **Only runs when it is called**

Writing a method does **not** execute it.

Consider this example:

```java
public class Main {

    static void myMethod() {
        System.out.println("I just got executed!");
    }

    public static void main(String[] args) {

    }
}
```

If you run this program, nothing is printed.

Why?

Because `myMethod()` has only been **created (declared)**. It has not been **called**.

---

# 2. Creating (Declaring) a Method

W3Schools gives this example:

```java
public class Main {

    static void myMethod() {
        // code to be executed
    }

}
```

Let's understand each part.

```java
static
```

The resource explains:

> **static means the method belongs to the class and not an object of the class.**

At this stage, that's enough. You'll learn about objects later in the course.

---

```java
void
```

The resource says:

> **void means that this method does not have a return value.**

In other words,

after the method finishes, it gives nothing back.

Example:

```java
static void sayHello() {
    System.out.println("Hello");
}
```

The method prints something,

but it doesn't return anything.

---

```java
myMethod
```

This is simply the method's name.

It identifies the method.

---

```java
()
```

These parentheses are required.

They hold the method's parameters (inputs).

This method has no parameters, so the parentheses are empty.

---

```java
{
}
```

The braces contain the method body.

This is where the code that performs the task is written.

---

# Putting it together

```java
static void myMethod() {
    System.out.println("Hello");
}
```

Reading it from left to right:

* `static` → belongs to the class.
* `void` → returns nothing.
* `myMethod` → method name.
* `()` → takes no parameters.
* `{}` → contains the code to execute.

---

# 3. Calling a Method

The resource says:

> To call a method, write the method name followed by parentheses and a semicolon.

Example:

```java
public class Main {

    static void myMethod() {
        System.out.println("I just got executed!");
    }

    public static void main(String[] args) {

        myMethod();

    }

}
```

Notice:

Inside `main()` we write

```java
myMethod();
```

This tells Java:

> Execute the code inside `myMethod`.

Output:

```text
I just got executed!
```

---

# 4. What Happens When a Method is Called?

Let's walk through the previous example.

### Step 1

Java starts here:

```java
public static void main(String[] args)
```

This is where program execution begins.

---

### Step 2

Java reads:

```java
myMethod();
```

It recognises this as a method call.

---

### Step 3

Java goes to the method definition:

```java
static void myMethod() {

    System.out.println("I just got executed!");

}
```

---

### Step 4

Java executes the statement:

```java
System.out.println("I just got executed!");
```

---

### Step 5

The method finishes.

Control returns to `main()`.

If there were more statements after `myMethod();`, Java would continue with them.

---

# 5. Calling a Method Multiple Times

The resource gives this example:

```java
public class Main {

    static void myMethod() {
        System.out.println("I just got executed!");
    }

    public static void main(String[] args) {

        myMethod();
        myMethod();
        myMethod();

    }

}
```

Output:

```text
I just got executed!
I just got executed!
I just got executed!
```

Notice something important.

The method is written **once**.

But it can be used **many times**.

This is one of the main reasons methods are useful.

---

# 6. Why Use Methods?

The W3Schools resource gives one key reason:

> **To reuse code: define the code once, and use it many times.**

Example without methods:

```java
System.out.println("Welcome!");
System.out.println("Welcome!");
System.out.println("Welcome!");
```

Example with a method:

```java
static void welcome() {
    System.out.println("Welcome!");
}
```

Now you simply call:

```java
welcome();
welcome();
welcome();
```

The code is written once and reused.

---

# 7. Declaring vs Calling

This is a common source of confusion.

### Declaration

Creates the method.

```java
static void myMethod() {

}
```

Nothing happens yet.

---

### Call

Executes the method.

```java
myMethod();
```

Now the code inside the method runs.

---

# 8. Summary

From today's lesson:

* A method is a block of code.
* A method only runs when it is called.
* A method is declared inside a class.
* The method body contains the code to execute.
* Methods are called using the method name followed by `()`.
* Methods can be called as many times as needed.
* One of the main benefits of methods is code reuse.

---

# 📝 Knowledge Check

Answer these without looking back at the lesson.

### Question 1

What is a method?

---

### Question 2

Why doesn't this program print anything?

```java
public class Main {

    static void hello() {
        System.out.println("Hello");
    }

    public static void main(String[] args) {

    }

}
```

---

### Question 3

What is the difference between:

```java
hello();
```

and

```java
static void hello() {

}
```

---

### Question 4

According to the resource, what is the main advantage of using methods?

---

### Question 5

Identify each part of this method.

```java
static void printMessage() {
    System.out.println("Hi");
}
```

* `static`
* `void`
* `printMessage`
* `()`
* `{ ... }`

---




# Question 5

Given this method:

```java
static void printMessage() {
    System.out.println("Hi");
}
```

Identify each part:

* `static`
* `void`
* `printMessage`
* `()`
* `{ ... }`

Let's go through them one by one.

---

## 1. `static`

```java
static
```

This is the **`static` keyword**.

From your W3Schools resource:

> **`static` means that the method belongs to the class and not an object of the class.**

At this stage, that's all you need to know.

Later, when you learn about objects and classes, this sentence will make much more sense.

---

## 2. `void`

```java
void
```

This is the **return type**.

`void` means:

> This method does **not** return a value.

For example:

```java
static void printMessage() {
    System.out.println("Hi");
}
```

prints:

```text
Hi
```

but it doesn't send anything back to whoever called it.

---

## 3. `printMessage`

```java
printMessage
```

This is called the **method name** or **method identifier**.

It is simply the name Java uses to identify this method.

Later, when you write:

```java
printMessage();
```

Java knows exactly which method to execute.

---

## 4. `()`

```java
()
```

These are the **parentheses**.

They contain the method's **parameters** (inputs).

In this example:

```java
()
```

they're empty.

That means:

> This method doesn't need any information from the caller.

Later you'll see methods like:

```java
greetUser(String name)
```

where the parentheses are no longer empty.

---

## 5. `{ ... }`

```java
{
    System.out.println("Hi");
}
```

This is called the **method body**.

Everything inside the braces belongs to the method.

The method body contains the instructions Java executes when the method is called.

In this case, there's only one instruction:

```java
System.out.println("Hi");
```

---

# Complete Breakdown

```java
static          // belongs to the class

void            // returns nothing

printMessage    // method name

()              // no parameters

{               // beginning of method body

    System.out.println("Hi");

}               // end of method body
```


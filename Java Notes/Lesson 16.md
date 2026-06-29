# 📚 Lesson 2 – Part 4: Parameter List

## 🎯 Learning Objectives

By the end of this section, you should be able to:

* Explain what a parameter list is.
* Identify parameters in a method.
* Understand that a method can have 0 to 255 parameters.
* Recognise different types of parameters.

---

# What Baeldung Says

Baeldung states:

> **We can specify input values for a method in its parameter list, which is enclosed in parentheses.**

Let's break this into smaller pieces.

---

# What is a Parameter List?

A **parameter list** defines the **inputs** that a method expects.

Think of a method as a small machine.

```
Input  ─────►  Method  ─────►  Output
```

Some machines need inputs to work.

For example, imagine a calculator.

If you ask it to add two numbers, you first have to provide those numbers.

Similarly, a Java method often needs information before it can do its job.

That information is provided through **parameters**.

---

# Where is the Parameter List?

Look at this method:

```java
public static String greetUser(String name) {
    return "Hello, " + name;
}
```

Let's identify the parts we've learned.

```text
public          → Access modifier
static          → Keyword
String          → Return type
greetUser       → Method identifier
(String name)   → Parameter list
```

Everything inside the parentheses is the **parameter list**.

---

# A Method Can Have No Parameters

Some methods don't need any input.

Example:

```java
public static void sayHello() {
    System.out.println("Hello!");
}
```

Notice the parentheses:

```java
()
```

They're empty.

This means the method doesn't require any information from whoever calls it.

---

# A Method Can Have One Parameter

Example:

```java
public static void greetUser(String name) {
    System.out.println("Hello, " + name);
}
```

Parameter list:

```java
(String name)
```

This method expects one piece of information:

* Type: `String`
* Name: `name`

---

# A Method Can Have Multiple Parameters

Example:

```java
public static int calculateSum(int a, int b) {
    return a + b;
}
```

Parameter list:

```java
(int a, int b)
```

There are two parameters.

| Type  | Name |
| ----- | ---- |
| `int` | `a`  |
| `int` | `b`  |

Notice that the parameters are separated by a comma.

---

# Every Parameter Has Two Parts

Every parameter consists of:

1. A **type**
2. A **name**

Example:

```java
String name
```

Break it down:

```text
String  → type
name    → parameter name
```

Another example:

```java
int age
```

Break it down:

```text
int  → type
age  → parameter name
```

---

# Different Types of Parameters

Baeldung says:

> **A parameter can be an object, a primitive or an enumeration.**

Based on what you've learned so far, let's focus on the examples you've already seen.

Primitive parameter:

```java
int age
```

Object parameter:

```java
String name
```

The article also mentions **enumerations**, but since it doesn't explain them here, you only need to know that Java allows them as parameter types. We'll study enums when your course introduces them.

---

# How Many Parameters Can a Method Have?

Baeldung mentions an interesting fact:

> **A method can have anywhere from 0 to 255 parameters.**

Examples:

No parameters:

```java
printMessage()
```

One parameter:

```java
printMessage(String message)
```

Two parameters:

```java
calculateSum(int a, int b)
```

Technically, Java allows up to **255** parameters.

In practice, however, most methods use only a few.

---

# Parentheses Always Exist

Notice something important.

Even when there are no parameters, the parentheses are still required.

Correct:

```java
sayHello()
```

Incorrect:

```java
sayHello
```

The parentheses tell Java that you're dealing with a method.

---

# Summary

From Baeldung:

* The **parameter list** provides the inputs a method needs.
* It is written inside parentheses `()`.
* A method can have:

  * 0 parameters
  * 1 parameter
  * many parameters (up to 255)
* Each parameter has:

  * a type
  * a name
* Parameters are separated by commas.

---

# 📝 Knowledge Check

Try these without looking back.

### Question 1

What is the parameter list?

---

### Question 2

How many parameters does this method have?

```java
public static void printMessage() {

}
```

---

### Question 3

Identify the parameters.

```java
public static int add(int first, int second) {

}
```

---

### Question 4

Every parameter consists of which two parts?

---

### Question 5

According to Baeldung, what is the maximum number of parameters a method can have?

---

## 📌 Progress Tracker

You've now completed **5 of the 6 parts** of a Java method:

| Part                | Status     |
| ------------------- | ---------- |
| ✅ Access modifier   | Complete   |
| ✅ Return type       | Complete   |
| ✅ Method identifier | Complete   |
| ✅ Parameter list    | Complete   |
| ⏳ Exception list    | Next       |
| ⏳ Method body       | After that |

After the next two sections, you'll have covered **all six components** exactly as presented in your Baeldung resource. Then we'll move on to **Method Signatures**, which is the next major topic in your course.





# 📚 Lesson 2 – Part 5 & Part 6

## Exception List & Method Body

**Based entirely on the Baeldung article "Methods in Java".**

---

# 🎯 Learning Objectives

By the end of this lesson, you should be able to:

* Explain what an exception list is.
* Recognise the `throws` keyword.
* Understand that the exception list is optional.
* Explain what the method body is.
* Understand where the method's logic is written.
* Know when a method body must contain a `return` statement.

---

# Part 5 – Exception List

Baeldung says:

> **We can specify which exceptions are thrown by a method by using the `throws` clause.**

Let's understand that sentence.

---

## What is an Exception List?

An **exception list** tells Java that a method **may throw an exception** while it is running.

The exception list comes **after the parameter list**.

Example from Baeldung:

```java
public void writeName(String name) throws IOException {
    PrintWriter out = new PrintWriter(new FileWriter("OutFile.txt"));
    out.println("Name: " + name);
    out.close();
}
```

Let's identify the parts.

```text
public                → Access modifier
void                  → Return type
writeName             → Method identifier
(String name)         → Parameter list
throws IOException    → Exception list
{ ... }               → Method body
```

Notice where the exception list appears:

```java
(String name) throws IOException
```

It comes **after the parameter list** and **before the method body**.

---

## Is the Exception List Required?

No.

Baeldung lists it as an **optional** part of a method.

Many methods don't have one.

Example:

```java
public static void greetUser(String name) {
    System.out.println("Hello " + name);
}
```

There is no exception list here.

This is perfectly valid.

---

## The `throws` Keyword

Baeldung explains that we use the keyword:

```java
throws
```

to introduce the exception list.

Example:

```java
throws IOException
```

At this stage, you do **not** need to understand what an `IOException` is.

Your resource simply introduces the syntax.

You'll learn about exceptions in a later module.

---

## Key Takeaway

For now, remember:

* The exception list is optional.
* It begins with the keyword `throws`.
* It appears after the parameter list.
* It lists exceptions that the method may throw.

---

# Part 6 – Method Body

Baeldung says:

> **The last part of a Java method is the method body, which contains the logic we want to execute.**

This is the part you'll spend the most time writing as a programmer.

---

## What is the Method Body?

The **method body** is the code inside the curly braces.

Example:

```java
public static void sayHello() {

    System.out.println("Hello");

}
```

Everything inside:

```java
{

    System.out.println("Hello");

}
```

is the method body.

---

## What Does the Method Body Contain?

Baeldung says:

> **The method body contains the logic we want to execute.**

That means the instructions that perform the method's task.

Example:

```java
public static int add(int a, int b) {

    return a + b;

}
```

The method body performs the addition and returns the result.

---

## Can a Method Body Be Empty?

Baeldung says:

> **We can write as many lines of code as we want — or none at all.**

Example:

```java
public static void doNothing() {

}
```

This is a valid method.

It simply has an empty body.

---

## Return Statements Inside the Method Body

Baeldung reminds us:

> **If a method declares a return type, then the method body must contain a return statement.**

Example:

```java
public static String getGreeting() {

    return "Hello";

}
```

The method body contains the required `return` statement.

Now compare it with this:

```java
public static String getGreeting() {

    System.out.println("Hello");

}
```

This is **not valid** because the method promises to return a `String`, but it never does.

---

## Putting Everything Together

Let's identify every part of this method:

```java
public static String greetUser(String name) throws IOException {
    return "Hello, " + name;
}
```

| Part              | Value                          |
| ----------------- | ------------------------------ |
| Access modifier   | `public`                       |
| `static` keyword  | `static`                       |
| Return type       | `String`                       |
| Method identifier | `greetUser`                    |
| Parameter list    | `(String name)`                |
| Exception list    | `throws IOException`           |
| Method body       | `{ return "Hello, " + name; }` |

Congratulations—you can now recognise every part of a basic Java method.

---

# 📌 Lesson 2 Summary

Baeldung describes a Java method as having **six parts**.

| Part              | Required?  |
| ----------------- | ---------- |
| Access modifier   | ❌ Optional |
| Return type       | ✅ Required |
| Method identifier | ✅ Required |
| Parameter list    | ❌ Optional |
| Exception list    | ❌ Optional |
| Method body       | ✅ Required |

Remember that **`static` is not one of the six parts**. Baeldung discusses it alongside the access modifier because it's another keyword that can appear in a method declaration.

---

# 📝 Lesson 2 Knowledge Check

Try these without looking back.

### Question 1

Identify every part of this method.

```java
private static int calculateSum(int a, int b) {

    return a + b;

}
```

---

### Question 2

Which parts of a method are optional?

---

### Question 3

What keyword introduces the exception list?

---

### Question 4

Where does the exception list appear?

A. Before the return type

B. After the parameter list

C. Inside the method body

---

### Question 5

What does the method body contain?

---

### Question 6

True or False?

A method with return type `String` may have an empty method body.

---

## 🎯 End of Lesson 2

You've now completed **all of Baeldung's "Method Syntax"** section.

### What you've mastered:

* ✅ Access modifier
* ✅ `static` keyword (as introduced by Baeldung)
* ✅ Return type
* ✅ Method identifier
* ✅ Parameter list
* ✅ Exception list
* ✅ Method body

The next lesson is one of the most important in your course:

# **Lesson 3 – Method Signatures**

This is where we'll answer one of your workshop questions directly:

> **"What are the components of a method signature? Are any of them optional?"**

We'll also learn why Java defines a method signature as **only the method name and parameter list**, even though a method declaration contains much more information. This lesson will prepare you for both your exercises and your workshop discussion.

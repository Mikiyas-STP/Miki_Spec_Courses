# 📚 Lesson 3 – Method Signatures

**Based entirely on:**

* Baeldung – *Methods in Java*
* Your learning objectives

---

# 🎯 Learning Objectives

By the end of this lesson, you should be able to:

* Explain what a method signature is.
* Identify the components of a method signature.
* Explain which parts are **not** part of a method signature.
* Read a method signature.
* Understand the workshop question:

  > **What are the components of a method signature? Are any of them optional?**

---

# What Baeldung Says

Baeldung gives the definition:

> **A method signature is comprised of only two components — the method's name and parameter list.**

This sentence is one of the most important in this topic.

Notice the word:

> **only**

That means everything else we've learned **is not part of the method signature**.

---

# What Is a Method Signature?

A **method signature** is **not** the entire method.

Instead, it is just a way of identifying a method using:

1. **Method name**
2. **Parameter list**

Nothing else.

---

# Think Back to Lesson 2

We learned that a method declaration can contain:

```text
Access modifier
Return type
Method identifier
Parameter list
Exception list
Method body
```

Now Baeldung tells us:

A **method signature** is much smaller.

It contains only:

```text
Method identifier
+
Parameter list
```

---

# Example 1

Consider this method:

```java
public static String greetUser(String name) {
    return "Hello " + name;
}
```

Let's identify everything.

| Part              | Value           |
| ----------------- | --------------- |
| Access modifier   | `public`        |
| `static`          | `static`        |
| Return type       | `String`        |
| Method identifier | `greetUser`     |
| Parameter list    | `(String name)` |
| Method body       | `{ ... }`       |

Now the question is:

**What is the method signature?**

Answer:

```text
greetUser(String name)
```

Notice what disappeared.

There is **no**:

* `public`
* `static`
* `String`
* method body

Only:

* method name
* parameter list

---

# Example 2

```java
private int calculateSum(int a, int b) {

    return a + b;

}
```

The signature is:

```text
calculateSum(int a, int b)
```

Again:

Everything else is ignored.

---

# Example 3

```java
void printMessage() {

}
```

Signature:

```text
printMessage()
```

Even an empty parameter list is still part of the signature.

---

# What Is NOT Part of the Signature?

Baeldung's definition lets us answer this directly.

The following are **not** part of a method signature:

❌ Access modifier

```java
public
```

❌ `static`

```java
static
```

❌ Return type

```java
String
```

❌ `throws`

```java
throws IOException
```

❌ Method body

```java
{

}
```

Only these remain:

✅ Method name

✅ Parameter list

---

# Reading a Signature

Suppose someone writes:

```text
calculateSum(int first, int second)
```

Without seeing the full method, you already know:

Method name:

```text
calculateSum
```

Parameters:

```text
int first

int second
```

You do **not** know:

* whether it's `public`
* whether it's `private`
* whether it's `static`
* what it returns

Because those things are **not part of the signature**.

---

# Parameter Names vs Parameter Types

Look carefully at this method:

```java
public int add(int a, int b) {

}
```

Signature:

```text
add(int a, int b)
```

Now another method:

```java
public int add(int first, int second) {

}
```

Signature:

```text
add(int first, int second)
```

Notice something.

The **parameter names changed**.

The **parameter types stayed the same**.

Baeldung includes the full parameter list in the signature, including the names, because it's describing the declaration as written. However, from Java's perspective when distinguishing overloaded methods, it's the **method name and parameter types** that matter, not the parameter names. Your course doesn't go into that compiler detail here, so for this lesson, follow Baeldung's simpler definition:

> A method signature consists of the method name and the parameter list.

---

# Why Is This Important?

Your workshop asks:

> **What are the components of a method signature?**

You can now answer:

> A method signature consists of **the method name (method identifier)** and **the parameter list**.

---

# Are Any Components Optional?

Another workshop question asks:

> **Are any of them optional?**

Let's think.

A method signature has:

1. Method name
2. Parameter list

Can a method exist without a name?

No.

Can a method exist without parentheses?

No.

Even if there are no parameters:

```java
printMessage()
```

the parameter list still exists.

It is simply empty.

Therefore:

**Neither component is optional.**

The parameter list may be **empty**, but it is still present.

---

# Summary

According to Baeldung:

A method signature contains only:

* Method identifier
* Parameter list

It does **not** include:

* Access modifier
* `static`
* Return type
* Exception list
* Method body

Both parts of the signature are required.

---

# 📝 Knowledge Check

## Question 1

What is the method signature?

```java
public static void greet() {

}
```

---

## Question 2

What is the method signature?

```java
private String getName(String firstName, String lastName) {

}
```

---

## Question 3

Which of these are part of a method signature?

* Access modifier
* Return type
* Method identifier
* Parameter list
* Method body

---

## Question 4

True or False?

The return type is part of the method signature.

---

## Question 5

Answer the workshop question in your own words:

> **What are the components of a method signature? Are any of them optional?**

---

## 📌 End of Lesson 3

This lesson completes the core concept of **method signatures**, one of the main learning objectives in your course.











# 📚 Lesson 4 – Calling Methods & `static` vs Instance Methods

**Based only on your Baeldung resource**

---

# 🎯 Learning Objectives

By the end of this lesson, you should be able to:

* Call a method in Java
* Understand the difference between **static methods** and **instance methods**
* Explain why `main()` can call some methods directly
* Recognise when you need to create an object to call a method

---

# 1. What Does “Calling a Method” Mean?

Baeldung says:

> A method is a block of code which only runs when it is called.

So far, you've only **defined methods**.

Now we focus on:

> 👉 actually running them

---

# Think of it like this

A method is like a **machine in a factory**.

* You build the machine → defining a method
* You press a button → calling the method
* The machine runs → execution happens

---

# 2. Basic Method Call

Baeldung example:

```java id="m9kq3x"
static void myMethod() {
    System.out.println("I just got executed!");
}
```

To call it:

```java id="x3l9pn"
public static void main(String[] args) {
    myMethod();
}
```

---

# What is happening?

When Java sees:

```java id="h4k2qz"
myMethod();
```

It:

1. Finds the method named `myMethod`
2. Executes its body
3. Returns back to `main`

---

# 3. Calling a Method Multiple Times

Baeldung shows:

```java id="c8m2wr"
public static void main(String[] args) {
    myMethod();
    myMethod();
    myMethod();
}
```

### What happens?

Output:

```
I just got executed!
I just got executed!
I just got executed!
```

---

# Key idea

A method is **reusable code**.

You don’t rewrite logic — you just call it again.

---

# 4. Static Methods (Very Important)

Baeldung explains:

> `static` means the method belongs to the class and not to instances.

---

# What does that mean in practice?

If a method is `static`:

```java id="n2m8qp"
public static void greet() {
    System.out.println("Hello");
}
```

You can call it directly:

```java id="v5p0kc"
greet();
```

or with the class name:

```java id="t8q3lm"
Main.greet();
```

---

# Why is this important?

Because `main()` is also `static`.

```java id="q9w1rx"
public static void main(String[] args)
```

So it can directly call other static methods.

---

# 5. Instance Methods (Non-static)

Baeldung contrast:

> Methods without `static` are instance methods and must be called on an object.

Example:

```java id="z1k8vc"
public void greet() {
    System.out.println("Hello");
}
```

---

# How do you call this?

You cannot do:

```java id="a9p3ld"
greet(); // ❌ error
```

Instead:

### Step 1: Create an object

```java id="b2m7xq"
Person person = new Person();
```

### Step 2: Call the method

```java id="k8w1dz"
person.greet();
```

---

# Why do we need an object?

Because the method belongs to an **instance**, not the class.

Think:

| Type            | Belongs to |
| --------------- | ---------- |
| static method   | Class      |
| instance method | Object     |

---

# 6. Full Example (Baeldung style)

```java id="r3n8kp"
public class Person {

    public void greet() {
        System.out.println("Hello");
    }

    public static void main(String[] args) {
        Person person = new Person();
        person.greet();
    }
}
```

---

# What is happening step-by-step?

1. JVM starts `main`
2. `Person person = new Person()` creates an object
3. `person.greet()` calls instance method
4. Method runs and prints "Hello"

---

# 7. Static vs Instance – Core Difference

Let’s make this crystal clear:

## Static method

```java id="s8m1qv"
public static void test() {
    System.out.println("Static");
}
```

Call:

```java id="l3p9wx"
test();
```

or

```java id="c7v2nm"
ClassName.test();
```

---

## Instance method

```java id="u4k8zd"
public void test() {
    System.out.println("Instance");
}
```

Call:

```java id="p9x1rm"
ClassName obj = new ClassName();
obj.test();
```

---

# 8. Baeldung’s Key Memory Insight (Simplified)

Baeldung mentions:

> Static methods are loaded into memory once during class loading.

You don’t need deep memory knowledge yet.

Just remember:

> Static methods are simpler to call because they don’t depend on objects.

---

# 🧠 Mental Model (Very Important)

Think like this:

### Static = global tool

You just use it directly.

---

### Instance = personal tool

You must first create it.

---

# 📝 Quick Check

### Q1

What happens when you call a method?

---

### Q2

Why can `main()` call static methods directly?

---

### Q3

What is required to call an instance method?

---

### Q4

Which is correct?

A:

```java
greet();
```

B:

```java
Person.greet();
```

C:

```java
Person p = new Person();
p.greet();
```

(Choose based on instance vs static)

---

### Q5

What is the main difference between static and instance methods?

---

# 📌 End of Lesson 4

You now understand:

* How methods are executed
* How to call methods
* Static vs instance behaviour
* Why objects are sometimes required

---

# 🚀 Next Lesson (Lesson 5 Preview)

Next we move to:

## 👉 Method Overloading (Baeldung section 5)

You will learn:

* Why Java allows multiple methods with the same name
* How parameter lists create uniqueness
* Real-world use cases (very important for interviews and clean code)

This is where your understanding of **method signatures becomes very powerful in practice**.







Good — we’ll continue.

---

# 📚 Lesson 5 – Method Overloading (Baeldung Section 5)

This is one of the most important concepts for writing clean Java code and understanding real-world APIs.

---

# 🎯 Learning Objectives

By the end of this lesson, you should be able to:

* Explain what method overloading is
* Understand why Java allows multiple methods with the same name
* Identify how Java distinguishes overloaded methods
* Write simple overloaded methods correctly
* Understand the role of the **parameter list in uniqueness**

---

# 1. What is Method Overloading?

Baeldung says:

> Java allows us to have two or more methods with the same identifier but different parameter list.

---

## Simple definition

Method overloading means:

> Same method name, different parameters.

---

## Example idea first

Think of a `print()` function:

* print text
* print number
* print two numbers

Same action idea → different inputs

---

# 2. Basic Example

Baeldung-style example:

```java id="a1m9qp"
public String getName(String firstName, String lastName) {
    return firstName + " " + lastName;
}
```

Now overloaded version:

```java id="b8x3kc"
public String getName(String firstName, String middleName, String lastName) {
    return firstName + " " + middleName + " " + lastName;
}
```

---

# What changed?

| Method | Parameters               |
| ------ | ------------------------ |
| 1      | (String, String)         |
| 2      | (String, String, String) |

Same name → `getName`
Different parameter list → allowed

---

# 3. Why is this allowed?

Because Java identifies methods using:

> Method signature = name + parameter list

So:

```text id="m1k9wp"
getName(String, String)
getName(String, String, String)
```

These are considered **different methods**.

---

# 4. Key Rule (Very Important)

Baeldung implies this clearly:

> Overloaded methods MUST differ in parameter list

That means:

✔ Allowed:

```java id="c9x1ld"
sum(int a, int b)
sum(double a, double b)
```

✔ Allowed:

```java id="q7m2nx"
sum(int a, int b)
sum(int a, int b, int c)
```

---

❌ Not allowed:

```java id="v3p8ld"
int sum(int a, int b)
double sum(int a, int b)
```

Why?

Because parameter list is the same → Java cannot distinguish them.

---

# 5. What Overloading is NOT

This is a common confusion.

---

## NOT overloading:

Only changing return type:

```java id="x8k2mp"
int add(int a, int b)

double add(int a, int b) // ❌ not allowed
```

Baeldung concept:

> Return type is NOT part of the method signature

So Java ignores it for overloading.

---

# 6. Real Example from Practice

```java id="p4m8qv"
public int add(int a, int b) {
    return a + b;
}

public int add(int a, int b, int c) {
    return a + b + c;
}
```

---

# How Java decides which one to call

```java id="t9x2lm"
add(2, 3);
```

→ calls 2-parameter version

```java id="h5k8vd"
add(2, 3, 4);
```

→ calls 3-parameter version

---

# 7. Why Overloading is Useful

Baeldung says:

> It is useful for simplified versions of the same functionality.

---

## Real-world analogy

Think of a coffee machine:

* coffee()
* coffee(with milk)
* coffee(with milk, sugar)

Same action → different options

---

# 8. Good Design Rule (Baeldung Insight)

Baeldung warns:

> Overloaded methods should behave in a similar manner.

---

## Why?

Bad design example:

```java id="m8q1xv"
getData(String name)
getData(int id)
```

But:

* one returns user info
* other deletes data ❌

That becomes confusing.

---

## Good design example:

```java id="k2v9ld"
getData(String name)
getData(int id)
```

Both:

* fetch data
* just different input types

---

# 9. Mental Model

Think:

| Same name        | Same purpose                        |
| ---------------- | ----------------------------------- |
| different inputs | different ways to perform same task |

---

# 🧠 Key Exam / Interview Insight

If someone asks:

> Why does Java support method overloading?

You answer:

> To allow multiple methods with the same name but different parameter lists, improving readability and flexibility while keeping related functionality grouped together.

---

# 📝 Quick Check

### Q1

What defines method overloading?

---

### Q2

Which part must be different for overloading to work?

---

### Q3

Is this valid?

```java id="r8m2qp"
int sum(int a, int b)
double sum(int a, int b)
```

Why?

---

### Q4

What will Java use to decide which overloaded method to call?

---

### Q5

Why is overloading useful in real applications?

---

# 📌 End of Lesson 5

You now understand:

* Method overloading concept
* Role of parameter list in uniqueness
* Why return type is ignored
* How Java chooses methods at runtime
* Design rules for clean overloading

---

# 🚀 Next Lesson (Lesson 6 Preview)

Next we move to:

## 👉 JavaDoc (from your Baeldung resource)

You will learn:

* What JavaDoc is
* Why documentation matters in real projects
* How to document methods properly
* Tags like:

  * `@param`
  * `@return`
  * `@throws`

This is a **professional-level skill** used in real companies, not just learning Java.





Good — now we move into the final part of your resource.

---

# 📚 Lesson 6 – JavaDoc (Baeldung Section: Introduction to Javadoc)

This is where you learn how professional Java code is documented so other engineers can understand and maintain it.

---

# 🎯 Learning Objectives

By the end of this lesson, you should be able to:

* Explain what JavaDoc is
* Understand who it is for and why it matters
* Write basic JavaDoc comments
* Use common tags like:

  * `@param`
  * `@return`
  * `@throws`
* Recognise JavaDoc structure in real methods and classes

---

# 1. What is JavaDoc?

Baeldung says:

> Javadoc is a tool for generating API documentation from comments present in source code.

---

## Simple explanation

JavaDoc is:

> A way of writing special comments that can be turned into documentation.

---

## Think of it like this

Normal comments:

```java id="c1m9qz"
// adds two numbers
```

JavaDoc comments:

```java id="x9k2ld"
/**
 * Adds two numbers and returns the result.
 */
```

---

# 2. Why do we use JavaDoc?

Baeldung says:

> Good API documentation contributes to the success of a software project.

---

## Real-world reason

You are not coding alone.

In real teams:

* Other developers read your code
* You may read your own code months later
* Large systems need clear documentation

---

## JavaDoc helps answer:

* What does this method do?
* What does it take as input?
* What does it return?
* What can go wrong?

---

# 3. JavaDoc Syntax

Baeldung shows:

```java id="m8q1wp"
/**
 * This is a Javadoc comment
 */
```

---

## Key rule

JavaDoc always starts with:

```text id="a9v3ld"
/**
```

and ends with:

```text id="k2m8qp"
*/
```

---

# 4. Where do we use JavaDoc?

Baeldung says:

You can place JavaDoc on:

* Classes
* Fields
* Methods

---

# 5. JavaDoc at Method Level (Most Important)

Example:

```java id="t9x1ld"
/**
 * Adds two integers and returns the result.
 *
 * @param a first number
 * @param b second number
 * @return sum of a and b
 */
public int add(int a, int b) {
    return a + b;
}
```

---

## Break it down

### Description section

```text id="d1k9qp"
Adds two integers and returns the result.
```

This explains **what the method does**.

---

### `@param`

```text id="p8m2ld"
@param a first number
@param b second number
```

Explains inputs.

---

### `@return`

```text id="r7x1qp"
@return sum of a and b
```

Explains output.

---

# 6. JavaDoc at Class Level

Example:

```java id="c9m1qp"
/**
 * Represents a simple calculator that performs basic operations.
 */
public class Calculator {
}
```

---

## Purpose

Explains:

> what the class is for

---

# 7. JavaDoc at Field Level

Example:

```java id="f8k2ld"
/**
 * Stores the user's name
 */
private String name;
```

---

Note from Baeldung:

> Private fields are not included unless explicitly configured

---

# 8. Common JavaDoc Tags

Baeldung highlights these:

| Tag           | Meaning                |
| ------------- | ---------------------- |
| `@param`      | describes method input |
| `@return`     | describes output       |
| `@throws`     | describes exceptions   |
| `@see`        | links related code     |
| `@since`      | version added          |
| `@deprecated` | outdated code          |

---

# 9. Example with `@throws`

From Baeldung:

```java id="z8m2qp"
/**
 * Writes a name to a file.
 *
 * @param name user name
 * @throws IOException if file cannot be written
 */
public void writeName(String name) throws IOException {
}
```

---

# 10. Key Idea: What JavaDoc is REALLY for

Baeldung emphasises:

> It describes the WHY, not just the WHAT.

---

## Bad documentation:

```java id="x2m9ld"
/**
 * This method adds two numbers.
 */
```

This is obvious from the code.

---

## Good documentation:

```java id="v8k1qp"
/**
 * Adds two numbers to support financial calculations
 * where precision and consistency are required.
 */
```

This explains WHY it exists.

---

# 11. JavaDoc Generation (Conceptual)

Baeldung mentions tools:

* `javadoc` command
* Maven plugin

You don’t need to master this yet.

Just understand:

> JavaDoc comments can be automatically turned into documentation pages.

---

# 🧠 Mental Model

Think of JavaDoc as:

> A professional instruction manual for your code

Not for the computer — for **other engineers**

---

# 📝 Quick Check

### Q1

What is JavaDoc?

---

### Q2

Who is JavaDoc written for?

---

### Q3

What does `@param` describe?

---

### Q4

What is the purpose of `@return`?

---

### Q5

What should JavaDoc explain according to Baeldung?

---

# 📌 End of Lesson 6

You now understand:

* JavaDoc concept
* Why documentation matters
* Syntax structure
* Common tags
* How professionals document methods and classes

---

# 🎉 Full Module Complete: Methods in Java

You’ve now covered:

* Method structure
* Method signatures
* Calling methods
* Static vs instance methods
* Method overloading
* JavaDoc

---

# 🚀 Next Step (Important)

If you want to level up like a real junior backend engineer, I suggest next:
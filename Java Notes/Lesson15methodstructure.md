
# 📚 Lesson 2 – Method Structure (Based on Baeldung)

## 🎯 Learning Objectives

By the end of this lesson, you should be able to:

* Identify all six parts of a Java method.
* Explain the purpose of each part.
* Know which parts are optional.
* Read a method from left to right.

---

## What Baeldung Says

Baeldung states that a Java method consists of **six parts**:

1. Access modifier *(optional)*
2. Return type
3. Method identifier
4. Parameter list *(optional)*
5. Exception list *(optional)*
6. Method body

We'll use this method throughout the lesson:

```java
public static String greetUser(String name) throws IOException {
    return "Hello, " + name;
}
```

Don't worry if you don't recognise every keyword yet. By the end of this lesson, you'll understand what each part is for.

---

## The Six Parts at a Glance

| Part              | Example              | Required? |
| ----------------- | -------------------- | --------- |
| Access modifier   | `public`             | No        |
| Return type       | `String`             | Yes       |
| Method identifier | `greetUser`          | Yes       |
| Parameter list    | `(String name)`      | No        |
| Exception list    | `throws IOException` | No        |
| Method body       | `{ ... }`            | Yes       |

One thing to notice immediately is that **not every part is required**.

Some methods won't have parameters.

Some won't throw exceptions.

Some won't specify an access modifier.

But **every method must have**:

* a return type (`void` counts as a return type),
* a method name,
* and a body.

We'll explore each part one at a time in the next sections of Lesson 2, starting with **access modifiers**, exactly in the order your Baeldung resource presents them. This keeps us aligned with your course while making each concept easier to digest before moving on.



---

# 📚 Lesson 2 – Method Structure

## Part 1 – Access Modifier

Baeldung says:

> **Access modifier: optionally we can specify from where in the code one can access the method.**

Let's unpack that sentence.

---

# What is an Access Modifier?

An **access modifier** tells Java:

> **Who is allowed to use this method?**

Think of it as setting permissions.

Imagine you have a room in your house.

You can decide who is allowed to enter.

```
🚪 Room

Everyone        ✅
Family only     ✅
Only me         ✅
Nobody          ❌
```

An access modifier does the same thing for methods.

It controls **who can call the method**.

---

# Is it Required?

No.

Baeldung specifically says it is **optional**.

If you don't write one:

```java
void sayHello() {

}
```

Java gives the method **default (package-private)** access.

You don't need to understand package-private yet. The important thing from the resource is:

> Access modifiers are optional.

---

# Common Access Modifiers

Baeldung mentions four:

| Modifier    | Meaning                               |
| ----------- | ------------------------------------- |
| `public`    | Accessible from anywhere              |
| `protected` | Accessible in certain related classes |
| `private`   | Accessible only inside the same class |
| *(default)* | Accessible within the same package    |

For now, just recognise these names. Your exercises will mainly use `public` and `private`.

---

# Example 1

```java
public static void sayHello() {

}
```

Here:

```
public
```

is the access modifier.

---

# Example 2

```java
private static int calculateSum(int a, int b) {

}
```

Here:

```
private
```

is the access modifier.

---

# Example 3

```java
static void printMessage() {

}
```

Notice something.

There is **no** access modifier.

This is still valid Java.

That is why Baeldung says the access modifier is optional.

---

# Check Your Understanding

Identify the access modifier.

### Example A

```java
public void login() {

}
```

Answer:

```
public
```

---

### Example B

```java
private int calculateAge() {

}
```

Answer:

```
private
```

---

### Example C

```java
void print() {

}
```

Answer:

No access modifier has been written.

---

# Baeldung's Note About `static`

Immediately after explaining access modifiers, Baeldung introduces something else.

It says:

> A method can also include the `static` keyword before or after the access modifier.

Example:

```java
public static void sayHello() {

}
```

or

```java
static public void sayHello() {

}
```

Both are valid Java.

However,

Baeldung also notes that **`public static` is the common style**, and that's the style you'll see almost everywhere.

---

# What Does `static` Mean?

Baeldung says:

> The method belongs to the class and not to the instances.

This is exactly the same explanation you saw in W3Schools.

At this stage, that's enough.

You'll study classes and objects later, so we won't go beyond what the resource says.

---

# Static vs Non-static

Baeldung compares two kinds of methods.

## Static method

```java
public static void print() {

}
```

Baeldung says:

> We can call this method **without creating an object**.

---

## Instance method

```java
public void print() {

}
```

Baeldung says:

> This method may only be invoked on an instance of the class.

Again, don't worry about objects yet. The key takeaway from the resource is:

* `static` methods can be called directly using the class name.
* Methods without `static` require an object.

We'll revisit this when we study classes.

---

# Memory Note (from Baeldung)

Baeldung briefly mentions:

> Static methods are loaded into memory once during class loading.

You do **not** need to memorise this.

It's simply explaining one reason why static methods can be more memory-efficient.

Since your course hasn't introduced memory management yet, it's enough to know that Baeldung mentions it as background information.

---

# Summary

From this section of the resource:

* An **access modifier** controls who can access a method.
* Access modifiers are **optional**.
* The four access modifiers are:

  * `public`
  * `protected`
  * `private`
  * default (package-private)
* A method may also include the `static` keyword.
* `static` means the method belongs to the class rather than an object.

---

# 📝 Quick Check

Without looking back, answer these:

1. Is an access modifier required for every method?

2. Name the four access modifiers mentioned by Baeldung.

3. According to Baeldung, what does the `static` keyword mean?

4. Which is the common style?

```java
static public void print()
```

or

```java
public static void print()
```

---

## Next Part

We'll continue with **Return Type**, where Baeldung explains:

* What a return type is.
* Why `void` is a return type.
* Why methods with a return type must use `return`.
* What happens after a `return` statement executes.

This section is especially important because it directly prepares you for **Exercise 3.1 (`greetUser`)** and **Exercise 3.2 (`calculateSum`)**, where you'll write methods that return values.

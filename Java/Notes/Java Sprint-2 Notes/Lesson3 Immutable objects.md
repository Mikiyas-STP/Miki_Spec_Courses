This article introduces **immutability**, which is an important concept in Java but is often explained in a confusing way. Here's a simpler version that keeps all the key ideas.

---

# Immutable Objects in Java (Simple Version)

## 1. What is an Immutable Object?

### Definition

An **immutable object** is an object whose data **cannot be changed after it is created**.

Once you create it, its state stays the same for its entire lifetime.

### Simple Example

Imagine a birth certificate.

Once it's issued, you don't change:

* name
* date of birth
* place of birth

If something changes, you create a new document instead of modifying the old one.

An immutable object works the same way.

---

## 2. Example with `String`

`String` is one of Java's most common immutable classes.

```java
String name = "baeldung";

String newName = name.replace("dung", "----");
```

You might think `replace()` changes `name`.

It doesn't.

After this code:

```java
System.out.println(name);
```

Output:

```
baeldung
```

And:

```java
System.out.println(newName);
```

Output:

```
bael----
```

The original string never changed.

Instead, Java created **a new String object**.

---

## 3. What Does `final` Mean?

The article explains `final` because many beginners confuse it with immutability.

### Definition

`final` means **the variable cannot point to a different object after it has been assigned**.

Example:

```java
final String name = "Mike";
```

This is **not allowed**:

```java
name = "John";   // Compile-time error
```

The variable must always refer to the same object.

---

## 4. Does `final` Make an Object Immutable?

**No.**

This is one of the most important ideas in the article.

Example:

```java
final List<String> names = new ArrayList<>();
```

You cannot do:

```java
names = new ArrayList<>();
```

But you **can** do:

```java
names.add("Mike");
```

The list changes.

So:

* the **reference** is fixed ✔️
* the **object itself** can still change ❌

Therefore:

> `final` does **not** automatically make an object immutable.

---

## 5. How Do We Create an Immutable Class?

An immutable class follows a few simple rules.

### Rule 1: Make fields `private`

```java
private double amount;
```

This prevents other classes from changing them directly.

---

### Rule 2: Make fields `final`

```java
private final double amount;
```

Now they can only be assigned once.

---

### Rule 3: Initialise fields in the constructor

```java
public Money(double amount) {
    this.amount = amount;
}
```

The value is set when the object is created.

---

### Rule 4: Don't provide setters

Bad:

```java
public void setAmount(double amount) {
    this.amount = amount;
}
```

Good:

No setter at all.

Once created, the value never changes.

---

### Rule 5: Only provide getters

```java
public double getAmount() {
    return amount;
}
```

Users can read the value but cannot change it.

---

## Example of an Immutable Class

```java
class Money {

    private final double amount;

    public Money(double amount) {
        this.amount = amount;
    }

    public double getAmount() {
        return amount;
    }
}
```

Usage:

```java
Money salary = new Money(5000);
```

You can read it:

```java
salary.getAmount();
```

But you cannot change it because there is no setter.

---

## 6. Primitive Types vs Objects

The article mentions an important difference.

### Primitive

```java
private final int age;
```

Since `int` is a primitive, Java guarantees it cannot change after construction.

---

### Object Reference

```java
private final Currency currency;
```

`currency` is an object.

`final` only guarantees that the reference won't change.

If the `Currency` class itself is mutable, its internal data could still change.

So immutability also depends on the objects your class contains.

---

## 7. Reflection

The article briefly mentions **reflection**.

Reflection is a special Java feature that allows code to inspect and even modify objects at runtime.

It can sometimes break immutability by changing private fields.

However:

* it bypasses the normal rules,
* it is rarely used in everyday programming,
* you don't need to worry about it as a beginner.

---

## 8. Why Are Immutable Objects Useful?

### They are thread-safe

If multiple threads use the same object:

```text
Thread A

Thread B

Thread C
```

None of them can change it.

So they cannot accidentally interfere with each other.

---

### They have no side effects

A **side effect** means changing something unexpectedly.

Example of a mutable object:

```
Person A changes it.

↓

Person B suddenly sees different data.
```

That change is a side effect.

With immutable objects:

```
Person A reads it.

↓

Person B reads it.

↓

Nobody changes it.
```

Everyone always sees the same data.

---

## Key Takeaways

| Concept                   | Simple Meaning                                                                                             |
| ------------------------- | ---------------------------------------------------------------------------------------------------------- |
| **Immutable Object**      | An object that cannot change after it is created.                                                          |
| **String**                | A built-in immutable class. Methods like `replace()` create a new object instead of changing the original. |
| **`final` Variable**      | The variable cannot point to a different object after assignment.                                          |
| **`final` ≠ Immutable**   | A `final` reference can still point to a mutable object.                                                   |
| **Immutable Class Rules** | `private` fields, `final` fields, initialise in the constructor, no setters, getters only.                 |
| **Thread-safe**           | Multiple threads can safely share immutable objects because their state never changes.                     |
| **Side-effect free**      | Reading or passing the object around doesn't accidentally change its data.                                 |

### The One Idea to Remember

The most important distinction is:

* **`final` protects the variable (the reference).**
* **Immutability protects the object (its state).**

For example:

```java
final List<String> list = new ArrayList<>();
list.add("Java"); // ✅ Allowed
```

The reference `list` never changes, but the `ArrayList` object does.

By contrast:

```java
String text = "Java";
text.replace("Java", "Python");
```

The original `String` object remains unchanged because `String` is immutable. `replace()` returns a **new** `String` object instead of modifying the existing one. This difference is the essence of immutability in Java.

# 📚 Session 5 — `for` Loops

## Learning Objectives

By the end of this session, you will be able to:

* Explain why loops exist.
* Understand every part of a `for` loop.
* Trace a loop step by step.
* Write loops that count up and down.
* Use `if` statements inside loops.
* Understand the enhanced `for` loop.
* Know when to use a `for` loop instead of a `while` loop.

---

# 1. Why Do We Need Loops?

Imagine you want to print:

```text
Hello
Hello
Hello
Hello
Hello
```

Without a loop:

```java
System.out.println("Hello");
System.out.println("Hello");
System.out.println("Hello");
System.out.println("Hello");
System.out.println("Hello");
```

This works...

But what about **1,000 times**?

Not practical.

A loop lets us tell Java:

> **Repeat this code for me.**

Instead of writing the same code over and over, we write it once.

---

# Real-world Analogy

Imagine a teacher calling the register.

Without a loop:

```text
Call Student 1
Call Student 2
Call Student 3
...
Call Student 30
```

With a loop:

```text
Repeat until every student has been called.
```

The teacher follows the same process each time.

Programming loops work the same way.

---

# 2. Basic `for` Loop Syntax

```java
for (initialisation; condition; update) {

    // code to repeat

}
```

This looks confusing at first.

Let's break it down.

---

## Part 1 — Initialisation

Example:

```java
int i = 1;
```

This creates the loop variable.

Think of it as:

> "Where should I start counting?"

Example:

```java
for (int i = 1; ... )
```

means

Start counting at **1**.

---

## Part 2 — Condition

Example:

```java
i <= 10
```

Java asks:

> "Should I do another iteration?"

If the answer is

```text
true
```

the loop continues.

If

```text
false
```

the loop stops.

---

## Part 3 — Update

Example:

```java
i++
```

means

Increase `i` by one.

It's exactly the same as:

```java
i = i + 1;
```

or

```java
i += 1;
```

---

# Put Everything Together

```java
for (int i = 1; i <= 5; i++) {

    System.out.println(i);

}
```

---

# Step-by-Step Execution

This is how the JVM thinks.

### Step 1

```java
int i = 1;
```

Now:

```text
i = 1
```

---

Check condition:

```java
i <= 5
```

Is

```text
1 <= 5
```

Yes.

Run loop body.

Output:

```text
1
```

---

Update:

```java
i++
```

Now

```text
i = 2
```

---

Again:

```text
2 <= 5

↓

true

↓

Print 2

↓

i = 3
```

---

Again

```text
3 <= 5
```

Print

```text
3
```

---

Again

```text
4 <= 5
```

Print

```text
4
```

---

Again

```text
5 <= 5
```

Print

```text
5
```

---

Update

```text
i = 6
```

Now

```text
6 <= 5
```

False.

Loop ends.

---

Output

```text
1
2
3
4
5
```

---

# Visual Flow

```text
Start

↓

i = 1

↓

Condition?

↓

Yes

↓

Run body

↓

Increase i

↓

Condition?

↓

Yes

↓

Run body

↓

...

↓

Condition?

↓

No

↓

Finish
```

---

# 3. Why Is It Called `i`?

You'll often see:

```java
int i
```

`i` stands for **index** or **iterator**.

It simply keeps track of which iteration you're on.

You could write:

```java
for (int banana = 1; banana <= 5; banana++)
```

It works.

But everyone uses `i`.

It's a programming convention.

---

# 4. Counting Down

You don't have to count upwards.

```java
for (int i = 10; i >= 1; i--) {

    System.out.println(i);

}
```

Output

```text
10
9
8
...
1
```

Notice

```java
i--
```

means

Decrease by one.

---

# 5. Changing the Step

Normally

```java
i++
```

adds one.

You can increase by two.

```java
for (int i = 0; i <= 10; i += 2)
```

Output

```text
0
2
4
6
8
10
```

---

Increase by five.

```java
for (int i = 0; i <= 50; i += 5)
```

Output

```text
0
5
10
15
...
```

---

# 6. Using `if` Inside a Loop

This is where things become powerful.

```java
for (int i = 1; i <= 10; i++) {

    if (i % 2 == 0) {

        System.out.println(i);

    }

}
```

Output

```text
2
4
6
8
10
```

---

## What does `%` mean?

The `%` operator gives the **remainder** after division.

Examples:

```text
10 % 2 = 0
```

because

```text
10 ÷ 2 = 5 remainder 0
```

---

```text
9 % 2 = 1
```

because

```text
9 ÷ 2 = 4 remainder 1
```

---

Therefore

```java
i % 2 == 0
```

means

"The number divides evenly by 2."

In other words

**even number.**

---

# Odd Numbers

```java
if (i % 2 != 0)
```

Output

```text
1
3
5
7
9
```

---

# 7. Nested Loops

A loop inside another loop.

```java
for (int i = 1; i <= 3; i++) {

    for (int j = 1; j <= 2; j++) {

        System.out.println(i + " " + j);

    }

}
```

Output

```text
1 1
1 2
2 1
2 2
3 1
3 2
```

We'll use nested loops later for patterns and matrices.

---

# 8. Enhanced `for` Loop (For-each)

Suppose we have an array.

```java
int[] numbers = {10, 20, 30, 40};
```

Instead of

```java
for (int i = 0; i < numbers.length; i++) {

    System.out.println(numbers[i]);

}
```

we can write

```java
for (int number : numbers) {

    System.out.println(number);

}
```

Read it as:

> For each `number` in `numbers`, print it.

Output

```text
10
20
30
40
```

---

# When Should You Use an Enhanced `for` Loop?

Use it when:

* You only need to read every element.
* You don't need the position (index).
* You don't need to skip around.

Don't use it if you need:

* the index
* to modify elements by index
* to jump to specific positions

---

# `for` vs Enhanced `for`

### Standard `for`

```java
for (int i = 0; i < numbers.length; i++)
```

You know:

* current index
* current value

---

### Enhanced `for`

```java
for (int number : numbers)
```

You only know:

* current value

Much cleaner when the index isn't needed.

---

# Common Beginner Mistakes

## Missing Semicolon

Wrong

```java
for (int i = 0 i < 5; i++)
```

Missing

```text
;
```

---

## Infinite Loop

```java
for (int i = 1; i <= 5;) {

}
```

No update.

`i` never changes.

The condition stays true forever.

---

## Wrong Condition

```java
for (int i = 10; i <= 1; i++)
```

Output

Nothing.

Because

```text
10 <= 1
```

is already false.

---

# Exercise 1

Print

```text
1
2
3
4
5
6
7
8
9
10
```

---

# Exercise 2

Print

```text
10
9
8
7
...
1
```

---

# Exercise 3

Print only even numbers from 1–20.

---

# Exercise 4

Print only odd numbers from 1–20.

---

# Exercise 5

Print

```text
5
10
15
20
25
30
```

using a `for` loop.

---

# Summary

A `for` loop has three parts:

```java
for (initialisation; condition; update)
```

* **Initialisation** → where to start.
* **Condition** → when to stop.
* **Update** → how the counter changes after each iteration.

You also learned:

* `i++` increases by one.
* `i--` decreases by one.
* `%` checks the remainder.
* `number % 2 == 0` identifies even numbers.
* Enhanced `for` loops simplify iterating over arrays and collections.

---

# Mini Quiz

Try to answer these without looking back.

### 1. What are the three parts of a `for` loop, and what does each one do?

---

### 2. What does `i++` mean?

---

### 3. What does `i += 2` do?

---

### 4. What does `%` (modulo) return?

---

### 5. How do you check if a number is even?

---

### 6. What will this print?

```java
for (int i = 1; i <= 3; i++) {
    System.out.println(i);
}
```

---

### 7. What will this print?

```java
for (int i = 5; i >= 1; i--) {
    System.out.println(i);
}
```

---

### 8. What is the difference between a standard `for` loop and an enhanced `for` loop?

---

## 💡 Think Like an Engineer

Imagine you're building a backend service that sends a welcome email to every new user who signed up today.

You have a list of 500 users.

**Question:** Would you use a loop? If so, which kind of loop (`for` or enhanced `for`), and **why**?

This is the kind of practical reasoning that turns syntax knowledge into engineering skill.

### Lesson 4: Methods, Signatures, and the Call Stack

Now that we know how to store data (Types), we need to know how to act on it. In Java, we don't just have "functions"; we have **Methods**.

#### 1. What problem does this solve?
As a codebase grows to 100,000 lines, you cannot have one long list of instructions. You need to:
*   **Reuse logic:** Don't write the same "calculate tax" code 50 times.
*   **Abstract complexity:** The person calling `sendEmail()` doesn't need to know how SMTP protocols work.
*   **Namespace logic:** Ensure that a `save()` method in the `User` class is different from a `save()` method in the `Document` class.

#### 2. Why does it exist?
Java is a "Class-first" language. Methods exist to define the **behavior** of an object or a class. Unlike JavaScript, where a function is a "first-class citizen" (it can float around on its own), a Java method **must** belong to a class.

#### 3. How does it work internally? (The Call Stack)
When you call a method, the JVM creates a **Stack Frame**.
1.  It pushes the frame onto the **Stack**.
2.  The frame contains the method's local variables and the "return address" (where to go back to when finished).
3.  When the method returns, the frame is "popped" off, and that memory is instantly freed.

**Senior Insight:** If a method calls itself infinitely (recursion), the Stack fills up until you get the famous **StackOverflowError**.

#### 4. Example in Java: The Method Signature
In Java, a method is defined by its **Signature**.
```java
public int calculateTotal(int price, double taxRate) {
    return (int) (price + (price * taxRate));
}
```
*   **Access Modifier (`public`):** Who can call this?
*   **Return Type (`int`):** What comes back? (Mandatory!)
*   **Method Name (`calculateTotal`):** Use camelCase.
*   **Parameters (`int price...`):** Must have types.

#### 5. Comparison with JavaScript and Python
*   **JS/Python:** `function calculate(a, b) { ... }`. You don't know what `a` and `b` are until the code runs. You don't know what it returns until it returns.
*   **Java:** The signature is a **Contract**. If the method says it returns an `int`, it is physically impossible for it to return a `String`. The compiler checks this "contract" everywhere the method is used.

#### 6. Real-world industry usage: Clean Code
In professional environments, we follow **Robert C. Martin’s "Clean Code"** rules for methods:
1.  **Small!** A method should rarely be longer than 20 lines. If it's longer, it's likely doing too much.
2.  **Do One Thing (SRP):** A method should either *change* something or *answer* something, but not both.
3.  **Descriptive Names:** `handleData()` is bad. `parseJsonToUserObject()` is good.

#### 7. Common mistakes
*   **Side Effects:** A method called `isLoggedIn()` should only return true/false. It should **not** also update the database. This makes debugging a nightmare.
*   **Too many parameters:** If a method has 7+ parameters, you should pass an **Object** instead.
*   **Ignoring `void`:** If a method is `void`, it returns nothing. Beginners often try to assign a `void` method to a variable.

#### 8. Mini Exercise: Overloading
Java allows **Method Overloading**—multiple methods with the same name but different parameters.

Look at this:
```java
public void printData(String s) { ... }
public void printData(int i) { ... }
public void printData(String s, int i) { ... }
```
**Challenge:** Why is this useful in a real-world library (like a Logging library or a Math library)? Why not just name them `printString()`, `printInt()`, etc.?

#### 9. Interview perspective
**Question:** "What makes up a method signature in Java?"
**The 'Senior' Answer:** "A method signature consists of the **method name** and the **parameter list** (number, order, and types of parameters). Notably, the return type and access modifiers are *not* part of the signature for the purposes of overloading, though they are required for the declaration."

#### 10. Key takeaways
*   Methods are **contracts**.
*   The **Call Stack** manages method execution and local memory.
*   **Overloading** allows the same action to be performed on different data types.
*   Keep methods **small** and **focused**.

---

**What is your take on the Overloading exercise?** (Think about the developer who has to *use* your code). 

Once you answer, we will move to **Lesson 5: Control Flow (Logic) and the "Professional" way to handle conditionals.**

Method Overloading does not save memory, and it doesn't prevent a StackOverflowError.
In reality, when you compile your code, the Java Compiler treats printData(String s) and printData(int i) as two completely different methods. They just happen to share a name in your text editor.
The Real Reason: Cognitive Load and API Design
The reason we use overloading is Developer Experience (DX).
Imagine if the System.out.println() method wasn't overloaded. You would have to remember:
System.out.printlnString("Hello")
System.out.printlnInt(10)
System.out.printlnBoolean(true)
That would be a nightmare to use! By overloading, we provide a unified interface. The developer only needs to remember one action: "Print". The compiler is smart enough to figure out which version to call based on what you put in the parentheses.
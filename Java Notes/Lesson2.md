### Lesson 2: The Entry Point — Deconstructing `public static void main(String[] args)`

In Node.js or Python, you can just write `console.log("Hello")` or `print("Hello")` at the top of a file and run it. In Java, you can't. You need a "Front Door."

#### 1. What problem does this solve?
In a project with 1,000 files, how does the computer know which line of code to execute first? Without a standard entry point, you’d have to manually tell the engine where to start every single time.

#### 2. Why does it exist?
Java is strictly **Object-Oriented**. Everything must live inside a Class. But to start a program, you have a "Chicken and the Egg" problem: You need an object to run code, but you need to run code to create an object. 

The `static main` method solves this by allowing the JVM to start the program without creating an instance of the class first.

#### 3. How does it work internally?
When you run `java MyProgram`, the JVM:
1.  Loads the `MyProgram.class` file into memory.
2.  Looks specifically for a method with the exact signature: `public static void main(String[] args)`.
3.  If it doesn't find it, it throws a `NoSuchMethodError`.
4.  If it finds it, it creates a "Stack Frame" and starts executing the instructions inside.

#### 4. Example in Java
```java
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, Alpha Systems!");
    }
}
```

#### 5. Comparison with JavaScript/Python
*   **Node.js/Python:** Execution is "Top-Down." The interpreter starts at line 1 of the file you point it to.
*   **Java:** Execution is "Method-Based." The JVM looks for the `main` method, regardless of where it sits in the file.

#### 6. Real-world industry usage
In modern enterprise Java (like **Spring Boot**), you will still see this. Every multi-million dollar Spring application has one single class with a `main` method that looks like this:
```java
public static void main(String[] args) {
    SpringApplication.run(MyLargeEnterpriseApp.class, args);
}
```
It’s the "Ignition Switch" for the entire system.

#### 7. Common mistakes
*   **Forgetting `static`:** If you forget `static`, the JVM can't call the method without "new-ing" up the class, so it will fail to start.
*   **Wrong Parameter:** If you write `main(String args)` (missing the brackets `[]`), the JVM won't recognize it as the entry point. It *must* be an array of Strings.

#### 8. Mini Exercise
I want you to try to "break" the front door. 
1. Take your `Test.java` from before.
2. Change `public` to `private`. Try to run it. What happens?
3. Change `void` to `int` and try to `return 0;`. Does it compile? Does it run?
4. **Report back on what the error messages tell you.**

#### 9. Interview perspective
**Question:** "Why is the main method static?"
**The 'Senior' Answer:** "Because `static` methods belong to the class itself rather than an instance of the class. This allows the JVM to invoke the entry point without having to instantiate the class, which simplifies the startup process and avoids the overhead of object creation before the program has even begun."

#### 10. Key takeaways
*   `public`: Accessible by the JVM from outside the package.
*   `static`: Can be called without creating an object.
*   `void`: The method returns nothing to the JVM.
*   `String[] args`: A way to pass command-line arguments into your app (like `npm run start --port=3000`).

---

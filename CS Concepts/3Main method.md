### Java `main()` Method – Short Notes

#### What is the `main()` Method?

The `main()` method is the **entry point** of a Java application. When the JVM starts a program, it looks for this method and begins execution from there.

```java
public static void main(String[] args) {
}
```

---

### Understanding the Signature

| Keyword         | Meaning                                                 |
| --------------- | ------------------------------------------------------- |
| `public`        | Accessible from anywhere; JVM must be able to call it.  |
| `static`        | Belongs to the class, so no object needs to be created. |
| `void`          | Does not return any value.                              |
| `main`          | Special method name recognised by the JVM.              |
| `String[] args` | Stores command-line arguments passed to the program.    |

---

### Command-Line Arguments

Example:

```bash
java MyProgram hello world
```

Then:

```java
args[0] = "hello";
args[1] = "world";
```

Example usage:

```java
public static void main(String[] args) {
    if (args.length > 0) {
        System.out.println(args[0]);
    }
}
```

---

### Alternative Valid Signatures

All of the following are valid:

```java
public static void main(String []args)
```

```java
public static void main(String args[])
```

```java
public static void main(String... args)
```

(Varargs version)

---

### Additional Keywords

```java
public strictfp static void main(String[] args)
```

* `strictfp` ensures consistent floating-point calculations across platforms.

```java
public static void main(final String[] args)
```

* `final` prevents reassignment of the `args` reference.

Other valid but rarely useful keywords:

```java
final static synchronized strictfp void main(final String[] args)
```

---

### Multiple `main()` Methods

A class can contain multiple overloaded `main()` methods:

```java
public static void main(String[] args) {
    System.out.println("Entry point");
}

public static void main(int number) {
    System.out.println(number);
}
```

However, the JVM only starts execution from:

```java
public static void main(String[] args)
```

(or its valid variants).

---

### Main Class in a JAR

For executable JAR files, the JVM needs to know which class contains the entry-point `main()` method.

This is specified in:

```text
META-INF/MANIFEST.MF
```

Example:

```text
Main-Class: mypackage.Main
```

---

### Key Takeaways

* `main()` is the **starting point** of a Java application.
* The standard signature is:

```java
public static void main(String[] args)
```

* `args` stores command-line arguments.
* Several alternative signatures are valid, but rarely used.
* A program can have multiple `main()` methods, but the JVM looks for the standard entry-point signature.
* Executable JARs specify the startup class using `MANIFEST.MF`.

### Interview Question

**Why must `main()` be `static`?**

Because the JVM needs to execute the method **before any object exists**. If `main()` were not static, the JVM would first need to create an object of the class, creating a circular problem.

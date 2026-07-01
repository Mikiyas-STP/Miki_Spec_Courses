Here’s a clean **study note version** you can keep and revise from. I’ve included the full solution + the written answers for the reflection questions.

---

# 📘 Exercise 1.1 — Product Class (Study Notes)

## 🎯 Goal

Learn:

* Encapsulation
* Constructors (overloading + chaining)
* Getters & Setters
* `toString()`
* Object creation and state

---

# 🧱 1. Product Class Solution

```java id="finalnote1"
package sprint2.exercises.exercise1;

public class Product {

    private String name;
    private double price;
    private int stockCount;

    // Full constructor
    public Product(String name, double price, int stockCount) {
        this.name = name;
        this.price = price;
        this.stockCount = stockCount;
    }

    // Constructor chaining (default stock = 0)
    public Product(String name, double price) {
        this(name, price, 0);
    }

    // Getters
    public String getName() {
        return name;
    }

    public double getPrice() {
        return price;
    }

    public int getStockCount() {
        return stockCount;
    }

    // Setters
    public void setName(String name) {
        this.name = name;
    }

    public void setPrice(double price) {
        this.price = price;
    }

    public void setStockCount(int stockCount) {
        this.stockCount = stockCount;
    }

    // toString
    @Override
    public String toString() {
        return "Product{name='" + name + "', price=" + price + ", stockCount=" + stockCount + "}";
    }

    // Main method (testing)
    public static void main(String[] args) {

        Product orange = new Product("Orange", 2.50);
        Product milk = new Product("Milk", 1.20, 10);
        Product bread = new Product("Bread", 1.00, 5);

        System.out.println(orange);
        System.out.println(milk);
        System.out.println(bread);

        orange.setPrice(3.00);
        System.out.println(orange);
    }
}
```

---

# 🧠 2. Theory Questions (Answers)

---

## ❓ Q1: How did constructor overloading change the way Product objects could be created?

### ✔ Answer:

Constructor overloading allows the same class to be used in multiple ways when creating objects.

It gives flexibility to create a Product with:

* only name and price
* or name, price, and stockCount

### 💡 Example:

```java id="ans1"
new Product("Orange", 2.50);
new Product("Orange", 2.50, 10);
```

### ✔ Key idea:

It makes object creation more flexible depending on available data.

---

## ❓ Q2: What problem does constructor chaining with `this()` solve?

### ✔ Answer:

Constructor chaining removes duplicated code by making one constructor call another.

Instead of repeating initialization logic, we centralise it in one constructor.

### 💡 Example:

```java id="ans2"
this(name, price, 0);
```

### ✔ Problem solved:

* avoids repeating code
* reduces mistakes
* makes updates easier (change logic in one place only)

---

## ❓ Q3: When creating multiple Product objects, how did constructor arguments affect the state of each object?

### ✔ Answer:

Each object’s state is determined by the values passed into its constructor.

Different arguments create different internal states.

### 💡 Example:

```java id="ans3"
new Product("Orange", 2.50);     // stockCount = 0
new Product("Milk", 1.20, 10);   // stockCount = 10
```

### ✔ Key idea:

Each object is independent and stores its own data.

Changing one object does not affect others.

---

# 🧠 Final Summary (Revision Cheat Sheet)

* **Overloading** → multiple ways to create objects
* **Chaining (`this()`)** → avoids duplicated constructor logic
* **Arguments** → define object state at creation
* **Encapsulation** → private fields + getters/setters protect data
* **toString()** → controls how object is printed

---
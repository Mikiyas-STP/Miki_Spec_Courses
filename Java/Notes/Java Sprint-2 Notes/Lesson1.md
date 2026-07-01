## 1. Class

**Definition:**
A **class** is a **blueprint or template** for creating objects. It describes what data an object has and what it can do.

**Simple analogy:**
A class is like a recipe. The recipe isn't the cake—it tells you how to make one.

**Example:**

```java
class Car {
    String colour;
    int speed;
}
```

This defines what every `Car` will have, but it doesn't create a car.

---

## 2. Object

**Definition:**
An **object** is a real instance created from a class.

**Simple analogy:**
If a class is a recipe, an object is the actual cake you baked.

**Example:**

```java
Car myCar = new Car();
```

`myCar` is an object of the `Car` class.

---

## 3. Field (Instance Variable)

**Definition:**
A **field** is a variable inside a class that stores information about an object.

**Simple analogy:**
A field is like a characteristic of a person (name, age, height).

**Example:**

```java
class Car {
    String colour;
    int speed;
}
```

Here:

* `colour` is a field.
* `speed` is a field.

---

## 4. Constructor

**Definition:**
A **constructor** is a special method that runs automatically when an object is created. It gives the object its starting values.

**Example:**

```java
class Car {

    String colour;

    Car(String colour) {
        this.colour = colour;
    }
}
```

Creating an object:

```java
Car myCar = new Car("Red");
```

The constructor sets the colour to `"Red"`.

---

## 5. Method

**Definition:**
A **method** is a block of code that tells an object what it can do.

**Simple analogy:**
If a field is what an object **has**, a method is what an object **does**.

**Example:**

```java
class Car {

    void drive() {
        System.out.println("The car is moving.");
    }
}
```

Calling the method:

```java
myCar.drive();
```

Output:

```
The car is moving.
```

---

## 6. State

**Definition:**
The **state** of an object is the current values stored in its fields.

**Example:**

```java
Car myCar = new Car("Red");
```

If:

```java
colour = "Red"
speed = 50
```

then the object's state is:

* Colour: Red
* Speed: 50

---

## 7. Behaviour

**Definition:**
**Behaviour** is what an object can do through its methods.

**Example:**

```java
myCar.drive();
myCar.stop();
```

Driving and stopping are behaviours.

---

## 8. `new` Keyword

**Definition:**
The `new` keyword creates a new object in memory.

**Example:**

```java
Car myCar = new Car();
```

`new Car()` creates a brand-new `Car` object.

---

## 9. `this` Keyword

**Definition:**
`this` refers to the **current object**.

**Example:**

```java
class Car {

    String colour;

    Car(String colour) {
        this.colour = colour;
    }
}
```

* `this.colour` → the object's field.
* `colour` → the constructor's parameter.

---

## 10. Access Modifier

**Definition:**
An **access modifier** controls who can use a class, field, constructor, or method.

The two most common are:

* `public` → anyone can access it.
* `private` → only the class itself can access it.

**Example:**

```java
private int speed;
public void drive() { }
```

Here:

* `speed` can only be accessed inside the `Car` class.
* `drive()` can be called from other classes.

---

## 11. Getter

**Definition:**
A **getter** is a method that lets you read the value of a private field.

**Example:**

```java
public int getSpeed() {
    return speed;
}
```

Usage:

```java
System.out.println(car.getSpeed());
```

---

## 12. Setter

**Definition:**
A **setter** is a method that lets you change the value of a private field.

**Example:**

```java
public void setSpeed(int speed) {
    this.speed = speed;
}
```

Usage:

```java
car.setSpeed(60);
```

---

## 13. Encapsulation

**Definition:**
**Encapsulation** means hiding an object's data and controlling access to it using methods.

**Simple analogy:**
A TV remote lets you change the volume, but it doesn't let you directly modify the electronics inside the TV.

**Example:**

```java
private int speed;

public void setSpeed(int speed) {
    this.speed = speed;
}
```

You cannot access `speed` directly, so the class controls how it changes.

---

## Quick Summary Table

| Term                | Simple Definition                                     |
| ------------------- | ----------------------------------------------------- |
| **Class**           | A blueprint for creating objects.                     |
| **Object**          | A real instance created from a class.                 |
| **Field**           | A variable that stores an object's data.              |
| **Constructor**     | A special method that runs when an object is created. |
| **Method**          | A function that defines what an object can do.        |
| **State**           | The current values of an object's fields.             |
| **Behaviour**       | The actions an object can perform using methods.      |
| **`new`**           | Creates a new object.                                 |
| **`this`**          | Refers to the current object.                         |
| **Access Modifier** | Controls who can access code or data.                 |
| **Getter**          | Reads a private field.                                |
| **Setter**          | Changes a private field.                              |
| **Encapsulation**   | Hides data and controls access through methods.       |

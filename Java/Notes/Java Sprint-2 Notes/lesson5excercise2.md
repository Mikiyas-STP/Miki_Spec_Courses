package sprint2.exercises.exercise2;
//Exercise 1.2 - Reference Behaviour
//Starting with the following in your main method:
//Product p1 = new Product("Laptop", 900);
//Product p2 = p1;
//p2.setPrice(1100);
//System.out.println(p1.getPrice());
//System.out.println(p2.getPrice());
//Tasks:
//Predict the output
//Run the code to verify
//Change how p2 is instantiated so that making changes to it does not affect p1

public class ProductTest {
    private String name;
    private double price;
    private int stockCount;

    //constructor
    public ProductTest(String name, double price, int stockCount ){
        this.name = name;
        this.price = price;
        this.stockCount = stockCount;
    }

    //constructor chaining
    public ProductTest(String name, double price){
        this(name, price, 0);
    }

    //getters
    public String getName(){
        return name;
    }

    public double getPrice(){
        return price;
    }

    public int getStockCount() {
        return stockCount;
    }

    //setters
    public void setName(String name){
        this.name = name;
    }

    public void setPrice(double price){
        this.price = price;
    }

    public void setStockCount(int stockCount){
        this.stockCount = stockCount;
    }

    //to String
    @Override
    public String toString() {
        return "Product{name='" + name + "', price=" + price + ", stockCount=" + stockCount + "}";
    }



    //main method
    public static void main(String[] args){
        ProductTest p1 = new ProductTest("Laptop", 900);
        ProductTest p2 = p1;
        p2.setPrice(1100);
        System.out.println(p1.getPrice());
        System.out.println(p2.getPrice());


    }
//predicted to be 900 and 1100 but i got 1100 and 1100
    //because ProductTest p2 = p1; doesnt create the same object, it points to the same object as p1.
    // i would create a new object like this
//ProductTest p2 = new ProductTest(p1.getName(), p1.getPrice(), p1.getStockCount());

}


These are exactly the right reflection questions — they test whether you understand **reference vs object**, which is a core Java/backend concept.

I’ll answer them clearly and directly.

---

# 🧠 1. Why did changing `p2` also change `p1`?

Because:

```java id="r1"
ProductTest p2 = p1;
```

### This does NOT create a new object.

It makes both variables point to the **same object in memory**.

So when you do:

```java id="r2"
p2.setPrice(1100);
```

You are modifying the **single shared object**, so `p1` sees the same change.

---

# 🧠 2. What does this tell you about what `p1` and `p2` actually store?

They do NOT store the actual object.

They store:

> A reference (memory address) pointing to the object.

### Simple model:

```text id="r3"
p1 ───► [ Product Object in memory ]
        ▲
p2 ────┘
```

So:

* `p1` = reference
* `p2` = reference
* both point to the same object

---

# 🧠 3. How did your fix prevent changes from affecting both?

You fixed it by creating a new object:

```java id="r4"
ProductTest p2 = new ProductTest("Laptop", 900);
```

or

```java id="r5"
ProductTest p2 = new ProductTest(p1.getName(), p1.getPrice(), p1.getStockCount());
```

---

### What changed?

Now you have:

```text id="r6"
p1 ───► [ Object A ]
p2 ───► [ Object B ]
```

Two separate objects in memory.

So changing one does NOT affect the other.

---

# 🧠 4. What new object(s) existed after your change compared to before?

### Before fix:

* 1 object total
* both `p1` and `p2` point to it

---

### After fix:

* 2 objects total

  * Object A → `p1`
  * Object B → `p2`

---

# 🧠 5. How can this cause bugs in large codebases?

This is VERY important for backend development.

---

## ⚠️ Common bug scenario

You pass an object into a method:

```java id="r7"
updateProduct(p1);
```

Inside method:

```java id="r8"
product.setPrice(0);
```

---

## 💥 Problem:

You accidentally modify the original object everywhere it is used.

So:

* UI shows wrong price
* database update becomes incorrect
* logs become misleading
* other services get corrupted data

---

# 🔥 Real-world backend impact

This causes bugs like:

### 1. Unexpected shared state

One service changes data → another service sees it change.

---

### 2. Data corruption

Same object reused across multiple layers.

---

### 3. Hard-to-debug issues

Because changes happen “somewhere else in the code”.

---

# 🧠 Key engineering lesson

> “If you don’t control object references, you don’t control your data.”

---

# ✔ Final summary (memorise this)

* `p1 = p2` copies reference, not object
* Both variables point to same memory
* Changing one changes the same object
* Fix = create a new object using `new`
* Bugs happen when shared references are unintentionally modified

--
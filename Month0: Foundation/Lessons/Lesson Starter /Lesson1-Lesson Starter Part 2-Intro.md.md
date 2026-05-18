**3-Part Mini-Series**:
* **Session 1 (Today):** Core Data Types & Operations (Strings, Lists, Dictionaries, and Logic).
* **Session 2:** Control Flow (Loops, If/Else, and Iteration tricks).
* **Session 3:** Functions, Scope, and a deep dive into Type Hints.

Let's dive into **Session 1**. Since you know JavaScript, I won't explain *what* a string or an array is. Instead, I will show you how Python *operates* on them, especially in a backend context.
---
### 1. Booleans and Logic Operators
In JavaScript, you use symbols (`&&`, `||`, `!`). Python is designed to read like English. It uses words.

```python
is_admin = True
is_active = False

# JavaScript: if (is_admin && !is_active)
if is_admin and not is_active:
    print("Admin is offline")

# JavaScript: if (is_admin || is_active)
if is_admin or is_active:
    print("User has access")
```
**Backend Tip:** In Python, `None`, `0`, empty strings `""`, empty lists `[]`, and empty dicts `{}` are all considered "Falsy". You can just write `if not my_list:` to check if a list is empty!

### 2. Strings: The Backend Workhorse
In backend engineering, you are constantly formatting strings for logs, database queries, or API responses.

**A. F-Strings (Python's Template Literals)**
In JS, you use backticks `` `Hello ${name}` ``. In Python, you put an `f` before the quotes and use curly braces. This is called an f-string, and you will use it every single day.
```python
username = "David"
role = "Admin"
# Notice the 'f' right before the string starts
log_message = f"User {username} logged in as {role}." 
```

**B. Core String Methods**
```python
text = "  hello world  "
print(text.strip())       # "hello world" (Like JS .trim())
print(text.upper())       # "  HELLO WORLD  "
print(text.startswith(" ")) # True (Very useful for checking paths or tokens!)

# Splitting and Joining
csv_data = "apple,banana,cherry"
items = csv_data.split(",")      # Creates a list:['apple', 'banana', 'cherry']
joined_str = " | ".join(items)   # 'apple | banana | cherry'
```

### 3. Lists (JavaScript Arrays)
Python lists are incredibly powerful. They have a feature called "slicing" which lets you grab chunks of data effortlessly.

**A. Slicing (Grabbing parts of a list)**
Syntax: `my_list[start:stop]`
```python
users =["Alice", "Bob", "Charlie", "David", "Eve"]

print(users[0:2])  # ['Alice', 'Bob'] (Grabs index 0 up to, but not including, 2)
print(users[-1])   # 'Eve' (Negative numbers count from the end! Very Pythonic)
print(users[2:])   #['Charlie', 'David', 'Eve'] (From index 2 to the end)
```

**B. Core List Methods**
```python
queue = ["task1", "task2"]
queue.append("task3")       # JS .push() -> Adds to the end
first_task = queue.pop(0)   # JS .shift() -> Removes and returns the item at index 0
```

### 4. Dictionaries (The Core of Python Backend)
This is the most important data structure you will learn. In JS, if you try to access a key that doesn't exist (`user.age`), it returns `undefined`. 
**In Python, if you use brackets `user["age"]` and the key isn't there, the entire program crashes with a `KeyError`.**

Because APIs often send us messy or incomplete JSON data, we need a safe way to check for keys.

**The Golden Rule of Dicts: Use `.get()`**
```python
payload = {
    "user_id": 105,
    "email": "test@example.com"
}

# DANGEROUS: If "name" is missing, your server returns a 500 Internal Server Error.
# print(payload["name"]) 

# SAFE: .get() returns None if the key is missing, instead of crashing.
name = payload.get("name") 

# SAFER: You can provide a default fallback value!
role = payload.get("role", "standard_user") 
print(role) # Prints "standard_user" because "role" wasn't in the payload
```

**Getting Keys and Values**
```python
print(payload.keys())   # dict_keys(['user_id', 'email'])
print(payload.values()) # dict_values([105, 'test@example.com'])
```

---

### Your Turn: Data Operations Challenge

Let's practice exactly what we just covered. No loops, no complex functions yet. Just sequential data operations.

**The Scenario:**
You receive a raw dictionary from a messy third-party API. You need to extract some data safely, format a string, and update a list.

Here is your starting code:

```python
# The raw data we received from the API
api_response = {
    "username": "  charlie_dev  ",
    "access_level": 5,
    "tags":["python", "backend"]
}

# TODO 1: Safely get the "username" from the dict.
# Chain the string method to remove the extra whitespace on the sides.
clean_username = 

# TODO 2: Safely get the "is_active" status from the dict.
# The API forgot to send it! Use .get() to default it to False.
is_active = 

# TODO 3: Append the string "api_v2" to the "tags" list inside the dictionary.


# TODO 4: Create an f-string that says: "User charlie_dev has access level 5."
# Use the clean_username variable you created, and the access_level from the dict.
log_message = 


# Print out your results to test them!
print(clean_username)
print(is_active)
print(api_response["tags"])
print(log_message)
```

Take your time! Read through the examples above to figure out how to do `TODO 1` through `TODO 4`. Let me know what you come up with.
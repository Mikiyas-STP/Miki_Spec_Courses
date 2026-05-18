# Session 2: Control Flow (Loops & Conditions)

Since you already know how logic works from JS, we are just going to look at the Python syntax for iterating through data. In backend engineering, you will loop through lists and dictionaries constantly.

### 1. The Standard `for` Loop
In JS, you have `for (let i=0; i<x; i++)` and `for...of`. Python really only uses the `for...of` style. We iterate *directly* over the items.

```python
emails =["alice@test.com", "bob@test.com", "charlie@test.com"]

# Read this like plain English
for email in emails:
    print(f"Sending welcome email to: {email}")
```

### 2. Looping with an Index (`enumerate`)
Sometimes you *do* need the index number (like `0, 1, 2`). Instead of setting up a counter manually, Python has a built-in function called `enumerate()`. It gives you both the index AND the item at the same time.

```python
# enumerate() returns two things: the index, and the value
for index, email in enumerate(emails):
    print(f"User {index}: {email}")
```

### 3. Looping through Dictionaries (`.items()`)
This is a critical backend skill. If you just loop over a dictionary, Python only gives you the keys. If you want the keys AND the values, you must use `.items()`.

```python
user_roles = {
    "alice": "admin",
    "bob": "user",
    "charlie": "moderator"
}

# .items() unpacks the dict into key-value pairs
for username, role in user_roles.items():
    if role == "admin":
        print(f"ALERT: Admin {username} logged in.")
```

### 4. If / Elif / Else
Just a quick reminder on conditionals. Python uses indentation instead of `{}`. 
* Use `==` for equality.
* Use `and` / `or` / `not` for logic.
* `elif` is short for "else if".

```python
status_code = 403

if status_code == 200:
    print("OK")
elif status_code == 403 or status_code == 401:
    print("Unauthorized!")
else:
    print("Unknown Error")
```

---

### Your Turn: The Rate Limiter Challenge

Let's put your new Dictionary skills together with Python Loops and Conditionals. 

**The Scenario:**
You are writing a script to check API usage. You have a list of user dictionaries. If a user has made more than 100 requests, they are "rate limited" and we need to block them.

**Your Task:**
1. Loop through the `api_users` list.
2. For each user, check if their `"requests"` count is strictly **greater than** `100`.
3. If it is, append their `"username"` to the `blocked_users` list.
4. Remember to use bracket notation `["key"]` to get the values!

Here is your starting code:

```python
api_users =[
    {"username": "alice_dev", "requests": 45},
    {"username": "bob_tester", "requests": 150},
    {"username": "charlie_script", "requests": 12},
    {"username": "dave_hacker", "requests": 999}
]

blocked_users =

#Answer
from typing import List, Dict

# The raw data
api_users = [
    {"username": "alice_dev", "requests": 45},
    {"username": "bob_tester", "requests": 150},
    {"username": "charlie_script", "requests": 12},
    {"username": "dave_hacker", "requests": 999}
]

def get_blocked_users(users_list: list[dict]) -> list[str]:
    # 1. Initialize the empty list
    blocked_users = []
    
    # 2. Iterate through the list of dictionaries
    for user in users_list:
        # 3. Check the condition (using bracket notation)
        if user["requests"] > 100:
            blocked_users.append(user["username"])
            
    # 4. CRITICAL: Return must be outside the for-loop
    # This ensures we check ALL users before returning the result.
    return blocked_users

# Testing the result
print(get_blocked_users(api_users))
# Output: ['bob_tester', 'dave_hacker']
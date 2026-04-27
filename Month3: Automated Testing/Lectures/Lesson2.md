
# Month 3, Week 2: Testing with "Mocks" (Overrides)

Your first test was great, but it was for a simple `/health` route. What happens when you test a route that creates a new user in the Database?

**The Problem:**
If you run `pytest` 50 times a day, your testing code will accidentally create 50 fake users in your real PostgreSQL database! We don't want that.

**The Solution: Dependency Overrides**
Remember **Dependencies** (the "Toolbox" and the "Bouncer")? 
FastAPI has a built-in feature that lets you swap out a real tool for a "Fake" tool **only during a test**. We call this "Mocking."

### How it works:
```python
# 1. The Real Dependency
def get_database():
    return "REAL_PRODUCTION_DATABASE"

@app.get("/data")
def read_data(db: str = Depends(get_database)):
    return {"db_used": db}

# --- THE TEST ---

# 2. The Fake Dependency
def fake_database():
    return "FAKE_TESTING_DATABASE"

# 3. The Override (The Magic!)
app.dependency_overrides[get_database] = fake_database

def test_read_data():
    # When this test runs, it will use 'fake_database' instead of 'get_database'!
    response = client.get("/data")
    assert response.json() == {"db_used": "FAKE_TESTING_DATABASE"}
```

This is incredible for London teams. It means you can test your code on an airplane without even having PostgreSQL installed on your laptop!

---

### Your Coding Challenge: Testing the "VIP Route"

You are writing a test for a route that checks a user's subscription tier. The real database is too slow for our tests, so we want to use an "Override".

**Task:**
1. I have provided the `app` and the real dependency `get_user_tier`.
2. Create a fake function called `override_user_tier()`. It should just return the string `"Gold"`.
3. Use `app.dependency_overrides` to swap `get_user_tier` with your new `override_user_tier`.
4. Inside `test_vip_access()`, use the `client.get()` to hit `/vip-status`.
5. Write an `assert` to check that the JSON returned is `{"tier": "Gold", "message": "Welcome to the VIP Lounge!"}`.

**Starter Code:**

```python
from fastapi import FastAPI, Depends
from fastapi.testclient import TestClient

app = FastAPI()

# The Real Dependency (Imagine this makes a slow DB call)
def get_user_tier():
    return "Bronze" 

@app.get("/vip-status")
def check_vip(tier: str = Depends(get_user_tier)):
    if tier == "Gold":
        return {"tier": tier, "message": "Welcome to the VIP Lounge!"}
    return {"tier": tier, "message": "Regular access."}

# --- YOUR TESTING CODE ---
client = TestClient(app)

# TODO: 1. Create your fake function 'override_user_tier'
# TODO: 2. Set up the dependency override using app.dependency_overrides[...] = ...

def test_vip_access():
    # TODO: 3. Hit the client and assert the VIP Lounge response!
    pass
```

**Let's see you bypass the database like a Senior QA Engineer!**

**Asked for more clarification**



You are absolutely right to stop me. I moved too fast. 

In the software engineering world, the concept of "Mocking" or "Faking" things for a test is one of the hardest ideas to wrap your head around the first time.

Let's put the code away for a second. Let's look at this like a **Movie Director**.

---

### The "Stunt Double" Analogy

Imagine you are filming an action movie. 

1. **The Route:** This is the Scene you are filming.
2. **The Dependency:** This is your lead actor, Tom Cruise.
3. **The Problem:** The script says the actor needs to jump off a 50-foot building. If you make Tom Cruise (your real database) do this 100 times for testing, he is going to get hurt (you will ruin your real data).
4. **The Solution:** For this one specific scene, you hire a **Stunt Double**. He wears the same jacket, he looks the same from a distance, but he is cheap, safe, and disposable.

### Translating the Analogy to FastAPI

When we write an Automated Test, we don't want to use our **Real Database**. 
* The real database is slow.
* If the test creates a user, we have to remember to delete that user afterwards so our database doesn't fill up with "test_user_1", "test_user_2", etc.

Instead, we use a **Fake Database** (The Stunt Double).

FastAPI makes hiring a stunt double incredibly easy. It has a built-in dictionary called `dependency_overrides`. 

You literally just tell FastAPI:
* *"Hey, if this route asks for Tom Cruise (Real DB), give it the Stunt Double (Fake DB) instead."*

### Let's see it in slow motion:

```python
# 1. THE REAL ACTOR (Slow, dangerous for tests)
def get_real_database():
    return "Connected to Production PostgreSQL!"

# 2. THE STUNT DOUBLE (Fast, safe, fake)
def get_fake_database():
    return "Fake Database for testing only."

# 3. THE SWAP (The Magic Line)
# We use a dictionary to swap the real function for the fake one.
app.dependency_overrides[get_real_database] = get_fake_database
```

When you write that last line, FastAPI secretly changes the locks. Any route that was supposed to use `get_real_database` will now automatically use `get_fake_database` instead.

---

### A Simpler Challenge: Just swapping the actors

Let's try this again, but much simpler. We won't even write the test part yet. We are just going to practice making the "Stunt Double" and doing the swap.

**The Scenario:**
You have a route that checks a user's bank balance. The real function talks to a real bank (very slow). For our test, we want to fake it so it always returns `1000000` (1 million).

**Task:**
1. I wrote the Real Function.
2. **You** write the Fake Function (Call it `fake_bank_balance`). It should take no arguments and just `return 1000000`.
3. **You** write the "Swap" line using `app.dependency_overrides`. Put the real function in the brackets `[]`, and set it equal to your fake function.

```python
from fastapi import FastAPI

app = FastAPI()

# --- 1. The Real Actor ---
def get_real_bank_balance():
    # Imagine this takes 10 seconds to talk to Visa/Mastercard
    return 5

# --- YOUR TURN ---

# TODO: 2. Write the Stunt Double (fake_bank_balance)
def 


# TODO: 3. Do the swap!
app.dependency_overrides[ ] = 
```

**Does the "Stunt Double" analogy make more sense? Try to just do steps 2 and 3 here.**
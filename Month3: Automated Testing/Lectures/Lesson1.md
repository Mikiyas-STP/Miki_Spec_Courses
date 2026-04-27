# Month 3, Week 1: Automated Testing (Pytest)

In your PERN stack, you might have used **Jest** or **Mocha**. In Python, the industry standard is **Pytest**.

### The Problem with Manual Testing
When a junior writes a new route, they usually open Postman, click "Send," see a `200 OK`, and say, *"It works!"*
But what if changing that code accidentally broke the login system? You won't know until users start complaining. 

### The Solution: Automated Tests
We write Python code that *tests* our Python code. Every time you save, you run `pytest` in your terminal, and it tests your entire app in 2 seconds.

### Concept 1: The `assert` Keyword
The heart of Pytest is the word `assert`. It means *"I swear this is true. If I am lying, crash the test."*

```python
def add(a, b):
    return a + b

# This is a test function (It MUST start with the word "test_")
def test_add():
    result = add(2, 3)
    assert result == 5  # The test passes!
```

### Concept 2: Testing FastAPI (`TestClient`)
FastAPI has a built-in tool that lets you pretend to be Postman or a React frontend. It sends fake requests to your API.

```python
from fastapi import FastAPI
from fastapi.testclient import TestClient

app = FastAPI()

@app.get("/hello")
def say_hello():
    return {"message": "Hello London"}

# --- THE TEST FILE ---
# We wrap our app in the TestClient
client = TestClient(app)

def test_say_hello():
    # 1. Send a fake GET request
    response = client.get("/hello")
    
    # 2. Assert the status code is what we expect
    assert response.status_code == 200
    
    # 3. Assert the JSON data is exactly correct
    assert response.json() == {"message": "Hello London"}
```
If someone accidentally changes the route to return `"Hello Paris"`, the test will fail, and GitHub will block them from merging the code!

---

### Your Coding Challenge: Test the Health Check

It is a standard practice that every API has a `/health` endpoint so DevOps systems (like AWS or Docker) know the server is awake.

**Task:**
1. I have written the FastAPI app for you.
2. Write a test function called `test_health_check()`.
3. Inside the test, use `client.get()` to hit the `/health` endpoint. Save this to a variable called `response`.
4. Write an `assert` to check if `response.status_code` is `200`.
5. Write an `assert` to check if `response.json()` equals `{"status": "healthy", "db": "connected"}`.

**Here is your starter code:**

```python
from fastapi import FastAPI
from fastapi.testclient import TestClient

# --- The Main App ---
app = FastAPI()

@app.get("/health")
def health_endpoint():
    return {"status": "healthy", "db": "connected"}

# --- The Testing Setup ---
client = TestClient(app)

# TODO: Write your test_health_check function here!
```

**Let's see your first Python Test!** If you can write tests, Senior Engineers will trust your code instantly.

**My Answer**
def test_health_check():

    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy", "db": "connected"}
i have quesdtion , if i am coding using python why am i seeing json which is javascript


**Spot on! 100% correct.** 

Your test function is perfect. If you put that in a file named `test_main.py` and typed `pytest` in your terminal, it would pass with flying colors. 

Now, let's address your question. It is an extremely smart observation, and it shows you are thinking deeply about the technologies.

### "Why am I using JSON if I am writing Python?"

You are correct: **JSON** stands for *JavaScript Object Notation*. Originally, it was invented specifically for JavaScript. 

But today, JSON doesn't "belong" to JavaScript anymore. It has become the **Universal Language of the Internet**. 

**The Analogy: English as a Global Language**
Imagine a French person (your React frontend) wants to talk to a Japanese person (your Python backend). They can't speak each other's native languages. So, they both agree to speak **English** (JSON) when they talk to each other.

*   React takes a JavaScript Object and turns it into JSON text.
*   The internet carries that JSON text to your server.
*   Python (FastAPI) receives the JSON text and translates it into a **Python Dictionary**.

When you write `response.json()` in your test, you are telling Python: *"Take the universal JSON text the server sent back, and turn it into a Python Dictionary so I can test it."*

Does that make sense? It's just a text format that every programming language agrees to use!

---
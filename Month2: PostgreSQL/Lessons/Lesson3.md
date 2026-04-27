# Month 2, Week 3: Project Structure (Separation of Concerns)

If you put all your Routes, Pydantic Schemas, and SQLAlchemy Models in one `main.py` file, it will become thousands of lines long. In Node.js, you split your project into folders like `controllers`, `models`, and `routes`. 

We do the exact same thing in the **PAPR Stack**, but with specific Python naming conventions.

### The "London Standard" Folder Structure

If you join a team using FastAPI, their codebase will look almost exactly like this:

```text
my_project/
├── database.py       # Boilerplate connection (Engine, SessionLocal, Base)
├── models.py         # SQLAlchemy Classes (Database Tables)
├── schemas.py        # Pydantic Classes (API Data Validation)
├── dependencies.py   # Helpers (get_db, verify_admin)
└── main.py           # The Routes (@app.get, @app.post)
```

**Why do we do this?**
Imagine you want to change the rules for what makes a valid password. 
Instead of scrolling through 2,000 lines of routing code in `main.py`, you know exactly where to go: **`schemas.py`**.

---

### Your Architectural Challenge

This is not a coding challenge; it is a **Thinking Challenge**. 

Imagine you are building a **Social Media App**. You have written the following 4 blocks of code. 

**Task:** Tell me exactly which file (`database.py`, `models.py`, `schemas.py`, `dependencies.py`, or `main.py`) each of these 4 blocks belongs in.

**Code Block 1:**
```python
def get_current_user(token: str = Header(...)):
    # ... checks the token ...
    return user
```

**Code Block 2:**
```python
class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True)
    content = Column(String)
```

**Code Block 3:**
```python
@app.get("/feed")
async def get_feed(db: Session = Depends(get_db)):
    # ... gets posts from db ...
    return posts
```

**Code Block 4:**
```python
class PostCreate(BaseModel):
    content: str = Field(..., max_length=280)
```

### 🧠 Follow-up Question:
If `main.py` needs to use the `PostCreate` class, how do you bring it into `main.py`? What is the exact Python keyword/syntax? *(Hint: Think about how you bring code from one file to another).*


**Correct Answer for the question**

To map your answers to the professional "London Standard" filenames:
*   **Block 1 (Helper function):** This goes in **`dependencies.py`**.
*   **Block 2 (Class definition for DB):** This goes in **`models.py`**.
*   **Block 3 (The Route):** This goes in **`main.py`**.
*   **Block 4 (Pydantic validation):** This goes in **`schemas.py`**.

You missed my follow-up question, but that is totally fine! 
If you want to use the `PostCreate` class inside `main.py`, you use Python's **import** syntax. 
It looks like this:
`from schemas import PostCreate`

This is how the files talk to each other.

---

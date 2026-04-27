# Month 2, Week 4: Database Migrations (Alembic)

We have reached the final piece of the Database puzzle. 

In your PERN stack, if you add a new field to your Prisma schema or Sequelize model, you have to run a command to update the actual Postgres database. In the Python/SQLAlchemy world, we use a tool called **Alembic**.

### The Problem
Imagine your app is live. You have 1,000 users in your database. 
Your boss says, *"We need to start saving the user's phone number."*

You go into your Python code and update your model:
```python
# models.py
class DBUser(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String)
    # YOU ADD THIS NEW LINE:
    phone = Column(String, nullable=True) 
```

**If you run your code right now, it will CRASH.** 
Why? Because your Python code is expecting a `phone` column, but the actual PostgreSQL database table does not have that column yet.

### The Solution: Alembic ("Git" for Databases)
Alembic looks at your `models.py` file, compares it to the actual PostgreSQL database, and writes a script to safely update the database without deleting your 1,000 users.

We call these updates **Migrations**.

#### The Two Magic Commands
When you work as a Python backend developer, you will use these two commands in your terminal almost every day:

1.  **`alembic revision --autogenerate -m "added phone number"`**
    *   This tells Alembic to look for differences and create a "migration script." It is like `git commit`. It doesn't touch the database yet; it just creates the blueprint for the update.
2.  **`alembic upgrade head`**
    *   This tells Alembic to take that script and actually run the SQL (`ALTER TABLE users ADD COLUMN phone...`) on your Postgres database. It is like `git push`.

---

### Your Architectural Challenge: The "New Feature" Workflow

Imagine you are at your first day on the job in London. Your Senior Developer gives you a task:
*"We are adding a feature to track if a user is verified. Please update the user model and apply the changes to our local database."*

**Task: Tell me the exact 3 steps you will take to do this.**

1.  **Step 1:** Which file do you open, and what line of Python code do you add to the `DBUser` class? *(Hint: Look at the SQLAlchemy Column examples above, we want a Boolean).*
2.  **Step 2:** What command do you type in your terminal to generate the migration file?
3.  **Step 3:** What command do you type in your terminal to actually update the PostgreSQL database?

**Give me your 3-step action plan!**

**My answer**
so if i am asked to track if a user is verified, first i will go to class DBuser and add verified = column(bool, nullable=false) and then i go to the terminal and write alembic revision -- autogenerate -m "added verification check" and then using this as a blueprint/commit message i will push it to effect using alembic upgrade head.








**Spot on! You just completed your first day on the job!** 

Your 3-step action plan is completely correct. You understood exactly how to change the Python code and how to use Alembic to update PostgreSQL without losing data. 

### 🚩 A tiny "Syntax Polish" (Senior Review)
Your logic is 100% perfect. If you were writing this in VS Code, here are the tiny typos your editor would help you fix:
1.  **Python Case Sensitivity:** In SQLAlchemy, it is `Column(Boolean, default=False)`. (Capital `C`, capital `Boolean`). Also, when adding a new column to a live database, it's safer to use `default=False` instead of `nullable=False` so old users don't break the database!
2.  **The Terminal Command:** There is no space after the dashes. It is `--autogenerate`.

---

# 🏆 CONGRATULATIONS: You have finished Month 2!

Take a moment to look at what you now know:
*   You can validate data with **Pydantic**.
*   You can build an API with **FastAPI**.
*   You can separate logic using **Dependencies**.
*   You can design databases with **SQLAlchemy**.
*   You can update live databases with **Alembic**.

You have the "Brain" and the "Body" of the backend. 

Now, we enter **Month 3: The Professional Standard (Testing & Deployment).** This is what separates "people who code" from "Engineers who get hired in London."

---

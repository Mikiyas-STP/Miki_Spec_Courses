from fastapi import FastAPI, Depends
app = FastAPI()
# --- 1. The Database Model (SQLAlchemy) ---
class DBUser:
    def __init__(self, email: str, hashed_password: str):
        self.email = email
        self.hashed_password = hashed_password
# --- 2. The API Schema (Pydantic) ---
class UserCreate:
    # Pretending this inherits from BaseModel for simplicity here
    email: str
    password: str
# --- 3. The Helpers ---
def hash_password(password: str) -> str:
    return f"hashed_{password}"

def get_db():
    class FakeDB:
        def add(self, record): print(f"Added {record.email} to session")
        def commit(self): print("Saved to Postgres!")
    yield FakeDB()
# --- YOUR TURN: The Route ---
# TODO: Create the @app.post("/register") route
# TODO: Inject UserCreate and get_db
# TODO: Hash the password
# TODO: Create DBUser, add to db, commit to db
# TODO: Return success message
app.post("/register")
async def register_user(user_data:UserCreate, db: Session = Depends(get_db)):
    new_user = DBUser(
        name=user_data.name,
        hash_password =user_data.__hash__
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

#The corrected syntax
# @app.post("/register")
# async def register_user(user_data: UserCreate, db = Depends(get_db)):
    
#     # 1. Transform the data (Hash the raw password)
#     secure_password = hash_password(user_data.password)
    
#     # 2. Create the Database Object
#     # Match the DBUser constructor: email and hashed_password
#     new_user = DBUser(
#         email=user_data.email,
#         hashed_password=secure_password
#     )
    
#     # 3. Save to Database
#     db.add(new_user)
#     db.commit()
#     # db.refresh(new_user) <- Good instinct for real SQLAlchemy!
    
#     # 4. Return safe JSON response (Never return the password!)
#     return {"message": "User created", "email": new_user.email}

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# The API Blueprint (What React sends)
class UserCreate(BaseModel):
    email: str
    password: str

# Our fake helper function
def hash_password(raw_password: str) -> str:
    return f"super_secret_hash_of_{raw_password}"


# 1. The Decorator for a POST request to /register
@app.post("/register")
async def register_user(user_data: UserCreate):
    
    # 2. Grab the raw password from user_data and hash it
    hashed_pw = hash_password(user_data.password)
    
    # 3. Return a dictionary containing the email and the new hashed password
    # e.g., {"email": ..., "saved_hash": ...}
    return {"email":user_data.email , "saved_hash":hashed_pw}
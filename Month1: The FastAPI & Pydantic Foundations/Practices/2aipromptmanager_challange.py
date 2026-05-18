from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

class AIRequest(BaseModel):
    # '...' means this field is REQUIRED
    prompt: str = Field(..., min_length=10)
    model_name: str = "gpt-3.5-turbo"
    # ge = greater than or equal | le = less than or equal
    token_limit: int = Field(..., ge=1, le=4000)

@app.post("/process-prompt")
async def create_prompt(request_data: AIRequest):
    # Convert Pydantic object to a standard Python Dictionary
    data_dict = request_data.model_dump() 
    
    return {
        "message": "ai_response", 
        "prompt_received": data_dict["prompt"],
        "config": data_dict
    }
@app.get("/model/{category}")
async def list_category(category: str, provider: str):
    # category comes from the URL path: /model/chat
    # provider comes from the Query String: ?provider=openai
    return {"message": f"Fetching {category} models from {provider}"}
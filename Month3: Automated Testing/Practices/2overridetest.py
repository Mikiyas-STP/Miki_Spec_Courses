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
def override_user_tier():
    return "Gold"
app.dependency_overrides[get_user_tier] = override_user_tier 

def test_vip_access():
    # TODO: 3. Hit the client and assert the VIP Lounge response! 
    response = client.get("/vip-status")
    assert response.status_code == 200
    assert response.json() == {"tier":"Gold","message":"Welcome to the VIP Lounge!"}


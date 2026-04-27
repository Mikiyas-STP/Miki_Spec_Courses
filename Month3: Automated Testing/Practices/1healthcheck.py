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
def test_health_check():

    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy", "db": "connected"}

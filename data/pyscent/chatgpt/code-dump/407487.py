from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_email_prompt():
    # Replace 'your_test_prompt' with the actual email prompt you want to test
    test_prompt = "Test email prompt content."

    response = client.post("/emails", json={"email_prompt": test_prompt})
    assert response.status_code == 200
    assert response.text.strip()  # Check if the response text is not empty

# Other tests and assertions can be added here

from fastapi.testclient import TestClient
from app.api import app

client = TestClient(app)


def test_create_employee_happy_path():
    payload = {
        "full_name": "Natalia Quiroga",
        "email": "natalia_unique_test@example.com",
    }

    response = client.post("/employees", json=payload)

    assert response.status_code == 201
    assert response.json() == {"message": "employee created"}


def test_create_employee_duplicate_email():
    payload = {
        "full_name": "Omar Pelusa",
        "email": "duplicate_test@example.com",
    }

    first_response = client.post("/employees", json=payload)
    assert first_response.status_code == 201

    second_response = client.post("/employees", json=payload)

    assert second_response.status_code == 400
    assert second_response.json() == {"detail": "email already exists"}


def test_create_employee_invalid_email():
    payload = {
        "full_name": "Invalid Email User",
        "email": "not-an-email",
    }

    response = client.post("/employees", json=payload)

    assert response.status_code == 422

    body = response.json()
    assert "detail" in body
    assert isinstance(body["detail"], list)
    assert body["detail"][0]["loc"][-1] == "email"


def test_create_employee_missing_email():
    payload = {
        "full_name": "Missing Email User",
    }

    response = client.post("/employees", json=payload)

    assert response.status_code == 422

    body = response.json()
    assert "detail" in body
    assert isinstance(body["detail"], list)
    assert body["detail"][0]["loc"][-1] == "email"
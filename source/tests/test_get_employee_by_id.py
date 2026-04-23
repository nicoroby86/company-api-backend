

from fastapi.testclient import TestClient
from app.api import app

client = TestClient(app)

def test_get_employee_not_found():
    response = client.get("/employees/999")
    
    assert response.status_code == 404
    assert response.json()['detail'] == 'employee not found'


def test_get_employee_invalid_type():
    response = client.get("/employees/abc")
    
    assert response.status_code == 422













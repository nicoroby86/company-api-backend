from fastapi.testclient import TestClient
from app.api import app

client = TestClient(app)

def test_get_employees_returns_list():
    response = client.get("/employees")
    
    assert response.status_code == 200
    
    data = response.json()
    assert isinstance(data, list)
    
    for employee in data:
        assert 'employee_id' in employee
        assert 'full_name' in employee
        assert 'email' in employee
        assert 'created_at' in employee
        assert isinstance(employee['employee_id'], int)
        assert isinstance(employee['full_name'], str)
        assert isinstance(employee['email'], str)
        assert isinstance(employee['created_at'], str)
        assert employee['full_name'] != ""
        assert employee['email'] != ""

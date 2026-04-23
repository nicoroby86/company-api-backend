from fastapi.testclient import TestClient
from app.api import app


client = TestClient(app)

def test_get_tasks_employee_with_tasks():
    response = client.get("/tasks?employee_id=1&status=pending")
    
    assert response.status_code == 200
    
    data = response.json() 
    assert isinstance(data, list)
    assert len(data) > 0
    
    for task in data:
        assert 'task_id' in task
        assert 'description' in task
        assert 'status' in task
        assert task['status'] == 'pending'

def test_get_tasks_employee_with_no_tasks():
    response = client.get("/tasks?employee_id=8&status=pending")
    
    assert response.status_code == 200
    assert response.json() == []

def test_get_tasks_invalid_employee_id():
    response = client.get("/tasks?employee_id=test&status=pending")
    
    assert response.status_code == 422
    
    data = response.json() 
    assert data['detail'][0]['loc'] == ['query', 'employee_id']

def test_get_tasks_invalid_status():
    response = client.get("/tasks?employee_id=1&status=invalid")
    
    assert response.status_code == 422
    
    data = response.json() 
    assert 'detail' in data
    assert data['detail'][0]['loc'] == ['query', 'status']









import pytest
from fastapi.testclient import TestClient

def test_login(client):
    """Test user login"""
    # Test login with correct credentials
    response = client.post(
        "/auth/login",
        data={"username": "testuser", "password": "testpassword"}
    )

    assert response.status_code == 200
    assert "access_token" in response.json()
    assert response.json()["token_type"] == "bearer"

def test_create_project(client):
    """Test project creation"""
    # First login to get token
    login_response = client.post(
        "/auth/login",
        data={"username": "testuser", "password": "testpassword"}
    )
    token = login_response.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # Create a project
    project_data = {
        "name": "Test Project",
        "idea": "A simple test project"
    }

    response = client.post(
        "/projects/create",
        json=project_data,
        headers=headers
    )

    assert response.status_code == 201
    assert "msg" in response.json()
    assert "ai_results" in response.json()

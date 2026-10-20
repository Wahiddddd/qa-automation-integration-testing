
import requests
import pytest

from data.test_data import TEST_INVALID_CREATE_USER
from db.database import get_user_by_id, delete_user_by_id

def test_create_user_valid():
    payload = {
        "username": "qa_day31",
        "email": "qa_day31@example.com",
        "role": "buyer"
    }

    response = requests.post(
        "http://127.0.0.1:5000/users",
        json=payload
    )

    assert response.status_code == 201

    body = response.json()
    user_id = body["id"]

    try:
        assert "id" in body
        assert "username" in body
        assert "email" in body
        assert "role" in body

        assert body["username"] == payload["username"]
        assert body["email"] == payload["email"]
        assert body["role"] == payload["role"]

    finally:
        delete_user_by_id(user_id)

    assert get_user_by_id(user_id) is None

def test_create_user_invalid():
    payload = {
        "username": "qa_day31",
        "role": "buyer"
    }

    response = requests.post("http://127.0.0.1:5000/users", json=payload)

    assert response.status_code == 400

    body = response.json()

    assert body["message"] == "username, email, dan role harus diisi"

@pytest.mark.parametrize("username, email, role", TEST_INVALID_CREATE_USER)

def test_create_user_empty_email(username, email, role):
    payload = {
        "username": username,
        "email" : email,
        "role": role
    }

    response = requests.post("http://127.0.0.1:5000/users", json=payload)

    assert response.status_code == 400

    body = response.json()

    assert body["message"] == "username, email, dan role harus diisi"

def test_create_user_email_number():
    payload = {
        "username": "qa_day31",
        "email": 12345,
        "role": "buyer"
    }

    response = requests.post(
        "http://127.0.0.1:5000/users",
        json=payload
    )

    assert response.status_code == 400

    body = response.json()
    assert body["message"] == "username, email, dan role harus berupa string"

def test_delete_user_by_id(created_user):
    user_id = created_user["id"]

    delete_user_by_id(user_id)

    db_user = get_user_by_id(user_id)

    assert db_user is None
    

import pytest
import requests
import uuid

from db.database import delete_user_by_id, delete_user_by_email


@pytest.fixture
def created_user():
    user_id = None

    try:
        response = requests.post(
            "http://127.0.0.1:5000/users",
            json={
                "username": "wahid_cleanup",
                "email": "wahid_cleanup@test.com",
                "role": "buyer"
            }
        )

        body = response.json()

        if isinstance(body, dict):
            user_id = body.get("id")

        assert response.status_code == 201

        yield body

    finally:
        if user_id is not None:
            delete_user_by_id(user_id)

@pytest.fixture
def created_user_unik_email(request):
    email = request.param
    user_id = None

    try:
        payload = {
            "username": "testEmail",
            "email": email,
            "role": "buyer"
        }

        response = requests.post(
            "http://127.0.0.1:5000/users",
            json=payload
        )

        body = response.json()

        if isinstance(body, dict):
            user_id = body.get("id")

        assert response.status_code == 201

        yield body

    finally:
        if user_id is not None:
            delete_user_by_id(user_id)
        else:
            delete_user_by_email(email)

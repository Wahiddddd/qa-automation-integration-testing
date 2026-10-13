import pytest
import requests

from db.database import delete_user_by_id


@pytest.fixture
def created_user():

    payload = {
        "username": "wahid_cleanup",
        "email": "wahid_cleanup@test.com",
        "role": "buyer"
    }

    response = requests.post(
        "http://127.0.0.1:5000/users",
        json=payload
    )

    assert response.status_code == 201

    body = response.json()

    user_id = body["id"]

    yield body

    delete_user_by_id(user_id)
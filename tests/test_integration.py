import requests
import pytest
from db.database import get_user_by_id, delete_user_by_id
from data.test_data import TEST_EMAIL_UNIK

@pytest.mark.smoke
@pytest.mark.regression
def test_create_user_api():

    payload = {
        "username": "qa_wahid",
        "email": "qa_wahid@test.com",
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

        db_user = get_user_by_id(user_id)

        assert db_user["id"] == body["id"]
        assert db_user["username"] == body["username"]
        assert db_user["email"] == body["email"]
        assert db_user["role"] == body["role"]
    finally:
        delete_user_by_id(user_id)

    assert get_user_by_id(user_id) is None

@pytest.mark.smoke
@pytest.mark.regression
def test_create_user_integration(created_user):
    assert created_user is not None

    assert created_user["username"] == "wahid_cleanup"
    assert created_user["email"] == "wahid_cleanup@test.com"
    assert created_user["role"] == "buyer"
    user_id = created_user["id"]

    db_user = get_user_by_id(user_id)

    assert db_user is not None
    
    assert created_user["username"] == db_user["username"]
    assert created_user["email"] == db_user["email"]
    assert created_user["role"] == db_user["role"]

@pytest.mark.parametrize("created_user_unik_email", TEST_EMAIL_UNIK, indirect=True)
def test_create_user_unik_email(created_user_unik_email):
    body = created_user_unik_email
    assert body["email"] in [
        "qa_tc01@example.com",
        "qa_tc02@example.com",
        "qa_tc03@example.com"
    ]

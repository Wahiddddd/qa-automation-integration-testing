import pytest
import requests
from data.test_data import TEST_USERS

from db.database import (
    get_connection,
    get_user_by_id,
    delete_user_by_id,
    insert_user
)

@pytest.mark.smoke
@pytest.mark.regression
def test_database_connection():
    connection = get_connection()

    assert connection.is_connected()

    connection.close()

'''def test_get_user_by_id():
    user = get_user_by_id(1)

    assert user is not None
    assert user["id"] == 1
    assert user["username"] == "emilys"
    assert user["email"] == "emily@test.com"
    assert user["role"] == "buyer"'''

@pytest.mark.regression
@pytest.mark.parametrize("expected_id, expected_username, expected_role", TEST_USERS)
def test_get_user_by_id(expected_id, expected_username, expected_role):
    user = get_user_by_id(expected_id)
    
    assert user is not None
    assert user["id"] == expected_id
    assert user["username"] == expected_username
    assert user["role"] == expected_role

@pytest.mark.smoke
@pytest.mark.sanity
@pytest.mark.regression
def test_delete_user_by_id():
    user_id = insert_user(
        "qa_delete_test",
        "qa_delete_test@test.com",
        "buyer"
    )

    try:
        # Pastikan user berhasil dibuat
        user = get_user_by_id(user_id)
        assert user is not None

        # Jalankan operasi yang sedang diuji
        delete_user_by_id(user_id)

        # Pastikan user sudah terhapus
        user_after_delete = get_user_by_id(user_id)
        assert user_after_delete is None

    finally:
        # Membersihkan user jika masih ada
        user = get_user_by_id(user_id)

        if user is not None:
            delete_user_by_id(user_id)
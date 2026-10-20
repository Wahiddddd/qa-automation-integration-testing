import pytest

TEST_USERS = (
    pytest.param(1, "emilys", "buyer", id="TC01"),
    pytest.param(2, "budi", "buyer", id="TC02"),
    pytest.param(3, "andi", "admin", id="TC03")   
)

TEST_INVALID_CREATE_USER = (
    pytest.param("qa_day31", "", "buyer", id="TC01"),
    pytest.param("qa_day31", None, "buyer", id="TC02")
)

TEST_EMAIL_UNIK = (
    pytest.param("qa_tc01@example.com", id="TC01"),
    pytest.param("qa_tc02@example.com", id="TC02"),
    pytest.param("qa_tc03@example.com", id="TC03")
)
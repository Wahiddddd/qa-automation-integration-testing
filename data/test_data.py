import pytest

TEST_USERS = (
    pytest.param(1, "emilys", "buyer", id="TC01"),
    pytest.param(2, "budi", "buyer", id="TC02"),
    pytest.param(3, "andi", "admin", id="TC03")   
)
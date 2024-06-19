import pytest
from main import get_all_records, create_new_account, create_new_income

def test_get_all_records():
    records = get_all_records()
    assert len(records) == 0

def test_create_new_account():
    create_new_account("John Doe", 1000)
    records = get_all_records()
    assert len(records) == 1
    assert records[0][1] == "John Doe"
    assert records[0][2] == 1000
    assert records[0][3] == "account"

def test_create_new_income():
    create_new_income("John Doe", 1000)
    records = get_all_records()
    assert len(records) == 2
    assert records[1][1] == "John Doe"
    assert records[1][2] == 1000
    assert records[1][3] == "income"
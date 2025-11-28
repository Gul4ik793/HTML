import pytest
from auth import login

#1.	Позитивный тест

def test_login():
    username = "admin"
    password = "admin123"
    result = login(username, password)
    assert result is True

#2.	Негативные тесты
def test_login_user():
    with pytest.raises(ValueError, match="Пользователь не найден"):
        login("tom", "123")


def test_login_password():
    with pytest.raises(ValueError, match="Неверный пароль"):
        login("admin", "admin")



#3.	Фикстура

@pytest.fixture(scope="module")
def valid_user():
    return {
        "username": "admin",
        "password": "admin123"
    }

def test_login_1(valid_user):
    username = valid_user["username"]
    password = valid_user["password"]
    user = login(username, password)
    assert user == True


def test_login_user1(valid_user):
    with pytest.raises(ValueError, match="Пользователь не найден"):
        login("tom", valid_user["password"])


def test_login_password1(valid_user):
    with pytest.raises(ValueError, match="Неверный пароль"):
        login(valid_user["username"], "1234")

#4.	Параметризация
@pytest.fixture(scope="module")
def valid_user():
    return {
        "username": "admin",
        "password": "admin123"
    }

@pytest.mark.parametrize("username, password, expected_result", [
    ("admin", "admin123", True),
    ("admin", "123", False),
    ("tom", "123", False),
])
def test_login_2(username, password, expected_result):
    if expected_result:
        result = login(username, password)
        if expected_result:
            assert result is True
        else:
            assert result is False
    else:
        with pytest.raises(ValueError):
            login(username, password)

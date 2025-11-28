def get_user(username):
    users = {
        "admin": {"username": "admin", "password": "admin123"},
        "guest": {"username": "guest", "password": "guest"}
    }
    return users.get(username)

def login(username, password):
    user = get_user(username)
    if not user:
        raise ValueError("Пользователь не найден")
    if user["password"] != password:
        raise ValueError("Неверный пароль")
    return True
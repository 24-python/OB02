class User:
    def __init__(self, user_id, name):
        self._user_id = user_id
        self._name = name
        self._access_level = 'user'

    def get_user_id(self):
        return self._user_id

    def get_name(self):
        return self._name

    def get_access_level(self):
        return self._access_level

    def set_name(self, name):
        self._name = name

    def set_access_level(self, access_level):
        if access_level in ['user', 'admin']:
            self._access_level = access_level
        else:
            raise ValueError("Invalid access level")


class Admin(User):
    def __init__(self, user_id, name, admin_access_level):
        super().__init__(user_id, name)
        self._access_level = 'admin'
        self._admin_access_level = admin_access_level
        self._users = []

    def get_admin_access_level(self):
        return self._admin_access_level

    def add_user(self, user):
        if isinstance(user, User):
            self._users.append(user)
        else:
            raise TypeError("Only instances of User can be added")

    def remove_user(self, user_id):
        self._users = [user for user in self._users if user.get_user_id() != user_id]

    def get_users(self):
        return self._users


# Пример использования
# Создаем обычного пользователя
user1 = User(1, 'Alice')
print(f"User ID: {user1.get_user_id()}, Name: {user1.get_name()}, Access Level: {user1.get_access_level()}")

# Создаем администратора
admin = Admin(2, 'Bob', 'high')
print(
    f"Admin ID: {admin.get_user_id()}, Name: {admin.get_name()}, Access Level: {admin.get_access_level()}, Admin Access Level: {admin.get_admin_access_level()}")

# Администратор добавляет пользователя в систему
admin.add_user(user1)
print(f"Users in system: {[user.get_name() for user in admin.get_users()]}")

# Администратор удаляет пользователя из системы
admin.remove_user(1)
print(f"Users in system after removal: {[user.get_name() for user in admin.get_users()]}")
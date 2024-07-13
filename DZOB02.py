class User():
    def __init__(self, user_id, name):
        self._user_id = user_id
        self._name = name
        self._access_level = 'user'

class Admin(User):
    def __init__(self, user_id, name, admin_access_level):
        super().__init__(user_id, name)
        self._admin_access_level = admin_access_level
        self._access_level = 'admin'
        self._user = []
        self    def add_user(self):
        print("Пользователь добавлен")
    def remove_user(self):
        print("Пользователь удален")

user1 =




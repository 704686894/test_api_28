import unittest
from apis.user_mannger_api import UserManngerApi
from datas import user_data
from setting import LOGIN


class TestUserCase(unittest.TestCase):
    user_id = 0

    @classmethod
    def setUpClass(cls) -> None:
        cls.user = UserManngerApi()


    def test_add_user(self):
        username = user_data.user_data.get('username')
        password = user_data.user_data.get('password')
        result = self.user.addUser(username,password)
        if result.get("data").get("id"):
            TestUserCase.user_id = result.get("data").get("id")
        self.assertEqual(0,result.get("errno"))

    def test_update_user(self):
        username = user_data.user_data.get('newuser')
        password = user_data.user_data.get('password')
        result = self.user.update_user1(TestUserCase.user_id,username,password)
        self.assertEqual(0,result.get("errno"))


    def test_del_user(self):
        username = user_data.user_data.get('newuser')
        password = user_data.user_data.get('password')
        result = self.user.delete_user(TestUserCase.user_id,username,password)
        self.assertEqual(0,result.get('errno'))

    def test_check_user(self):
        result = self.user.check_user1()
        self.assertEqual(0,result.get('errno'))
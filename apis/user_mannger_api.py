from apis.base import Base
from loguru import logger

from setting import LOGIN


class UserManngerApi(Base):
    def __init__(self):
        self.add_user = "/admin/admin/create"
        self.update_user = "/admin/admin/update"
        self.check_user = "/admin/admin/list?page=1&limit=20&sort=add_time&order=desc"
        self.del_user = "/admin/admin/delete"


    def addUser(self,username,password,**kwargs):
        add_url = self.baseUrl_get(self.add_user)
        add_data = {'username':username,'password':password}
        if kwargs:
           add_data.update(**kwargs)
        logger.info("新增管理员为：{}".format(add_data))
        return self.post(add_url,add_data)

    def update_user1(self,userId,username,password,**kwargs):
        update_url = self.baseUrl_get(self.update_user)
        update_data = {'id':userId,'username':username,'password':password}
        if kwargs:
            update_data.update(**kwargs)
        logger.info("修改管理员操作成功：{}".format(update_data))
        return self.post(update_url,update_data)

    def delete_user(self, userId, username, password, **kwargs):
        del_url = self.baseUrl_get(self.del_user)
        del_data = {"id": userId, "username": username, "password": password}
        if kwargs:
            del_data.update(**kwargs)
        logger.info("删除管理员操作成功：{}".format(del_data))
        return self.post(del_url, del_data)

    def check_user1(self):
        check_user = self.baseUrl_get(self.check_user)
        return self.get(check_user)







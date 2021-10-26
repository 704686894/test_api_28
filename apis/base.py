import requests
from loguru import logger
from cacheout import Cache

from setting import BASE_URL

cache = Cache()

class Base(object):


    def baseUrl_get(self,path,parmes=None):
        if parmes:
            return BASE_URL + path + parmes
        return BASE_URL + path


    def get(self,url):
        try:
            response = requests.get(url,headers=self.get_headers())
            result = response.json()
            logger.info("请求get数据：{}".format(result))
            return result
        except Exception as e:
            logger.error("请求get方法失败：{}".format(e))

    def post(self,url,data):
        try:
            response = requests.post(url,json=data,headers=self.get_headers())
            result = response.json()
            logger.info("请求post数据：{}".format(result))
            return result
        except Exception as e:
            logger.error("请求post方法失败：{}".format(e))

    def login(self,username,password):
        login_path = "/admin/auth/login"
        login_url = self.baseUrl_get(login_path)
        login_data = {"username":username,"password":password}
        result = self.post(login_url,login_data)
        try:
            if 0 == result.get("errno"):
                logger.info("登录成功")
                token = result.get("data").get("token")
                cache.set("token",token)
            else:
                logger.error("登录失败：{}".format(result))
        except Exception as e:
            logger.error("登录出现异常{}".format(e))




    def get_headers(self):
         headers = {"Content-Type":"application/json"}
         token = cache.get("token")
         if token:

            headers.update({"X-Litemall-Admin-Token":token})
            logger.warning("请求头返回数据：{}，提示多个接口需要带token".format(headers))
         return  headers

# if __name__ == '__main__':
#     b = Base()
#     print(b.baseUrl_get("admin/auth/login"))
#     print(b.baseUrl_get("admin/auth/login","page=1&limit=20&sort=add_time&order=desc"))
#     print(b.baseUrl_get("http://www.weather.com.cn/data/sk/101010100.html"))
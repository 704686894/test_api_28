import unittest

from HTMLTestRunner import HTMLTestRunner
from apis.base import Base
from setting import FILE_NAME, LOGIN

if __name__ == '__main__':

    Base().login(LOGIN.get("username"),LOGIN.get("password"))

    suite = unittest.TestLoader().discover("./cases","test*.py")
    with open(FILE_NAME,'wb') as f:
       runner = HTMLTestRunner(f,title='测试报告')
       runner.run(suite)
    f.close()
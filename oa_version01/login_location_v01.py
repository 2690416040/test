from selenium.webdriver.common.by import By
class LoginLocation:
    def __init__(self):
        #用户名
        self.username=(By.NAME,"account")
        #密码
        self.password=(By.NAME,"password")
        #登录按钮
        self.button=(By.ID,"submit")
        #错误提示信息
        self.error=(By.ID,"status")
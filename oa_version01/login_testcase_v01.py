import unittest
from selenium import webdriver
from ddt import ddt,data,unpack
from oa_version01.login_location_v01 import LoginLocation
from time import sleep
#使用unittest框架编写测试用例
@ddt
class LoginTest(unittest.TestCase):
    def setUp(self) -> None:
        self.driver=webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)
        self.lct=LoginLocation()
        url="http://192.168.31.145:8066/"
        self.driver.get(url)
    def tearDown(self) -> None:
        self.driver.quit()
    #准备测试数据
    @data(["1","admin","","http://192.168.31.145:8066/general/"],
          ["2","admin","","http://192.168.31.145:8066/general/"],
          ["3","123", "","用户名或密码错误！"],
          ["4","admin","666","用户名或密码错误！"])
    @unpack
    #编写测试用例
    def test_login(self,i,u,p,e):
        username=self.driver.find_element(*self.lct.username)
        username.send_keys(u)
        password=self.driver.find_element(*self.lct.password)
        password.send_keys(p)
        button=self.driver.find_element(*self.lct.button)
        button.click()
        #断言
        #用户名和密码正确的断言
        if u=="admin" and p=="":
            actual1=self.driver.current_url#登录成功后获取地址栏中的URL
            try:
                self.assertEqual(e,actual1,"实际结果跟预期结果不一致，请知晓！")
                print("第",i,"条测试用例，登录正确用户名和密码是",u,p)
            except AssertionError as e1:
                print("登录错误",e1)
        #用户名和密码错误的断言
        else:
            error=self.driver.find_element(*self.lct.error)
            actual2=error.text
            try:
                self.assertEqual(actual2,e)
                print("第",i,"条测试用例","登录错误的用户名和密码是",u,p)
            except AssertionError as e2:
                print("登录错误",e2)
if __name__=="__main__":
    unittest.main()












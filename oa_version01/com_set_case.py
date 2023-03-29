from selenium import webdriver
import unittest
from ddt import ddt,data,unpack
import csv
from oa_version01.com_set_location import ComPary
from oa_version01.login_location_v01 import LoginLocation
from time import sleep
#通过CSV的方式获取测试数据
def test_data():
    file=open("D:\oa_selenium_project\company_infor_set_data_v01.csv","r")
    datas=csv.reader(file)
    my_list=[]
    for line in datas:
        my_list.append(line)
    file.close()
    return my_list
#使用unittest框架
@ddt
class CompanyInforSetTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver=webdriver.Firefox()
        cls.driver.implicitly_wait(15)
        cls.driver.maximize_window()
        cls.cis=ComPary()
        url="http://192.168.31.145:8066/"
        cls.driver.get(url)
    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
    def setUp(self) -> None:
        pass
    def tearDown(self) -> None:
        pass
    #登录被测系统
    def login(self,u,p):
        self.lct=LoginLocation()
        self.username=self.driver.find_element(*self.lct.username)
        self.username.send_keys(u)
        self.password=self.driver.find_element(*self.lct.password)
        self.password.send_keys(p)
        self.button=self.driver.find_element(*self.lct.button)
        sleep(1)
        self.button.click()
    #准备用户登录的测试数据
    def test_1_login(self):
        login_datas={"username":"admin","password":""}
        #登录
        self.login(login_datas["username"],login_datas["password"])
        #点击各个模块
        #点击系统设置模块
        self.a_set=self.driver.find_element(*self.cis.a_set)
        self.a_set.click()
        #点击组织机构设置
        self.b_set=self.driver.find_element(*self.cis.b_set)
        self.b_set.click()
        #点击单位信息设置
        self.c_set=self.driver.find_element(*self.cis.c_set)
        self.c_set.click()
        #对ifname的处理
        self.driver.switch_to.frame(0)
        #准备测试数据
    @data(*test_data())
    @unpack
    #编写测试用例
    def test_companyinforset(self, cn, ct, cf, cp, ca, cs, ce, cb, cbn):
        # 1、单位名称
        self.company_name = self.driver.find_element(*self.cis.d_set)
        self.company_name.clear()
        self.company_name.send_keys(cn)
        # 2、单位电话
        self.company_telphone = self.driver.find_element(*self.cis.e_set)
        self.company_telphone.clear()
        self.company_telphone.send_keys(ct)
        # 3、单位传真
        self.company_fax = self.driver.find_element(*self.cis.f_set)
        self.company_fax.clear()
        self.company_fax.send_keys(cf)
        # 4、单位邮编
        self.company_post_code = self.driver.find_element(*self.cis.g_set)
        self.company_post_code.clear()
        self.company_post_code.send_keys(cp)
        # 5、单位地址
        self.company_address = self.driver.find_element(*self.cis.h_set)
        self.company_address.clear()
        self.company_address.send_keys(ca)
        # 6、官方网址
        self.company_site = self.driver.find_element(*self.cis.i_set)
        self.company_site.clear()
        self.company_site.send_keys(cs)
        # 7、电子邮箱
        self.company_email = self.driver.find_element(*self.cis.email_set)
        self.company_email.clear()
        self.company_email.send_keys(ce)
        # 8、开户银行
        self.company_bank = self.driver.find_element(*self.cis.k_set)
        self.company_bank.clear()
        self.company_bank.send_keys(cb)
        # 9、银行账号
        self.company_bank_no = self.driver.find_element(*self.cis.l_set)
        self.company_bank_no.clear()
        self.company_bank_no.send_keys(cbn)
        # 10、更新按钮
        self.update = self.driver.find_element(*self.cis.update)
        sleep(1)
        self.update.click()
        #断言
        try:
            #实际结果
            self.d_set=self.driver.find_element(*self.cis.d_set)
            actual=self.d_set.get_attribute("value")
            #预期结果
            expected=cn
            self.assertEqual(actual,expected,"实际结果与预期结果不一致")
            print("单位名称是：",cn)
        except AssertionError as e:
            print(e)

if __name__=="__main__":
        unittest.main()










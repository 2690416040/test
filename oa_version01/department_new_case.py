from selenium import webdriver
import unittest
from ddt import ddt,data,unpack
from oa_version01.login_location_v01 import LoginLocation
from oa_version01.department_new_location import DepartMent
import csv
from selenium.webdriver.support.select import Select
#使用csv的方式获取数据
def get_data(f):
    user_file=open(f,"r")
    datas=csv.reader(user_file)
    my_list=[]
    for line in datas:
        my_list.append(line)
    user_file.close()
    return my_list
#使用unittest框架
@ddt
class DepartmentNew(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver=webdriver.Firefox()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(20)
        cls.dm=DepartMent()
        test_url="http://192.168.31.145:8066/"
        cls.driver.get(test_url)
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
        username=self.driver.find_element(*self.lct.username)
        username.send_keys(u)
        password=self.driver.find_element(*self.lct.password)
        password.send_keys(p)
        button=self.driver.find_element(*self.lct.button)
        button.click()
    #预置条件
    def test_1_paran(self):
        self.login("admin","")
        #进入系统后对模块进行点击操作
        #1、系统设置
        self.login_set=self.driver.find_element(*self.dm.login_set)
        self.login_set.click()
        #2、组织机构设置
        self.zz_set = self.driver.find_element(*self.dm.zz_set)
        self.zz_set.click()
        # 3、部门机构设置
        self.bm_set = self.driver.find_element(*self.dm.bm_set)
        self.bm_set.click()
        #ifname(id="context")
        self.ifname_context=self.driver.switch_to.frame("context")
        # ifname切换到右边(idname="right")
        self.ifname_right = self.driver.switch_to.frame("right")
        # 4、新建部门按钮
        self.insert_set = self.driver.find_element(*self.dm.insert_set)
        self.insert_set.click()
    @data(*get_data("D:\oa_selenium_project\department_new_data1_v01.csv"))
    @unpack
    #编写一级部门的测试用例
    def test_case1(self,i,no,na,p,t,f,fun):
        #1、部门编号
        self.bm_id=self.driver.find_element(*self.dm.bm_id)
        self.bm_id.clear()
        self.bm_id.send_keys(no)
        # 2、部门名称
        self.bm_name = self.driver.find_element(*self.dm.bm_name)
        self.bm_name.clear()
        self.bm_name.send_keys(na)
        # 3、上级部门(下拉框)
        self.bm_parent = self.driver.find_element(*self.dm.bm_parent)
        self.bm_select=Select(self.bm_parent)
        self.bm_select.select_by_visible_text(p)
        """
        #调式代码,获取下拉框中的所有数据
        list1=[]
        for v in self.bm_select.options:
            list1.append(v.text)
            print(v.text)
        print(list1)
        """
        # 4、部门电话
        self.bm_no = self.driver.find_element(*self.dm.bm_no)
        self.bm_no.clear()
        self.bm_no.send_keys(t)
        # 5、部门传真
        self.bm_fax = self.driver.find_element(*self.dm.bm_fax)
        self.bm_fax.clear()
        self.bm_fax.send_keys(f)
        # 6、职能说明
        self.bm_func = self.driver.find_element(*self.dm.bm_func)
        self.bm_func.clear()
        self.bm_func.send_keys(fun)
        # 7、保存按钮
        self.button = self.driver.find_element(*self.dm.button)
        self.button.click()
        # 切换回到ifname主页面(id="context")
        self.ifname_context1 = self.driver.switch_to.default_content()
        #断言
        try:
            from selenium.webdriver.common.by import By
            # ifname(id="context")
            self.ifname_context = self.driver.switch_to.frame("context")
            # ifname切换到左边(idname="left")
            self.ifname_right1 = self.driver.switch_to.frame("left")
            #对添加成功的部门重新定位
            expe="//span[text()='"+na+"']"
            self.org_tree1=(By.XPATH,expe)
            self.bm_name=self.driver.find_element(*self.org_tree1)
            self.bm_name.click()
            print("第",i,"条测试用例,新建一级部门成功")
        except AssertionError as e1:
            print(e1,"新建一级部门失败")
        # #切换回到ifname主页面(id="context")
        self.driver.switch_to.default_content()
        #切换到ifname(id="context")
        self.driver.switch_to.frame("context")
        # 在切换到ifname中的fname的右边(name="right")
        self.driver.switch_to.frame("right")
        #为下一条测试用例做准备，点击新增部门按钮
        #再次定位新建部门按钮
        self.department_new2 = self.driver.find_element(*self.dm.department_new2)
        self.department_new2.click()

    #编写二级部门的测试用例
    @data(*get_data("D:\oa_selenium_project\department_new_data2_v01.csv"))
    @unpack
    # 编写测试用例
    def test_case2(self, i, no, na, p, t, f, fun):
        # 1、部门编号
        self.bm_id = self.driver.find_element(*self.dm.bm_id)
        self.bm_id.clear()
        self.bm_id.send_keys(no)
        # 2、部门名称
        self.bm_name = self.driver.find_element(*self.dm.bm_name)
        self.bm_name.clear()
        self.bm_name.send_keys(na)
        # 3、上级部门(下拉框)
        self.bm_parent = self.driver.find_element(*self.dm.bm_parent)
        self.bm_select = Select(self.bm_parent)
        self.bm_select.select_by_visible_text(p)
        # 4、部门电话
        self.bm_no = self.driver.find_element(*self.dm.bm_no)
        self.bm_no.clear()
        self.bm_no.send_keys(t)
        # 5、部门传真
        self.bm_fax = self.driver.find_element(*self.dm.bm_fax)
        self.bm_fax.clear()
        self.bm_fax.send_keys(f)
        # 6、职能说明
        self.bm_func = self.driver.find_element(*self.dm.bm_func)
        self.bm_func.clear()
        self.bm_func.send_keys(fun)
        # 7、保存按钮
        self.button = self.driver.find_element(*self.dm.button)
        self.button.click()
        # 切换回到ifname主页面(id="context")
        self.ifname_context1 = self.driver.switch_to.default_content()
        # 断言
        try:
            from selenium.webdriver.common.by import By
            # ifname(id="context")
            self.ifname_context = self.driver.switch_to.frame("context")
            # ifname切换到左边(idname="left")
            self.ifname_right1 = self.driver.switch_to.frame("left")

            #处理添加一级部门
            #(1)去掉一级部门数据前面的(特殊字符:┊-),使用处理函数(lstrip)
            p1=p.lstrip("┊-")
            #(2)对一级部门处理后的数据添加[]
            p1="["+p1+"]"
            #(3)把处理好的数据组成一个表达式
            expe1="//span[text()='"+p1+"']"
            #(4)把定位方式组成一个元组
            self.org_tree1=(By.XPATH,expe1)
            #（5）定位一级部门
            self.bm_name=self.driver.find_element(*self.org_tree1)
            self.bm_name.click()

            # 处理二级部门
            expe2 = "//span[text()='" + na + "']"
            self.org_tree2 = (By.XPATH, expe2)
            self.bm_name = self.driver.find_element(*self.org_tree2)
            self.bm_name.click()
            print("第", i, "条测试用例,新建二级部门成功")
        except AssertionError as e2:
            print(e2, "新建二级部门失败")
        # #切换回到ifname主页面(id="context")
        self.driver.switch_to.default_content()
        # 切换到ifname(id="context")
        self.driver.switch_to.frame("context")
        # 在切换到ifname中的fname的右边(name="right")
        self.driver.switch_to.frame("right")
        # 为下一条测试用例做准备，点击新建部门按钮
        # 再次定位新建部门按钮
        self.department_new2 = self.driver.find_element(*self.dm.department_new2)
        self.department_new2.click()

    #编写部门和编号测试用例
    @data(*get_data("D:\oa_selenium_project\department_new_data3_v01.csv"))
    @unpack
    # 编写测试用例
    def test_case3(self, i, no, na, p, t, f, fun):
        # 1、部门编号
        self.bm_id = self.driver.find_element(*self.dm.bm_id)
        self.bm_id.clear()
        self.bm_id.send_keys(no)
        # 2、部门名称
        self.bm_name = self.driver.find_element(*self.dm.bm_name)
        self.bm_name.clear()
        self.bm_name.send_keys(na)
        # 3、上级部门(下拉框)
        self.bm_parent = self.driver.find_element(*self.dm.bm_parent)
        self.bm_select = Select(self.bm_parent)
        self.bm_select.select_by_visible_text(p)
        # 4、部门电话
        self.bm_no = self.driver.find_element(*self.dm.bm_no)
        self.bm_no.clear()
        self.bm_no.send_keys(t)
        # 5、部门传真
        self.bm_fax = self.driver.find_element(*self.dm.bm_fax)
        self.bm_fax.clear()
        self.bm_fax.send_keys(f)
        # 6、职能说明
        self.bm_func = self.driver.find_element(*self.dm.bm_func)
        self.bm_func.clear()
        self.bm_func.send_keys(fun)
        # 7、保存按钮
        self.button = self.driver.find_element(*self.dm.button)
        self.button.click()
        # 切换回到ifname主页面(id="context")
        self.driver.switch_to.default_content()
        # 断言
        try:
            #部门编号为空的情况
            if i=="5":
                #定位弹出提示框取出错误提示信息，跟预期结果作对比
                self.department_id_error=self.driver.find_element(*self.dm.bm_orgid)
                #实际结果
                actual=self.department_id_error.text
                #预期结果
                expected="部门编号：内容不能为空！"
                self.assertEqual(actual,expected,"实际结果与预期结果不一致，请知晓")
                print("第",i,"条测试用例执行,部门编号不能为空")
            elif i=="6":
                # 定位弹出提示框取出错误提示信息，跟预期结果作对比
                self.department_name_error = self.driver.find_element(*self.dm.bm_orgname)
                # 实际结果
                actual = self.department_name_error.text
                # 预期结果
                expected = "部门名称：内容不能为空！"
                self.assertEqual(actual, expected, "实际结果与预期结果不一致，请知晓")
                print("第", i, "条测试用例执行,部门名称不能为空")
        except AssertionError as e3:
            print(e3, "部门编号或者部门名称不能为空")
        # #切换回到ifname主页面(id="context")
        self.driver.switch_to.default_content()
        # 切换到ifname(id="context")
        self.driver.switch_to.frame("context")
        # 在切换到ifname中的fname的右边(name="right")
        self.driver.switch_to.frame("right")
if __name__=="__main__":
    unittest.main()








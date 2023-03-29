from selenium.webdriver.common.by import By
class DepartMent:
    def __init__(self):
        #系统设置
        self.login_set=(By.XPATH,"//td[text()='系统设置']")
        # 组织机构设置
        self.zz_set = (By.XPATH, "//div[text()='组织机构设置']")
        # 部门机构设置
        self.bm_set = (By.XPATH, "//span[text()='部门机构设置']")
        # 新建部门
        self.insert_set = (By.XPATH, "//span[text()='新建部门']")
        # 5.新增部门
        self.department_new2 = (By.XPATH, '//span[text()="新增部门"]')
        # 部门编号
        self.bm_id = (By.NAME,"dept_no")
        # 部门名称
        self.bm_name = (By.NAME, "dept_name")
        # 上级部门
        self.bm_parent= (By.NAME, "dept_parent")
        # 部门电话
        self.bm_no = (By.NAME, "tel_no")
        # 部门传真
        self.bm_fax= (By.NAME, "fax_no")
        # 职能说明
        self.bm_func = (By.NAME, "dept_func")
        #保存按钮
        self.button=(By.XPATH,"//span[text()='保存']")
        #部门编号为空
        self.bm_orgid=(By.XPATH,"//div[text()='部门编号：内容不能为空！']")
        #部门名称为空
        self.bm_orgname = (By.XPATH, "//div[text()='部门名称：内容不能为空！']")




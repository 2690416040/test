from selenium.webdriver.common.by import By
class ComPary:
    def __init__(self):
        #系统设置
        self.a_set=(By.XPATH,"//td[text()='系统设置']")
        #组织机构设置
        self.b_set=(By.XPATH,"//div[text()='组织机构设置']")
        #单位信息设置
        self.c_set=(By.XPATH,"//span[text()='单位信息设置']")
        #单位名称
        self.d_set=(By.NAME,"unit_name")
        #单位电话
        self.e_set=(By.NAME,"tel_no")
        #单位传真
        self.f_set=(By.NAME,"fax_no")
        #单位邮编
        self.g_set=(By.NAME,"post_no")
        #单位地址
        self.h_set=(By.NAME,"address")
        #官方地址
        self.i_set=(By.NAME,"url")
        #电子邮箱
        self.email_set=(By.NAME,"email")
        #开户银行
        self.k_set=(By.NAME,"bank_name")
        #银行账号
        self.l_set=(By.NAME,"bank_no")
        #更新按钮
        self.update=(By.XPATH,"//span[text()='更新']")




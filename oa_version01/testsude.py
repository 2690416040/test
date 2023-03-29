import unittest
from oa_version01.login_testcase_v01 import LoginTest
from oa_version01.com_set_case import CompanyInforSetTestCase
from oa_version01.department_new_case import DepartmentNew
if __name__=="__main__":
    t=unittest.TestLoader()
    login_case=t.loadTestsFromTestCase(LoginTest)
    companyinforset_case=t.loadTestsFromTestCase(CompanyInforSetTestCase)
    department_new_case=t.loadTestsFromTestCase(DepartmentNew)
    test_case=[login_case,companyinforset_case,department_new_case]
    suite=unittest.TestSuite(test_case)
    runner=unittest.TextTestRunner()
    runner.run(suite)
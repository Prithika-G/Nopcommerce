import time
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import Readconfig
from utilities import Xlutils
from utilities.customLogger import LogGen


class Test_002_DDT_Login:
    baseURL = Readconfig.getApplicationURL()
    path = "/home/ticvictech/PycharmProjects/PythonDemo/TestData/Logindata.xlsx"
    logger = LogGen.loggen()



    def test_login_ddt(self, setup):
        self.logger.info("****Test_002_DDT_Login*****")
        self.logger.info("**** Verifying Login DDT test ****")
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        time.sleep(3)
        self.lp = LoginPage(self.driver)

        self.rows = Xlutils.getRowCount(self.path, 'Sheet1')

        #lst_status = []

        self.columns = Xlutils.getColumnCount(self.path, 'Sheet1')
        #self.logger.info("Number of Rows in a Excel:", self.rows)
        #lst_status = []
        #self.logger.info("Number of columns in excel:", self.columns)

        lst_status = []
        for r in range(2, self.rows+1):
            self.username = Xlutils.readData(self.path, 'Sheet1', r, 1)  #Excel sheet1  and 1st row, 1st column
            self.password = Xlutils.readData(self.path, 'Sheet1', r, 2)
            self.exp = Xlutils.readData(self.path, 'Sheet1', r, 3)

            self.lp.setUserName(self.username)
            print("user name --", self.username)
            time.sleep(3)
            self.lp.setPassword(self.password)
            print("pass -", self.password)
            time.sleep(5)
            self.lp.clickLogin()
            time.sleep(2)

            act_title = self.driver.title
            print("act_title -- ", act_title)
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp == "pass":
                   print("Testcase Passed successfully")
                   self.logger.info("**** Passed ****")
                   self.lp.clickLogout()
                   lst_status.append("Pass")
                elif self.exp == "fail":
                   self.logger.info("****Failed****")
                   self.lp.clickLogout()
                   lst_status.append("Fail")
            elif act_title != exp_title:
                if self.exp == 'pass':
                    self.logger.info("***Failed****")
                    lst_status.append("Fail")
                elif self.exp == 'fail':
                    self.logger.info("****Passed***")
                    lst_status.append("Pass")

        if "fail" not in lst_status:
            self.logger.info("****Login DDT test passed...")
            self.driver.close()
            assert True
        else:
            self.logger.info("****Login DDT test passed... ")
            self.driver.close()
            assert False

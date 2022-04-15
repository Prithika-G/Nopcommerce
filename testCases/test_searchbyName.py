import time

from pageObjects.LoginPage import LoginPage
from pageObjects.AddcustomerPage import AddCustomer
from pageObjects.SearchCustomer import SearchCustomerPage
from utilities.readProperties import Readconfig
from utilities.customLogger import LogGen

class Test_SearchCustomerByEmail:
    baseURL = Readconfig.getApplicationURL()
    username = Readconfig.getUseremail()
    password = Readconfig.getPassword()
    logger = LogGen.loggen()

    def test_searchbyemail(self, setup):
        self.logger.info("Search customer by email")
        self.driver = setup
        time.sleep(4)
        self.driver.get(self.baseURL)
        time.sleep(4)
        self.driver.maximize_window()
        time.sleep(2)

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        time.sleep(2)
        self.lp.setPassword(self.password)
        time.sleep(2)
        self.lp.clickLogin()
        self.logger.info("*** Login successfully completed ****")

        self.os = AddCustomer(self.driver)
        self.os.clickMenu()
        time.sleep(2)

        self.logger.info("*** Searching customer by emailID ****")
        self.ad = SearchCustomerPage(self.driver)
        time.sleep(2)
        self.ad.setFname("James")
        time.sleep(2)
        self.ad.setLname("Pan")
        self.driver.execute_script("window.scrollTo(0, 200)")
        time.sleep(2)

        self.ad.clickButton()
        time.sleep(2)
        status = self.ad.searchName("James Pan")
        print("search status --", status)
        time.sleep(2)
        assert True == status
        self.logger.info(" ****  customer Name Found ***")
        self.driver.close()



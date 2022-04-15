import random
import string
import time

from selenium.webdriver.common.by import By

from pageObjects.AddcustomerPage import AddCustomer
from pageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen
from utilities.readProperties import Readconfig


#def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    #return ''.join(random.choice(chars) for x in range(size))

class Test_004_Customer:
    baseURL = Readconfig.getApplicationURL()
    username = Readconfig.getUseremail()
    password = Readconfig.getPassword()
    logger = LogGen.loggen()


    def test_002(self, setup):
        self.driver = setup
        time.sleep(2)
        self.driver.get(self.baseURL)
        time.sleep(2)
        self.driver.maximize_window()
        time.sleep(2)


        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("***** Login Successful ***** ")


        self.os = AddCustomer(self.driver)
        self.os.clickMenu()
        self.os.clickAdd()
        time.sleep(2)
        self.logger.info("**** Create New Customer Details ****")
        self.email = random_generator() + "@gmail.com"
        print(self.email)
        time.sleep(2)
        self.os.setEmail(self.email)
        time.sleep(2)
        self.os.setPassword("te123")
        time.sleep(2)
        self.os.setFname("RAJ")
        self.os.setLname("KUMAR")
        self.os.setGender("Male")
        self.os.setDob("8/08/1999")
        self.os.setCompanyname("Ticvic")
        self.os.ClickTax()
        time.sleep(2)
        self.os.clickNews()
        time.sleep(2)
        self.os.SetCustomRole("Guests")
        time.sleep(2)
        self.os.setManagerofVendor("Vendor 2")
        self.os.clickActive()
        self.os.setComment("This is a new customer")
        self.os.clickSave()

        self.logger.info("**** Saving customer information ****")

        self.msg = self.driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[1]").text

        print(self.msg)
        if 'customer has been added successfully' in self.msg:
            assert True == True
            print("Verified successfully create a new customer Passed")

            self.logger.info("**** Add customer Test Passed ***")

        else:
            self.driver.save_screenshot(".//Screenshot//" + "cus_failed.png")
            print("Verified Un-successfully create a new customer Failed")
            self.logger.info("*** Add customer Test Failed")
            assert True == False

        self.driver.close()
        self.logger.info("**** Ending Home PAge ****")


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))


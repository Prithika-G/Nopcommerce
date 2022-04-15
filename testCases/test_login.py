import time
import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import Readconfig
from utilities.customLogger import LogGen

class Test_001_Login:
    baseURL = Readconfig.getApplicationURL()
    username = Readconfig.getUseremail()
    password = Readconfig.getPassword()
    logger = LogGen.loggen()

    def test_homePageTitle(self, setup):
        self.logger.info("**** Test_001_Login ****")
        self.logger.info("**** Verifying Home PAge Title ****")
        self.driver = setup
        time.sleep(4)
        self.driver.get(self.baseURL)
        time.sleep(4)
        self.driver.maximize_window()
        time.sleep(2)
        act_title = self.driver.title
        time.sleep(3)
        #self.driver.close()
        if act_title == "Your store. Login":
            self.driver.save_screenshot("/home/ticvictech/PycharmProjects/PythonDemo/Screenshot/save_screen.png")
            time.sleep(2)
            assert True
            self.driver.close()
            self.logger.info("***** Verifying Home PAge Title Test is passed *****")
            time.sleep(2)

        else:
            #self.driver.save_screenshot(".//Screenshot//" + "test1.png")
            #self.logger.info("***** Verifying Home PAge Title Test is failed ****")
            assert False

    def test_login(self, setup):
        self.logger.info("**** Verifying Login test ****")
        self.driver = setup
        time.sleep(4)
        self.driver.get(self.baseURL)
        time.sleep(3)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        time.sleep(2)
        self.lp.setPassword(self.password)
        time.sleep(2)
        self.lp.clickLogin()
        act_title = self.driver.title
        time.sleep(2)
        #self.driver.close()
        if act_title == "Dashboard / nopCommerce administration":
            self.logger.info("**** Verifying Login test is passed ****")
            assert True
            time.sleep(2)
            self.lp.clickLogout()
            time.sleep(3)
            self.driver.close()
        else:
            self.logger.info("**** Verifying Login test is  failed ****")
            self.lp.clickLogout()
            #self.driver.close()
            self.logger.error("***Login test ***")
            time.sleep(2)
            assert False


import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class AddCustomer:
    customer_menu_xpath = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/a[1]"
    customer_submenu_xpath = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/ul/li[1]/a/p"
    customer_add_xpath = "/html/body/div[3]/div[1]/form[1]/div/div/a"
    textbox_email_id = "Email"
    textbox_password_id = "Password"
    textbox_firstname_id = "FirstName"
    textbox_lastname_id = "LastName"
    radio_gender_male_xpath = "//input[@id='Gender_Male']"
    radio_gender_female_xpath = "//input[@id='Gender_Female']"
    new_date_birth_xpath = "//input[@id='DateOfBirth']"
    textbox_company_id = "Company"
    new_checkbox_id = "IsTaxExempt"


    dropdown_news_xpath = "//*[@id='customer-info']/div[2]/div[9]/div[2]/div/div[1]/div/div/input"
    select_dropdown_news_xpath = "//ul[@id='SelectedNewsletterSubscriptionStoreIds_listbox']/li[1]"

    dropdown_customer_xpath = "//*[@id='customer-info']/div[2]/div[10]/div[2]/div/div[1]/div/div"
    dropdown_custom_registered_xpath = "//li[contains(text(),'Registered')]"
    dropdown_custom_admin_xpath = "//li[contains(text(),'Administrators')]"
    dropdown_custom_guest_xpath = "//li[contains(text(),'Guests')]"
    dropdown_custom_vendor_xpath = "//li[contains(text(),'Vendors')]"
    dropdown_manage_vendor_xpath = "//*[@id='VendorId']"

    radiobutton_active_xpath = "//input[@name='Active']"
    admin_comment_xpath = "//textarea[@name='AdminComment']"
    save_name = "save"

    def __init__(self, driver):
        self.driver = driver

    def clickMenu(self):
        self.driver.find_element(By.XPATH, self.customer_menu_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.customer_submenu_xpath).click()


    def clickAdd(self):
        self.driver.find_element(By.XPATH, self.customer_add_xpath).click()
        time.sleep(2)

    def setEmail(self, email):
        self.driver.find_element(By.ID, self.textbox_email_id).send_keys(email)
        time.sleep(2)

    def setPassword(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)
        time.sleep(2)

    def setFname(self, fname):
        self.driver.find_element(By.ID, self.textbox_firstname_id).send_keys(fname)
        time.sleep(2)

    def setLname(self, lname):
        self.driver.find_element(By.ID, self.textbox_lastname_id).send_keys(lname)
        time.sleep(2)

    def setGender(self, gender):
        if gender == 'Male':
            self.driver.find_element(By.XPATH, self.radio_gender_male_xpath).click()
        elif gender == 'Female':
            self.driver.find_element(By.XPATH, self.radio_gender_female_xpath).click()
        else:
            self.driver.find_element(By.XPATH, self.radio_gender_male_xpath).click()

    def setDob(self, dob):
        self.driver.find_element(By.XPATH, self.new_date_birth_xpath).send_keys(dob)
        time.sleep(2)

    def setCompanyname(self, comname):
        self.driver.find_element(By.ID, self.textbox_company_id).send_keys(comname)
        time.sleep(2)

    def ClickTax(self):
        self.driver.find_element(By.ID, self.new_checkbox_id).click()
        time.sleep(2)

        self.driver.execute_script("window.scrollTo(0, 200)")

    def clickNews(self):
        self.driver.find_element(By.XPATH, self.dropdown_news_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.select_dropdown_news_xpath).click()
        time.sleep(2)

    def SetCustomRole(self, role):
        self.driver.find_element(By.XPATH, self.dropdown_customer_xpath).click()
        time.sleep(3)

        if role == 'Registered':
            print(" role data --", role)
            self.listitem = self.driver.find_element(By.XPATH, self.dropdown_custom_registered_xpath)
            time.sleep(2)

        elif role == 'Administrators':
            print(" role data --", role)
            self.listitem = self.driver.find_element(By.XPATH, self.dropdown_custom_admin_xpath)
            time.sleep(2)

        elif role == 'Guests':
            time.sleep(2)
            print("Remove Register")
            self.driver.find_element(By.XPATH, "//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            time.sleep(2)
            print("select Guest")
            self.listitem = self.driver.find_element(By.XPATH, self.dropdown_custom_guest_xpath)
            print("Guest selected")
            time.sleep(2)

        elif role == 'Vendors':
            print("New role data --", role)
            self.listitem = self.driver.find_element(By.XPATH, self.dropdown_custom_vendor_xpath)
            time.sleep(2)

        else:
            # self.listitem = self.driver.find_element_by_xpath(self.dropdown_custom_guest_xpath)
            # time.sleep(2)
            print("Your Expected Custom role Data not listed in the dropdown -", role)
            print("Actual ")


        time.sleep(2)
        self.driver.execute_script("arguments[0].click();", self.listitem)

    def setManagerofVendor(self, value):
        drp = Select(self.driver.find_element(By.XPATH, self.dropdown_manage_vendor_xpath))
        drp.select_by_visible_text(value)

    def clickActive(self):
        self.driver.find_element(By.XPATH, self.radiobutton_active_xpath).click()

    def setComment(self, comment):
        self.driver.find_element(By.XPATH, self.admin_comment_xpath).send_keys(comment)

    def clickSave(self):
        self.driver.find_element(By.NAME, self.save_name).click()







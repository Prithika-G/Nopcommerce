import time
from selenium.webdriver.common.by import By

class SearchCustomerPage:
    search_email_id = "SearchEmail"
    search_f_name_id = "SearchFirstName"
    search_l_name_id = "SearchLastName"
    button_search_id = "search-customers"

    table_header_xpath = "//table[@role='grid']"
    table_data_xpath = "//table[@id='customers-grid']"
    table_row_xpath = "//table[@id='customers-grid']//tbody/tr"
    table_Column_xpath = "//table[@id='customers-grid']//tbody/tr/td"

    def __init__(self, driver):
        self.driver = driver

    def setEmail(self, email):
        self.driver.find_element(By.ID, self.search_email_id).click()
        print("search email")
        self.driver.find_element(By.ID, self.search_email_id).send_keys(email)
        time.sleep(2)

    def setFname(self, first_n):
        self.driver.find_element(By.ID, self.search_f_name_id).click()
        self.driver.find_element(By.ID, self.search_f_name_id).send_keys(first_n)
        time.sleep(2)

    def setLname(self, last_n):
        self.driver.find_element(By.ID, self.search_l_name_id).click()
        self.driver.find_element(By.ID, self.search_l_name_id).send_keys(last_n)
        time.sleep(2)

    def clickButton(self):
        self.driver.find_element(By.ID, self.button_search_id).click()
        time.sleep(2)

    def getNoOfRows(self):
        return len(self.driver.find_elements(By.XPATH, self.table_row_xpath))

    def getNoOfColumns(self):
        return len(self.driver.find_elements(By.XPATH, self.table_Column_xpath))

    def searchEmail(self, email):
        flag = False
        row = self.getNoOfRows()
        print("rvalue1 ----", row)

        if row == 1:
            table = self.driver.find_element(By.XPATH, self.table_data_xpath)
            email_id = table.find_element(By.XPATH, "//table[@id='customers-grid']/tbody/tr[1]/td[2]").text
            print(email_id)
            print(email)
            if email_id == email:
                flag = True


        elif row !=1:
            for r in range(1, row+1):
                print(self.getNoOfRows())
                print("rvale ----", r)
                table = self.driver.find_element(By.XPATH, self.table_data_xpath)
                email_id = table.find_element(By.XPATH, "//table[@id='customers-grid']/tbody/tr[" + str(r) + "]/td[2]").text
                print(email_id)
                print(email)
                if email_id == email:
                    flag = True
                    break
        return flag

    def searchName(self, name):
        flag = False
        row = self.getNoOfRows()

        if row == 1:
            table = self.driver.find_element(By.XPATH, self.table_data_xpath)
            print(table)
            Name = table.find_element(By.XPATH, "//table[@id='customers-grid']/tbody/tr[1]/td[3]").text
            if Name == name:
                flag = True

        elif row >= 1:
            for r in range(1, self.getNoOfRows() + 1):
                table = self.driver.find_element(By.XPATH, "self.table_data_xpath")
                Name = table.find_element(By.XPATH, "//table[@id='customers-grid']/tbody/tr[" + str(r) + "]/td[3]").text
                if Name == name:
                    flag = True
                    break

        return flag






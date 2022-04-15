from selenium import webdriver
import pytest
from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager
#from selenium.webdriver.chrome.service import Service

@pytest.fixture()
def setup(browser):
    global driver
    if browser == 'Chrome':
        driver = webdriver.Chrome("/home/ticvictech/PycharmProjects/PythonDemo/Driver/chromedriver")
        print("Launching Chrome browser")
    elif browser == 'firefox':
        #driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))   # To install the chrome driver automatically
        driver = webdriver.Firefox(executable_path="/home/ticvictech/PycharmProjects/PythonDemo/Driver/geckodriver")
        print("Launching  Firefox browser")
    else:
        #driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver = webdriver.Chrome("/home/ticvictech/PycharmProjects/PythonDemo/Driver/chromedriver")
    return driver

def pytest_addoption(parser):   #this will get the value from CLI
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


def pytest_configure(config):
    config._metadata['Project Name'] = 'nop commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Prithika'

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)










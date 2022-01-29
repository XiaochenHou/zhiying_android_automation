from selenium.common.exceptions import NoSuchElementException
from time import sleep

from selenium.webdriver.common.by import By

PHONE_NUMBER = "13661045480"
EXTRACT_CODE = "test_for_test"
DEVICE_NAME = "emulator-5554"
P_VERSION = "11.0.0"


def check_exists(driver, method, path):
    try:
        driver.find_element(method, path)
    except NoSuchElementException:
        return False
    return True


def wait(sec):
    # print(f'wait for {sec} seconds')
    sleep(0)


def back(driver):
    sleep(2)
    driver.back()

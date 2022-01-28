PHONE_NUMBER = "13661045480"
EXTRACT_CODE = "test_for_test"
DEVICE_NAME = "emulator-5554"
P_VERSION = "11.0.0"

from selenium.common.exceptions import NoSuchElementException


def check_exists(driver, method, path):
    try:
        driver.find_element(method, path)
    except NoSuchElementException:
        return False
    return True

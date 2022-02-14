from selenium.common.exceptions import NoSuchElementException
from time import sleep

PHONE_NUMBER = "13661045480"  # 自己手机号
EXTRACT_CODE = "test_for_test"  # 提取会议记录码
DEVICE_NAME = "emulator-5554"  # 设备名称(adb devices)
P_VERSION = "11.0.0"  # 安卓版本
SEARCH_CONTENT = "会议"  # 自定义搜索内容
ADDRESS = "0.0.0.0:4723/wd/hub"  # windows把0.0.0.0改为127.0.0.1


def check_exists(driver, method, path):
    """
    The function checks whether a specific element is exit on the current page
    :param driver: input the driver of the program
    :param method: search the element by this method, e.g. By.ID
    :param path: the path followed by the method
    :return: a boolean value tells the main program whether the element exits
    """
    try:
        driver.find_element(method, path)
    except NoSuchElementException:
        return False
    return True


def back(driver):
    """
    Customised back function that sleep 2 seconds and then proceed back method
    :param driver: the driver passed in
    :return: returns nothing
    """
    sleep(2)
    driver.back()


def tear_down(driver):
    """
    Customised ending function that prints out the ending dialogue and quit the application
    :param driver: the driver passed in
    :return: nothing
    """
    sleep(2)
    print("========ALL TESTS DONE!========")
    driver.quit()

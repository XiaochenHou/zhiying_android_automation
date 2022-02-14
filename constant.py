from selenium.common.exceptions import NoSuchElementException
from time import sleep

PHONE_NUMBER = "13661045480"        # 自己手机号
EXTRACT_CODE = "test_for_test"      # 提取会议记录码
DEVICE_NAME = "emulator-5554"       # 设备名称(adb devices)
P_VERSION = "11.0.0"                # 安卓版本
SEARCH_CONTENT = "会议"              # 自定义搜索内容
ADDRESS = "0.0.0.0:4723/wd/hub"     # windows把0.0.0.0改为127.0.0.1

def check_exists(driver, method, path):
    try:
        driver.find_element(method, path)
    except NoSuchElementException:
        return False
    return True


def back(driver):
    sleep(2)
    driver.back()


def tear_down(driver):
    sleep(2)
    print("========ALL TESTS DONE!========")
    driver.quit()

from appium import webdriver
from constant import DEVICE_NAME, P_VERSION


def set_things_up():
    print("configuration started...")
    cap = {}
    cap["deviceName"] = DEVICE_NAME
    cap["platformName"] = "Android"
    cap["platformVersion"] = P_VERSION
    cap["appPackage"] = "com.iflytek.zhiying"
    cap["appActivity"] = "com.iflytek.zhiying.LaunchActivity"
    cap['autoGrantPermissions'] = 'true'
    cap["noReset"] = "true"
    cap["newCommandTimeout"] = 2000
    driver = webdriver.Remote('0.0.0.0:4723/wd/hub', cap)
    driver.implicitly_wait(15)
    print("configuration done!")
    return driver

from appium import webdriver
from selenium.webdriver.common.by import By
from constant import PHONE_NUMBER, DEVICE_NAME, P_VERSION
from constant import wait


def set_things_up():
    print("configuration started...")
    cap = {}
    cap["deviceName"] = DEVICE_NAME
    cap["platformName"] = "Android"
    cap["platformVersion"] = P_VERSION
    cap["appPackage"] = "com.iflytek.zhiying"
    cap["appActivity"] = "com.iflytek.zhiying.LaunchActivity"
    cap["useNewWDA"] = "true"
    cap["clearSystemFiles"] = "true"
    cap["wdaStartupRetryInterval"] = 1000
    cap["waitForQuiescence"] = "false"
    cap["shouldUseSingletonTestManager"] = "false"
    cap['autoGrantPermissions'] = 'true'
    cap["wdaEventloopIdleDelay"] = 3
    driver = webdriver.Remote('0.0.0.0:4723/wd/hub', cap)
    print("configuration done!")
    return driver


def login_testing(driver):
    wait(3)
    print("========test officially started========")
    agree_btn = driver.find_element(By.XPATH, "//*[@text='同意并继续']")
    agree_btn.click()
    wait(5)
    driver.find_element(By.XPATH, "//*[@resource-id='com.iflytek.zhiying:id/iv_select']").click()
    phone_num = driver.find_element(By.XPATH, "//*[@resource-id='com.iflytek.zhiying:id/edt_phone_num']")
    print("yes")
    phone_num.send_keys(PHONE_NUMBER)
    driver.find_element(By.XPATH, "//*[@resource-id='com.iflytek.zhiying:id/btn_get_verify_code']").click()
    driver.find_element(By.XPATH, "//*[@resource-id='com.iflytek.zhiying:id/edt_verification_code']").send_keys(
        str(input("please input the verification_code: ")))
    driver.find_element(By.XPATH, "//*[@resource-id='com.iflytek.zhiying:id/tv_login']").click()
    print("Login testing done!")

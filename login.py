from selenium.webdriver.common.by import By

from constant import PHONE_NUMBER


def login_testing(driver):
    print("========test officially started========")
    agree_btn = driver.find_element(By.XPATH, "//*[@text='同意并继续']")
    agree_btn.click()

    driver.find_element(By.XPATH, "//*[@resource-id='com.iflytek.zhiying:id/iv_select']").click()
    phone_num = driver.find_element(By.XPATH, "//*[@resource-id='com.iflytek.zhiying:id/edt_phone_num']")
    print("phone number filled in")
    phone_num.send_keys(PHONE_NUMBER)
    driver.find_element(By.XPATH, "//*[@resource-id='com.iflytek.zhiying:id/btn_get_verify_code']").click()
    driver.find_element(By.XPATH, "//*[@resource-id='com.iflytek.zhiying:id/edt_verification_code']").send_keys(
        str(input("please input the verification_code: ")))
    driver.find_element(By.XPATH, "//*[@resource-id='com.iflytek.zhiying:id/tv_login']").click()
    print("Login testing done!")

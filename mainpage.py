from time import sleep

from constant import wait, back
from selenium.webdriver.common.by import By
from constant import EXTRACT_CODE, check_exists


def main_page_testing(driver):
    print("========main_page_testing started========")
    sleep(2)
    driver.implicitly_wait(2)
    while True:
        if check_exists(driver, By.ID, "com.iflytek.zhiying:id/tv_next"):
            driver.find_element(By.ID, "com.iflytek.zhiying:id/tv_next").click()
        else:
            break
    driver.implicitly_wait(15)
    # 扫一扫
    home_scan = driver.find_element(By.ID, "com.iflytek.zhiying:id/iv_home_scan")
    home_scan.click()
    print("home_scan clicked")

    back(driver)

    # cancel the questionnaire
    # if check_exists(driver, By.ID, "com.iflytek.zhiying:id/tv_cancel"):
    #     driver.find_element(By.ID, "com.iflytek.zhiying:id/tv_cancel").click()

    # main page search function test starts here
    print("search functionality test...")
    driver.find_element(By.ID, "com.iflytek.zhiying:id/rlv_home_search").click()  # click search bar
    driver.find_element(By.ID, "com.iflytek.zhiying:id/edt_search").send_keys("会议")
    driver.hide_keyboard()
    back(driver)
    print("search functionality test done!")

    # upload a picture
    print("upload functionality test...")
    driver.find_element(By.ID, "com.iflytek.zhiying:id/tv_cloud_upload").click()

    driver.find_element(By.ID, "com.iflytek.zhiying:id/llt_photo").click()

    driver.find_element(By.ID, "com.iflytek.zhiying:id/btnCheck").click()
    driver.find_element(By.ID, "com.iflytek.zhiying:id/picture_tv_ok").click()

    print("upload functionality done!")

    # delete the picture uploaded
    print("delete functionality test...")
    driver.find_element(By.ID, "com.iflytek.zhiying:id/iv_home_document_more").click()

    driver.implicitly_wait(1)
    if check_exists(driver, By.ID, "com.iflytek.zhiying:id/tv_del_file"):
        driver.find_element(By.ID, "com.iflytek.zhiying:id/tv_del_file").click()
    else:
        driver.find_element(By.ID, "com.iflytek.zhiying:id/tv_pop_delete").click()
    driver.implicitly_wait(15)
    driver.find_element(By.ID, "com.iflytek.zhiying:id/btn_selectPositive").click()
    print("delete functionality test done!")

    # 提取会议记录
    print("meeting extraction test...")
    driver.find_element(By.ID, "com.iflytek.zhiying:id/tv_extract_the_file").click()

    driver.find_element(By.ID, "com.iflytek.zhiying:id/tv_extraction_code_extraction").click()

    driver.find_element(By.ID, "com.iflytek.zhiying:id/edt_extract_code").send_keys(EXTRACT_CODE)
    driver.hide_keyboard()
    back(driver)

    print("meeting extraction test done!")

from setup import wait
from selenium.webdriver.common.by import By
from constant import EXTRACT_CODE


def main_page_testing(driver):
    wait(3)
    print("========main_page_testing started========")
    driver.find_element(By.ID, "com.iflytek.zhiying:id/tv_next").click()
    wait(1)
    # 扫一扫
    driver.find_element(By.ID, "com.iflytek.zhiying:id/tv_next").click()
    home_scan = driver.find_element(By.ID, "com.iflytek.zhiying:id/iv_home_scan")
    home_scan.click()
    print("home_scan clicked")
    wait(2)
    driver.back()
    wait(3)

    driver.find_element(By.ID, "com.iflytek.zhiying:id/tv_cancel").click()  # cancel the questionnaire

    # main page search function test starts here
    print("search functionality test...")
    driver.find_element(By.ID, "com.iflytek.zhiying:id/rlv_home_search").click()  # click search bar
    wait(2)
    driver.find_element(By.ID, "com.iflytek.zhiying:id/edt_search").send_keys("会议")
    driver.hide_keyboard()
    wait(5)
    driver.back()
    print("search functionality test done!")

    wait(1)

    # upload a picture
    print("upload functionality test...")
    driver.find_element(By.ID, "com.iflytek.zhiying:id/tv_cloud_upload").click()
    wait(2)
    driver.find_element(By.ID, "com.iflytek.zhiying:id/llt_photo").click()
    wait(2)
    driver.find_element(By.ID, "com.iflytek.zhiying:id/btnCheck").click()
    driver.find_element(By.ID, "com.iflytek.zhiying:id/picture_tv_ok").click()
    wait(5)
    print("upload functionality done!")

    # delete the picture uploaded
    print("delete functionality test...")
    driver.find_element(By.ID, "com.iflytek.zhiying:id/iv_home_document_more").click()
    wait(1)
    driver.find_element(By.ID, "com.iflytek.zhiying:id/tv_del_file").click()
    wait(1)
    driver.find_element(By.ID, "com.iflytek.zhiying:id/btn_selectPositive").click()
    wait(2)
    print("delete functionality test done!")

    # 提取会议记录
    print("meeting extraction test...")
    driver.find_element(By.ID, "com.iflytek.zhiying:id/tv_extract_the_file").click()
    wait(2)
    driver.find_element(By.ID, "com.iflytek.zhiying:id/tv_extraction_code_extraction").click()
    wait(1)
    driver.find_element(By.ID, "com.iflytek.zhiying:id/edt_extract_code").send_keys(EXTRACT_CODE)
    driver.hide_keyboard()
    driver.back()
    wait(3)
    print("meeting extraction test done!")

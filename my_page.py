from time import sleep
from selenium.webdriver.common.by import By
from constant import back


def my_page_testing(driver):
    driver.find_element(By.XPATH,
                        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout[3]").click()
    sleep(1)
    print("========my page testing started========")
    print("testing the cloud...")
    # 获取云空间
    driver.find_element(By.ID, "com.iflytek.zhiying:id/tv_cloud_space").click()
    driver.find_element(By.ID, "com.iflytek.zhiying:id/iv_help").click()
    sleep(2)
    back(driver)
    driver.find_element(By.ID, "com.iflytek.zhiying:id/iv_cloud_list").click()
    sleep(2)
    back(driver)
    back(driver)
    print("cloud testing done!")

    print("now test the recycle bin...")
    driver.find_element(By.ID, "com.iflytek.zhiying:id/tv_recycle_bin").click()
    driver.find_element(By.XPATH,
                        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.RelativeLayout[2]/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.LinearLayout[2]/android.widget.ImageView").click()
    print("deleting the file")
    driver.find_element(By.ID, "com.iflytek.zhiying:id/tv_pop_delete").click()
    driver.find_element(By.ID, "com.iflytek.zhiying:id/btn_selectPositive").click()
    back(driver)
    print("deleted!")

    print("testing other entries...")
    driver.find_element(By.ID, "com.iflytek.zhiying:id/tv_account_setting").click()
    back(driver)
    print("setting done!")
    driver.find_element(By.ID, "com.iflytek.zhiying:id/tv_product_use_guidance").click()
    sleep(2)
    back(driver)
    print("guide done!")
    driver.find_element(By.ID, "com.iflytek.zhiying:id/tv_feedback").click()
    sleep(2)
    back(driver)
    print("feedback done!")
    el12 = driver.find_element(By.ID, "com.iflytek.zhiying:id/tv_about")
    el12.click()
    el13 = driver.find_element(By.ID, "com.iflytek.zhiying:id/tv_version_update")
    el13.click()
    back(driver)
    back(driver)
    print("about done!")
    print("========my page done!========")
    driver.find_element(By.XPATH,
                        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout[1]").click()

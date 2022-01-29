from time import sleep

from constant import back
from selenium.webdriver.common.by import By


def document_page_test(driver):
    print("========Document Page Test Started========")
    # switch to the document page
    driver.find_element(By.XPATH,
                        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout[2]").click()

    print("switched to the document page")
    print("testing the three dots...")
    three_dots = driver.find_element(By.XPATH,
                                     "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.viewpager.widget.ViewPager/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.RelativeLayout[2]/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.LinearLayout[2]/android.widget.ImageView")
    three_dots.click()

    cooperation = driver.find_element(By.ID, "com.iflytek.zhiying:id/tv_cooperation_list")
    cooperation.click()
    # sleep(10)
    back(driver)
    print("cooperation done!")

    three_dots = driver.find_element(By.XPATH,
                                     "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.viewpager.widget.ViewPager/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.RelativeLayout[2]/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.LinearLayout[2]/android.widget.ImageView")
    three_dots.click()

    share = driver.find_element_by_id("com.iflytek.zhiying:id/tv_pop_share")
    share.click()

    back(driver)
    print("share done!")
    print("three dots tests done!")

    print("collection test starts...")
    document = driver.find_element_by_xpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.viewpager.widget.ViewPager/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.RelativeLayout[2]/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]")
    document.click()
    sleep(1)
    # 收藏
    star = driver.find_element_by_xpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.RelativeLayout[2]/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.ImageView[2]")
    star.click()
    back(driver)
    # 检查收藏
    check_collection(driver)
    # 与我协作
    driver.find_element(By.XPATH,
                        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.viewpager.widget.ViewPager/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.TextView").click()

    print("now check the upload page")
    driver.find_element(By.XPATH,
                        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.viewpager.widget.ViewPager/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/androidx.appcompat.app.ActionBar.Tab[2]").click()

    # upload button
    driver.find_element(By.ID, "com.iflytek.zhiying:id/iv_upload_file").click()

    back(driver)
    print("upload page done!")
    print("========document page done!========")

    # reset the page to home page
    driver.find_element(By.XPATH,
                        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.viewpager.widget.ViewPager/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/androidx.appcompat.app.ActionBar.Tab[1]").click()
    driver.find_element(By.XPATH,
                        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout[1]").click()


def check_collection(driver):
    # go to the main page
    print("now check the collection")
    driver.find_element(By.XPATH,
                        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout[1]").click()

    driver.find_element(By.ID, "com.iflytek.zhiying:id/tv_collect").click()
    sleep(2)
    # 取消收藏
    driver.find_element(By.ID, "com.iflytek.zhiying:id/iv_document_collect").click()

    print("the star unchecked")
    back(driver)

    print("collection check done!")
    driver.find_element(By.XPATH,
                        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout[2]").click()

from mainpage import main_page_testing
from setup import set_things_up
from login import login_testing
from document_page import document_page_test

if __name__ == '__main__':
    driver = set_things_up()
    # 登录测试
    login_testing(driver)

    # 首页测试
    main_page_testing(driver)

    # 文件页测试
    document_page_test(driver)
    print("========ALL TESTS DONE!========")
    driver.quit()

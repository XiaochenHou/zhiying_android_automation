from mainpage import main_page_testing
from setup import login_testing, set_things_up
from document_page import document_page_test

if __name__ == '__main__':
    driver = set_things_up()
    login_testing(driver)
    main_page_testing(driver)
    document_page_test(driver)
    print("========ALL TESTS DONE!========")
    driver.quit()

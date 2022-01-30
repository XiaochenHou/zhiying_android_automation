from constant import tear_down
from mainpage import main_page_testing
from my_page import my_page_testing
from setup import set_things_up
from login import login_testing
from document_page import document_page_test
import argparse

parser = argparse.ArgumentParser(description="Automatic smoke test for iflytek zhiying application")
parser.add_argument('--main', action='store_true', help='tests for the main page, 首页测试')
parser.add_argument('--doc', action='store_true', help='tests for the document page, 文件页测试')
parser.add_argument('--my', action='store_true', help='tests for the my page, 我的页测试')
args = parser.parse_args()
if __name__ == '__main__':
    full_test = not any(vars(args).values())
    print("is this a full test? " + str(full_test))
    driver = set_things_up(full_test)
    # 登录测试，需要reset应用
    if full_test:
        login_testing(driver)

    # 首页测试
    if args.main or full_test:
        main_page_testing(driver)

    # 文件页测试
    if args.doc or full_test:
        document_page_test(driver)

    # 我的页面测试
    if args.my or full_test:
        my_page_testing(driver)

    # 退出应用
    tear_down(driver)

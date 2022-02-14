from appium import webdriver
from constant import DEVICE_NAME, P_VERSION, ADDRESS


def set_things_up(full_test):
    print('''
    ==================================
      _ ___ _ __   _______ ___ _  __
     (_) __| |\ \ / /_   _| __| |/ /
     | | _|| |_\ V /  | | | _|| ' < 
     |_|_| |____|_|   |_| |___|_|\_\\
    ==================================
    ''')
    print("Configuration Started...")
    cap = {}
    cap["deviceName"] = DEVICE_NAME
    cap["platformName"] = "Android"
    cap["platformVersion"] = P_VERSION
    cap["appPackage"] = "com.iflytek.zhiying"
    cap["appActivity"] = "com.iflytek.zhiying.LaunchActivity"
    cap['autoGrantPermissions'] = 'true'
    if not full_test:
        cap["noReset"] = "true"

    driver = webdriver.Remote(ADDRESS, cap)
    driver.implicitly_wait(15)
    print("Configuration Done!")
    return driver

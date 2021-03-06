import os
from time import sleep

import pytest
import allure
from allure.constants import AttachmentType
from appium import webdriver as appium_webdriver
from application import Application as droid_app
import work_dir.environment
import work_dir.droid_driver as droid_driver

__author__ = 'EKravchenko'


def search_folder(end_folder):
    path = os.path.abspath(os.curdir)
    while path:
        for root, dirs, files in os.walk(path, topdown=True):
            if end_folder in root:
                return os.path.join(root[0:root.find(end_folder)], end_folder)
        path = os.path.dirname(path)


def get_free_device():
    import subprocess

    cmd = 'adb devices'
    s = subprocess.check_output(cmd.split())
    str_list = str(s).split('\\')
    for device in str_list:
        if device[0] == 'n' and len(device) > 2:
            old_activity = ''
            for i in range(0, 5):
                cmd = "adb shell dumpsys window windows | grep -E 'mCurrentFocus'"
                s = subprocess.check_output(cmd.split())
                activity_str = str(s)
                new_activity = activity_str[activity_str.find('com.'):]
                if old_activity == new_activity:
                    return device[1:]
                else:
                    old_activity = new_activity
                    sleep(1)
    raise Exception('You dont have free devices')


@pytest.fixture(scope="session", autouse=True)
def testing_session(request, create_caps):
    print("start testing session")
    print("init driver")
    caps = create_caps['caps']
    driver_url = create_caps['url']
    droid_driver.driver = create_driver(driver_url, caps)

    def close_testing_session():
        print("resource_teardown")
        droid_driver.driver.quit()

    request.addfinalizer(close_testing_session)


def pytest_addoption(parser):
    parser.addoption("--app", action="store",
                     default=os.path.abspath(
                         os.path.join(os.path.dirname(__file__), "MapsMe.apk")),
                     help="Application path")
    parser.addoption("--platformName", action="store", default="Android", help="Which mobile OS platform to use")
    parser.addoption("--platformVersion", action="store", default="7.0", help="Mobile OS version")
    parser.addoption("--deviceName", action="store", default=get_free_device(),
                     help="The kind of mobile device or emulator to use")
    parser.addoption("--appPackage", action="store", default="com.mapswithme.maps.pro",
                     help="Java package of the Android app you want to run")
    parser.addoption("--driver_url", action="store", default="http://localhost:4723/wd/hub", help="For multi run")


@pytest.fixture(scope="session")
def create_caps(request):
    url = request.config.getoption("--driver_url")
    caps = {'platformName': request.config.getoption("--platformName"),
            'platformVersion': request.config.getoption("--platformVersion"),
            'deviceName': request.config.getoption("--deviceName"),
            'appPackage': request.config.getoption("--appPackage"),
            'appActivity': 'com.mapswithme.maps.DownloadResourcesActivity',
            'launchTimeout': 360000,
            'unicodeKeyboard': 'True'

            }
    return dict(url=url, caps=caps)


@pytest.fixture(scope="session")
def app(request):
    app_object = droid_app()
    return app_object


def create_driver(url, caps):
    driver = appium_webdriver.Remote(url, caps)
    driver.implicitly_wait(5)
    return driver


@pytest.fixture(scope="session", autouse=True)
def storage(request):
    return type('storage', (), {})()


@pytest.fixture(scope="session")
def env(request):
    return work_dir.environment


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        try:
            droid_driver.driver.close_app()
            droid_driver.driver.launch_app()
            #print(storage.log)
        except:
            pass

    if call.excinfo is not None:
        parent = item.parent
        parent._previousfailed = item


def pytest_runtest_setup(item):
    previousfailed = getattr(item.parent, "_previousfailed", None)
    if previousfailed is not None:
        pytest.xfail("previous test failed (%s)" % previousfailed.name)

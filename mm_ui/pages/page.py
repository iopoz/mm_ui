from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import xml.etree.ElementTree as ET
from selenium.webdriver.support.wait import WebDriverWait

from work_dir import droid_driver


class Page(object):
    def __init__(self):
        self.driver = droid_driver.driver
        self.wait = WebDriverWait(self.driver, 15)
        self.long_wait = WebDriverWait(self.driver, 90)

    @property
    def screen_size(self):
        return self.driver.get_window_size()

    def wait_until_not_exist(self, locator):
        return self.wait.until(EC.visibility_of_element_located((By.ID, locator)))

    def wait_until_exist(self, locator):
        return self.wait.until_not(EC.visibility_of_element_located((By.ID, locator)))

    def long_wait_until_not_exist(self, locator):
        return self.wait.until_not(EC.visibility_of_element_located((By.ID, locator)))

    @property
    def get_page_source(self):
        source = self.driver.page_source
        content = ET.fromstring(source.rstrip('\n'))
        if content:
            return content
        else:
            raise Exception('Empty page source. Please check.')

    @property
    def scroll_screen(self):
        start_y = int(self.screen_size['height'] * 0.8)
        end_y = int(self.screen_size['height'] * 0.2)
        start_x = int(self.screen_size['width'] / 2)
        self.driver.swipe(start_x, start_y, start_x, end_y, 4000)


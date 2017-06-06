from selenium.common.exceptions import NoSuchElementException

from pages.enter_to_application_page import EnterToApplicationPage


class EnterToApplication(object):
    def __init__(self, app):
        self.e2ap = EnterToApplicationPage()
        self.app = app

    def first_enter(self):
        try:
            self.e2ap.next_btn.click()
            self.e2ap.done_btn.click()
            return 'Application was run firstly \n'
        except NoSuchElementException:
            self.app.first_enter = False
            msg = 'Application was run before \n'
            print(msg)
            return msg

    def download_maps(self):
        try:
            download_maps_btn = self.e2ap.downloader_map_btn
            download_maps_btn.is_displayed()
            download_maps_btn.click()
            self.e2ap.download_progress()
            return 'map is downloaded \n'
        except NoSuchElementException:
            try:
               self.e2ap.download_progress()
               return 'map is downloaded \n'
            except:
                return 'map is already downloaded \n'

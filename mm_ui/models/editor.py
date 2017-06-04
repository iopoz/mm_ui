from selenium.common.exceptions import NoSuchElementException
from pages.full_editor_place_page import FullEditorPlacePage

__author__ = 'io'


class Editor(object):
    def __init__(self, app):
        self.ep = FullEditorPlacePage()
        self.app = app

    PAGE = None

    def is_editor_opened(self):
        return self.ep.name_place_frame.is_displayed()

    def add_new_language(self, type_l, name):
        self.ep.new_language_btn.click()
        attempt = 100
        while attempt > 0:
            language = self.ep.get_interested_language(type_l)
            if language is not None:
                language.click()
                break
            else:
                self.ep.scroll_screen
                attempt -= 1
        assert self.ep.name_place_frame.is_displayed()
        self.ep.get_name_by_location(type_l).send_keys(name)

    def add_zip_code(self, code):
        try:
            zip_elm = self.ep.zip
            zip_elm.is_displayed()
        except NoSuchElementException:
            self.ep.scroll_screen
        self.ep.zip.send_keys(code)

    # def check_fields(self, fields, count=3):
    #     if count > 0:
    #         try:
    #             self.ep.cuisine.is_displayed()
    #             page = self.ep.get_page_source
    #             match = 0
    #             for k, v in fields.items():
    #                 if self.ep.get_field(page, v):
    #                     match +=1
    #             return match == len(fields) - 1
    #         except NoSuchElementException:
    #             self.ep.scroll_screen
    #             self.check_fields(fields, count-1)
    def is_field_correct(self, field, count=3):
        if count > 0:
            if self.PAGE is None:
                self.PAGE = self.ep.get_page_source
            try:
                self.ep.get_field(self.PAGE, field).get('text')
                return True
            except AttributeError:
                self.ep.scroll_screen
                self.PAGE = self.ep.get_page_source
                return self.is_field_correct(field, count - 1)
        else:
            return False

    def turn_wifi_on(self, count=3):
        if count > 0:
            try:
                wifi = self.ep.wifi
                wifi.is_displayed()
                if wifi.get_attribute('checked') == 'false':
                    wifi.click()
            except NoSuchElementException:
                self.ep.scroll_screen
                self.turn_wifi_on(count-1)

    def scroll_to_editor_top(self, count=4):
        if count > 0:
            try:
                self.ep.top_screen.is_displayed()
                return 'screen was scrolled to top'
            except NoSuchElementException:
                self.ep.scroll_screen_to_top
                self.scroll_to_editor_top(count - 1)

    def edit_working_time(self, open_time, close_time, count=3):
        if count > 0:
            try:
                time_btn = self.ep.working_time_editor_btn
                time_btn.is_displayed()
                time_btn.click()
                self.ep.open_time.send_keys(open_time)
                self.ep.close_time.send_keys(close_time)
                self.app.navigation.save_changes()
            except NoSuchElementException:
                self.ep.scroll_screen
                self.edit_working_time(open_time, close_time, count - 1)

    def edit_email(self, email, count=3):
        if count > 0:
            try:
                email_btn = self.ep.email
                email_btn.is_displayed()
                email_btn.send_keys(email)
            except NoSuchElementException:
                self.ep.scroll_screen
                self.edit_email(email, count - 1)

    def add_cuisine(self, cuisine, count = 3):
        if count > 0:
            try:
                cuisine_btn = self.ep.cuisine
                cuisine_btn.is_displayed()
                cuisine_btn.click()
                attempt = 100
                while attempt > 0:
                    cuisine_chb = self.ep.get_cuisine_by_name(cuisine)
                    if cuisine_chb is not None:
                        if cuisine_chb.get_attribute('checked') == 'false':
                            cuisine_chb.click()
                        break
                    else:
                        self.ep.scroll_screen
                        attempt -= 1
                self.app.navigate.save_changes()
            except NoSuchElementException:
                self.ep.scroll_screen
                self.add_cuisine(cuisine, count - 1)

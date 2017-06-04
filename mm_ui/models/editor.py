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
    def check_time(self, fields):
        pass
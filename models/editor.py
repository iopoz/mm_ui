from math import cos, sin
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
        except:
            self.ep.scroll_screen
        self.ep.zip.send_keys(code)

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
            except:
                self.ep.scroll_screen
                self.turn_wifi_on(count - 1)

    def scroll_to_editor_top(self, count=4):
        if count > 0:
            try:
                self.ep.top_screen.is_displayed()
                return 'screen was scrolled to top'
            except:
                self.ep.scroll_screen_to_top
                self.scroll_to_editor_top(count - 1)

    def edit_working_time(self, open_time, close_time, count=3):
        if count > 0:
            try:
                time_btn = self.ep.working_time_editor_btn
                time_btn.is_displayed()
                time_btn.click()
                self.ep.open_time.click()
                open_time = open_time.split(':')
                close_time = close_time.split(':')
                self.set_time(open_time)
                self.set_time(close_time)
                self.app.navigate.save_changes()
            except:
                self.ep.scroll_screen
                self.edit_working_time(open_time, close_time, count - 1)

    def set_time(self, time):
        radio = self.ep.get_hour_radio(time[0])
        self.__move_time_arrow(radio['top'], radio['bottom'], time[0], angle=30)
        radio = self.ep.get_minutes_radio
        self.__move_time_arrow(radio['top'], radio['bottom'], time[1])

        self.ep.ok_time_btn.click()

    def __move_time_arrow(self, top_radio, bottom_radio, value, angle=6):
        top_center = {'x': int(top_radio.location['x'] + top_radio.size['width']/2),
                      'y': int(top_radio.location['y'] + top_radio.size['height']/2)}

        bottom_center = {'x': int(bottom_radio.location['x'] + bottom_radio.size['width'] / 2),
                         'y': int(bottom_radio.location['y'] + bottom_radio.size['height'] / 2)}
        r = int((bottom_center['y'] - top_center['y'])/2)
        end_y = top_center['y'] + (r - int(r * cos(int(value) * angle)))
        end_x = top_center['x'] + (int(r * sin(int(value) * angle)))
        start_x = top_center['x']
        start_y = top_center['y']
        self.ep.driver.swipe(start_x, start_y, end_x, end_y, 6000)


    def edit_email(self, email, count=3):
        if count > 0:
            try:
                email_btn = self.ep.email
                email_btn.is_displayed()
                email_btn.send_keys(email)
            except:
                self.ep.scroll_screen
                self.edit_email(email, count - 1)

    def add_cuisine(self, cuisine, count=3):
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
            except:
                self.ep.scroll_screen
                self.add_cuisine(cuisine, count - 1)

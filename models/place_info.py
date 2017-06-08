from selenium.common.exceptions import NoSuchElementException

from pages.short_about_place_page import ShortAboutPlacePage


class PlaceInfo(object):
    def __init__(self, app):
        self.app = app
        self.sapp = ShortAboutPlacePage()

    PAGE = None

    def is_place_details_shown(self):
        elm = self.sapp.short_about_place
        self.PAGE = self.sapp.get_page_source
        return elm.is_displayed()

    def is_place_known(self):
        try:
            self.sapp.downloader_status.is_displayed()
            return False
        except NoSuchElementException:
            return True

    def download_map(self):
        self.sapp.downloader_status.click()
        self.sapp.download_progress

    def is_arrow_up(self):
        try:
            self.sapp.about_place_coordinate.is_displayed()
            return False
        except NoSuchElementException:
            return True

    def open_place_details(self, count=3):
        if count > 0:
            try:
                self.sapp.editor_place.is_displayed()
                self.PAGE = self.sapp.get_page_source
            except NoSuchElementException:
                self.sapp.scroll_screen
                self.open_place_details(count-1)
        return 'place details is opened'

    def is_place_name_matched(self, name):
        return name in self.sapp.get_place_title(self.PAGE)

    def is_place_type_matched(self, name):
        return name in self.sapp.get_place_subtitle(self.PAGE)

    def is_place_address_matched(self, name):
        return name in self.sapp.get_place_address(self.PAGE)

    def is_place_distance_existed(self):
        return self.sapp.get_place_distance(self.PAGE)

    def is_place_direction_existed(self):
        return self.sapp.get_place_direction(self.PAGE)

    def get_place_info(self):
        info={'time': self.sapp.get_place_time(self.PAGE),
              'phone': self.sapp.get_place_phone(self.PAGE),
              'site': self.sapp.get_place_web(self.PAGE),
              'cuisine': self.sapp.get_place_cuisine(self.PAGE),
              'coordinate': self.sapp.about_place_coordinate.text}
        return info

    def change_coordinate_type(self):
        self.sapp.about_place_coordinate.click()

    def is_coordinates_changed(self, old_type):
        return old_type != self.sapp.about_place_coordinate.text

    def click_edit_place(self):
        self.sapp.editor_place.click()

    def get_coordinate(self):
        return self.sapp.about_place_coordinate.text
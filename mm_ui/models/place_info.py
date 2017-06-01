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

    def is_arrow_up(self):
        try:
            self.sapp.about_place_coordinate.is_displayed()
            return False
        except NoSuchElementException:
            return True

    def open_place_details(self):
        if self.is_arrow_up():
            self.sapp.short_about_place.click()
            self.PAGE = self.sapp.get_page_source
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
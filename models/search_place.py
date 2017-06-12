# coding: utf-8
from pages.search_page import SearchPage


class SearchPlace(object):
    def __init__(self, app):
        self.spp = SearchPage()
        self.app = app

    def search_place_by_coordinates(self, coordinates):
        self.app.navigate.set_query(coordinates)
        self.spp.show_on_map_btn.click()

    def open_place_by_name_address(self, name, address):
        self.app.navigate.set_query(name)
        msg = self.get_place_from_bottom(name, address)
        return msg

    def get_place_from_bottom(self, name, address, count=10):
        if count > 0:
            try:
                self.spp.get_search_result_btn(name, address).click()
                return 'place %s %s was selected \n' % (name, address)
            except:
                self.spp.scroll_screen
                self.get_place_from_bottom(name, address, count-1)
        else:
            return 'place %s %s wasn\'t found \n' % (name, address)

    def open_category_tab(self):
        self.spp.search_tabs_btn(u'категории').click()

    def open_category_by_name(self, name):
        self.open_category_tab()
        self.spp.get_category(name).click()
        return 'selected category %s \n' % name

    def open_place_from_category(self, name, address):
        msg = self.get_place_from_bottom(name, address, count=50)
        return msg
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
                return 'place was selected'
            except:
                self.spp.scroll_screen()
                self.get_place_from_bottom(name, address, count-1)
        else:
            return 'place wasn\'t found'




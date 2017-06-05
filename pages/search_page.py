from pages.page import Page


class SearchPage(Page):
    @property
    def search_tabs_view(self):
        return self.driver.find_element_by_id('tabs')

    def search_tabs_btn(self, name):
        tabs = self.search_tabs_view.find_elements_by_class_name('ActionBar$Tab')
        for tab in tabs:
            if name.lower() in tab.find_element_by_class_name('android.widget.TextView').text.lower():
                return tab
        raise Exception('element absents!')

    @property
    def catigory_table(self):
        return self.driver.find_element_by_id('recycler')

    def get_catigory(self, name):
        catigories = self.catigory_table.find_elements_by_class_name('android.widget.TextView')
        for catigory in catigories:
            if name in catigory.text:
                return catigory
        return None

    @property
    def show_on_map_btn(self):
        return self.driver.find_element_by_id('show_on_map')

    @property
    def place_list(self):
        return self.catigory_table.find_elements_by_class_name('android.widget.RelativeLayout')

    def get_place_by_name(self, name):
        place_list = self.place_list
        for place in place_list:
            if name in place.find_element_by_id('title'):
                return place
        return None

    @property
    def search_result_view(self):
        return self.driver.find_element_by_id('results_frame')

    def get_search_result_btn(self, p_name, p_address):
        rows = self.search_result_view.find_elements_by_class_name('android.widget.RelativeLayout')
        for row in rows:
            if p_name in row.find_element_by_id('title').text:
                if p_address in row.find_element_by_id('region').text:
                    return row
        raise Exception('element %s with %s absents on screen' % (p_name, p_address))
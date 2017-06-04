from pages.page import Page


class ShortAboutPlacePage(Page):
    @property
    def short_about_place(self):
        return self.wait_until_not_exist('pp__details')

    @property
    def short_about_place_title(self):
        return self.driver.find_element_by_id('tv__title')

    def get_place_title(self, page):
        return page.find(".//*[@resource-id='com.mapswithme.maps.pro:id/tv__title']").get(
            'text')  # contains(@address,'Downing')

    @property
    def short_about_place_subtitle(self):
        return self.driver.find_element_by_id('tv__subtitle')

    def get_place_subtitle(self, page):
        return page.find(".//*[@resource-id='com.mapswithme.maps.pro:id/tv__subtitle']").get('text')

    @property
    def short_about_place_address(self):
        return self.driver.find_element_by_id('tv__address')

    def get_place_address(self, page):
        return page.find(".//*[@resource-id='com.mapswithme.maps.pro:id/tv__address']").get('text')

    @property
    def short_about_place_direction(self):
        return self.driver.find_element_by_id('av__direction')

    def get_place_direction(self, page):
        return page.find(".//*[@resource-id='com.mapswithme.maps.pro:id/av__direction']").get('enabled') == 'true'

    @property
    def short_about_place_distance(self):
        return self.driver.find_element_by_id('tv__straight_distance')

    def get_place_distance(self, page):
        return page.find(".//*[@resource-id='com.mapswithme.maps.pro:id/tv__straight_distance']").get(
            'enabled') == 'true'

    @property
    def about_place(self):
        return self.driver.find_element_by_id('pp__details_frame')

    @property
    def about_place_time(self):
        return self.driver.find_element_by_id('today_opening_hours')

    def get_place_time(self, page):
        return page.find(".//*[@resource-id='com.mapswithme.maps.pro:id/today_opening_hours']").get('text')

    @property
    def about_place_phone(self):
        return self.driver.find_element_by_id('tv__place_phone')

    def get_place_phone(self, page):
        return page.find(".//*[@resource-id='com.mapswithme.maps.pro:id/tv__place_phone']").get('text')

    @property
    def about_place_web(self):
        return self.driver.find_element_by_id('tv__place_website')  # tv__place_website

    def get_place_web(self, page):
        return page.find(".//*[@resource-id='com.mapswithme.maps.pro:id/tv__place_website']").get('text')

    @property
    def about_place_cuisine(self):
        return self.driver.find_element_by_id('tv__place_cuisine')  # tv__place_cuisine

    def get_place_cuisine(self, page):
        return page.find(".//*[@resource-id='com.mapswithme.maps.pro:id/tv__place_cuisine']").get('text')

    @property
    def about_place_coordinate(self):
        return self.driver.find_element_by_id('tv__place_latlon')  # tv__place_latlon

    # def about_place_btns_view(self):
    #     return self.driver.find_element_by_id('pp__buttons')

    # def get_about_place_btn(self, name):
    #     btns = self.about_place_btns_view.find_elements_by_class_name('android.widget.LinearLayout')
    #     for btn in btns:
    #         if name in btn.find_element_by_id('title').text:
    #             return btn
    #     raise Exception('Button %s absents', % name)

    # def search_result_view(self):
    #     return self.find_element_by_id('results_frame')
    #
    # def get_search_result_btn(self, p_name, p_address)
    #     rows = self.search_result_view.find_elements_by_class_name('android.widget.RelativeLayout')
    #     for row in rows:
    #         if p_name in row.find_element_by_id('title').text:
    #             if p_address in row.find_element_by_id('region').text:
    #                 return row
    #     return None

    @property
    def editor_place(self):
        return self.driver.find_element_by_id('tv__editor')

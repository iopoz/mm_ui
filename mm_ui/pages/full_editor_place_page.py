from pages.page import Page


class FullEditorPlacePage(Page):
    @property
    def place_category_field(self):
        parent_elm = self.wait_until_not_exist('category')
        return parent_elm.find_element_by_id('name')

    @property
    def name_place_frame(self):
        return self.wait_until_not_exist('cv__name')

    def get_name_by_location(self, location):
        languages = self.name_place_frame.find_elements_by_class_name('TextInputLayout')
        for language in languages:
            if location in language.text:
                return language.find_element_by_id('input')
        return None

    @property
    def new_language_btn(self):
        return self.driver.find_element_by_id('add_langs')

    @property
    def language_list(self):
        return self.driver.find_elements_by_id('name')

    def get_interested_language(self, language):
        l_list = self.language_list
        for l in l_list:
            if language == l.text and l.location['y'] < int(self.screen_size['height'] * 0.8):
                return l
        return None

    @property
    def address_frame(self):
        return self.driver.find_element_by_id('cv__address')

    @property
    def street_block(self):
        return self.driver.find_element_by_id('block_street')

    @property
    def street(self):
        return self.driver.find_element_by_id('street')

    @property
    def building_block(self):
        return self.driver.find_element_by_id('block_building')

    @property
    def building(self):
        return self.building_block.find_element_by_id('input')

    @property
    def zip_block(self):
        return self.driver.find_element_by_id('block_zipcode')

    @property
    def zip(self):
        return self.zip_block.find_element_by_id('input')

    @property
    def more_details_frame(self):
        return self.driver.find_element_by_id('cv__metadata')

    @property
    def working_time(self):
        return self.driver.find_element_by_id('opening_hours')

    @property
    def working_time_editor_btn(self):
        return self.driver.find_element_by_id('edit_opening_hours')

    @property
    def phone_block(self):
        return self.driver.find_element_by_id('block_phone')

    @property
    def phone(self):
        return self.phone_block.find_element_by_id('input')

    @property
    def web_block(self):
        return self.driver.find_element_by_id('block_website')

    @property
    def web(self):
        return self.web_block.find_element_by_id('input')

    @property
    def cuisine_block(self):
        return self.driver.find_element_by_id('block_cuisine')

    @property
    def cuisine(self):
        return self.cuisine_block.find_element_by_id('cuisine')

    @property
    def wifi(self):
        return self.driver.find_element_by_id('sw__wifi')

    def get_field(self, page, value):
        return page.find(".//*[@text='%s']" % value)

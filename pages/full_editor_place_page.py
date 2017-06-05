from math import cos, sin

from pages.page import Page


class FullEditorPlacePage(Page):
    @property
    def place_category_field(self):
        parent_elm = self.wait_until_not_exist('category')
        return parent_elm.find_element_by_id('name')
    @property
    def top_screen(self):
        return self.driver.find_element_by_id('category')

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
        el = self.driver.find_element_by_id('street')
        if el.location['y'] < int(self.screen_size['height'] * 0.8):
            return el
        raise Exception('element is not available')

    @property
    def building_block(self):
        return self.driver.find_element_by_id('block_building')

    @property
    def building(self):
        el = self.building_block.find_element_by_id('input')
        if el.location['y'] < int(self.screen_size['height'] * 0.8):
            return el
        raise Exception('element is not available')

    @property
    def zip_block(self):
        return self.driver.find_element_by_id('block_zipcode')

    @property
    def zip(self):
        el = self.zip_block.find_element_by_id('input')
        if el.location['y'] < int(self.screen_size['height'] * 0.8):
            return el
        raise Exception('element is not available')

    @property
    def more_details_frame(self):
        return self.driver.find_element_by_id('cv__metadata')

    @property
    def working_time(self):
        el = self.driver.find_element_by_id('opening_hours')
        if el.location['y'] < int(self.screen_size['height'] * 0.8):
            return el
        raise Exception('element is not available')

    @property
    def working_time_editor_btn(self):
        el = self.driver.find_element_by_id('edit_opening_hours')
        if el.location['y'] < int(self.screen_size['height'] * 0.8):
            return el
        raise Exception('element is not available')

    @property
    def open_time(self):
        return self.wait_until_not_exist('tv__time_open')

    @property
    def close_time(self):
        return self.wait_until_not_exist('tv__time_close')

    def get_hour_radio(self, hour):
        radios = self.driver.find_elements_by_class_name('android.widget.RadialTimePickerView$RadialPickerTouchHelper')
        for radio in radios:
            if str(hour) in radio.get_attribute('content-desc'):
                return radio

    def get_minutes_radio(self, minute):
        radios = self.driver.find_elements_by_class_name('android.widget.RadialTimePickerView$RadialPickerTouchHelper')
        top_radio = None
        bottom_radio = None
        for radio in radios:
            if radio.get_attribute('content-desc') == '0':
                top_radio = radio
            if radio.get_attribute('content-desc') == '30':
                bottom_radio = radio
                break
        top_center = {'x': int(top_radio.location['x'] + top_radio.size['width']/2),
                      'y': int(top_radio.location['y'] + top_radio.size['height']/2)}

        bottom_center = {'x': int(bottom_radio.location['x'] + bottom_radio.size['width'] / 2),
                         'y': int(bottom_radio.location['y'] + bottom_radio.size['height'] / 2)}
        r = int(bottom_center['y'] - top_center['y']/2)
        end_y = top_center['y'] + (r - int(r * cos(minute * 6)))
        end_x = top_center['x'] + (int(r * sin(minute * 6)))
        start_x = top_center['x']
        start_y = top_center['y']
        return {'s_x': start_x, 's_y': start_y, 'e_x': end_x, 'e_y': end_y}

    @property
    def ok_time_btn(self):
        return self.driver.find_element_by_id('button1')


    @property
    def phone_block(self):
        return self.driver.find_element_by_id('block_phone')

    @property
    def phone(self):
        el = self.phone_block.find_element_by_id('input')
        if el.location['y'] < int(self.screen_size['height'] * 0.8):
            return el
        raise Exception('element is not available')

    @property
    def web_block(self):
        return self.driver.find_element_by_id('block_website')

    @property
    def web(self):
        el = self.web_block.find_element_by_id('input')
        if el.location['y'] < int(self.screen_size['height'] * 0.8):
            return el
        raise Exception('element is not available')

    @property
    def email_block(self):
        return self.driver.find_element_by_id('block_email')

    @property
    def email(self):
        el = self.email_block.find_element_by_id('input')
        if el.location['y'] < int(self.screen_size['height'] * 0.8):
            return el
        raise Exception('element is not available')

    @property
    def cuisine_block(self):
        return self.driver.find_element_by_id('block_cuisine')

    @property
    def cuisine(self):
        el = self.cuisine_block.find_element_by_id('cuisine')
        if el.location['y'] < int(self.screen_size['height'] * 0.8):
            return el
        raise Exception('element is not available')

    def get_cuisine_by_name(self, cuisine):
        cuisines = self.driver.find_elements_by_class_name('android.widget.LinearLayout')
        for cuisine_crnt in cuisines:
            if cuisine in cuisine_crnt.find_element_by_id('cuisine').text:
                return cuisine_crnt.find_element_by_id('selected')
        return None

    @property
    def wifi(self):
        return self.driver.find_element_by_id('sw__wifi')

    def get_field(self, page, value):
        return page.find(".//*[@text='%s']" % value)

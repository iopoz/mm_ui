from selenium.common.exceptions import NoSuchElementException

from pages.navigation_page import NavigationPage


class Navigate(object):
    def __init__(self, app):
        self.app = app
        self.np = NavigationPage()

    def go_to_search(self):
        self.np.driver.orientation = "LANDSCAPE"
        self.np.search_btn.click()
        self.np.driver.orientation = "PORTRAIT"

    def set_query(self, query):
        self.np.query_field.clear()
        self.np.query_field.send_keys(query)

    def save_changes(self):
        self.np.save_btn.click()

    def back_to_map(self):
        self.np.back_btn.click()

    def navigate_to_my_place(self):
        self.np.my_position.click()

    def get_my_coordinate(self):
        self.navigate_to_my_place()

        try:
            self.app.place_details.is_place_details_shown
            if self.app.place_details.is_arrow_up:
                self.app.place_details.sapp.short_about_place_title.click()
        except NoSuchElementException:
            screen = self.np.map_screen
            x = int(screen.size['width']/2)
            y = int(screen.size['height']/2)
            self.np.driver.swipe(x, y, x, y)
            self.app.place_details.sapp.short_about_place.click()
        return self.app.place_details.get_coordinate() + '\n'

    def hide_bottom_menu(self):
        screen = self.np.screen_size
        x = int(screen['width'] / 3)
        y = int(screen['height'] / 3)
        self.np.driver.swipe(x, y, x, y)

    def clear_search_results(self):
        self.np.clear_btn.click()

    def cancel_system_message(self):
        self.np.cancel_btn.click()

    def is_system_message_shown(self):
        try:
            self.np.system_message.is_displayed()
            return True
        except NoSuchElementException:
            return False
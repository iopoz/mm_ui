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



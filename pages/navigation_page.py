from pages.page import Page


class NavigationPage(Page):
    @property
    def save_btn(self):
        return self.driver.find_element_by_id('save')

    @property
    def back_btn(self):
        tb = self.driver.find_element_by_id('toolbar')
        return tb.find_element_by_class_name('android.widget.ImageButton')#android.widget.ImageButton

    @property
    def query_field(self):
        return self.driver.find_element_by_id('query')

    @property
    def menu_btn(self):
        return self.driver.find_element_by_id('menu')

    @property
    def search_btn(self):
        return self.driver.find_element_by_id('search')

    @property
    def p2p_btn(self):
        return self.driver.find_element_by_id('p2p')

    @property
    def bookmarks_btn(self):
        return self.driver.find_element_by_id('bookmarks')

    @property
    def my_position(self):
        return self.driver.find_element_by_id('my_position')

    @property
    def clear_btn(self):
        return self.driver.find_element_by_id('clear')

    @property
    def system_message(self):
        return self.driver.find_element_by_id('action_bar_root')

    @property
    def cancel_btn(self):
        return self.system_message.find_element_by_id('button2')

    @property
    def ok_btn(self):
        return self.system_message.find_element_by_id('button1')
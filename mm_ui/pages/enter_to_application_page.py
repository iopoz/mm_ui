from pages.page import Page


class EnterToApplicationPage(Page):
    @property
    def next_btn(self):
        return self.driver.find_element_by_id('next')

    @property
    def done_btn(self):
        return self.driver.find_element_by_id('done')

    @property
    def downloader_map_btn(self):
        return self.driver.find_element_by_id('downloader_button')
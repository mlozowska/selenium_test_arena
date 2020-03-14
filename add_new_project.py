from tests.test_arena_homework import get_random_string


class AddNewProject:

    def __init__(self, browser):
        self.browser = browser

    def new_project_adding(self):
        name = self.browser.find_element_by_id('name')
        prefix = self.browser.find_element_by_id('prefix')
        save = self.browser.find_element_by_id('save')

        name.send_keys(get_random_string(10))
        prefix.send_keys(get_random_string(6))
        save.click()
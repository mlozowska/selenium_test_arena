from tests.test_arena_homework import get_random_string
import random
import string


class SearchProject:

    def __init__(self, browser):
        self.browser = browser

    def search_project_name(self):
        search_bar = self.browser.find_element_by_id('search')
        search_button = self.browser.find_element_by_id('j_searchButton')
        search_bar.send_keys(get_random_string(10))
        search_button.click()

    def get_random_string(length):
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

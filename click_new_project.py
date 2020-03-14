class NewProjectIcon:

    def __init__(self, browser):
        self.browser = browser

    def new_project_opening(self):
        button_links = self.browser.find_elements_by_class_name('button_link')
        button_links[0].click()


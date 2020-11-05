class AdminPanel:
    
    def __init__(self, browser):
        self.browser = browser

    def open_admin_panel(self):
        admin_button = self.browser.find_element_by_css_selector('.header_admin a')
        admin_button.click()


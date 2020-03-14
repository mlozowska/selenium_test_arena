class LoginPage:

    def __init__(self, browser):
        self.browser = browser

    def login(self, login, password):
        login_field = self.browser.find_element_by_id('email')
        password_field = self.browser.find_element_by_id('password')
        submit_button = self.browser.find_element_by_id('login')
        login_field.send_keys(login)
        password_field.send_keys(password)
        submit_button.click()





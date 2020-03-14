

class ProjectSectionOpening:
    def __init__(self, browser):
        self.browser = browser

    def project_section_opening(self):
        projects = self.browser.find_element_by_class_name('activeMenu')
        projects.click()




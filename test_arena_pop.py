
import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from pages.home_page import AdminPanel
from pages.add_new_project import AddNewProject
from pages.click_new_project import NewProjectIcon
from pages.login_page import LoginPage
from pages.project_section import ProjectSectionOpening
from pages.search_project_name import SearchProject



@pytest.fixture()
def browser():
    browser = Chrome(executable_path=ChromeDriverManager().install())
    browser.get('http://demo.testarena.pl')
    yield browser
    browser.quit()


def test_arena(browser):
    login_page = LoginPage(browser)
    login_page.login('administrator@testarena.pl', 'sumXQQ72$L')

    admin_panel = AdminPanel(browser)
    admin_panel.open_admin_panel()

    new_project = NewProjectIcon(browser)
    new_project.new_project_opening()

    add_project = AddNewProject(browser)
    add_project.new_project_adding()

    open_project_section = ProjectSectionOpening(browser)
    open_project_section.project_section_opening()

    search_project_name = SearchProject(browser)
    search_project_name.search_project_name()




from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select

from simbirsoft.pages.page import Page


class AccountPage(Page):
    @property
    def customer_select(self) -> Select:
        element = self.find_element_by_attribute_value("id", "userSelect")
        return Select(element)

    @property
    def login_button(self) -> WebElement:
        return self.find_element_by_exact_text("Login")

    def select_customer(self, customer_name: str) -> None:
        customer_select = self.customer_select
        customer_select.select_by_visible_text(customer_name)

    def login(self) -> None:
        self.login_button.click()

from selenium.webdriver.remote.webelement import WebElement

from simbirsoft.pages.page import Page


class LoginPage(Page):
    @property
    def customer_login_button(self) -> WebElement:
        return self.find_element_by_exact_text("Customer Login")

    @property
    def manager_login_button(self) -> WebElement:
        return self.find_element_by_exact_text("Bank Manager Login")

    def login_customer(self, url: str) -> None:
        self.driver.get(url)
        self.customer_login_button.click()

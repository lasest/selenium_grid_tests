import re

from selenium.webdriver.remote.webelement import WebElement

from simbirsoft.pages.page import Page


class CustomerPage(Page):
    @property
    def greeting_strong(self) -> WebElement:
        return self.find_element_by_partial_text("Welcome", "strong")

    @property
    def deposit_form(self) -> WebElement:
        return self.find_element_by_attribute_value(
            "ng-submit", "deposit()", clickable=False
        )

    @property
    def withdrawl_form(self) -> WebElement:
        return self.find_element_by_attribute_value(
            "ng-submit", "withdrawl()", clickable=False
        )

    @property
    def transactions_tab_button(self) -> WebElement:
        return self.find_element_by_attribute_value("ng-click", "transactions()")

    @property
    def deposit_tab_button(self) -> WebElement:
        return self.find_element_by_attribute_value("ng-click", "deposit()")

    @property
    def withdrawl_tab_button(self) -> WebElement:
        return self.find_element_by_attribute_value("ng-click", "withdrawl()")

    @property
    def deposit_amount_input(self) -> WebElement:
        return self.find_element_by_attribute_value(
            "ng-model", "amount", base_element=self.deposit_form
        )

    @property
    def withdrawl_amount_input(self) -> WebElement:
        return self.find_element_by_attribute_value(
            "ng-model", "amount", base_element=self.withdrawl_form
        )

    @property
    def deposit_submit_button(self) -> WebElement:
        return self.find_element_by_attribute_value(
            "type", "submit", base_element=self.deposit_form
        )

    @property
    def withdrawl_submit_button(self) -> WebElement:
        return self.find_element_by_attribute_value(
            "type", "submit", base_element=self.withdrawl_form
        )

    @property
    def account_status_div(self) -> WebElement:
        return self.find_element_by_partial_text("Account Number :")

    def deposit(self, amount: int) -> None:
        self.deposit_tab_button.click()
        self.deposit_amount_input.send_keys(str(amount))
        self.deposit_submit_button.click()

    def withdraw(self, amount: int) -> None:
        self.withdrawl_tab_button.click()
        self.withdrawl_amount_input.send_keys(str(amount))
        self.withdrawl_submit_button.click()

    def get_balance(self) -> int:
        account_status_text = self.account_status_div.text

        balance_regex = r"Balance\s*:\s*(\d+)"
        groups = re.search(balance_regex, account_status_text)
        if not groups:
            raise ValueError(
                f"Failed to extract account balance from string: {account_status_text}"
            )

        balance = int(groups[1])
        return balance

    def open_transactions_page(self) -> None:
        self.transactions_tab_button.click()

    def get_user_name(self) -> str:
        greeting_text = self.greeting_strong.text
        user_name_regex = r"Welcome\s([A-Za-z]+\s[A-Za-z]+)\s!!"
        groups = re.search(user_name_regex, greeting_text)
        if not groups:
            raise ValueError(
                f"Failed to extract user name from string: {greeting_text}"
            )

        return groups[1]

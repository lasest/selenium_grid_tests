from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from simbirsoft.models import Transaction
from simbirsoft.pages.page import Page


class TransactionsPage(Page):
    @property
    def transaction_trs(self) -> list[WebElement]:
        xpath = "//tbody"
        table_body = self.find_element_by_xpath(xpath)

        xpath = "./tr"
        self.find_element_by_xpath(xpath, base_element=table_body)

        rows = table_body.find_elements(By.TAG_NAME, "tr")  # type: ignore

        return rows

    def get_transactions(self) -> list[Transaction]:
        rows = self.transaction_trs
        transactions = [Transaction.from_tr(row) for row in rows]

        return transactions

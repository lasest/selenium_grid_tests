from typing import Callable, Generator

import pytest
from selenium import webdriver

import simbirsoft.configuration as configuration
import simbirsoft.export as export
import simbirsoft.pages as pages
import simbirsoft.utils as utils
from simbirsoft.tests.fixtures import driver  # type: ignore

WEBSITE_URL = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login"
CUSTOMER_NAME = "Harry Potter"


@pytest.fixture(scope="function")
def login() -> Generator[Callable[[webdriver.Remote], None], None, None]:
    def perform_login(driver: webdriver.Remote) -> None:
        pages.LoginPage(driver).login_customer(WEBSITE_URL)

        account_page = pages.AccountPage(driver)
        account_page.select_customer(CUSTOMER_NAME)
        account_page.login()

    yield perform_login


def test_login(
    driver: webdriver.Remote, login: Callable[[webdriver.Remote], None]
) -> None:
    login(driver)

    customer_page = pages.CustomerPage(driver)
    assert customer_page.get_user_name() == CUSTOMER_NAME


def test_deposit(
    driver: webdriver.Remote, login: Callable[[webdriver.Remote], None]
) -> None:
    login(driver)
    customer_page = pages.CustomerPage(driver)
    customer_page.deposit(100)

    assert customer_page.get_balance() == 100


def test_withdraw(
    driver: webdriver.Remote, login: Callable[[webdriver.Remote], None]
) -> None:
    login(driver)
    customer_page = pages.CustomerPage(driver)
    customer_page.deposit(150)
    customer_page.withdraw(100)

    assert customer_page.get_balance() == 50


def test_transactions(
    driver: webdriver.Remote, login: Callable[[webdriver.Remote], None]
) -> None:
    day = utils.get_day_number() + 1
    amount = utils.get_fibbonachi_number_by_index(day)

    login(driver)
    customer_page = pages.CustomerPage(driver)
    customer_page.deposit(amount)
    customer_page.withdraw(amount)

    assert customer_page.get_balance() == 0

    customer_page.open_transactions_page()

    transactions_page = pages.TransactionsPage(driver)
    transactions = transactions_page.get_transactions()

    assert len(transactions) == 2
    for transaction in transactions:
        assert transaction.amount == amount

    filename = export.get_timestamp_filename(".csv")
    export_path = configuration.EXPORT_PATH / filename
    export.export_transactions(transactions, export_path)

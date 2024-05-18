from typing import Generator

import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions

import simbirsoft.configuration as configuration


@pytest.fixture(scope="function")
def driver() -> Generator[webdriver.Remote, None, None]:
    hub_url = f"http://{configuration.HUB_HOST}:4444/wd/hub"
    options = FirefoxOptions()
    driver = webdriver.Remote(command_executor=hub_url, options=options)

    yield driver
    driver.quit()

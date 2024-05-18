from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Page:
    def __init__(self, driver: webdriver.Remote) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_element_by_xpath(
        self,
        xpath: str,
        wait: bool = True,
        clickable: bool = True,
        visible: bool = True,
        base_element: WebElement | None = None,
    ) -> WebElement:
        waiter = self.wait if base_element is None else WebDriverWait(base_element, 10)  # type: ignore

        if wait and clickable:
            element = waiter.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        elif wait and visible:
            element = waiter.until(EC.visibility_of_element_located((By.XPATH, xpath)))
        elif wait:
            element = waiter.until(EC.presence_of_element_located((By.XPATH, xpath)))
        else:
            element = (
                self.driver.find_element(By.XPATH, xpath)
                if base_element is None
                else base_element.find_element(By.XPATH, xpath)  # type: ignore
            )

        return element

    def find_element_by_exact_text(
        self,
        text: str,
        tagname: str = "*",
        wait: bool = True,
        clickable: bool = True,
        visible: bool = True,
        strip: bool = True,
        base_element: WebElement | None = None,
    ) -> WebElement:
        if strip:
            text = text.strip()

        xpath = f"//{tagname}[text()='{text}']"
        element = self.find_element_by_xpath(
            xpath,
            wait=wait,
            clickable=clickable,
            visible=visible,
            base_element=base_element,
        )
        return element

    def find_element_by_partial_text(
        self,
        text: str,
        tagname: str = "*",
        wait: bool = True,
        clickable: bool = True,
        visible: bool = True,
        strip: bool = True,
        base_element: WebElement | None = None,
    ) -> WebElement:
        if strip:
            text = text.strip()

        xpath = f"//{tagname}[contains(text(), '{text}')]"
        element = self.find_element_by_xpath(
            xpath,
            wait=wait,
            clickable=clickable,
            visible=visible,
            base_element=base_element,
        )
        return element

    def find_element_by_attribute_value(
        self,
        attribute: str,
        value: str,
        tagname: str = "*",
        wait: bool = True,
        clickable: bool = True,
        visible: bool = True,
        base_element: WebElement | None = None,
    ) -> WebElement:
        xpath = f"//{tagname}[@{attribute}='{value}']"
        element = self.find_element_by_xpath(
            xpath,
            wait=wait,
            clickable=clickable,
            visible=visible,
            base_element=base_element,
        )
        return element

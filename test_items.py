import pytest
from selenium.webdriver.common.by import By
import time

class TestAddBasketButton:
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

    def test_site_contains_add_to_basket_button(self, browser):
        browser.get(self.link)
        time.sleep(30)

        browser.implicitly_wait(10)

        # Проверка на наличие кнопки. Метод .find_elements возвращает список найденных элементов.
        # И если длина списка == 1, то метод нашёл искомый элемент (в нашем случае одну кнопку).
        assert len(browser.find_elements(By.CLASS_NAME, "btn-add-to-basket")) == 1, "NOT FIND ADD TO BASKET BUTTON"

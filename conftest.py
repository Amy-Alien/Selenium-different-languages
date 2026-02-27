import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store",
                     default="chrome", help="Choose browser: chrome or firefox")
    parser.addoption("--language", action="store", default="es", help="Choose language")

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("--browser_name")
    language = request.config.getoption("--language")
    if browser_name == "chrome":
        options = ChromeOptions()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})

        print("--- Starting Chrome browser ---")
        browser = webdriver.Chrome(options=options)

    elif browser_name == "firefox":
        options = FirefoxOptions()
        options.set_preference('intl.accept_languages', language)

        print("--- Starting Firefox browser ---")
        browser = webdriver.Firefox(options=options)

    yield browser
    print("--- Quit browser ---")
    time.sleep(2)
    browser.quit()



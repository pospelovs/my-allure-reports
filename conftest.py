import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='None',
                     help="Choose browser: Chrome or Firefox")

@pytest.fixture(scope="function")
def browser(request):
    browser = request.config.getoption("browser")
    if browser=='Chrome':
        print("\nstart Chrome browser for test..")
        options = webdriver.chrome.options.Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': "en"})
        browser = webdriver.Chrome(options=options)
    elif browser=='Firefox':
        print("\nstart Firefox browser for test..")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", "en")
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser should be Chrome or Firefox")
    browser.maximize_window()
    yield browser
    print("\nquit browser..")
    browser.quit()

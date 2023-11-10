import pytest
from selene import be, have, browser



@pytest.fixture
def browser_configs():
    browser.config.window_width = 1690
    browser.config.window_height = 1080
    yield
    browser.quit()


def test_google_find_selene(browser_configs):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_google_find(browser_configs):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('tghdsjdkiue').press_enter()
    browser.element('[class="card-section"]').should(have.text('По запросу tghdsjdkiue ничего не найдено'))
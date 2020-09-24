import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
	parser.addoption('--language', action='store', default="ru",\
	help="Choose language: ru, en, ar, ca, cs, da, de, en-gb, el, \
	es, fi, fr, it, ko, nl, pl, pt, pt-br, ro, ru, sk, uk, zh-hans")

@pytest.fixture(scope="function")
def language(request):
    return request.config.getoption("--language")
    

	
@pytest.fixture(scope="function")
def browser(language):

	options = Options()
	options.add_experimental_option('prefs', {'intl.accept_languages': language})
	browser = webdriver.Chrome(options=options)	
	browser.maximize_window ()
	browser.implicitly_wait(5)
	
	yield browser
	
	browser.quit()
import pytest
from selenium import webdriver

def pytest_addoption(parser):
	parser.addoption('--language', action='store', default="ru",\
	help="Choose language: ru, en, ar, ca, cs, da, de, en-gb, el, \
	es, fi, fr, it, ko, nl, pl, pt, pt-br, ro, ru, sk, uk, zh-hans")

@pytest.fixture(scope="function")
def language(request):
    return request.config.getoption("--language")
    

	
@pytest.fixture(scope="function")
def browser():
	browser = webdriver.Chrome()
	browser.implicitly_wait(5)
	browser.maximize_window ()
	yield browser
	browser.quit()
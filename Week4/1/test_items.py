from selenium.common.exceptions import NoSuchElementException
import time
import sys

btn_add_to_basket="btn-add-to-basket1"
all_goods = "[href$='/catalogue/']"
first_of_all_goods = "section .row li:nth-child(1) a[title]"
title_of_card_item = ".product_main h1"


def test_check_btn_add_to_basket(browser, language):
	try:
		#Arrange
		Link_main_page=f"http://selenium1py.pythonanywhere.com/{language}/"
		print(Link_main_page)
		browser.get(Link_main_page)
		#Act
		browser.find_element_by_css_selector(all_goods).click()
		first_item = browser.find_element_by_css_selector(first_of_all_goods)  # берем первый в списке товар
		title_of_first_item = first_item.get_attribute('title')
		first_item.click()
		#Assert
		#Проверяем наличие элемента на странице
		time.sleep(3)
		assert browser.find_element_by_class_name(btn_add_to_basket).text != (''), "No button add to basket"
	
	except AssertionError as e:
		print(e.args[0])
		

	except NoSuchElementException:
		print("No element on page")

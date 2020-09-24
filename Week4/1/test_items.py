from selenium import webdriver

#Locators
btn_add_to_basket="btn-add-to-basket"
all_goods = "[href$='/catalogue/']"
first_of_all_goods = "section .row li:nth-child(1) a[title]"
title_of_card_item = ".product_main h1"
Link_main_page="http://selenium1py.pythonanywhere.com"


def test_check_btn_add_to_basket(browser):
	#Arrange
	browser.get(Link_main_page)
	
	#Act
	browser.find_element_by_css_selector(all_goods).click()
	first_item = browser.find_element_by_css_selector(first_of_all_goods) 
	title_of_first_item = first_item.get_attribute('title')
	first_item.click()
	
	#Assert
		
	assert browser.find_element_by_class_name(btn_add_to_basket).text != (''), "No button add to basket"


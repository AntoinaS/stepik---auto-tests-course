from selenium import webdriver
import sys
import random

main_page_link = "http://selenium1py.pythonanywhere.com/ru/"

# LOCATORS

# 1 registration
login_logout = "login_link"
email_registration = "id_registration-email"
pass_registration = "id_registration-password1"
pass2_registration = "id_registration-password2"
enter_registrationForm = "[value='Register']"
alert_success = "alertinner"
# 2 authorization
email_login = "id_login-username"
pass_login = "id_login-password"
login = "[value='Log In']"
# 3 password recovery
forgot_pass_link = "[href='/ru/password-reset/']"
forgot_pass_email = "id_email"
forgot_pass_sent_link = ".form-group button"
user_mail_link = "https://www.mailinator.com/"
user_email_enter_on_mail = "[autofocus='autofocus']"
find_user_email_on_mail = "go-to-public"
find_letter_with_link = "//*[contains(text(), 'pythonanywhere')]"
forgot_pass_url_success_sent_link = "http://selenium1py.pythonanywhere.com/ru/password-reset/done/"
# 4 product view
all_goods = "[href='/ru/catalogue/']"
first_of_all_goods = "section .row li:nth-child(1) a[title]"
title_of_card_item = ".product_main h1"
# 5 add to basket
add_item_to_basket = "btn-block"


##1 #РЕГИСТРАЦИЯ

def Registration(email, pass1, pass2):
    try:
        ##Arrange
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get(main_page_link)

        ##Act
        # 1 tap button registration
        browser.find_element_by_id(login_logout).click()
        # 2 enter email
        browser.find_element_by_id(email_registration).send_keys(email)
        # 3 enter first pass
        browser.find_element_by_id(pass_registration).send_keys(pass1)
        # 4 enter second pass
        browser.find_element_by_id(pass2_registration).send_keys(pass2)
        # 5 tap to button
        browser.find_element_by_css_selector(enter_registrationForm).click()

        # Assert
        real_alert_after_registration = browser.find_element_by_class_name(alert_success).text

        assert "Спасибо за регистрацию!" in real_alert_after_registration, "Assert on Registration not pas"


    except AssertionError as e:
        print(e.args[0])
    except Exception:
        print("Unexpected error:", sys.exc_info()[0])


    finally:
        browser.quit()


##2 #АВТОРИЗАЦИЯ

def Autorisation(email, pass1):
    try:
        ##Arrange
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get(main_page_link)

        ##Act
        # 1 tap button registration
        browser.find_element_by_id(login_logout).click()
        # 2 enter email
        browser.find_element_by_id(email_login).send_keys(email)
        # 3 enter valid pass
        browser.find_element_by_id(pass_login).send_keys(pass1)
        # 4 tap button
        browser.find_element_by_css_selector(login).click()

        # Assert
        real_alert_after_login = browser.find_element_by_class_name(alert_success).text

        assert "Рады видеть вас снова" in real_alert_after_login, "Assert on Autorisation not pas"

    except AssertionError as e:
        print(e.args[0])
    except Exception:
        print("Unexpected error:", sys.exc_info()[0])


    finally:
        browser.quit()


##3 #ВОССТАНОВЛЕНИЕ ПАРОЛЯ

def Password_recovery(email):
    try:
        ##Arrange
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get(main_page_link)

        ##Act
        # 1 tap button registration
        browser.find_element_by_id(login_logout).click()
        # 2 tap forgot pass
        browser.find_element_by_css_selector(forgot_pass_link).click()
        # 3 enter email
        browser.find_element_by_id(forgot_pass_email).send_keys(email)
        # 4 tap send mess
        browser.find_element_by_css_selector(forgot_pass_sent_link).click()

        ##Assert
        real_url = browser.current_url
        assert real_url == forgot_pass_url_success_sent_link, "Assert on Password_recovery not pas"

        # 5 go to 1@mailinator.com
        browser.get(user_mail_link)
        browser.find_element_by_css_selector(user_email_enter_on_mail).send_keys("1@mailinator.com")
        browser.find_element_by_id(find_user_email_on_mail).click()
        browser.find_element_by_xpath(
            find_letter_with_link).click()  # тут мы ищем в ящике письмо от конкретного отправителя
        # Т.к. письма нет, то я отправителя придумала, тест будет заведомо падат
        # 6 tap link
        # 7 enter new pass (нет письма и нет формы смены пароля)

        # Assert
        # проверка будет в сообщении об успешной смене пароля

    except AssertionError as e:
        print(e.args[0])
    except Exception:
        print("Не нашли такой элемент на странице", sys.exc_info()[0])

    finally:
        browser.quit()


##4 #ПРОСМОТР ТОВАРА (ЮЗЕР НЕ АВТОРИЗОВАН)

def Product_view():
    try:
        ##Arrange
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get(main_page_link)

        ##Act
        # 1 tap on section all goods
        browser.find_element_by_css_selector(all_goods).click()
        # 2 tap on first item of goods
        first_item = browser.find_element_by_css_selector(first_of_all_goods)  # берем первый в списке товар
        title_of_first_item = first_item.get_attribute('title')
        first_item.click()

        ##Assert
        real_title_of_card_item = browser.find_element_by_css_selector(title_of_card_item).text
        assert real_title_of_card_item == title_of_first_item, \
            "Assert on Product_view not pas"

    except AssertionError as e:
        print(e.args[0])
    except Exception:
        print("Unexpected error:", sys.exc_info()[0])


    finally:
        browser.quit()


##5 #ДОБАВЛЕНИЕ ТОВАРА В КОРЗИНУ(ЮЗЕР НЕ АВТОРИЗОВАН)

def Add_to_basket():
    try:
        ##Arrange
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get(main_page_link)

        ##Act
        # 1 tap on section all goods
        browser.find_element_by_css_selector(all_goods).click()
        # 2 add to basket
        browser.find_element_by_class_name(add_item_to_basket).click()  # добавляем любой товар в корзину

        ##Assert
        real_alert_after_adding_to_basket = browser.find_element_by_class_name(alert_success).text

        assert "был добавлен в вашу корзину." in real_alert_after_adding_to_basket, \
            "Assert on Add_to_basket not pas"

    except AssertionError as e:
        print(e.args[0])
    except Exception:
        print("Unexpected error:", sys.exc_info()[0])

    finally:
        browser.quit()


random_mail = str(random.randint(1, 100000)) + "@mailinator.com"

Registration(random_mail, "Qdgh1sss#kk", "Qdgh1sss#kk")
Autorisation("1@mailinator.com", "U7LqDeeRv2q2cvQ")
Password_recovery("1@mailinator.com")
Product_view()
Add_to_basket()

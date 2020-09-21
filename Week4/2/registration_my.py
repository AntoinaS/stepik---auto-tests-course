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

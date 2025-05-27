from selene import browser, have
import time


# AAA Arrange Act Assert
# BDD Given When Then

def test_registration_form():
    browser.open('/')

    browser.element('#firstName').type('Igor')
    browser.element('#lastName').type('Degtyarenko')
    browser.element('#userEmail').type('div@novoch.ru')
    browser.all('[name=gender]').element('[value=Male]')
    time.sleep(3)


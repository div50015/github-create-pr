from selene import browser, have
import time


# AAA Arrange Act Assert
# BDD Given When Then

def test_registration_form():
    browser.open('/')

    browser.element('#firstName').type('Igor')
    browser.element('#lastName').type('Degtyarenko')
    browser.element('#userEmail').type('div@novoch.ru')
    # browser.element('[name=gender][value=Female]+label').click()
    # browser.all('[name=gender]').element_by(have.value('Female')).element('..').click()
    browser.all('[for^=gender-radio]').element_by(have.text('Female')).click()
    time.sleep(3)


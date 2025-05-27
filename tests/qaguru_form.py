from selene import browser, have, command
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
    browser.element('#userNumber').type('9185024041')
    from selenium.webdriver import Keys
    browser.element('#dateOfBirthInput').send_keys(Keys.CONTROL, 'a').type('04 August 1967').press_enter()
    browser.element('#subjectsInput').type('History').press_enter()
    browser.element('[for=hobbies-checkbox-2]').click()

    browser.element('#currentAddress').type('Russian Novocherkassk')

    time.sleep(3)


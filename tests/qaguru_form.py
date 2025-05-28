import os.path

from selene import browser, have, command
import time
from selenium.webdriver import Keys

# AAA Arrange Act Assert
# BDD Given When Then

def test_registration_form():
    browser.open('/')

    browser.element('#firstName').type('Igor')
    browser.element('#lastName').type('Degtyarenko')
    browser.element('#userEmail').type('div@novoch.ru')
    # browser.element('[name=gender][value=Female]+label').click()
    # browser.all('[name=gender]').element_by(have.value('Female')).element('..').click()
    browser.all('[for^=gender-radio]').element_by(have.text('Male')).click()
    browser.element('#userNumber').type('9185024041')
    browser.element('#dateOfBirthInput').send_keys(Keys.CONTROL, 'a').type('04 August 1967').press_enter()
    browser.element('#subjectsInput').type('History').press_enter()
    browser.element('[for=hobbies-checkbox-1]').click()
    import tests
    browser.element('#uploadPicture').send_keys(os.path.dirname(tests.__file__),'/files/ball.jpg')
    browser.element('#currentAddress').type('Russian Novocherkassk')
    browser.element('#state').click()
    browser.all('[id^=react-select-3-option]').element_by(have.text('Rajasthan')).click()
    browser.element('#city').click()
    browser.all('[id^=react-select-4-option]').element_by(have.text('Jaipur')).click()
    browser.element('#submit').click()

    browser.element('.table').all('td').should(have.texts(
        'Student Name', 'Igor Degtyarenko',
        'Student Email', 'div@novoch.ru',
        'Gender', 'Male',
        'Mobile', '9185024041',
        'Date of Birth', '04 August,1967',
        'Subjects', 'History',
        'Hobbies', 'Sports',
        'Picture', 'ball.jpg',
        'Address', 'Russian Novocherkassk',
        'State and City', 'Rajasthan Jaipur',
        )
    )


    time.sleep(3)


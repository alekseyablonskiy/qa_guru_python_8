from selene import have, command
from selene.support.shared import browser
from demoqa_tests.model.controls import dropdown
from demoqa_tests.utils import path_to_file


def open_page():
    browser.open('/automation-practice-form')
    browser.driver.maximize_window()


def input_info(*, name, surname, email, mobile, address):
    browser.element('#firstName').type(name)
    browser.element('#lastName').type(surname)
    browser.element('#userEmail').type(email)
    browser.element('#userNumber').type(mobile)
    browser.element('#currentAddress').type(address)


def select_gender(gender):
    browser.all('[name=gender]').element_by(have.value(gender)).element('..').click()


def select_birthday(*, month, year, day):
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element(f'[value="{month}"]').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element(f'[value="{year}"]').click()
    browser.element(f'.react-datepicker__day--0{day}').click()


def input_subject(subject):
    browser.element('#subjectsInput').type(subject).press_enter()


def select_hobby(hobby):
    browser.all('[for^=hobbies-checkbox]').element_by(have.text(hobby)).click()


def upload_picture(path_to_picture):
    path_to_file.create_path('#uploadPicture', path_to_picture)


def select_state(value):
    dropdown.select('#state', by_text=value)


def select_city(value):
    dropdown.select('#city', by_text=value)


def submit():
    browser.element('#submit').press_enter()


def validation_form(*args):
    browser.element('.table').all('td').even.should(have.texts(args))


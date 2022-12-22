from selene import have, command
from selene.support.shared import browser

from demoqa_tests.model.controls import drop_down, radio_button, check_boxes, date_picker
from demoqa_tests.utils import path_to_file


def open_page():
    browser.open('/automation-practice-form')


def input_info(*, name, surname, email, mobile, address):
    browser.element('#firstName').type(name)
    browser.element('#lastName').type(surname)
    browser.element('#userEmail').type(email)
    browser.element('#userNumber').type(mobile)
    browser.element('#currentAddress').type(address)


def select_gender(gender):
    radio_button.select_by_value(browser.all('[name=gender]'), gender)


def select_birthday(*, month, year, day):
    browser.element('#dateOfBirthInput').click()
    date_picker.select_date(month, year, day)


def input_subject(subject):
    browser.element('#subjectsInput').type(subject).press_enter()


def select_hobbies(*texts):
    check_boxes.select(browser.all('[for^=hobbies-checkbox]'), *texts)


def upload_picture(path_to_picture):
    path_to_file.create_path('#uploadPicture', path_to_picture)


def select_state(value):
    drop_down.select('#state', by_text=value)


def select_city(value):
    drop_down.select('#city', by_text=value)


def submit():
    browser.element('#submit').press_enter()


def assert_of_registered_user(*args):
    browser.element('.table').all('td').even.should(have.texts(args))


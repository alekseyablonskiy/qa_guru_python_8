from demoqa_tests.model.pages import practice_form


def test_filled_form():
    practice_form.open_page()

    # WHEN
    practice_form.input_info(name='Aleksey',
                             surname='Yablonskiy',
                             email='alekseyablonskiy@gmail.com',
                             mobile='1234567890',
                             address='Minsk'
                             )

    practice_form.select_gender('Male')

    practice_form.select_birthday(day='27', month='10', year='1996')

    practice_form.input_subject('Computer Science')

    practice_form.select_hobby('Music')

    practice_form.upload_picture('resources/picture.jpg')

    practice_form.select_state('NCR')
    practice_form.select_city('Delhi')

    practice_form.submit()

    # THEN

    practice_form.validation_form(
            'Aleksey Yablonskiy',
            'alekseyablonskiy@gmail.com',
            'Male',
            '1234567890',
            '27 October,1996',
            'Computer Science',
            'Music',
            'picture.jpg',
            'Minsk',
            'NCR Delhi'
    )
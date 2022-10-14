from json import loads

from cleaner import clean_frame
from window_settings import *


def home_page_buttons():
    register_button = Button(
        window_opener,
        text='Register',
        bg='red',
        fg='white',
        borderwidth=0,
        width=20,
        height=3,
        command=register
    )

    login_button = Button(
        window_opener,
        text='Login',
        bg='green',
        fg='white',
        width=20,
        height=3,
        command=login
    )

    frame.create_window(350, 260, window=register_button)
    frame.create_window(350, 315, window=login_button)


def register():
    clean_frame()

    frame.create_text(100, 50, text='First name:')
    frame.create_text(100, 75, text='Second name:')
    frame.create_text(100, 100, text='User name:')
    frame.create_text(100, 125, text='Password:')

    frame.create_window(200, 50, window=first_name_box)
    frame.create_window(200, 75, window=last_name_box)
    frame.create_window(200, 100, window=user_name_box)
    frame.create_window(200, 125, window=password_box)

    reg_button = Button(
        window_opener,
        text='Register',
        bg='blue',
        fg='white',
        height=3,
        width=6,
        command=registration
    )
    frame.create_window(250, 175, window=reg_button)


def login():
    clean_frame()


def registration():
    register_dict = {
        'first_name': first_name_box.get(),
        'last_name': last_name_box.get(),
        'user_name': user_name_box.get(),
        'password': password_box.get(),
        'products': []
    }

    if check_validity_of_reg_details(register_dict):
        pass


def check_validity_of_reg_details(reg_dict):
    for box in reg_dict.values():
        if box == '':
            frame.create_text(
                300,
                300,
                text='Please, fulfil all boxes!',
                fill='red',
                tags='error'
            )
            return False

    frame.delete('error')

    db_usernames = []
    with open('./data_base/data_base.json', 'r') as user_names:
        for line in user_names:
            db_usernames.append(loads(line))

    for list_i in range(len(db_usernames)):
        print(db_usernames[list_i]["username"])
        if db_usernames[list_i]['username'] == reg_dict['username']:
            frame.create_text(
                300,
                300,
                text='This username is already exist',
                fill='red')


first_name_box = Entry(window_opener, bd=0)
last_name_box = Entry(window_opener, bd=0)
user_name_box = Entry(window_opener, bd=0)
password_box = Entry(window_opener, bd=0, show="*")

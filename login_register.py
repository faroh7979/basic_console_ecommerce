from window_settings import *


def home_page_buttons():
    register_button = Button(
        window_opener,
        text='Register',
        bg='red',
        fg='white',
        borderwidth=0,
        width=20,
        height=5,
        command=register
    )

    login_button = Button(
        window_opener,
        text='Login',
        bg='green',
        fg='white',
        width=20,
        height=5,
        command=login
    )

    frame.create_window(350, 260, window=register_button)


def register():
    pass


def login():
    pass



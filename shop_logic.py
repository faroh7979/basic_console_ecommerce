from json import load, dump
from tkinter import Button

from PIL import Image, ImageTk

from basic_console_ecommerce.cleaner import clean_frame
from basic_console_ecommerce.window_settings import frame, window_opener


def shop_display():
    clean_frame()
    display_items()


def display_items():

    global info_dict

    with open('./data_base/available_products.json', 'r') as stocks:
        info_dict = load(stocks)

    x = 150
    y = 50

    for element, element_info in info_dict.items():
        image_element = ImageTk.PhotoImage(Image.open(element_info['image']))
        images.append(image_element)

        frame.create_text(x, y, text=element, font=('Comic Sans MS', 15))
        frame.create_image(x, y + 100, image=image_element)

        if element_info['quantity'] > 0:  # if the product is out of stock

            color = 'green'
            text = f'In stock: {element_info["quantity"]}'

            element_button = Button(
                window_opener,
                text='Buy',
                bg='green',
                fg='white',
                width=5,
                height=3,
                command=lambda element=element: buy_items(element)  # to save the reference
            )

            frame.create_window(x, y + 230, window=element_button)

        else:

            color = 'red'
            text = 'Out of stock'

        frame.create_text(x, y + 180, text=text, font=('Comic Sans MS', 12), fill=color)

        x += 200
        if x > 550:
            x = 150
            y += 300


def buy_items(product):

    info_dict[product]['quantity'] -= 1

    with open('./data_base/available_products.json', 'w') as stock:
        dump(info_dict, stock)

    display_items()


images = []

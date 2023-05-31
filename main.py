from Main_Window import Main_Window
from Request import Request

import random
import customtkinter as ctk
from app import App


ctk.set_appearance_mode('Dark')
ctk.set_default_color_theme('dark-blue')


random.seed(8179)

def add_test_cards(app):
    app.add_new_card(0, 'Что то, что нужно сделать завтра')
    app.add_new_card(0, 'что то, что нужно сделать на этой неделе')
    app.add_new_card(1, 'То, над чем я работаю сейчас')
    app.add_new_card(1, 'Что то над чем я так же работаю сейчас')
    app.add_new_card(1, 'И над этим тоже')
    app.add_new_card(3, 'Это уже готово!')


if __name__ == '__main__':
    app = App(1920, 1080)
    add_test_cards(app)
    app.mainloop()
    request = Request()
    Main_Window(request)

Main_Window()
#request = Request()








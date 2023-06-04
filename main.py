from Main_Window import Main_Window
from Request import Request

import random
import customtkinter as ctk
from app import App


ctk.set_appearance_mode('Dark')
ctk.set_default_color_theme('dark-blue')


random.seed(8179)

request = Request()
Main_Window(request)

Main_Window()
#request = Request()








import customtkinter as ctk
import tkinter as tk
from Request import Request

class User_Window:
    def __init__(self, width = 900, height = 700):
        self.width = width
        self.height = height
        self.app = ctk.CTk()
        self.app.title("Task manager")
        self.app.geometry(f"{width}x{height}")
        self.app.configure(bg = "#689AD3")

        #создаем полотно
        self.canvas = ctk.CTkCanvas(self.app, width = width, height = height)
        self.canvas.pack(fill = "both", expand = True)
        self.canvas.config(bg = '#689AD3')
        
        self.create_buttons()
        self.app.mainloop()
    
    #создаем кнопки
    def create_buttons(self):
        button1 = ctk.CTkButton(self.app, corner_radius= 30, bg_color = '#689AD3', fg_color= '#2c4663', text = "Создать доску", width=200, height =50, font=("Arial", 20), command =self.create_board)
        button2 = ctk.CTkButton(self.app, corner_radius= 30, bg_color = '#689AD3', fg_color= '#2c4663', text = "Найти доску", width=225, height =50, font=("Arial", 20), command = self.find_board)
        button3 = ctk.CTkButton(self.app, corner_radius= 30, bg_color = '#689AD3', fg_color= '#2c4663', text = "Закрыть", width=100, height =25, font=("Arial", 16), command = self.close_window)
        #добавляем кнопки на полотно
        self.canvas.create_window(self.width//4, self.height//2 -100, window= button1)
        self.canvas.create_window(self.width // 1.5 , self.height // 2 -100 , window=button2)
        self.canvas.create_window(self.width // 2-300 , self.height // 2 + 300, window=button3)
        
    #закрытие окна
    def close_window(self):
        from Main_Window import Main_Window
        self.app.destroy()
        Main_Window()
    
    def create_board(self):
        button4 = ctk.CTkButton(self.app, corner_radius= 30, bg_color = '#689AD3', fg_color= '#2c4663', text = "Создать приватную доску", width=150, height =40,  font=("Arial", 18))
        self.canvas.create_window(self.width//4, self.height//2 -50, window= button4)
        button5 = ctk.CTkButton(self.app, corner_radius = 30, bg_color = '#689AD3', fg_color= '#2c4663', text = "Создать публичную доску", width=150, height =40, font=("Arial", 18))
        self.canvas.create_window(self.width//4, self.height//2, window= button5)

    def find_board(self):
        frame = tk.Frame(self.app, bg = '#689AD3')
        self.selected_board = tk.StringVar(frame)
        boards = [""]
        self.selected_board.set(boards[0])
        boards_menu =tk.OptionMenu(frame, self.selected_board, *boards)
        boards_menu.config(width=20, font=("Arial", 14))
        boards_menu.pack()
        self.canvas.create_window(600, 300,window=frame)

        button6 = ctk.CTkButton(self.app, corner_radius= 30, bg_color = '#689AD3', fg_color= '#2c4663', text = "Выбрать", width=100, height =25,  font=("Arial", 10))
        self.canvas.create_window(self.width//1.5, self.height//2+20, window= button6)
    
   



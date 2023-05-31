import customtkinter as ctk
import tkinter as tk
from Request import Request
from customtkinter import CTkEntry

class User_Window:
    def __init__(self,request, width = 900, height = 700):
        self.width = width
        self.height = height
        self.app = ctk.CTk()
        self.request = request
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
        button1 = ctk.CTkButton(self.app, corner_radius= 30, bg_color = '#689AD3', fg_color= '#2c4663', text = "Создать доску", width=200, height =50, font=("Arial", 20), command =self.create_zim)
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
    
    def create_zim(self):
        radiobutton_var = ctk.StringVar(value="Private")
        radiobutton_1 = ctk.CTkRadioButton(master=self.app, variable=radiobutton_var, value="Private", bg_color = '#2c4663' , text = "Приватная доска")
        self.canvas.create_window(self.width//4, self.height//2 -50, window=  radiobutton_1)
        radiobutton_2 = ctk.CTkRadioButton(master=self.app, variable=radiobutton_var, value="Public", bg_color= '#2c4663', text = "Публичная доска")
        self.canvas.create_window(self.width//4, self.height//2, window= radiobutton_2)
        frame2 = ctk.CTkFrame(self.app, bg_color="#689AD3", fg_color= '#689AD3')
        self.name_board = CTkEntry(frame2, bg_color='#689AD3', fg_color= '#2c4663', width=200, font=("Arial", 12))
        self.name_board.pack(pady=10)
        self.canvas.create_window(230, 400, window=frame2)
        button4 = ctk.CTkButton(self.app, corner_radius= 30, bg_color = '#689AD3', fg_color= '#2c4663', text = "ок", width=100, height =25, font=("Arial", 20), command= self.create_board)
        self.canvas.create_window(240, 450, window= button4)


    def create_board(self):
        desk_name= self.name_board.get()
        desk_type=self.radiobutton.get()
        create = self.request.create_desk(desk_name,desk_type)
        if create == "Desk exists!":
            self.show_error_window("Доска с таким названием уже существует")
        else:
            #тут создаеться доска
            return #нужно убрать


    def find_board(self):
        boards_list = self.request.UnloadData()
        frame = tk.Frame(self.app, bg = '#689AD3')
        self.selected_board = tk.StringVar(frame)
        boards = [""]
        boards.extend(boards_list)
        self.selected_board.set(boards[0])
        boards_menu =tk.OptionMenu(frame, self.selected_board, *boards)
        boards_menu.config(width=20, font=("Arial", 14))
        boards_menu.pack()
        self.canvas.create_window(600, 300,window=frame)

        button6 = ctk.CTkButton(self.app, corner_radius= 30, bg_color = '#689AD3', fg_color= '#2c4663', text = "Выбрать", width=100, height =25,  font=("Arial", 10))
        self.canvas.create_window(self.width//1.5, self.height//2+20, window= button6)
    
   



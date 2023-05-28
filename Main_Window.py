import customtkinter as ctk
from Registration_Window import Registration_Window
from Login_Window import Login_Window

class Main_Window:
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
        button1 = ctk.CTkButton(self.app, corner_radius= 30, bg_color = '#689AD3', fg_color= '#2c4663', text = "Зарегестрироваться", width=200, height =50, font=("Arial", 20), command = (self.open_registration_window))
        button2 = ctk.CTkButton(self.app, corner_radius= 30, bg_color = '#689AD3', fg_color= '#2c4663', text = "Войти", width=200, height =50, font=("Arial", 20), command = (self.open_login_window))
        button3 = ctk.CTkButton(self.app, corner_radius= 30, bg_color = '#689AD3', fg_color= '#2c4663', text = "Закрыть", width=200, height =50, font=("Arial", 20), command = (self.close_window))
        #добавляем кнопки на полотно
        self.canvas.create_window(self.width//2, self.height//2 -100, window= button1)
        self.canvas.create_window(self.width // 2 , self.height // 2 , window=button2)
        self.canvas.create_window(self.width // 2 , self.height // 2 + 100, window=button3)

    #закрытие окна
    def close_window(self):
        self.app.withdraw()

    def open_registration_window(self):
        self.app.withdraw()
        Registration_Window()
    
    def open_login_window(self):
        self.app.withdraw()
        Login_Window()


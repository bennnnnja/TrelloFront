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
        ctk.set_appearance_mode("dark")  
        ctk.set_default_color_theme("blue") 

        self.create_buttons()
        self.app.mainloop()

    def create_buttons(self):
        frame_1 = ctk.CTkFrame(master=self.app)
        frame_1.pack(pady=20, padx=60, fill="both", expand=True)

        label_1 = ctk.CTkLabel(master=frame_1, text="")
        label_1.pack(pady=10, padx=10)

        button_1 = ctk.CTkButton(master=frame_1, corner_radius= 30, fg_color= '#2c4663', text = "Войти", width=200, height =50, font=("Arial", 20),command = self.open_login_window)
        button_1.pack(pady=10, padx=10)

        button_2 = ctk.CTkButton(master=frame_1, corner_radius= 30, fg_color= '#2c4663', text = "Зарегестрироваться", width=200, height =50, font=("Arial", 20),command = self.open_registration_window)
        button_2.pack(pady=10, padx=10)

        button_3 = ctk.CTkButton(master=frame_1, corner_radius= 30, fg_color= '#2c4663', text ="Выход", width=200, height =50, font=("Arial", 20), command = self.close_window)
        button_3.pack(pady=10, padx=10)
    
    def close_window(self):
        self.app.destroy()

    def open_registration_window(self):
        self.app.withdraw()
        Registration_Window()
        
    
    def open_login_window(self):
        self.app.withdraw()
        Login_Window()

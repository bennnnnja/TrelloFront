import customtkinter as ctk
from customtkinter import CTkEntry
from User_Window import User_Window

class Login_Window:
    def __init__(self, width=900, height=700):
        self.width = width
        self.height = height
        self.app = ctk.CTk()
        self.app.title("Окно входа")
        self.app.geometry(f"{width}x{height}")
        self.app.configure(bg_color= "#689AD3")
        self.login_valid = False
        self.password_valid = False
        

        # создаем Canvas
        self.canvas = ctk.CTkCanvas(self.app, width=width, height=height)
        self.canvas.pack(fill="both", expand=True)
        # устанавливаем фон Canvas
        self.canvas.config(bg='#689AD3')

        self.create_buttons()
        self.create_input_field()
        self.app.mainloop()


    def create_buttons(self):
        # создаем кнопки
        button1 = ctk.CTkButton(self.app, corner_radius= 15, bg_color = '#689AD3', fg_color= '#2c4663', text="ОК", width=100, height=25, font=("Arial", 14), command=self.open_user_window)
        button2 = ctk.CTkButton(self.app, corner_radius= 15, bg_color = '#689AD3', fg_color= '#2c4663', text="Отмена", width=100, height=25, font=("Arial", 14), command=self.close_login_window)

        # добавляем кнопки на Canvas
        self.canvas.create_window(self.width // 2 - 300, self.height // 2 + 300, window=button1)
        self.canvas.create_window(self.width // 2 + 300, self.height // 2 + 300, window=button2)

    #команда для кнопки Отмена
    def close_login_window(self):
        self.app.withdraw()

    # команда для кнопки OK доделать когда будет бэк
    def open_user_window(self):
        self.validate_login()
        self.validate_password()
        login = self.login_entry.get()
        password = self.password_entry.get()
         
        
        if not self.login_valid:
            self.show_error_window("Некоректный логин. Логин должен быть длинее 6 символов")
            return

        if not self.password_valid:
            self.show_error_window("Некоректный пароль. Пароль может содердать только цыфры и буквы и должен быть не короче 8 символов")
            return
        if self.login_valid and self.password_valid:
             self.app.withdraw()
             # создаем экземпляр класса AddWindow
             User_Window()
             # Показываем главное окно после закрытия окна AddWindow
             self.app.deiconify()
        


    # устанавливаем параметры для окна ошибок
    def show_error_window(self, message):
        error_window = ctk.CTkToplevel(self.app)
        error_window.title("Ошибка")
        error_window.geometry("500x100")

        error_message = ctk.CTkLabel(error_window, text=message, width=250, font=("Arial", 12))
        error_message.pack(pady=10)

        button_frame = ctk.CTkFrame(error_window)
        button_frame.pack()

        ok_button = ctk.CTkButton(button_frame, text="ОК", command=error_window.destroy)
        ok_button.pack(pady=5)

    # валидация логина
    def validate_login(self):
        login = self.login_entry.get()
        if len(login) < 6 or not login.isalnum():
            self.login_valid = False
        else:
            self.login_valid = True

    # валидация пароля
    def validate_password(self):
        password = self.password_entry.get()
        if len(password) < 8 or not password.isalnum():
            self.password_valid = False
        else:
            self.password_valid = True

    def create_input_field(self):
        # блок с названиями
        frame1 = ctk.CTkFrame(self.app, bg_color='#689AD3' , fg_color= '#689AD3')

        ctk.CTkLabel(frame1, text="Логин:", bg_color='#689AD3', fg_color= '#2c4663', width= 150, font=("Arial", 17)).grid(row=0, column=0, sticky="n", pady=10)
        ctk.CTkLabel(frame1, text="Пароль:", bg_color='#689AD3', fg_color= '#2c4663', width= 150, font=("Arial", 17)).grid(row=1, column=0, sticky="n", pady=10)

        self.canvas.create_window(200, 300, window=frame1)

        # блок с полями ввода
        frame2 = ctk.CTkFrame(self.app, bg_color="#689AD3", fg_color= '#689AD3')

        self.login_entry = CTkEntry(frame2, bg_color='#689AD3', fg_color= '#2c4663', width=400, font=("Arial", 12))
        self.login_entry.pack(pady=10)
        self.login_entry.bind("<FocusOut>", lambda event: self.validate_login())

        self.password_entry = CTkEntry(frame2, bg_color='#689AD3', fg_color= '#2c4663', width=400, font=("Arial", 12))
        self.password_entry.pack(pady=10)
        self.password_entry.bind("<FocusOut>", lambda event: self.validate_password())

        self.canvas.create_window(500, 300, window=frame2)

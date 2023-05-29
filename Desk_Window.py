import customtkinter as ctk
from customtkinter import CTkEntry

class Desk_Window:
    def __init__(self, width=900, height=700):
        self.width = width
        self.height = height
        self.app = ctk.CTk()
        self.app.title("Доска")
        self.app.geometry(f"{width}x{height}")
        self.app.configure(bg_color= "#689AD3")
        
        

        # создаем Canvas
        self.canvas = ctk.CTkCanvas(self.app, width=width, height=height)
        self.canvas.pack(fill="both", expand=True)
        # устанавливаем фон Canvas
        self.canvas.config(bg='#689AD3')

        self.create_buttons()
        self.app.mainloop()
        self.create_carts()

    def create_buttons(self):
        # создаем кнопки
        button1 = ctk.CTkButton(self.app, corner_radius= 15, bg_color = '#689AD3', fg_color= '#2c4663', text="Создать карточку", width=100, height=25, font=("Arial", 14), command=self.create_carts)
        button2 = ctk.CTkButton(self.app, corner_radius= 15, bg_color = '#689AD3', fg_color= '#2c4663', text="Удалить карточку", width=100, height=25, font=("Arial", 14))

        # добавляем кнопки на Canvas
        self.canvas.create_window(self.width + 1, self.height + 1, window=button1)
        self.canvas.create_window(self.width - 300, self.height - 50, window=button2)  

    def create_carts(self):
        self.grid_rowconfigure(0, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)

        self.textbox = ctk.CTkTextbox(master=self, width=400, corner_radius=0)
        self.textbox.grid(row=0, column=0, sticky="nsew")
        self.textbox.insert("0.0", "Some example text!\n" * 50)
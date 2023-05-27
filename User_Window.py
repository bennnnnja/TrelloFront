import customtkinter as ctk

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
        button1 = ctk.CTkButton(self.app, corner_radius= 30, bg_color = '#689AD3', fg_color= '#2c4663', text = "Создать доску", width=200, height =50, font=("Arial", 20), command = (self.choose_option))
        button2 = ctk.CTkButton(self.app, corner_radius= 30, bg_color = '#689AD3', fg_color= '#2c4663', text = "Найти доску", width=225, height =50, font=("Arial", 20), command = ())
        button3 = ctk.CTkButton(self.app, corner_radius= 30, bg_color = '#689AD3', fg_color= '#2c4663', text = "Закрыть", width=100, height =25, font=("Arial", 16), command = (self.close_window))
        #добавляем кнопки на полотно
        self.canvas.create_window(self.width//4, self.height//2 -100, window= button1)
        self.canvas.create_window(self.width // 1.5 , self.height // 2 -100 , window=button2)
        self.canvas.create_window(self.width // 2-300 , self.height // 2 + 300, window=button3)

    #закрытие окна
    def close_window(self):
        self.app.destroy()
    
    # команда для кнопки создать доску
    def choose_option(self):
        options_list =["","Создать частную доску", "Создать публичную доску"]
        self.selected_value = ctk.StringVar(self.app)
        self.selected_value.set("Выберите тип доски:")
        question_menu = ctk.CTkOptionMenu(self.app, self.selected_value, *options_list)
        question_menu.pack()
        
        button4 = ctk.CTkButton(self.app ,corner_radius= 30, bg_color = '#689AD3', fg_color= '#2c4663', text = "Ок", width=100, height =25, font=("Arial", 16), command =())#open board
        self.canvas.create_window(self.width//4, self.height//2, window = button4)


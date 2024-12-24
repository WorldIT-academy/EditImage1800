import customtkinter as ctk
from ..tools import read_json
from ..tools import create_folder_media

class App(ctk.CTk):
    def __init__(self):
        ctk.CTk.__init__(self)
        create_folder_media()
        # у змінну CONFIG записуємо дані прочитаного файлу json, у вигляді словника
        self.CONFIG = read_json(name_json= "config.json")
        # Задаємо ширину нашого застосунку 
        self.WIDTH = int(self.winfo_screenwidth() * self.CONFIG["app_width"])
        # Задаємо висоту нашого застосунку
        self.HEIGHT = int(self.winfo_screenheight() * self.CONFIG["app_height"])
        # Задаємо розміри нашому застосунку
        self.geometry(f"{self.WIDTH}x{self.HEIGHT}")
        # Задаємо назву нашого застосунку
        self.title(self.CONFIG['app_title'])

        self.iconbitmap("static/icon/window.ico")
        
        # # self.ICON = 

app = App()

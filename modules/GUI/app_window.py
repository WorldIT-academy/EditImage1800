import PIL.Image
import customtkinter as ctk
from ..tools import read_json
from ..tools import create_folder_media
import os
from ..tools import rewrite_json
from .app_frames import AppFrame

class App(ctk.CTk):
    def __init__(self):
        ctk.CTk.__init__(self, fg_color= '#ffffff')
        create_folder_media()
        # у змінну CONFIG записуємо дані прочитаного файлу json, у вигляді словника
        self.CONFIG = read_json(name_json= "config.json")
        # Задаємо ширину нашого застосунку 
        self.WIDTH = int(self.winfo_screenwidth() * self.CONFIG["app_width"])
        # Задаємо висоту нашого застосунку
        self.HEIGHT = int(self.winfo_screenheight() * self.CONFIG["app_height"])
        #
        self.CONFIG["app_size"]["width"] = self.WIDTH
        self.CONFIG["app_size"]["height"] = self.HEIGHT
        # Записуємо зміни в конфігураційний файл json
        rewrite_json(dict= self.CONFIG, name_json= "config.json")
        
        # Задаємо розміри нашому застосунку
        self.geometry(f"{self.WIDTH}x{self.HEIGHT}")
        # Задаємо назву нашого застосунку
        self.title(self.CONFIG['app_title'])
        
        image = PIL.Image.open(os.path.abspath(os.path.join(__file__, '..', '..', '..', 'static', 'icon', 'window.ico')))
        self.ICON = ctk.CTkImage(image)
        self.iconbitmap(self.ICON)
        
        self.HEADER = AppFrame(
            ch_master= self, 
            ch_width= self.CONFIG["app_size"]["width"],
            ch_height= self.CONFIG["app_size"]["height"] * 0.05,
            ch_fg_color= '#181818'
        ) 
        self.HEADER.grid(row= 0, column= 0)
        
        self.CONTENT = AppFrame(
            ch_master= self,
            ch_width = self.CONFIG["app_size"]["width"],
            ch_height = self.CONFIG["app_size"]["height"] * 0.95,
            ch_fg_color = '#1f1f1f'
        ) 
        self.CONTENT.grid(row= 1, column= 0, pady = 1)
        

app = App()
d
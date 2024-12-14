import customtkinter as ctk
from ..tools import read_json


class App(ctk.CTk):
    def __init__(self):
        ctk.CTk.__init__(self)
        
        self.CONFIG = read_json(name_json= "config.json")
        
        self.WIDTH =  int(self.winfo_screenwidth() * self.CONFIG["app_width"])
        self.HEIGHT = int(self.winfo_screenheight() * self.CONFIG["app_height"])

        self.geometry(f"{self.WIDTH}x{self.HEIGHT}")
        self.title(self.CONFIG['app_title'])

app = App()

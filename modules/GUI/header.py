import customtkinter as ctk
from ..tools import read_json

class Header(ctk.CTkFrame):
    def __init__(self, ch_master: object, **kwargs):
        self.CONFIG = read_json(name_json = "config.json")
        ctk.CTkFrame.__init__(
            self, 
            master= ch_master,
            width= self.CONFIG['app_size']['width'],
            height= self.CONFIG['app_size']['height'] * 0.04,
            fg_color= '#181818',
            corner_radius= 0
        )
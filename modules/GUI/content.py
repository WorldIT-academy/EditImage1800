import customtkinter as ctk
from ..tools import read_json

class Content(ctk.CTkFrame):
    def __init__(self, ch_master: object, **kwargs):
        self.CONFIG = read_json(name_json = "config.json")
        ctk.CTkFrame.__init__(
            self, 
            master= ch_master,
            width= self.CONFIG['app_size']['width'],
            height= self.CONFIG['app_size']['height'] * 0.96,
            fg_color= '#1f1f1f',
            corner_radius= 0
        )
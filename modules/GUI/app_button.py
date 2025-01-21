import PIL.Image
import customtkinter as ctk
import os
import PIL


class AppButton(ctk.CTkButton):
    def __init__(self, ch_master: object, name_image: str, scale_icon: float, **kwargs):
        
        self.NAME_IMAGE = name_image
        self.SIZE = (int(scale_icon), int(scale_icon)) # Розмір зображення кнопки у форматі фігури
        
        ctk.CTkButton.__init__(
            self, 
            master = ch_master, 
            width= int(scale_icon), 
            height= int(scale_icon), 
            text= '',
            fg_color= ch_master._fg_color,
            hover_color= '#373535',
            corner_radius= 10,
            image= self.load_image(),
            **kwargs
        )
    def load_image(self):
        PATH = os.path.abspath(os.path.join(__file__, "..", "..", "..", "static", "icon", self.NAME_IMAGE))
        return ctk.CTkImage(
            light_image = PIL.Image.open(PATH), 
            size = self.SIZE
        )
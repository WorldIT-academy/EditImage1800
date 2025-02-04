import customtkinter as ctk
# from ..tools import read_json

class AppFrame(ctk.CTkFrame):
    '''
        Клас для створення фрейму застосунку.

        Аргументи:  
            >>> ch_master (object): батьківський віджет
            >>> ch_width (int): ширина фрейму
            >>> ch_height (int): висота фрейму
            >>> ch_fg_color (str): колір фона фрейму
    '''
    def __init__(self, ch_master: object, ch_width: int, ch_height: int, ch_fg_color: str, **kwargs):
        
        ctk.CTkFrame.__init__(
            self, 
            master= ch_master,
            width= ch_width,
            height= ch_height,
            fg_color= ch_fg_color,
            corner_radius= 0
        )
        # 
        self.pack_propagate(False)
        
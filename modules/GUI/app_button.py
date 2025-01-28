r"""
    #### Модуль, що зберігає в собі інструкцію-клас (AppButton), яка створює кнопку у графічному інтерфейсі застосунку
    
    [Посилання на git](https://github.com/WorldIT-academy/EditImage1800/blob/main/modules/GUI/app_button.py)
    
    ### Приклад застосування:
    
    ```python
    app_button = AppButton(ch_master= self.VERTICAL_MENU, name_image= "explorer.png", scale_icon= self.VERTICAL_MENU._current_width * 0.5)
    ```
    Необхідні модулі:
    
    - :mod:`customtkinter` - модуль для створення графічного інтерфейсу;
    - :mod:`PIL.Image` - модуль для роботи з зображеннями;
    - :mod:`os` - модуль для роботи з системними шляхами.
    
"""

import PIL.Image
import customtkinter as ctk
import os

class AppButton(ctk.CTkButton):
    
    def __init__(self, ch_master: object, name_image: str, scale_icon: float, function: object, **kwargs):
        '''
            #### Клас для створення кнопки застосунку.
            
            ### Аргументи класу AppButton:
            >>> 1. ch_master (object): батьківський віджет
            >>> 2. name_image (str): назва зображення кнопки
            >>> 3. scale_icon (float): масштаб зображення кнопки
            >>> 4. **kwargs: додаткові параметри віджету
        '''
        
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
            command= function,
            **kwargs
        )
    def load_image(self) -> ctk.CTkImage:
        '''
            Завантажує зображення кнопки з папки static/icon.
            
            ### Повертає:
            - :mod:`ctk.CTkImage`: зображення кнопки.
        '''
        PATH = os.path.abspath(os.path.join(__file__, "..", "..", "..", "static", "icon", self.NAME_IMAGE))
        return ctk.CTkImage(
            light_image = PIL.Image.open(PATH), 
            size = self.SIZE
        )
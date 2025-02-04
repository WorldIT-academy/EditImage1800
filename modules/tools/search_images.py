
import tkinter.filedialog as filedialog
from .text_setup import GREEN, YELLOW, BLUE, RED
from ..gui.app_button import AppButton
import customtkinter as ctk

def get_file_path(parent: ctk.CTk, button_parent: ctk.CTkScrollableFrame | ctk.CTkFrame) -> str:
    r"""
        Запитує користувача на вибір файла з можливістю вибору декількох файлів
        
        Виводить їх у консоль
        
        Видає список шляхів до обраних файлів
        
        Args:
            :mod:`parent` (CTk): батьківське вікно, тобто сам додаток
            :mod:`button_parent` (CTkScrollabelFrame): вікно, в якому знаходиться кнопки
    """
    list_name_file = filedialog.askopenfilenames(
        title= 'Get File Path',
        initialdir= '/',
        filetypes= [('file image', ['*.png', '*.ico', '*.jpg', '*.jpeg', '*.svg'])],
        parent= parent
    )
    print()
    for name_file in list_name_file:
        
        print(f'{GREEN}File: {BLUE}-> {YELLOW}{name_file.split('/')[-1]}')
        button = AppButton(
            ch_master= button_parent,
            text= name_file.split('/')[-1]  
        )
        button.pack(anchor= "w", padx= 20, pady= 20)  # Встановлення кнопки на вікно

        
    print()
    return list_name_file
    


import tkinter.filedialog as filedialog
from .text_setup import GREEN, YELLOW, BLUE, RED
from ..gui.app_button import AppButton
import customtkinter as ctk
from ..gui.app_images import ImageLabel
from tkinter import BOTH, TOP, Y

list_images = []

def show_images(button_name: str, frame: ctk.CTkFrame):
    #
    list_objects_frame = frame.winfo_children()
    for object in list_objects_frame:
        if isinstance(object, ImageLabel):
            object.pack_forget()
            # object.place_forget()
            # object.grid_forget()
    #
    for image in list_images:
        if image.FILE_PATH.split('/')[-1] == button_name:
            image.pack()

def get_file_path(parent: ctk.CTk, button_parent: ctk.CTkScrollableFrame | ctk.CTkFrame, dashboard: ctk.CTkFrame):
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
        
        image = ImageLabel(ch_master= dashboard, file_path= name_file)
        list_images.append(image)
        
        button = AppButton(
            ch_master= button_parent,
            text= name_file.split('/')[-1],
            # ДЗ: написати функцію show_images() котра відображає зображення відносно натиснутої кнопки,
            # виключно по центру фрейму в якому розміщено зображення
            # Додати до параметру function функцію show_images()
            function= lambda name_button = name_file.split('/')[-1]: show_images(button_name= name_button, frame= dashboard) 
        )
        
        # list_buttons.append(button)
        button.pack(anchor= "w", padx= 20, pady= 20)  # Встановлення кнопки на вікно

        
    print()
    return list_name_file
    

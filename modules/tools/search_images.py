
import tkinter.filedialog as filedialog
from .text_setup import GREEN, YELLOW, BLUE, RED
from ..gui.app_button import AppButton

def get_file_path(parent: object, button_parent: object) -> str:
    list_name_file = filedialog.askopenfilenames(
        title= 'Get File Path',
        initialdir= '/',
        filetypes= [('file image', ['*.png', '*.ico', '*.jpg', '*.jpeg', '*.svg'])],
        parent= parent
    )
    print()
    y = 10
    for name_file in list_name_file:
        
        print(f'{GREEN}File: {BLUE}-> {YELLOW}{name_file.split('/')[-1]}')
        button = AppButton(
            ch_master= button_parent,
            text= name_file.split('/')[-1]  
        )
        button.place(x = 20, y = y)
        y += 30  # 
        
        
    print()
    return list_name_file
    


# from customtkinter import filedialog
import tkinter.filedialog as filedialog

def get_file_path(parent: object) -> str:
    list_name_file = filedialog.askopenfilenames(
        title= 'Get File Path',
        initialdir= '/',
        filetypes= [('file image', ['*.png', '*.ico', '*.jpg', '*.jpeg', '*.svg'])],
        parent= parent
    )
    print()
    for name in list_name_file:
        print(name)
    print()
    return list_name_file
    

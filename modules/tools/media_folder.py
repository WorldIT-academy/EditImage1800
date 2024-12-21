import os
from os.path import abspath , join

import colorama

colorama.init()

def create_folder_media():
    try:
        # creating path to media folder 
        # ".." this command let move from file to folder or from folder to folder in reversal order 
        # __file__ point start for creating abspath
        path_media_folder = abspath(join(__file__, "..", "..", "..", "media"))

        os.makedirs(join(path_media_folder, 'images', 'downloads'), exist_ok= True)
        os.makedirs(join(path_media_folder, 'images', 'edits'), exist_ok= True)

        print(f"{colorama.Fore.GREEN}Creating folders{colorama.Style.RESET_ALL}")
    except Exception as e:
        print(f"{colorama.Fore.RED}Error: {str(e)}{colorama.Style.RESET_ALL}")


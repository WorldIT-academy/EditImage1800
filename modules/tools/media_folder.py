import os
import colorama

colorama.init()

def create_folder_media():
    if not os.path.exists('media'):  # check if directory exists
        os.mkdir('media')
        os.mkdir('media/images')
        os.mkdir('media/images/downloads')
        os.mkdir('media/images/edits')
        print(f"{colorama.Fore.GREEN}Creating folders{colorama.Style.RESET_ALL}")


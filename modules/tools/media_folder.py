import os
from .search_path import search_path
from .text_setup import *

# function for creating path to media folder 
def create_folder_media():
    try:
        # using seach_path function to find path to folder(read more in .search_path file)
        path_media_folder = search_path("media")

        # checking if folder 'images' and 'downloads' or 'edits' exists, if not - creating them
        for path in ['downloads', 'edits']:
            os.makedirs(os.path.join(path_media_folder, 'images', path), exist_ok= True)
            if not os.path.exists(os.path.join(path_media_folder, 'images', path)):
                print(f"{GREEN}Creating folder {YELLOW}{path}{RESET_STYLE}")

    except Exception as e:
        print(f"{RED}Error: {str(e)}{RESET_STYLE}")
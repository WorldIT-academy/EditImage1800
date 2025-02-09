import customtkinter as ctk
import PIL.Image

from ..tools.text_setup import *

class ImageLabel(ctk.CTkLabel):
    def __init__(self, ch_master: ctk.CTkFrame, file_path: str, **kwargs):
        
        self.FILE_PATH = file_path
        self.WIDTH = int(ch_master._current_width * 0.9)
        self.HEIGHT = int(ch_master._current_height * 0.9)
        
        ctk.CTkLabel.__init__(
            self,
            master= ch_master,
            image= self.load_image(),
            text= '',
            **kwargs
        )
        
    def load_image(self) -> ctk.CTkImage:
        try:
            image = PIL.Image.open(fp= self.FILE_PATH)
            image.width
            return ctk.CTkImage(
                light_image= image,
                size= self.check_size_image(image= image)
            )
        except Exception as error:
            print(f'{GREEN}Error loading image: {BLUE}-> {YELLOW}{error}')
            
    def check_size_image(self, image: PIL.Image) -> tuple:
        try:
            # Якщо зображення квадратне
            if image.width == image.height:
                if image.width > self.WIDTH:
                    return (self.HEIGHT, self.HEIGHT)
                else:
                    return (image.width, image.height)
            # Якщо зображення з різними, шириною та висотою
            else:
                if image.width > self.WIDTH and image.height > self.HEIGHT:
                    return (self.WIDTH, self.HEIGHT)
                else:
                    return (image.width, image.height)
                
        except Exception as error:
            print(f'{GREEN}Error checking image size: {BLUE}-> {YELLOW}{error}')

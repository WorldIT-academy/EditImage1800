import customtkinter as ctk
import PIL.Image

from ..tools.text_setup import *

class ImageLabel(ctk.CTkLabel):
    def __init__(self, ch_master: ctk.CTkFrame, file_path: str, **kwargs):
        
        self.FILE_PATH = file_path
        self.WIDTH = int(ch_master._current_width * 0.8)
        self.HEIGHT = int(ch_master._current_height * 0.8)
        
        ctk.CTkLabel.__init__(
            self,
            master= ch_master,
            image= self.load_image(),
            text= '',
            **kwargs
        )
    #
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
    #
    def check_size_image(self, image: PIL.Image) -> tuple[int, int]:
        try:
            # Якщо зображення квадратне
            if image.width == image.height:
                if image.height >= self.HEIGHT:
                    return (self.HEIGHT, self.HEIGHT)
                else:
                    return (image.width, image.height)
            # Якщо зображення з різними, шириною та висотою
            else:
                if image.width >= self.WIDTH or image.height >= self.HEIGHT:
                    delta_width = image.width / self.WIDTH
                    delta_height = image.height / self.HEIGHT
                    
                    if delta_height > 1:
                        return (int(image.width / delta_height), self.HEIGHT)
                    elif delta_width > 1:
                        return (self.WIDTH, int(image.height / delta_width))
                    elif delta_height > 1 and delta_width > 1:
                        if delta_height >= delta_width: 
                            return (int(self.WIDTH / delta_height), int(self.HEIGHT / delta_height))
                        else: 
                            return (int(self.WIDTH / delta_width), int(self.HEIGHT / delta_width))
                else:
                    return (image.width, image.height)
                
        except Exception as error:
            print(f'{GREEN}Error checking image size: {BLUE}-> {YELLOW}{error}')

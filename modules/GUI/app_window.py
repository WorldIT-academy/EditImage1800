import customtkinter as ctk
from ..tools import create_folder_media, get_file_path, read_json
from ..tools.search_path import search_path
from .app_frames import AppFrame
from .app_button import AppButton

class App(ctk.CTk):
    def __init__(self):
        ctk.CTk.__init__(self, fg_color= '#ffffff')
        
        create_folder_media()
        # у змінну CONFIG записуємо дані прочитаного файлу json, у вигляді словника
        self.CONFIG = read_json(path = "static/json/config.json")
        # Задаємо ширину нашого застосунку 
        self.WIDTH = int(self.winfo_screenwidth() * self.CONFIG["app_width"])
        # Задаємо висоту нашого застосунку
        self.HEIGHT = int(self.winfo_screenheight() * self.CONFIG["app_height"] - 50)
        # Задаємо розміри нашому застосунку
        self.geometry(f"{self.WIDTH}x{self.HEIGHT}")
        # Перерисовуємо застосунок
        self.update()
        # Забороняємо розширення застосунку
        self.resizable(False, False)
        # змінюємо назву вікна
        self.title(self.CONFIG['app_title'])
        # змінюємо значок вікна
        self.iconbitmap(search_path("static/icon/window.ico"))
        # змінюємо тему вікна та темну
        ctk.set_appearance_mode("Dark")
        
        #
        self.HEADER = AppFrame(
            ch_master= self, 
            ch_width= self.WIDTH + 1,
            ch_height= self.HEIGHT * 0.05,
            ch_fg_color= '#181818',
        )

        self.HEADER.place(x = 0, y = 0)
        #
        self.CONTENT = AppFrame(
            ch_master= self,
            ch_width = self.WIDTH,
            ch_height = self.HEIGHT * 0.95,
            ch_fg_color = '#ffffff'
        ) 
        
        self.CONTENT.place(x = 0, y = self.HEADER._current_height + 1)
        #
        self.VERTICAL_MENU = AppFrame(
            ch_master = self.CONTENT,
            ch_width= self.CONTENT._current_width * 0.05,  
            ch_height= self.CONTENT._current_height,
            ch_fg_color= '#181818'
        )
        self.VERTICAL_MENU.place(x = 0, y = 0)
        #
        self.EXPLORER = AppFrame(
            ch_master= self.CONTENT,
            ch_width= self.CONTENT._current_width * 0.15,
            ch_height= self.CONTENT._current_height,
            ch_fg_color= "#181818"
        )
        self.EXPLORER.place(x = self.CONTENT._current_width * 0.05 + 1, y= 0)
        #
        self.DASHBOARD = AppFrame(
            ch_master= self.CONTENT,
            ch_width= self.CONTENT._current_width * 0.8,
            ch_height= self.CONTENT._current_height,
            ch_fg_color= "#ffffff"
        )
        self.DASHBOARD.place(x = self.CONTENT._current_width * 0.2, y= 0)
        #
        self.HEADER_DASHBOARD = AppFrame(
            ch_master = self.DASHBOARD,
            ch_width=  self.DASHBOARD._current_width,
            ch_height= self.DASHBOARD._current_height * 0.03,
            ch_fg_color = "#181818"
        )
        self.HEADER_DASHBOARD.place(x = 0, y = 0)

        self.CONTENT_DASHBOARD = AppFrame(
            ch_master= self.DASHBOARD,
            ch_width= self.DASHBOARD._current_width,
            ch_height= self.DASHBOARD._current_height * 0.97,
            ch_fg_color= "#1f1f1f"
        )
        self.CONTENT_DASHBOARD.place(x = 0, y = self.DASHBOARD._current_height * 0.03) 
        
        self.BUTTON_VERTICAL = AppButton(
            ch_master= self.VERTICAL_MENU,
            name_image= "explorer.png",
            scale_icon= self.VERTICAL_MENU._current_width * 0.5,
            function= lambda: get_file_path(parent = self, button_parent= self.EXPLORER, dashboard= self.CONTENT_DASHBOARD)
        )
        self.BUTTON_VERTICAL.pack()

app = App()
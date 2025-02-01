import customtkinter

class CloseButton(customtkinter.CTkButton):
    def __init__(self, root, master, **kwargs):
        self.root = root

        customtkinter.CTkButton.__init__(
            self,
            master=master,
            text="x",
            font = customtkinter.CTkFont(size = 25),
            text_color = "#000000",
            command=self.on_close,
            width = 25,
            height = 25,
            fg_color = "transparent",
            **kwargs
        )

    def on_close(self):
        self.root.destroy()
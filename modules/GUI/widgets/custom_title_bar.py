import customtkinter

class CustomTitleBar(customtkinter.CTkFrame):
    def __init__(self, root, **kwargs):
        customtkinter.CTkFrame.__init__(self, root, **kwargs)

        self.root = root
        self.mouse_last_x = 0
        self.mouse_last_y = 0

        self.bind("<B1-Motion>", self.move_app)
        self.bind("<Button-1>", self.update_last_mouse_coords)

    def move_app(self, event):
        self.root.geometry(f"+{event.x_root - self.mouse_last_x}+{event.y_root - self.mouse_last_y}")

    def update_last_mouse_coords(self, event):
        self.mouse_last_x = event.x
        self.mouse_last_y = event.y
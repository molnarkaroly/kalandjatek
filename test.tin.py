import tkinter as tk

class CustomButton(tk.Button):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self['command'] = self.on_button_click

    def on_button_click(self):
        print(self['text'])

class MyApp:
    def __init__(self, master):
        self.master = master
        self.levels = [1, 2, 3, 4, 5]
        self.create_buttons()

    def create_buttons(self):
        for level in self.levels:
            for i in range(level):
                button = CustomButton(self.master, text=f"Button {i+1} of level {level}")
                button.pack(pady=5)

root = tk.Tk()
app = MyApp(root)
root.mainloop()

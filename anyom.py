import tkinter as tk

lista = ["alma", "alpaka", "albatrosz",]
e = 0
x = 0
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

        self.a_count = ""

    def create_widgets(self):
        self.a_label = tk.Label(self, text="A: 0")
        self.a_label.pack()

        self.quit_button = tk.Button(self, text="Quit", command=self.master.destroy)
        self.quit_button.pack()

        self.a_button = tk.Button(self, text="+1", command=self.count_a)
        self.a_button.pack()

    def count_a(self):
        lista[e] = self.a_count
        self.a_count = lista[e + x]
        x += 1
        self.a_label.config(text="A: {}".format(self.a_count))


root = tk.Tk()
app = Application(master=root)
app.mainloop()

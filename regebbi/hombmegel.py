import tkinter as tk

root = tk.Tk()

# Létrehozunk egy gombot és hozzáadjuk a felhasználói felülethez
button = tk.Button(root, text="Látható gomb", command= self.count_a)
button.pack()

# Elrejtjük a gombot
#button.pack_forget()

def count_a(self):
        self.a_label.config(text="A: {}".format(self.a_count))
        button.pack_forget()
        
root.mainloop()

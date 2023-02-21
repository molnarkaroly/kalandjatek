import tkinter as tk

root = tk.Tk()

# Létrehozunk egy gombot és hozzáadjuk a felhasználói felülethez
button = tk.Button(root, text="Látható gomb")
button.pack()

# Elrejtjük a gombot
#button.pack_forget()

root.mainloop()

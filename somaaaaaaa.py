import tkinter as tk

def hide_button_1():
    button1.pack_forget()
    valtozo = 0
    label.config(text="Hello, World!")

def hide_button_2():
    button2.pack_forget()
    valtozo = 1
    label.config(text="Hello, school!")

def hide_button_3():
    button3.pack_forget()
    valtozo = 1
    label.config(text="Hello, your mom!")

utak = [10,12,13]

szint= 1



root = tk.Tk()
root.geometry("200x200")

label = tk.Label(root, text="")
label.pack(pady=5)

if len(utak) == 1:
    button1 = tk.Button(root, text= utak[0], command=hide_button_1)
    szint = utak[0]
    button1.pack(pady=10)

if len(utak) == 2:
    button1 = tk.Button(root, text=utak[0], command=hide_button_1)
    szint = utak[0]
    button1.pack(pady=10)

    button2 = tk.Button(root, text=utak[1], command=hide_button_2)
    szint = utak[1]
    button2.pack(pady=10)

if len(utak) == 3:
    button1 = tk.Button(root, text=utak[0], command=hide_button_1)
    szint = utak[0]
    button1.pack(pady=10)

    button2 = tk.Button(root, text=utak[1], command=hide_button_2)
    szint = utak[1]
    button2.pack(pady=10)

    button3 = tk.Button(root, text=utak[2], command=hide_button_3)
    szint = utak[2]
    button3.pack(pady=10)



#button1 = tk.Button(root, text="Click you!", command=hide_button_1)
#button1.pack(pady=10)

#button2 = tk.Button(root, text="Click me!", command=hide_button_2)
#button2.pack(pady=10)

#button3 = tk.Button(root, text="Click me!", command=hide_button_3)
#button3.pack(pady=10)


root.mainloop()
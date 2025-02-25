from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# Create root
root = Tk()

# Create frame with grid
frm = ttk.Frame(root, padding=20)
frm.grid()

chromecasts=["Chromecast 1", "Chromecast 2", "Chromecast 3"]

def btn_click(chromecast: str):
    messagebox.showinfo("title", chromecast)
    #root.destroy()

row=0
for chromecast in chromecasts:
    ttk.Button(frm, padding=20, text=chromecast, command=lambda: btn_click(chromecast)).grid(column=0, row=row)
    ttk.Button(frm, padding=20, text=chromecast, command=lambda: btn_click(chromecast)).grid(column=1, row=row)
    row+=1

# Start the Tkinter event loop
root.mainloop()

import tkinter as tk

def show_info_message():
  title = "Information"
  message = "This is an informational message."
  tk.messagebox.showinfo(title, message)

def show_warning_message():
  title = "Warning!"
  message = "Are you sure you want to continue?"
  response = tk.messagebox.askquestion(title, message)
  if response == "yes":
    print("User confirmed.")
  else:
    print("User canceled.")

root = tk.Tk()
info_button = tk.Button(root, text="Show Info", command=show_info_message)
warning_button = tk.Button(root, text="Show Warning", command=show_warning_message)

info_button.pack()
warning_button.pack()

root.mainloop()

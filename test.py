import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("Test")

label = tk.Label(root, text="Tkinter Works")
label.pack(pady=50)

root.mainloop()
import tkinter as tk
window = tk.Tk()
window.title("My first desktop app")
window.geometry("600x400")
message = tk.Label(text = "This is great, happy New Year")
message.grid(column=0, row=0)
window.mainloop()
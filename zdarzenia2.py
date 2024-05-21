import tkinter as tk

def on_text_change(event):
    label.config(text=f"Aktualna zawartość: {entry.get()}")

root = tk.Tk()
root.geometry("300x300")
root.title("Reakcja na zmianę tekstu")

entry = tk.Entry(root)
entry.pack()
entry.bind("<KeyRelease>", on_text_change)

label = tk.Label(root, text="Wpisz coś...")
label.pack()

root.mainloop()

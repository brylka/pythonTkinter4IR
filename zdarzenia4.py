import tkinter as tk
from tkinter import ttk

def on_slider_change(event):
    label.config(text=f"Wartość suwaka: {slider.get()}")

root = tk.Tk()
root.geometry("300x200")
root.title("Reakcja na przesunięcie suwaka")

slider = ttk.Scale(root, from_=0, to=100, orient='horizontal', command=on_slider_change)
slider.pack()

label = tk.Label(root, text="Przesuń suwak...")
label.pack()

root.mainloop()

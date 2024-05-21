import tkinter as tk
from tkinter import messagebox

def on_close():
    if messagebox.askokcancel("Zamknij", "Czy na pewno chcesz zamknąć aplikację?"):
        root.destroy()

root = tk.Tk()
root.geometry("300x300")
root.title("Obsługa zdarzenia zamknięcia okna")

root.protocol("WM_DELETE_WINDOW", on_close)

root.mainloop()

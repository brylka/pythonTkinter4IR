import tkinter as tk

def on_mouse_click(event):
    label.config(text=f"Kliknięto myszą na pozycji: ({event.x}, {event.y})")

root = tk.Tk()
root.geometry("300x300")
root.title("Obsługa zdarzeń myszy")

label = tk.Label(root, text="Kliknij gdziekolwiek w oknie...")
label.pack()

root.bind("<B1-Motion>", on_mouse_click)

root.mainloop()

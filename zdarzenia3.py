import tkinter as tk

def on_key_press(event):
    label.config(text=f"Wciśnięto klawisz: {event.char}")

root = tk.Tk()
root.geometry("300x300")
root.title("Obsługa zdarzeń klawiatury")

label = tk.Label(root, text="Wciśnij dowolny klawisz...")
label.pack()

root.bind("<Key>", on_key_press)

root.mainloop()

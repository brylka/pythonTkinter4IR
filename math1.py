import tkinter as tk
import math


def calculate_quadratic():
    try:
        # Pobieranie współczynników z pól tekstowych
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())

        # Obliczanie delty
        delta = b ** 2 - 4 * a * c
        delta_label.config(text=f"Delta: {delta}")

        # Obliczanie pierwiastków w zależności od delty
        if delta < 0:
            roots_label.config(text="Brak pierwiastków rzeczywistych.")
        elif delta == 0:
            x = -b / (2 * a)
            roots_label.config(text=f"Pierwiastek podwójny: x = {x}")
        else:
            sqrt_delta = math.sqrt(delta)
            x1 = (-b - sqrt_delta) / (2 * a)
            x2 = (-b + sqrt_delta) / (2 * a)
            roots_label.config(text=f"Pierwiastki: x1 = {x1}, x2 = {x2}")
    except ValueError:
        # Obsługa błędu, gdy dane nie są prawidłowymi liczbami
        roots_label.config(text="Proszę wprowadzić prawidłowe liczby.")
    finally:
        pass
        # Czyszczenie pól tekstowych po obliczeniach
        entry_a.delete(0, tk.END)
        entry_b.delete(0, tk.END)
        entry_c.delete(0, tk.END)


# Tworzenie głównego okna
root = tk.Tk()
root.title("Kalkulator funkcji kwadratowej")

# Tworzenie i umieszczanie widgetów
label_f = tk.Label(root, text="f(x) = ax² + bx + c")
label_f.pack()

label_a = tk.Label(root, text="Wartość a:")
label_a.pack()

entry_a = tk.Entry(root)
entry_a.pack()

label_b = tk.Label(root, text="Wartość b:")
label_b.pack()

entry_b = tk.Entry(root)
entry_b.pack()

label_c = tk.Label(root, text="Wartość c:")
label_c.pack()

entry_c = tk.Entry(root)
entry_c.pack()

calculate_button = tk.Button(root, text="Oblicz", command=calculate_quadratic)
calculate_button.pack()

delta_label = tk.Label(root, text="Delta: ")
delta_label.pack()

roots_label = tk.Label(root, text="Pierwiastki: ")
roots_label.pack()

# Uruchomienie głównej pętli Tkinter
root.mainloop()

import tkinter as tk
import math


def is_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a


def calculate_triangle():
    try:
        # Pobieranie wartości z pól tekstowych
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())

        if is_triangle(a, b, c):
            # Obliczanie kątów przy użyciu twierdzenia cosinusów
            alpha = math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c))
            beta = math.acos((a ** 2 + c ** 2 - b ** 2) / (2 * a * c))
            gamma = math.acos((a ** 2 + b ** 2 - c ** 2) / (2 * a * b))

            # Konwersja radianów na stopnie
            alpha = math.degrees(alpha)
            beta = math.degrees(beta)
            gamma = math.degrees(gamma)

            result_label.config(text=f"Kąty: α = {alpha:.2f}°, β = {beta:.2f}°, γ = {gamma:.2f}°")
        else:
            result_label.config(text="Podane długości nie tworzą trójkąta.")
    except ValueError:
        result_label.config(text="Proszę wprowadzić prawidłowe liczby.")
    finally:
        # Czyszczenie pól tekstowych po obliczeniach
        entry_a.delete(0, tk.END)
        entry_b.delete(0, tk.END)
        entry_c.delete(0, tk.END)


# Tworzenie głównego okna
root = tk.Tk()
root.title("Kalkulator trójkątów")

# Tworzenie i umieszczanie widgetów
label_info = tk.Label(root, text="Podaj długości boków trójkąta:")
label_info.pack()

label_a = tk.Label(root, text="Bok a:")
label_a.pack()

entry_a = tk.Entry(root)
entry_a.pack()

label_b = tk.Label(root, text="Bok b:")
label_b.pack()

entry_b = tk.Entry(root)
entry_b.pack()

label_c = tk.Label(root, text="Bok c:")
label_c.pack()

entry_c = tk.Entry(root)
entry_c.pack()

calculate_button = tk.Button(root, text="Oblicz", command=calculate_triangle)
calculate_button.pack()

result_label = tk.Label(root, text="Kąty:")
result_label.pack()

# Uruchomienie głównej pętli Tkinter
root.mainloop()

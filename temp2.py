import tkinter as tk

def convert_temperature(conversion_type):
    try:
        value = float(entry_value.get())
        if conversion_type == "c_to_f":
            result = value * 9/5 + 32
            label_result.config(text=f"{value} °C = {result:.2f} °F")
        elif conversion_type == "c_to_k":
            result = value + 273.15
            label_result.config(text=f"{value} °C = {result:.2f} K")
        elif conversion_type == "f_to_c":
            result = (value - 32) * 5/9
            label_result.config(text=f"{value} °F = {result:.2f} °C")
        elif conversion_type == "f_to_k":
            result = (value - 32) * 5/9 + 273.15
            label_result.config(text=f"{value} °F = {result:.2f} K")
        elif conversion_type == "k_to_c":
            result = value - 273.15
            label_result.config(text=f"{value} K = {result:.2f} °C")
        elif conversion_type == "k_to_f":
            result = (value - 273.15) * 9/5 + 32
            label_result.config(text=f"{value} K = {result:.2f} °F")
    except ValueError:
        label_result.config(text="Proszę wpisać prawidłową liczbę.")

root = tk.Tk()
root.title("Konwerter Temperatur")

# Pole do wprowadzania temperatur
entry_value = tk.Entry(root, width=10)
entry_value.pack(pady=10)

# Etykieta z wynikiem
label_result = tk.Label(root, text="Tutaj pojawi się wynik")
label_result.pack(pady=10)

# Przyciski do konwersji
button_c_to_f = tk.Button(root, text="C na F", command=lambda: convert_temperature("c_to_f"))
button_c_to_f.pack(side=tk.LEFT, padx=5)

button_c_to_k = tk.Button(root, text="C na K", command=lambda: convert_temperature("c_to_k"))
button_c_to_k.pack(side=tk.LEFT, padx=5)

button_f_to_c = tk.Button(root, text="F na C", command=lambda: convert_temperature("f_to_c"))
button_f_to_c.pack(side=tk.LEFT, padx=5)

button_f_to_k = tk.Button(root, text="F na K", command=lambda: convert_temperature("f_to_k"))
button_f_to_k.pack(side=tk.LEFT, padx=5)

button_k_to_c = tk.Button(root, text="K na C", command=lambda: convert_temperature("k_to_c"))
button_k_to_c.pack(side=tk.LEFT, padx=5)

button_k_to_f = tk.Button(root, text="K na F", command=lambda: convert_temperature("k_to_f"))
button_k_to_f.pack(side=tk.LEFT, padx=5)

root.mainloop()

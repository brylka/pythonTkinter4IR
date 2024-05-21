import tkinter as tk

def convert_c_to_f():
    try:
        celsius = float(entry_value.get())
        fahrenheit = celsius * 9/5 + 32
        label_result.config(text=f"{celsius} °C = {fahrenheit:.2f} °F")
    except ValueError:
        label_result.config(text="Proszę wpisać prawidłową liczbę.")

def convert_c_to_k():
    try:
        celsius = float(entry_value.get())
        kelvin = celsius + 273.15
        label_result.config(text=f"{celsius} °C = {kelvin:.2f} K")
    except ValueError:
        label_result.config(text="Proszę wpisać prawidłową liczbę.")

def convert_f_to_c():
    try:
        fahrenheit = float(entry_value.get())
        celsius = (fahrenheit - 32) * 5/9
        label_result.config(text=f"{fahrenheit} °F = {celsius:.2f} °C")
    except ValueError:
        label_result.config(text="Proszę wpisać prawidłową liczbę.")

def convert_f_to_k():
    try:
        fahrenheit = float(entry_value.get())
        kelvin = (fahrenheit - 32) * 5/9 + 273.15
        label_result.config(text=f"{fahrenheit} °F = {kelvin:.2f} K")
    except ValueError:
        label_result.config(text="Proszę wpisać prawidłową liczbę.")

def convert_k_to_c():
    try:
        kelvin = float(entry_value.get())
        celsius = kelvin - 273.15
        label_result.config(text=f"{kelvin} K = {celsius:.2f} °C")
    except ValueError:
        label_result.config(text="Proszę wpisać prawidłową liczbę.")

def convert_k_to_f():
    try:
        kelvin = float(entry_value.get())
        fahrenheit = (kelvin - 273.15) * 9/5 + 32
        label_result.config(text=f"{kelvin} K = {fahrenheit:.2f} °F")
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
button_c_to_f = tk.Button(root, text="C na F", command=convert_c_to_f)
button_c_to_f.pack(side=tk.LEFT, padx=5)

button_c_to_k = tk.Button(root, text="C na K", command=convert_c_to_k)
button_c_to_k.pack(side=tk.LEFT, padx=5)

button_f_to_c = tk.Button(root, text="F na C", command=convert_f_to_c)
button_f_to_c.pack(side=tk.LEFT, padx=5)

button_f_to_k = tk.Button(root, text="F na K", command=convert_f_to_k)
button_f_to_k.pack(side=tk.LEFT, padx=5)

button_k_to_c = tk.Button(root, text="K na C", command=convert_k_to_c)
button_k_to_c.pack(side=tk.LEFT, padx=5)

button_k_to_f = tk.Button(root, text="K na F", command=convert_k_to_f)
button_k_to_f.pack(side=tk.LEFT, padx=5)

root.mainloop()

import tkinter as tk

def convert_length(conversion_type):
    try:
        value = float(entry_value.get())
        if conversion_type == "m_to_in":
            result = value * 39.3701
            label_result.config(text=f"{value} metrów = {result:.2f} cali")
        elif conversion_type == "m_to_mi":
            result = value / 1609.34
            label_result.config(text=f"{value} metrów = {result:.5f} mil")
        elif conversion_type == "in_to_m":
            result = value / 39.3701
            label_result.config(text=f"{value} cali = {result:.3f} metrów")
        elif conversion_type == "in_to_mi":
            result = value / 63360
            label_result.config(text=f"{value} cali = {result:.5f} mil")
        elif conversion_type == "mi_to_m":
            result = value * 1609.34
            label_result.config(text=f"{value} mil = {result:.3f} metrów")
        elif conversion_type == "mi_to_in":
            result = value * 63360
            label_result.config(text=f"{value} mil = {result:.2f} cali")
    except ValueError:
        label_result.config(text="Proszę wpisać prawidłową liczbę.")

root = tk.Tk()
root.title("Konwerter Długości")

# Pole wejściowe do podawania długości
entry_value = tk.Entry(root, width=10)
entry_value.pack(pady=10)

# Etykieta z wynikiem
label_result = tk.Label(root, text="Tutaj pojawi się wynik")
label_result.pack(pady=10)

# Ramka dla pierwszego rzędu przycisków
frame1 = tk.Frame(root)
frame1.pack(pady=5)

button_m_to_in = tk.Button(frame1, text="Metry na Cal", command=lambda: convert_length("m_to_in"))
button_m_to_in.pack(side=tk.LEFT, padx=5)

button_m_to_mi = tk.Button(frame1, text="Metry na Mile", command=lambda: convert_length("m_to_mi"))
button_m_to_mi.pack(side=tk.LEFT, padx=5)

# Ramka dla drugiego rzędu przycisków
frame2 = tk.Frame(root)
frame2.pack(pady=5)

button_in_to_m = tk.Button(frame2, text="Cale na Metry", command=lambda: convert_length("in_to_m"))
button_in_to_m.pack(side=tk.LEFT, padx=5)

button_in_to_mi = tk.Button(frame2, text="Cale na Mile", command=lambda: convert_length("in_to_mi"))
button_in_to_mi.pack(side=tk.LEFT, padx=5)

# Ramka dla trzeciego rzędu przycisków
frame3 = tk.Frame(root)
frame3.pack(pady=5)

button_mi_to_m = tk.Button(frame3, text="Mile na Metry", command=lambda: convert_length("mi_to_m"))
button_mi_to_m.pack(side=tk.LEFT, padx=5)

button_mi_to_in = tk.Button(frame3, text="Mile na Cale", command=lambda: convert_length("mi_to_in"))
button_mi_to_in.pack(side=tk.LEFT, padx=5)

root.mainloop()

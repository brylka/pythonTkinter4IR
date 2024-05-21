import tkinter as tk

def meters_to_inches():
    try:
        meters = float(entry_value.get())
        inches = meters * 39.3701
        label_result.config(text=f"{meters} metrów = {inches:.2f} cali")
    except ValueError:
        label_result.config(text="Proszę wpisać prawidłową liczbę.")

def meters_to_miles():
    try:
        meters = float(entry_value.get())
        miles = meters / 1609.34
        label_result.config(text=f"{meters} metrów = {miles:.5f} mil")
    except ValueError:
        label_result.config(text="Proszę wpisać prawidłową liczbę.")

def inches_to_meters():
    try:
        inches = float(entry_value.get())
        meters = inches / 39.3701
        label_result.config(text=f"{inches} cali = {meters:.3f} metrów")
    except ValueError:
        label_result.config(text="Proszę wpisać prawidłową liczbę.")

def inches_to_miles():
    try:
        inches = float(entry_value.get())
        miles = inches / 63360
        label_result.config(text=f"{inches} cali = {miles:.5f} mil")
    except ValueError:
        label_result.config(text="Proszę wpisać prawidłową liczbę.")

def miles_to_meters():
    try:
        miles = float(entry_value.get())
        meters = miles * 1609.34
        label_result.config(text=f"{miles} mil = {meters:.3f} metrów")
    except ValueError:
        label_result.config(text="Proszę wpisać prawidłową liczbę.")

def miles_to_inches():
    try:
        miles = float(entry_value.get())
        inches = miles * 63360
        label_result.config(text=f"{miles} mil = {inches:.2f} cali")
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

button_m_to_in = tk.Button(frame1, text="Metry na Cal", command=meters_to_inches)
button_m_to_in.pack(side=tk.LEFT, padx=5)

button_m_to_mi = tk.Button(frame1, text="Metry na Mile", command=meters_to_miles)
button_m_to_mi.pack(side=tk.LEFT, padx=5)

# Ramka dla drugiego rzędu przycisków
frame2 = tk.Frame(root)
frame2.pack(pady=5)

button_in_to_m = tk.Button(frame2, text="Cale na Metry", command=inches_to_meters)
button_in_to_m.pack(side=tk.LEFT, padx=5)

button_in_to_mi = tk.Button(frame2, text="Cale na Mile", command=inches_to_miles)
button_in_to_mi.pack(side=tk.LEFT, padx=5)

# Ramka dla trzeciego rzędu przycisków
frame3 = tk.Frame(root)
frame3.pack(pady=5)

button_mi_to_m = tk.Button(frame3, text="Mile na Metry", command=miles_to_meters)
button_mi_to_m.pack(side=tk.LEFT, padx=5)

button_mi_to_in = tk.Button(frame3, text="Mile na Cale", command=miles_to_inches)
button_mi_to_in.pack(side=tk.LEFT, padx=5)

root.mainloop()

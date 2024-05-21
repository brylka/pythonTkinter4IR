import tkinter as tk

# Przeliczniki długości
conversion_factors = {
    "m_to_in": (lambda m: m * 39.3701, "metrów", "cali"),
    "m_to_mi": (lambda m: m / 1609.34, "metrów", "mil"),
    "in_to_m": (lambda i: i / 39.3701, "cali", "metrów"),
    "in_to_mi": (lambda i: i / 63360, "cali", "mil"),
    "mi_to_m": (lambda mi: mi * 1609.34, "mil", "metrów"),
    "mi_to_in": (lambda mi: mi * 63360, "mil", "cali")
}

def convert_length(conversion_type):
    try:
        value = float(entry_value.get())
        convert, from_unit, to_unit = conversion_factors[conversion_type]
        result = convert(value)
        label_result.config(text=f"{value} {from_unit} = {result:.2f} {to_unit}")
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

# Lista przycisków
conversion_buttons = [
    ("Metry na Cal", "m_to_in"),
    ("Metry na Mile", "m_to_mi"),
    ("Cale na Metry", "in_to_m"),
    ("Cale na Mile", "in_to_mi"),
    ("Mile na Metry", "mi_to_m"),
    ("Mile na Cale", "mi_to_in")
]

# Dodawanie przycisków parami
for i in range(0, len(conversion_buttons), 2):
    frame = tk.Frame(root)
    frame.pack(pady=5)
    for (button_text, conversion_type) in conversion_buttons[i:i+2]:
        button = tk.Button(frame, text=button_text, command=lambda ct=conversion_type: convert_length(ct))
        button.pack(side=tk.LEFT, padx=5)

root.mainloop()

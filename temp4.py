import tkinter as tk

class TemperatureConverterApp:
    conversion_factors = {
        "c_to_f": (lambda c: c * 9 / 5 + 32, "°C", "°F"),
        "c_to_k": (lambda c: c + 273.15, "°C", "K"),
        "f_to_c": (lambda f: (f - 32) * 5 / 9, "°F", "°C"),
        "f_to_k": (lambda f: (f - 32) * 5 / 9 + 273.15, "°F", "K"),
        "k_to_c": (lambda k: k - 273.15, "K", "°C"),
        "k_to_f": (lambda k: (k - 273.15) * 9 / 5 + 32, "K", "°F")
    }

    def __init__(self, root):
        self.root = root
        self.root.title("Konwerter Temperatur")

        # Pole do wprowadzania temperatur
        self.entry_value = tk.Entry(root, width=10)
        self.entry_value.pack(pady=10)

        # Etykieta z wynikiem
        self.label_result = tk.Label(root, text="Tutaj pojawi się wynik")
        self.label_result.pack(pady=10)

        # Ramka na przyciski
        frame = tk.Frame(root)
        frame.pack(pady=5)

        # Dodawanie przycisków z pętlą
        conversion_buttons = [
            ("C na F", "c_to_f"),
            ("C na K", "c_to_k"),
            ("F na C", "f_to_c"),
            ("F na K", "f_to_k"),
            ("K na C", "k_to_c"),
            ("K na F", "k_to_f")
        ]

        for (button_text, conversion_type) in conversion_buttons:
            button = tk.Button(
                frame,
                text=button_text,
                command=lambda ct=conversion_type: self.convert_temperature(ct)
            )
            button.pack(side=tk.LEFT, padx=5)

    def convert_temperature(self, conversion_type):
        try:
            value = float(self.entry_value.get())
            convert, from_unit, to_unit = self.conversion_factors[conversion_type]
            result = convert(value)
            self.label_result.config(
                text=f"{value} {from_unit} = {result:.2f} {to_unit}"
            )
        except ValueError:
            self.label_result.config(text="Proszę wpisać prawidłową liczbę.")


if __name__ == "__main__":
    root = tk.Tk()
    app = TemperatureConverterApp(root)
    root.mainloop()

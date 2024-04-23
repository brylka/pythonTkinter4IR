import tkinter as tk

def calculate(operation):
    try:
        # Pobieranie wartości z pól tekstowych i konwersja na liczby
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        # Wykonanie odpowiedniej operacji w zależności od przycisku
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                raise ValueError("Dzielenie przez zero!")
        elif operation == 'pow':
            result = num1 ** num2
        elif operation == 'sqrt':
            if num1 >= 0 and num2 != 0:
                result = num1 ** (1/num2)
            else:
                raise ValueError("Nieprawidłowe dane dla pierwiastkowania!")
        # Formatowanie i wyświetlanie wyniku
        label_wynik.config(text=f"{num1} {operation} {num2} = {result}")
    except ValueError as e:
        # Obsługa błędu
        label_wynik.config(text=str(e))
    finally:
        # Czyszczenie pól tekstowych
        entry1.delete(0, tk.END)
        entry2.delete(0, tk.END)

# Tworzenie głównego okna
root = tk.Tk()
root.title("Kalkulator")

# Tworzenie i umieszczanie widgetów
label1 = tk.Label(root, text="Wprowadź pierwszą liczbę:")
label1.pack()

entry1 = tk.Entry(root)
entry1.pack()

label2 = tk.Label(root, text="Wprowadź drugą liczbę:")
label2.pack()

entry2 = tk.Entry(root)
entry2.pack()

# Ramka na przyciski
frame = tk.Frame(root)
frame.pack(pady=10)

# Przyciski dla różnych operacji
button_plus = tk.Button(frame, text="+", command=lambda: calculate('+'))
button_plus.pack(side=tk.LEFT, padx=5)

button_minus = tk.Button(frame, text="-", command=lambda: calculate('-'))
button_minus.pack(side=tk.LEFT, padx=5)

button_multiply = tk.Button(frame, text="*", command=lambda: calculate('*'))
button_multiply.pack(side=tk.LEFT, padx=5)

button_divide = tk.Button(frame, text="/", command=lambda: calculate('/'))
button_divide.pack(side=tk.LEFT, padx=5)

button_pow = tk.Button(frame, text="^", command=lambda: calculate('pow'))
button_pow.pack(side=tk.LEFT, padx=5)

button_sqrt = tk.Button(frame, text="sqrt", command=lambda: calculate('sqrt'))
button_sqrt.pack(side=tk.LEFT, padx=5)

label_wynik = tk.Label(root, text="Wynik: ")
label_wynik.pack()

# Uruchomienie głównej pętli Tkinter
root.mainloop()

import tkinter as tk

def add():
    try:
        # Pobieranie wartości z pól tekstowych i konwersja na liczby
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        # Dodawanie liczb
        wynik = num1 + num2
        # Wyświetlanie wyniku
        label_wynik.config(text=f"Wynik: {wynik}")
    except ValueError:
        # Obsługa błędu, gdy wprowadzone dane nie są liczbami
        label_wynik.config(text="Proszę wprowadzić prawidłowe liczby.")

# Tworzenie głównego okna
root = tk.Tk()
root.title("Kalkulator dodawania")

# Tworzenie i umieszczanie widgetów
label1 = tk.Label(root, text="Wprowadź pierwszą liczbę:")
label1.pack()

entry1 = tk.Entry(root)
entry1.pack()

label2 = tk.Label(root, text="Wprowadź drugą liczbę:")
label2.pack()

entry2 = tk.Entry(root)
entry2.pack()

button = tk.Button(root, text="Oblicz", command=add)
button.pack()

label_wynik = tk.Label(root, text="Wynik: ")
label_wynik.pack()

# Uruchomienie głównej pętli Tkinter
root.mainloop()

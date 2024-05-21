# Zdarzenia
Tkinter obsługuje różne typy zdarzeń związanych z myszą oraz klawiaturą. Oto niektóre z nich:
## Zdarzenia myszy:
- `<Button-1>`, `<Button-2>`, `<Button-3>`: Kliknięcie odpowiednio lewym, środkowym (kołem myszy) i prawym przyciskiem myszy.
- `<B1-Motion>`, `<B2-Motion>`, `<B3-Motion>`: Przesuwanie myszy z wciśniętym odpowiednio lewym, środkowym lub prawym przyciskiem.
- `<ButtonRelease-1>`, `<ButtonRelease-2>`, `<ButtonRelease-3>`: Zdarzenia generowane przy zwolnieniu odpowiedniego przycisku myszy.
- `<Double-Button-1>`, `<Double-Button-2>`, `<Double-Button-3>`: Podwójne kliknięcie odpowiednim przyciskiem myszy.
- `<Enter>`, `<Leave>`: Zdarzenia generowane, gdy kursor myszy wchodzi na obszar widgetu (<Enter>) lub opuszcza go (<Leave>).
- `<MouseWheel>`: Obracanie kółkiem myszy.
## Zdarzenia klawiatury:
- `<KeyPress>`, `<KeyRelease>`: Wciśnięcie i zwolnienie klawisza na klawiaturze.
- `<KeyPress-{key}>`, na przykład `<KeyPress-A>`: Wciśnięcie konkretnego klawisza (w tym przypadku klawisza 'A').
- `<Control-KeyPress-C>`, `<Alt-KeyPress-A>`: Kombinacje klawiszy z klawiszami modyfikującymi jak Control, Alt, Shift.
- `<Key>`: Zdarzenie generowane przy każdym wciśnięciu klawisza, gdy widget ma fokus. Daje możliwość obsługi dowolnych wciśnięć klawiszy.
## Zdarzenia dotyczące okna aplikacji:
- `<Configure>`: Zmiana rozmiaru okna.
- `<FocusIn>`, `<FocusOut>`: Zdarzenia generowane, gdy widget uzyskuje lub traci fokus.
## Zdarzenia specjalne:
- `<Destroy>`: Zdarzenie generowane, gdy widget jest niszczony.
- `<Expose>`: Zdarzenie wywoływane, gdy część widgetu staje się widoczna po tym, jak była zakryta.

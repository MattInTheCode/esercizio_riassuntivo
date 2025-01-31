# chiediamo l'altezza all'utente e se è inferiore a 400 cm non può fare la lavatrice

altezza_utente = float(input("Inserisci la tua altezza per passare:"))


minimo_altezza = 400



if altezza_utente >= minimo_altezza:
    print("Puoi fare la lavatrice!")
else:
    print("Non puoi fare la lavatrice, altezza insufficiente.")

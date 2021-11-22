lista_numeri = [3, 3, 5, 1, 2]

def somma(lista_numeri):
    risultato = 0
    for item in lista_numeri:
        risultato = risultato + item
    print('risultato: {}'.format(risultato))

    risultato = somma(lista_numeri)
    
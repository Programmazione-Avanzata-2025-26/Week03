class Impiegato:
    # Metodo speciale __ che costruisce ed inizializza l'impiegato
    def __init__(self, nome, cognome, paga):
        self._nome = nome
        self._cognome = cognome
        self._paga = paga

    """
    def stampati(self):
        print(self._nome, self._cognome, self._paga)
    """

    # Altri metodi speciali, dunded methods con __

    def __str__(self):
        return (f"Impiegato {self._nome} "
                f"{self._cognome}, paga {self._paga} euro")

    def __repr__(self):
        return (f'{type(self).__name__} (nome={self._nome}, '
                f'cognome={self._cognome}, paga={self._paga})')



i = Impiegato("Mario", "Rossi", 20000)

#i.stampati()

#print(i.descriviti())

print(i.__str__())

print(i.__repr__())

print(i) # Anche senza usare i metodi definiti, ora che sono stati definiti
         # non viene più stampato il riferimento/l'ind. di memoria

# Posso anche creare altri oggetti Impiegato

altroImpiegato = Impiegato("Gianna", "Verdi", 50000)

# Ed aggiungerli ad una struttura dati, es. una lista

listaDiImpiegati = []

listaDiImpiegati.append(i)
listaDiImpiegati.append(altroImpiegato)

# Che posso poi scandire, es. con un for, e stampare

for impiegato in listaDiImpiegati:
    print(impiegato.__str__()) # Anche senza __str__()


class Impiegato:
    # Metodo speciale __ che costruisce ed inizializza l'impiegato
    def __init__(self, nome, cognome, paga):
        self._nome = nome
        self._cognome = cognome
        self._paga = paga
        self._dipartimento

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




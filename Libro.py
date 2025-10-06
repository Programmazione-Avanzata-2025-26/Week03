# Nella OOP una regola d'oro è
# quella di "proteggere" gli attibuti
# definendoli privati

# In Python con _ (lasca) o __ (seria)

class Libro:
    def __init__(self):
        self.__titolo = "" # __ Protezione forte (error)
        self.__autore= ""
        self.__numPagine= 0
        self._anno = 0 # Protezione più lasca (warning)

    # Imposta l'anno in maniera controllata
    """
    def impostaAnno(self, anno):
        if anno<0:
            print("Tentativo di imp. anno negativo")
        else:
            self.__anno = anno
    """


    # Restituisce l'anno
    """
    def dammiAnno(self):
        return self.__anno
    """



    @anno.setter
    def anno(self, anno):
        if anno<0:
            print("Tentativo di imp. anno negativo")
        else:
            self._anno = anno

    @property
    def anno(self): # Metodo getter per l'attributo anno
        return self._anno

l1 = Libro()

print(l1.__titolo) # L'attributo non è più accessibile (o quasi)
                   # Python gli cambia nome per rendere
                   # più difficile accedere in lettura/scrittura
                   # al valore

l1._anno = 2008
l1._anno = -500

# l1.__numPagine=-2000

# Come accedere ad un attributo non visibile?

l1.impostaAnno(-500)
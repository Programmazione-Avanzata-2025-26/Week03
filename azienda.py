from dipartimento import Dipartimento
from impiegato import Impiegato

i = Impiegato("Mario", "Rossi", 20000)

#i.stampati()

#print(i.descriviti())

print(i) # Equivalente a print(i.__str__())

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

# Posso anche introdurre il concetto di dipartimento,
# es. ciascuno caratterizzato da un nome: basta
# definire una nuova classe, Dipartimento

# Posso poi costruire un oggetto di quel tipo/quella classe

dipartimentoA = Dipartimento("Risorse umane")

# Come faccio poi a dire/a rappresentare il fatto che
# un impiegato lavori in un determinato dipartimento?

impiegato._dipartimento = dipartimentoA

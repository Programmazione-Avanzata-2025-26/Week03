

class Car:

    # Variabile o attributo di classe
    # Posseduta da ed uguale in tutti gli oggetti di classe Car
    wheels = 4

    """
    def __init__(self): # self è par. obbligatorio
        # Variabili o attributi di istanza
        # Ogni oggetto creato a partire dalla classe Car
        # ne ha una propria copia e i suoi valori possono cambiare
        self.licensePlate = 0 # licensePlate è un attributo (si capisce da self.)
        self.bodyColor = ""
        self.turnedOn = False
    """

    def __init__(self, licensePlate, bodyColor):
        self.licensePlate = licensePlate
        self.bodyColor = bodyColor
        self.turnedOn = False # Posso anche inizializzarlo senza usare parametri


    def paint(self, color): # Riceve come parametro il nuovo colore
        self.bodyColor = color # Assegna color all'attributo self.bodyColor

    def turnOn(self): # Cambia lo stato dell'oggetto Car, mettendo turnedOn a True
        self.turnedOn = True

    def printYourself(self):
        print(self.licensePlate, self.bodyColor, self.turnedOn)

c1 = Car() # Voglio creare un oggetto di tipo Car
           # Python vede le () ed invoca __init__()

c2 = Car()

# Per accedere al contenuto degli oggetti
# si può utilizzare la notazione puntata c1.

# Assegno all'attributo licensePlate di c1 un valore
c1.licensePlate = "AB123CD"

# Poi vi accedo e lo stampo nella console
print(c1.licensePlate)

# Stampo anche licensePlate di c2

print(c2.licensePlate)

# Stampo tutti gli attributi
print(c1.licensePlate, c1.bodyColor, c1.turnedOn)

# Oppure, invoco printYourself()

c1.paint("Green")
c1.turnOn()
c1.printYourself()

# La sintassi sopra è equivalente a ...
Car.printYourself(c1)

c2.paint("Blue")
c2.printYourself()

# Se in un qualunque punto del codice prendo il nome
# di un oggetto e scrivo

c1.hasBeenWashed = True

c1.wheels = 6 # Sto creando un nuovo attributo / variabile di istanza

Car.wheels = 8 # Per accedere alla variabile di classe devo usare Car




class Zimmer:
    def __init__(self, nummer, anzahl, preis, farbe, mehrblick, reservierung):
        self.__nummer = nummer
        self.__anzahl = anzahl
        self.__preis = preis
        self.__farbe = farbe
        self.__mehrblick = mehrblick
        self.__reservierung = reservierung

    def __str__(self):
        return 'Nummer: {} - Anzahl der Gaste: {} - Preis: {} $ - Farbe: {} - Mehrblick: {} - Reservierungen: {}'.format(self.__nummer, self.__anzahl, self.__preis, self.__farbe, self.__mehrblick, self.__reservierung)

    def __repr__(self):
        return 'Nummer: {} - Anzahl der Gaste: {} - Preis: {} $ - Farbe: {} - Mehrblick: {} - Reservierungen: {}'.format(self.__nummer, self.__anzahl, self.__preis, self.__farbe, self.__mehrblick, self.__reservierung)

    # Nummer
    @property
    def nummer(self):
        return self.__nummer

    @nummer.setter
    def nummer(self, nr):
        self.__nummer = nr

    # Anzahl
    @property
    def anzahl(self):
        return self.__anzahl

    @anzahl.setter
    def anzahl(self, a):
        self.__anzahl = a

    # Preis
    @property
    def preis(self):
        return self.__preis

    @preis.setter
    def preis(self, p):
        self.__preis = p

    # Farbe
    @property
    def farbe(self):
        return self.__farbe

    @farbe.setter
    def farbe(self, f):
        self.__farbe = f

    # Mehrblick
    @property
    def mehrblick(self):
        return self.__mehrblick

    @mehrblick.setter
    def mehrblick(self, m):     # m = ["Ja", "Nein"]
        self.__mehrblick = m

    # Reservierungen
    @property
    def reservierungen(self):
        return self.__reservierung

    @reservierungen.setter
    def reservierungen(self, r):
        self.__reservierung = r

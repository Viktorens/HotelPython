class Gast:
    def __init__(self, vorname, nachname, reservierung):
        self.__vorname = vorname
        self.__nachname = nachname
        self.__reservierung = reservierung

    def __str__(self):
        return 'Vorname: {} - Nachname: {} - Reservierte Zimmer: {}'.format(self.__vorname, self.__nachname, self.__reservierung)

    def __repr__(self):
        return 'Vorname: {} - Nachname: {} - Reservierte Zimmer: {}'.format(self.__vorname, self.__nachname, self.__reservierung)

    # Vorname
    @property
    def vorname(self):
        return self.__vorname

    @vorname.setter
    def vorname(self, v):
        self.__vorname = v

    # Nachname
    @property
    def nachname(self):
        return self.__nachname

    @nachname.setter
    def nachname(self, n):
        self.__nachname = n

    # Reservierungen
    @property
    def reservierungen(self):
        return self.__reservierung

    @reservierungen.setter
    def reservierungen(self, r):
        self.__reservierung = r

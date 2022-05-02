class Reservierung:
    def __init__(self, anzahl, zimmer, zeitraum):
        self.__anzahl = anzahl
        self.__zimmer = zimmer
        self.__zeitraum = zeitraum

    def __str__(self):
        return 'Gaeste: {} - Zimmer: {} - Zeitraum: {}'.format(self.__anzahl, self.__zimmer, self.__zeitraum)

    def __repr__(self):
        return 'Gaeste: {} - Zimmer: {} - Zeitraum: {}'.format(self.__anzahl, self.__zimmer, self.__zeitraum)

    # Anzahl der Gaeste
    @property
    def anzahl(self):
        return self.__anzahl

    @anzahl.setter
    def anzahl(self, a):
        self.__anzahl = a

    # Zimmer
    @property
    def zimmer(self):
        return self.__zimmer

    @zimmer.setter
    def zimmer(self, z):
        self.__zimmer = z

    # Zeitraum
    @property
    def zeitraum(self):
        return self.__zeitraum

    @zeitraum.setter
    def zeitraum(self, zr):
        self.__zeitraum = zr

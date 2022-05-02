class controller_zimmer:
    def __init__(self, repo_zimmer):
        self.__repo_zimmer = repo_zimmer

    def add(self, zimmer):
        self.__repo_zimmer.add_zimmer(zimmer)

    def change(self, nummer, preis):
        self.__repo_zimmer.change_preis(nummer, preis)

    def delete(self, nummer):
        self.__repo_zimmer.delete_zimmer(nummer)

    def print(self):
        self.__repo_zimmer.print_zimmer()

    def anzahl(self, nr):
        self.__repo_zimmer.anzahl_print(nr)

    def filter(self, preis, mehrblick):
        self.__repo_zimmer.filter_zimmer(preis, mehrblick)

    def frei(self):
        self.__repo_zimmer.freie_zimmern()

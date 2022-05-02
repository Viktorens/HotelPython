class controller_reservierung:
    def __init__(self, repo_reservierung):
        self.__repo_reservierung = repo_reservierung

    def add(self, v_name, n_name, wahl, nacht, nr):
        self.__repo_reservierung.add_reservierung(v_name, n_name, wahl, nacht, nr)

    def print(self):
        self.__repo_reservierung.print_reserv()

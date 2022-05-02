class controller_gast:
    def __init__(self, repo_gast):
        self.__repo_gast = repo_gast

    def add(self, gast):
        self.__repo_gast.add_gast(gast)

    def change_name(self, gast):
        self.__repo_gast.change_name(gast)

    def delete(self, gast):
        self.__repo_gast.delete_gast(gast)

    def print(self):
        self.__repo_gast.print_gast()

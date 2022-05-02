from Repository.repository_gast import repository_gast
from Repository.repository_zimmer import repository_zimmer
from Repository.repository_reservierung import repository_reservierung
from Controller.controller_gast import controller_gast
from Controller.controller_zimmer import controller_zimmer
from Controller.controller_reservierung import controller_reservierung
from UI.ui_menu import *
from tkinter import *


def main():
    # Gast
    repo_gast = repository_gast()
    control_gast = controller_gast(repo_gast)

    # Zimmer
    repo_zimmer = repository_zimmer()
    control_zimmer = controller_zimmer(repo_zimmer)

    # Reservierung
    repo_reservierung = repository_reservierung()
    control_reservierung = controller_reservierung(repo_reservierung)

    # App
    root = Tk()
    app = menu_GUI(root, control_gast, control_zimmer, control_reservierung)
    app.draw_window()
    messagebox._show('Warning', 'Our App is still in early acces. Please report any bugs on the bug tracker. Thank you!', icon='warning')
    root.mainloop()


main()

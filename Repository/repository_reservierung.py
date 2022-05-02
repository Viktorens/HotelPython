from Entities.Reservierung import Reservierung
from Entities.Gast import Gast
from Repository.repository_gast import repository_gast
from Repository.repository_zimmer import repository_zimmer
from Controller.controller_gast import controller_gast
from Controller.controller_zimmer import controller_zimmer
from UI.ui_errors import *
from UI.ui_confirmation import *
from UI.ui_reservierungen import print_liste_anzahl
from Testing.testing import *
from datetime import datetime, timedelta


# Gast
repo_gast = repository_gast()
control_gast = controller_gast(repo_gast)
# Zimmer
repo_zimmer = repository_zimmer()
control_zimmer = controller_zimmer(repo_zimmer)


class repository_reservierung:
    def __init__(self, file='reservierungen.txt'):
        self.__fName = file
        self.__liste = []
        self.__loadFromFile()

    # Load from File
    def __loadFromFile(self):
        self.__liste = []
        f = open(self.__fName, 'r')
        for line in f:
            data = line.strip().split(' ')
            try:
                reservierung = Reservierung(int(data[1]), int(data[4]), 'Von ' + data[8] + ' bis ' + data[10])
                self.__liste.append(reservierung)
            except ValueError:
                invalid_datei_reservierungen()

    # Store to File
    def __storeToFile(self):
        f = open(self.__fName, 'w')
        for el in self.__liste:
            f.write(str(el) + '\n')
        f.close()

    @property
    def liste(self):
        return self.__liste

    # Add a reservation to the list
    def add_reservierung(self, v_name, n_name, wahl, nacht, nr):

        # Check name if already exists in database
        try:
            vorname = v_name
            assert gast_name(vorname) is True
        except AssertionError:
            return invalid_vornanme(vorname)

        try:
            nachname = n_name
            assert gast_name(nachname) is True
        except AssertionError:
            return invalid_nachnanme(nachname)

        else:
            # gast = Gast(vorname, nachname, 0)
            if repo_gast.check_name(Gast(vorname, nachname, 0)) is False:
                control_gast.add(Gast(vorname, nachname, 0))
            else:
                try:
                    assert repo_gast.check_for_reservations(vorname, nachname) is False
                except AssertionError:
                    return hat_reservierung(vorname, nachname)

        # Check if number of room is correct
        nr_anzahl, rooms_check = repo_zimmer.anzahl(nr)
        try:
            if int(wahl) not in rooms_check:
                return wrong_anzahl()
        except ValueError:
            return not_number(wahl)
        else:
            nummer = int(wahl)

        # Calculate number of days
        try:
            tagen = int(nacht)
        except ValueError:
            return not_number(nacht)
        else:
            zeitraum = datetime.now() + timedelta(tagen)
            z = zeitraum.strftime('%d-%B-%Y')
            successful_reservation(v_name, n_name, z)

        # Make the reservation
        zeit = zeitraum.strftime('%d-%B-%Y')
        zeitraum_print = 'Von ' + datetime.today().strftime('%d-%B-%Y') + ' bis ' + zeit
        repo_zimmer.add_reserv(nummer)
        reservierung = Reservierung(nr_anzahl, nummer, zeitraum_print)
        repo_gast.add_reserv(vorname, nachname, nummer)
        self.__liste.append(reservierung)
        self.__storeToFile()

    # Show all reservations
    def print_reserv(self):
        self.__loadFromFile()
        print_elements = ('\n'.join(map(str, self.__liste)))
        print_liste_anzahl(print_elements)

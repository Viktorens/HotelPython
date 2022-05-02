from UI.ui_zimmer import *
from UI.ui_errors import *
from UI.ui_confirmation import *
from Entities.Zimmer import Zimmer
from Testing.testing import *
from datetime import datetime


class repository_zimmer:
    def __init__(self, file='zimmern.txt'):
        self.__fName = file
        self.__liste = []
        self.__loadFromFile()

    def __loadFromFile(self):
        self.__liste = []
        f = open(self.__fName, 'r')
        for line in f:
            data = line.strip().split(' ')
            try:
                zimmer = Zimmer(int(data[1]), int(data[6]), int(data[9]), data[13], data[16], int(data[19]))
                self.__liste.append(zimmer)
            except ValueError:
                invalid_datei_zimmer()

    def __storeToFile(self):
        f = open(self.__fName, 'w')
        for el in self.__liste:
            f.write(str(el) + '\n')
        f.close()

    @property
    def liste(self):
        return self.__liste

    @liste.setter
    def liste(self, liste):
        self.__liste = liste

    # Add room
    def add_zimmer(self, zimmer):
        # Nummer
        try:
            for el in range(len(self.__liste)):
                if int(zimmer.nummer) == self.__liste[el].nummer:
                    return already_room(zimmer.nummer)
            nummer = zimmer.nummer
            int(nummer)
        except ValueError:
            return not_number(zimmer.nummer)

        # Anzahl
        try:
            anzahl = zimmer.anzahl
            int(anzahl)
        except ValueError:
            return not_number(anzahl)

        # Preis
        try:
            preis = zimmer.preis
            int(preis)
        except ValueError:
            return not_number(preis)

        # Farbe
        try:
            farbe = zimmer.farbe
            assert zimmer_farbe(farbe) is True
        except AssertionError:
            return invalid_color(farbe)

        # Mehrblick
        mehrblick = zimmer.mehrblick
        zimmer = Zimmer(nummer, anzahl, preis, farbe, mehrblick, 0)
        return self.__liste.append(zimmer), self.__storeToFile(), confirmation_add(zimmer.nummer)

    # Change room price
    def change_preis(self, nr, pr):
        try:
            nummer = int(nr)
            if nummer > len(self.__liste):
                return room_not_found(nr)

            for el in range(len(self.__liste)):
                if nummer == self.__liste[el].nummer:
                    try:
                        preis = int(pr)
                        self.__liste[el].preis = preis
                        self.__storeToFile()
                        confirmation_change(nummer, preis)
                    except ValueError:
                        return not_number(pr)

        except ValueError:
            return not_number(nr)

    # Delete room
    def delete_zimmer(self, nr):
        try:
            nummer = int(nr)
            el = 0
            ok = 0
            while el < len(self.__liste):
                if nummer == self.__liste[el].nummer:
                    self.__liste.pop(el)
                    ok = ok + 1
                    self.__storeToFile()
                    delete_room_confirmation(nummer)
                else:
                    el = el + 1
            if ok == 0:
                room_not_found(nummer)
        except ValueError:
            return not_number(nr)

    # Show all rooms
    def print_zimmer(self):
        self.__loadFromFile()
        print_elements = ('\n'.join(map(str, self.__liste)))
        print_liste(print_elements)

    # Check if room with number of guest exists (Reservierung)
    def anzahl_print(self, nr):
        self.__loadFromFile()
        try:
            anzahl = int(nr)
            ok = 0
            rooms_check = []
            rooms = []
            for i in range(len(self.__liste)):
                if self.__liste[i].anzahl >= anzahl and self.__liste[i].reservierungen == 0:
                    ok = ok + 1
                    rooms.append(self.__liste[i])
                    rooms_check.append(self.__liste[i].nummer)
            if ok == 0:
                return wrong_anzahl()
        except ValueError:
            return not_number(nr)
        else:
            print_elements = ('\n'.join(map(str, rooms)))
            print_liste(print_elements)
            return anzahl, rooms_check

    def anzahl(self, nr):
        self.__loadFromFile()
        try:
            anzahl = int(nr)
            ok = 0
            rooms_check = []
            rooms = []
            for i in range(len(self.__liste)):
                if self.__liste[i].anzahl >= anzahl and self.__liste[i].reservierungen == 0:
                    ok = ok + 1
                    rooms.append(self.__liste[i])
                    rooms_check.append(self.__liste[i].nummer)
            if ok == 0:
                return wrong_anzahl()
        except ValueError:
            return not_number(nr)
        else:
            return anzahl, rooms_check

    # Shows that a room is occupied (Reservierungen)
    def add_reserv(self, nummer):
        for el in range(len(self.__liste)):
            if nummer == int(self.__liste[el].nummer):
                self.__liste[el].reservierungen = 1
                self.__storeToFile()

    # Filter Price (Reservierung)
    def filter_zimmer(self, preis, mehr):
        self.__loadFromFile()
        preis_room = []
        try:
            end = int(preis)
            mehrblick = mehr
            ok = 0
            for i in range(len(self.__liste)):
                if int(self.__liste[i].preis) <= end and mehrblick in self.__liste[i].mehrblick and self.__liste[i].reservierungen == 0:
                    ok = ok + 1
                    preis_room.append(self.__liste[i])
            if ok == 0:
                return preis_not_found()

            print_elements = ('\n'.join(map(str, preis_room)))
            print_liste_preis(print_elements)
        except ValueError:
            return not_number(preis)

    # Show which rooms are free today
    def freie_zimmern(self):
        self.__loadFromFile()
        # self.__storeToFile()
        frei = [datetime.today().strftime('%d-%B-%Y')]
        for el in range(len(self.__liste)):
            if self.__liste[el].reservierungen == 0:
                frei.append(self.__liste[el])
        print_elements = ('\n'.join(map(str, frei)))
        print_liste(print_elements)

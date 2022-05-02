from tkinter import messagebox


# Gast
def new_gast_welcome(vorname, nachname):
    messagebox.showinfo('Done', 'Hallo %s %s. Du bist regiestriert' % (vorname, nachname))


def change_name_confirmation(vorname, nachname):
    messagebox.showinfo('Done', 'Name wurde aktualisiert zum: %s %s' % (vorname, nachname))


def delete_name_confirmation(vorname, nachname):
    messagebox.showinfo('Done', '%s %s wurde aus unsere Datein gelöscht' % (vorname, nachname))


# Zimmer
def confirmation_add(nummer):
    messagebox.showinfo('Done', 'Das Zimmer mit dem Nummer: %s wurde regiestriert' % nummer)


def confirmation_change(nummer, preis):
    messagebox.showinfo('Done', 'Das Zimmer mit dem Nummer: %s hat den neuen Preis: %s $' % (nummer, preis))


def delete_room_confirmation(nummer):
    messagebox.showinfo('Done', '%s wurde aus unsere Datein gelöscht' % nummer)


# Reservation
def successful_reservation(vorname, nachname, zeit):
    messagebox.showinfo('Done', 'Fertig %s %s. Sie haben Ihre Reservierung bis am %s gemacht!' % (vorname, nachname, zeit))

from tkinter import *
from tkinter import messagebox
from datetime import datetime
import sys
import os


class reservierungen_GUI:
    def __init__(self, gui_master, gast, controller_zimmer, controller_reservierungen):
        self.__window = gui_master
        self.__gast = gast
        self.__controller_zimmer = controller_zimmer
        self.__controller_reservierungen = controller_reservierungen

        self.__window.resizable(0, 0)
        self.__window.protocol("WM_DELETE_WINDOW", exit_app)

        self.__vorname_txt = Entry(self.__window, width=10, bg=theme()[2], foreground='black')
        self.__nachname_txt = Entry(self.__window, width=10, bg=theme()[2], foreground='black')
        self.__anzahl_gaste_txt = Entry(self.__window, width=10, bg=theme()[2], foreground='black')
        self.__wahl_txt = Entry(self.__window, width=10, bg=theme()[2], foreground='black')
        self.__anzahl_nacht_txt = Entry(self.__window, width=10, bg=theme()[2], foreground='black')
        self.__preis_txt = Entry(self.__window, width=10, bg=theme()[2], foreground='black')
        self.__mehrblick = "NA"

    def draw_window(self):
        w = 525  # width for the window
        h = 300  # height for the window
        # get screen width and height
        ws = self.__window.winfo_screenwidth()  # width of the screen
        hs = self.__window.winfo_screenheight()  # height of the screen
        # calculate x and y coordinates for the Tk root window
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        self.__window.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.__window.title("Menu Reservierungen")
        self.__window.config(bg=theme()[0])

        # UI
        intro = Label(self.__window, text='- MENU RESERVIERUNGEN -', font='Arial 10', bg=theme()[0], foreground=theme()[1])
        intro.place(relx=0.5, rely=0.0, anchor=N)

        hotel_name = Label(self.__window, text='© Gamma Deluxe Resort 2021', font='Courier 8', bg=theme()[0], foreground=theme()[1])
        hotel_name.place(relx=1.0, rely=1.0, anchor=SE)

        anzahl = Label(self.__window, text='Anzahl der Gäste', bg=theme()[0], foreground=theme()[1])
        anzahl.place(relx=0.17, rely=0.15, anchor=W)
        self.__anzahl_gaste_txt.place(relx=0.45, rely=0.12, anchor=N)

        btn1 = Button(self.__window, text='Suche Zimmer', font='Arial 10', width=12, relief=RAISED, bg='gray', activebackground='gray', activeforeground='white', command=self.__anzahl_gaste)
        btn1.place(relx=0.7, rely=0.105, anchor=N)

        vorname = Label(self.__window, text='Vorname', bg=theme()[0], foreground=theme()[1])
        vorname.place(relx=0.07, rely=0.295, anchor=W)
        self.__vorname_txt.place(relx=0.28, rely=0.27, anchor=N)

        nachname = Label(self.__window, text='Nachname', bg=theme()[0], foreground=theme()[1])
        nachname.place(relx=0.07, rely=0.395, anchor=W)
        self.__nachname_txt.place(relx=0.28, rely=0.37, anchor=N)

        wahl_1 = Label(self.__window, text='Nummer der ausgewählte Zimmer', bg=theme()[0], foreground=theme()[1])
        wahl_1.place(relx=0.75, rely=0.275, anchor=E)
        wahl_2 = Label(self.__window, text='aus der Liste', bg=theme()[0], foreground=theme()[1])
        wahl_2.place(relx=0.75, rely=0.33, anchor=E)
        self.__wahl_txt.place(relx=0.84, rely=0.27, anchor=N)

        nacht = Label(self.__window, text='Anazhl der Nächte', bg=theme()[0], foreground=theme()[1])
        nacht.place(relx=0.75, rely=0.4, anchor=E)
        self.__anzahl_nacht_txt.place(relx=0.84, rely=0.37, anchor=N)

        btn2 = Button(self.__window, text='Mach den Reservierung', font='Arial 10', width=17, relief=RAISED, bg='gray', activebackground='gray', activeforeground='white', command=self.__make_a_reservation)
        btn2.place(relx=0.5, rely=0.51, anchor=CENTER)

        btn3 = Button(self.__window, text='Zimmer die ' + datetime.today().strftime('%d %B %Y') + ' frei sind', font='Arial 10', width=29, relief=RAISED, bg='gray', activebackground='gray', activeforeground='white', command=self.__free_rooms_today)
        btn3.place(relx=0.275, rely=0.61, anchor=CENTER)

        btn4 = Button(self.__window, text='Zeige die Liste von Reservierungen', font='Arial 10', width=29, relief=RAISED, bg='gray', activebackground='gray', activeforeground='white', command=self.__print_list)
        btn4.place(relx=0.735, rely=0.61, anchor=CENTER)

        preis = Label(self.__window, text='Preis', bg=theme()[0], foreground=theme()[1])
        preis.place(relx=0.07, rely=0.75, anchor=W)
        self.__preis_txt.place(relx=0.22, rely=0.72, anchor=N)

        mehrblick = Label(self.__window, text='Mehrblick', bg=theme()[0], foreground=theme()[1])
        mehrblick.place(relx=0.35, rely=0.75, anchor=W)

        i = StringVar()
        ja_rbtn = Radiobutton(self.__window, text='Ja', value=0, variable=i, command=self.setJa, bg=theme()[0], foreground='black', activebackground=theme()[0], activeforeground=theme()[1])
        nein_rbtn = Radiobutton(self.__window, text='Nein', value=1, variable=i, command=self.setNein, bg=theme()[0], foreground='black', activebackground=theme()[0], activeforeground=theme()[1])
        ja_rbtn.place(relx=0.475, rely=0.72, anchor=W)
        nein_rbtn.place(relx=0.475, rely=0.79, anchor=W)

        btn5 = Button(self.__window, text='Filtern nach Preis und Mehrblick', font='Arial 10', width=23, relief=RAISED, bg='gray', activebackground='gray', activeforeground='white', command=self.__filter)
        btn5.place(relx=0.5955, rely=0.755, anchor=W)

        btn_return = Button(self.__window, text='<', font='Arial 10', width=2, relief=RAISED, bg='gray', activebackground='gray', activeforeground='white', command=self.__return)
        btn_return.place(relx=0.0, rely=0.4, anchor=W)

        # Menu bar
        menubar = Menu(self.__window)
        # View
        view_btn = Menu(self.__window, tearoff=0, bg=theme()[0], foreground=theme()[1], activebackground='gray')
        view_btn.add_command(label='Light Mode', command=light_theme)
        view_btn.add_command(label='Dark Mode', command=dark_theme)
        # Help
        help_btn = Menu(self.__window, tearoff=0, bg=theme()[0], foreground=theme()[1], activebackground='gray')
        help_btn.add_command(label='FAQ')
        help_btn.add_command(label='Contact us')
        help_btn.add_command(label='Licenses')
        help_btn.add_command(label='Terms and Privacy Policy')
        help_btn.add_separator()
        help_btn.add_command(label='Version 0.1.0')
        help_btn.add_separator()
        help_btn.add_command(label='Report bugs')
        menubar.add_cascade(label='View', menu=view_btn)
        menubar.add_cascade(label='Help', menu=help_btn)
        self.__window.config(menu=menubar)

    # Commands for buttons
    # Anzahl der Gaste Button
    def __anzahl_gaste(self):
        self.__controller_zimmer.anzahl(self.__anzahl_gaste_txt.get())

    # Make a reservation Button
    def __make_a_reservation(self):
        self.__controller_reservierungen.add(self.__vorname_txt.get(), self.__nachname_txt.get(), self.__wahl_txt.get(), self.__anzahl_nacht_txt.get(), self.__anzahl_gaste_txt.get())

        # clear textboxes
        self.__vorname_txt.delete(0, 'end')
        self.__nachname_txt.delete(0, 'end')
        self.__anzahl_gaste_txt.delete(0, 'end')
        self.__wahl_txt.delete(0, 'end')
        self.__anzahl_nacht_txt.delete(0, 'end')

    # Free rooms Button
    def __free_rooms_today(self):
        self.__controller_zimmer.frei()

    # Filter price Button
    def __filter(self):
        self.__controller_zimmer.filter(self.__preis_txt.get(), self.__mehrblick)

        # clear textboxes
        self.__preis_txt.delete(0, 'end')

    def setJa(self):
        self.__mehrblick = "Ja"  # sets Mehrblick to Ja

    def setNein(self):
        self.__mehrblick = "Nein"  # sets Mehrblick to Nein

    # Print Liste Button
    def __print_list(self):
        self.__controller_reservierungen.print()

    # Return Button
    def __return(self):
        from UI.ui_menu import menu_GUI
        self.__window.destroy()
        self.__window = Tk()
        self.menu = menu_GUI(self.__window, self.__gast, self.__controller_zimmer, self.__controller_reservierungen)
        self.menu.draw_window()
        self.__window.mainloop()


# Print elements in new window
def print_liste_anzahl(print_elements):
    print_window = Tk()
    w = 525  # width for the window
    h = 300  # height for the window

    # get screen width and height
    ws = print_window.winfo_screenwidth()  # width of the screen
    hs = print_window.winfo_screenheight()  # height of the screen

    # calculate x and y coordinates for the Tk root window
    x = (ws / 2) + ((w + 10) / 2)
    y = (hs / 2) - ((h - 20) / 2)
    print_window.geometry('%dx%d+%d+%d' % (w, h, x, y))
    print_window.title('Liste von Reservierungen')

    # TextBox
    text = Text(print_window)
    text.insert(INSERT, print_elements)
    text.tag_add("here", "1.0", "end")
    text.tag_config('here', font='Courier 8')
    text.pack()


# Checks settings for mode
def theme_checker():
    color = []
    file = open('config.xml', 'r')
    for i, line in enumerate(file):
        if i == 2:
            data = line.strip().split(' ')
            theme_color = data[2]
            color.append(theme_color)
    return color


# Theme chooser, storing in the config file
def light_theme():
    if theme_checker()[0] == 'dark':
        msg = messagebox.askquestion('Warning', 'Please restart the app in order to see the changes.' '\n' 'Any unsaved data will be lost! Do you want to continue?', icon='warning')
        if msg == 'yes':
            a_file = open("config.xml", "r")
            list_of_lines = a_file.readlines()
            list_of_lines[2] = "    theme = light\n"

            a_file = open("config.xml", "w")
            a_file.writelines(list_of_lines)
            a_file.close()
            python = sys.executable
            os.execl(python, python, *sys.argv)


def dark_theme():
    if theme_checker()[0] == 'light':
        msg = messagebox.askquestion('Warning', 'Please restart the app in order to see the changes.' '\n' 'Any unsaved data will be lost! Do you want to continue?', icon='warning')
        if msg == 'yes':
            a_file = open("config.xml", "r")
            list_of_lines = a_file.readlines()
            list_of_lines[2] = "    theme = dark\n"

            a_file = open("config.xml", "w")
            a_file.writelines(list_of_lines)
            a_file.close()
            python = sys.executable
            os.execl(python, python, *sys.argv)


# Setting the right color for background, foreground, etc
def theme():
    # Light
    light_bg = '#eeeeee'
    light_forebg = '#323031'
    light_boxes = 'white'
    # Dark
    dark_bg = '#323031'
    dark_forebg = '#eeeeee'
    dark_boxes = 'dark gray'
    if theme_checker()[0] == 'light':
        return light_bg, light_forebg, light_boxes
    elif theme_checker()[0] == 'dark':
        return dark_bg, dark_forebg, dark_boxes


# Exit App
def exit_app():
    msg = messagebox.askquestion('Exit', 'Do you want to exit the application?', icon='warning')
    if msg == 'yes': quit()

from tkinter import *
from tkinter import messagebox
from Entities.Zimmer import Zimmer
import sys
import os


class zimmer_GUI:
    def __init__(self, gui_master, gast, controller, reservierungen):
        self.__window = gui_master
        self.__gast = gast
        self.__controller = controller
        self.__reservierungen = reservierungen

        self.__window.resizable(0, 0)
        self.__window.protocol("WM_DELETE_WINDOW", exit_app)

        self.__nummer_txt = Entry(self.__window, width=10, bg=theme()[2], foreground='black')
        self.__anzahl_txt = Entry(self.__window, width=10, bg=theme()[2], foreground='black')
        self.__preis_txt = Entry(self.__window, width=10, bg=theme()[2], foreground='black')
        self.__farbe_txt = Entry(self.__window, width=10, bg=theme()[2], foreground='black')
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
        self.__window.title("Menu Zimmer")
        self.__window.config(bg=theme()[0])

        # UI
        intro = Label(self.__window, text='- MENU ZIMMER -', font='Arial 10', bg=theme()[0], foreground=theme()[1])
        intro.place(relx=0.5, rely=0.0, anchor=N)

        hotel_name = Label(self.__window, text='© Gamma Deluxe Resort 2021', font='Courier 8', bg=theme()[0], foreground=theme()[1])
        hotel_name.place(relx=1.0, rely=1.0, anchor=SE)

        nummer = Label(self.__window, text='Nummer', bg=theme()[0], foreground=theme()[1])
        nummer.place(relx=0.07, rely=0.15, anchor=W)
        self.__nummer_txt.place(relx=0.32, rely=0.12, anchor=N)

        anzahl = Label(self.__window, text='Anzahl der Gäste', bg=theme()[0], foreground=theme()[1])
        anzahl.place(relx=0.07, rely=0.25, anchor=W)
        self.__anzahl_txt.place(relx=0.32, rely=0.22, anchor=N)

        preis = Label(self.__window, text='Preis', bg=theme()[0], foreground=theme()[1])
        preis.place(relx=0.425, rely=0.15, anchor=W)
        self.__preis_txt.place(relx=0.57, rely=0.12, anchor=N)

        farbe = Label(self.__window, text='Farbe', bg=theme()[0], foreground=theme()[1])
        farbe.place(relx=0.425, rely=0.25, anchor=W)
        self.__farbe_txt.place(relx=0.57, rely=0.22, anchor=N)

        mehrblick = Label(self.__window, text='Mehrblick', bg=theme()[0], foreground=theme()[1])
        mehrblick.place(relx=0.82, rely=0.2, anchor=E)

        i = StringVar()
        ja_rbtn = Radiobutton(self.__window, text='Ja', value=0, variable=i, command=self.setJa, bg=theme()[0], foreground='black', activebackground=theme()[0], activeforeground=theme()[1])
        nein_rbtn = Radiobutton(self.__window, text='Nein', value=1, variable=i, command=self.setNein, bg=theme()[0], foreground='black', activebackground=theme()[0], activeforeground=theme()[1])
        ja_rbtn.place(relx=0.9, rely=0.15, anchor=E)
        nein_rbtn.place(relx=0.93, rely=0.25, anchor=E)

        btn1 = Button(self.__window, text='Füge eine neue Zimmer', font='Arial 10', width=30, relief=RAISED, bg='gray', activebackground='gray', activeforeground='white', command=self.__add_zimmer)
        btn1.place(relx=0.5, rely=0.425, anchor=CENTER)

        btn2 = Button(self.__window, text='Aktualisierung des Preises einer Zimmer', font='Arial 10', width=30, relief=RAISED, bg='gray', activebackground='gray', activeforeground='white', command=self.__change_price)
        btn2.place(relx=0.5, rely=0.525, anchor=CENTER)

        btn3 = Button(self.__window, text='Lösche ein Zimmer', font='Arial 10', width=30, relief=RAISED, bg='gray', activebackground='gray', activeforeground='white', command=self.__delete_name)
        btn3.place(relx=0.5, rely=0.625, anchor=CENTER)

        btn4 = Button(self.__window, text='Zeige alle Zimmern', font='Arial 10', width=30, relief=RAISED, bg='gray', activebackground='gray', activeforeground='white', command=self.__print_list)
        btn4.place(relx=0.5, rely=0.725, anchor=CENTER)

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
    # Add room Button
    def __add_zimmer(self):
        zimmer = Zimmer(self.__nummer_txt.get(), self.__anzahl_txt.get(), self.__preis_txt.get(), self.__farbe_txt.get(), self.__mehrblick, 0)
        self.__controller.add(zimmer)

        # clear textboxes
        self.__nummer_txt.delete(0, 'end')
        self.__anzahl_txt.delete(0, 'end')
        self.__preis_txt.delete(0, 'end')
        self.__farbe_txt.delete(0, 'end')

    def setJa(self):
        self.__mehrblick = "Ja"  # sets Mehrblick to Ja

    def setNein(self):
        self.__mehrblick = "Nein"  # sets Mehrblick to Nein

    # Change price Button
    def __change_price(self):
        self.__controller.change(self.__nummer_txt.get(), self.__preis_txt.get())

        # clear textboxes
        self.__nummer_txt.delete(0, 'end')
        self.__preis_txt.delete(0, 'end')

    # Delete name Button
    def __delete_name(self):
        self.__controller.delete(self.__nummer_txt.get())

        # clear textboxes
        self.__nummer_txt.delete(0, 'end')
        self.__preis_txt.delete(0, 'end')

    # Print Liste Button
    def __print_list(self):
        self.__controller.print()

    # Return Button
    def __return(self):
        from UI.ui_menu import menu_GUI
        self.__window.destroy()
        self.__window = Tk()
        self.menu = menu_GUI(self.__window, self.__gast, self.__controller, self.__reservierungen)
        self.menu.draw_window()
        self.__window.mainloop()


# Print elements in new window
def print_liste(print_elements):
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
    print_window.title('Liste von Zimmern')

    # TextBox
    text = Text(print_window)
    text.insert(INSERT, print_elements)
    text.tag_add("here", "1.0", "end")
    text.tag_config('here', font='Courier 8')
    text.pack()


# Print elements from filter in new window
def print_liste_preis(print_elements):
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
    print_window.title('Filter nach Preis und Mehrblick')

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

from tkinter import *
from tkinter import messagebox
from Entities.Gast import Gast
import sys
import os


class gast_GUI:
    def __init__(self, gui_master, controller, zimmer, reservierungen):
        self.__window = gui_master
        self.__controller = controller
        self.__zimmer = zimmer
        self.__reservierungen = reservierungen

        self.__window.resizable(0, 0)
        self.__window.protocol("WM_DELETE_WINDOW", exit_app)

        self.__vorname_txt = Entry(self.__window, width=25, bg=theme()[2], foreground='black')
        self.__nachname_txt = Entry(self.__window, width=25, bg=theme()[2], foreground='black')

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
        self.__window.title("Menu Gast")
        self.__window.config(bg=theme()[0])

        # UI
        intro = Label(self.__window, text='- MENU GAST -', font='Arial 10', bg=theme()[0], foreground=theme()[1])
        intro.place(relx=0.5, rely=0.0, anchor=N)

        hotel_name = Label(self.__window, text='© Gamma Deluxe Resort 2021', font='Courier 8', bg=theme()[0], foreground=theme()[1])
        hotel_name.place(relx=1.0, rely=1.0, anchor=SE)

        vorname = Label(self.__window, text='Vorname', bg=theme()[0], foreground=theme()[1])
        vorname.place(relx=0.2, rely=0.15, anchor=W)
        self.__vorname_txt.place(relx=0.5, rely=0.12, anchor=N)

        nachname = Label(self.__window, text='Nachname', bg=theme()[0], foreground=theme()[1])
        nachname.place(relx=0.2, rely=0.25, anchor=W)
        self.__nachname_txt.place(relx=0.5, rely=0.22, anchor=N)

        btn1 = Button(self.__window, text='Füge ein neuen Gast', font='Arial 10', width=21, relief=RAISED, bg='gray', activebackground='gray', activeforeground='white', command=self.__add_gast)
        btn1.place(relx=0.5, rely=0.38, anchor=N)

        btn2 = Button(self.__window, text='Aktualisierung der Name', font='Arial 10', width=21, relief=RAISED, bg='gray', activebackground='gray', activeforeground='white', command=self.__change_name)
        btn2.place(relx=0.5, rely=0.48, anchor=N)

        btn3 = Button(self.__window, text='Lösche ein Gast', font='Arial 10', width=21, relief=RAISED, bg='gray', activebackground='gray', activeforeground='white', command=self.__delete_name)
        btn3.place(relx=0.5, rely=0.58, anchor=N)

        btn4 = Button(self.__window, text='Zeige alle Gäste', font='Arial 10', width=21, relief=RAISED, bg='gray', activebackground='gray', activeforeground='white', command=self.__print_list)
        btn4.place(relx=0.5, rely=0.68, anchor=N)

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
    # Add name Button
    def __add_gast(self):
        gast = Gast(self.__vorname_txt.get(), self.__nachname_txt.get(), 0)
        self.__controller.add(gast)

        # clear textboxes
        self.__vorname_txt.delete(0, 'end')
        self.__nachname_txt.delete(0, 'end')

    # Change name Button
    def __change_name(self):
        gast = Gast(self.__vorname_txt.get(), self.__nachname_txt.get(), 0)
        self.__controller.change_name(gast)

        # clear textboxes
        self.__vorname_txt.delete(0, 'end')
        self.__nachname_txt.delete(0, 'end')

    # Delete name Button
    def __delete_name(self):
        gast = Gast(self.__vorname_txt.get(), self.__nachname_txt.get(), 0)
        self.__controller.delete(gast)

        # clear textboxes
        self.__vorname_txt.delete(0, 'end')
        self.__nachname_txt.delete(0, 'end')

    # Print Liste Button
    def __print_list(self):
        self.__controller.print()

    # Return Button
    def __return(self):
        from UI.ui_menu import menu_GUI
        self.__window.destroy()
        self.__window = Tk()
        self.menu = menu_GUI(self.__window, self.__controller, self.__zimmer, self.__reservierungen)
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
    print_window.title('Liste von Gäste')

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

from tkinter import *
from tkinter import messagebox
from UI.ui_gast import gast_GUI
from UI.ui_zimmer import zimmer_GUI
from UI.ui_reservierungen import reservierungen_GUI
import sys
import os


class menu_GUI:
    def __init__(self, gui_master, controller_gast, controller_zimmer, controller_reservierungen):
        self.__window = gui_master
        self.__controller_gast = controller_gast
        self.__controller_zimmer = controller_zimmer
        self.__controller_reservierungen = controller_reservierungen

        self.__window.resizable(0, 0)
        self.__window.protocol("WM_DELETE_WINDOW", exit_app)

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
        self.__window.title("Hotel")
        self.__window.config(bg=theme()[0])

        # UI
        intro = Label(self.__window, text='Herzliche Willkommen bei Gamma Deluxe Resort!', font='Arial 12', bg=theme()[0], foreground=theme()[1])
        intro.place(relx=0.5, rely=0.1, anchor=CENTER)

        hotel_name = Label(self.__window, text='© Gamma Deluxe Resort 2021', font='Courier 8', bg=theme()[0], foreground=theme()[1])
        hotel_name.place(relx=1.0, rely=1.0, anchor=SE)

        version = Label(self.__window, text='Made by the best FP team :)', font='Courier 8', bg=theme()[0], foreground=theme()[1])
        version.place(relx=0.0, rely=1.0, anchor=SW)

        btn_gast = Button(self.__window, text='Gäste', font='Arial 10', width=12, relief=RAISED, bg='gray', activebackground='gray', activeforeground='white', command=self.__menu_gast)
        btn_gast.place(relx=0.5, rely=0.3, anchor=CENTER)

        btn_zimmer = Button(self.__window, text='Zimmern', font='Arial 10', width=12, relief=RAISED, bg='gray', activebackground='gray', activeforeground='white', command=self.__menu_zimmer)
        btn_zimmer.place(relx=0.5, rely=0.4, anchor=CENTER)

        btn_reservierung = Button(self.__window, text='Reservierungen', font='Arial 10', width=12, relief=RAISED, bg='gray', activebackground='gray', activeforeground='white', command=self.__menu_reservierungen)
        btn_reservierung.place(relx=0.5, rely=0.5, anchor=CENTER)

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
    # Gast Button
    def __menu_gast(self):
        self.__window.destroy()
        self.__window = Tk()
        self.app = gast_GUI(self.__window, self.__controller_gast, self.__controller_zimmer, self.__controller_reservierungen)
        self.app.draw_window()
        self.__window.mainloop()

    # Zimmer Button
    def __menu_zimmer(self):
        self.__window.destroy()
        self.__window = Tk()
        self.app = zimmer_GUI(self.__window, self.__controller_gast, self.__controller_zimmer, self.__controller_reservierungen)
        self.app.draw_window()
        self.__window.mainloop()

    # Reservierungen Button
    def __menu_reservierungen(self):
        self.__window.destroy()
        self.__window = Tk()
        self.app = reservierungen_GUI(self.__window, self.__controller_gast, self.__controller_zimmer, self.__controller_reservierungen)
        self.app.draw_window()
        self.__window.mainloop()


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

# Niels van Brakel - 1710314

import csv
import Kluisjes
import Kaartjes
import Project_NS
from tkinter import *

###############################################
#
# Script
#
###############################################


def keuze_1():
    Kaartjes.GUI_Kaartjes()
    GUI_menu()


def keuze_2():
    Kluisjes.GUI_kluisjes()
    GUI_menu()
def keuze_3():
    Project_NS.station_lijst()
    Project_NS.GUI()
    Project_NS.treininfo('http://webservices.ns.nl/ns-api-avt?station=Utrecht','Utrecht')
    GUI_menu()





###############################################
#
# GUI
#
###############################################

menu = Tk()
menu.configure(background='white')
photo_menu = PhotoImage(file="download.png")

menu.wm_title("")
menu.iconbitmap('favicon.ico')
menu.resizable(width=False, height=False)
menu.geometry('{}x{}'.format(800, 450))

def GUI_menu():
    logo_menu=Label(image=photo_menu, borderwidth=0, highlightthickness=0)
    logo_menu.place(x=0, y=0)


    title=Label(text="Hoofdmenu", borderwidth=0, highlightthickness=0, bg='white', fg="#003082", font="calibri 20 bold")
    title.place(x=330, y=0)

    btn1 = Button (menu, text ="Kaartje bestellen", command=keuze_1, fg='white', bg='#0079D3', activebackground='#003082', activeforeground='white', bd=0, font="calibri 15 bold")
    btn1.place(x=50,y=150,width=200, height=150)

    btn2 = Button (menu, text ="Kluisjes", command=keuze_2, fg='white', bg='#0079D3', activebackground='#003082', activeforeground='white', bd=0, font="calibri 15 bold")
    btn2.place(x=300,y=150,width=200, height=150)

    btn3 = Button (menu, text ="Vertrektijden", command=keuze_3, fg='white', bg='#0079D3', activebackground='#003082', activeforeground='white', bd=0, font="calibri 15 bold")
    btn3.place(x=550,y=150,width=200, height=150)

GUI_menu()
menu.mainloop()

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

#De fucties die worden aangeroepen zodra er op een knopje gedrukt wordt
def kaartjesPaneel():
    Kaartjes.GUI_Kaartjes()
    GUI_menu()
def kluisjesPaneel():
    Kluisjes.GUI_kluisjes()
    GUI_menu()
def stationPaneel():
    Project_NS.station_lijst()
    Project_NS.GUI()
    Project_NS.treininfo('http://webservices.ns.nl/ns-api-avt?station=Utrecht','Utrecht')
    GUI_menu()

###############################################
#
# GUI
#
###############################################

#de eigenschappen van het scherm
menu = Tk()
menu.configure(background='white')
photo_menu = PhotoImage(file="download.png")
menu.wm_title("")
menu.iconbitmap('favicon.ico')
menu.resizable(width=False, height=False)
menu.geometry('{}x{}'.format(800, 450))

#Het menu met de knoppen om te navigeren naar andere schermen
def GUI_menu():
    logo_menu=Label(image=photo_menu, borderwidth=0, highlightthickness=0)
    logo_menu.place(x=0, y=0)

    title=Label(menu, text="Hoofdmenu", borderwidth=0, highlightthickness=0, bg='white', fg="#003082", font="calibri 20 bold")
    title.place(x=330, y=0)

    btnKaartjes = Button (menu, text ="Kaartje bestellen", command=kaartjesPaneel, fg='white', bg='#0079D3', activebackground='#003082', activeforeground='white', bd=0, font="calibri 15 bold")
    btnKaartjes.place(x=50,y=150,width=200, height=150)

    btnKluisjes = Button (menu, text ="Kluisjes", command=kluisjesPaneel, fg='white', bg='#0079D3', activebackground='#003082', activeforeground='white', bd=0, font="calibri 15 bold")
    btnKluisjes.place(x=300,y=150,width=200, height=150)

    btnStation = Button (menu, text ="Vertrektijden", command=stationPaneel, fg='white', bg='#0079D3', activebackground='#003082', activeforeground='white', bd=0, font="calibri 15 bold")
    btnStation.place(x=550,y=150,width=200, height=150)

###############################################
#
# De functies die worden aangeroepen om het scherm te starten
#
###############################################

GUI_menu()
menu.mainloop()

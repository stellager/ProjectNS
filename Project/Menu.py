# Niels van Brakel - 1710314

import csv

from tkinter import *

###############################################
#
# Script
#
###############################################


def keuze_1():
    print("nog maken")

def keuze_2():
    import Kluisjes.py
    GUI_menu()   
def keuze_3():
    from Project_NS2 import station_lijst
    from Project_NS2 import GUI
    from Project_NS2 import treininfo
    station_lijst()
    GUI()

    treininfo('http://webservices.ns.nl/ns-api-avt?station=Utrecht','Utrecht')
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

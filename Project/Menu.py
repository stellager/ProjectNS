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

def keuze_3():
    import Project_NS.py

###############################################
#
# GUI
#
###############################################

root = Tk()
root.configure(background='white')
photo = PhotoImage(file="download.png")

root.wm_title("")
root.iconbitmap('favicon.ico')
root.resizable(width=False, height=False)
root.geometry('{}x{}'.format(800, 450))

logo=Label(image=photo, borderwidth=0, highlightthickness=0)
logo.place(x=0, y=0)

title=Label(text="Hoofdmenu", borderwidth=0, highlightthickness=0, bg='white', fg="#003082", font="calibri 20 bold")
title.place(x=330, y=0)

btn1 = Button (root, text ="Kaartje bestellen", command=keuze_1, fg='white', bg='#0079D3', activebackground='#003082', activeforeground='white', bd=0, font="calibri 15 bold")
btn1.place(x=50,y=150,width=200, height=150)

btn2 = Button (root, text ="Kluisjes", command=keuze_2, fg='white', bg='#0079D3', activebackground='#003082', activeforeground='white', bd=0, font="calibri 15 bold")
btn2.place(x=300,y=150,width=200, height=150)

btn3 = Button (root, text ="Vertrektijden", command=keuze_3, fg='white', bg='#0079D3', activebackground='#003082', activeforeground='white', bd=0, font="calibri 15 bold")
btn3.place(x=550,y=150,width=200, height=150)

root.mainloop()

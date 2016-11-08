import random
import csv
from tkinter import *
from tkinter import messagebox

bestand = "kluisjes.csv"

###############################################
#
# Script
#
###############################################

def willekeurig():


    nummer_1 = str(random.randrange(1,10))
    nummer_2 = str(random.randrange(1,10))
    nummer_3 = str(random.randrange(1,10))
    nummer_4 = str(random.randrange(1,10))

    code = nummer_1+nummer_2+nummer_3+nummer_4
    return code

def lezen_csv(x):

    lijst = []

    with open(x, 'r') as CSV:
        reader = csv.reader(CSV, delimiter=';')

        for rij in reader:
            lijst.append(rij)

    return lijst

def schrijven_csv(x, y):

    with open(x, 'w', newline='') as CSV:
        writer = csv.writer(CSV, delimiter=';')

        for i in range(len(y)):
            writer.writerow((y[i][0], y[i][1]))

def keuze_1():

    global bestand
    x = lezen_csv(bestand)

    code = int(willekeurig())

    for i in range(len(x)):
        if x[i][1] == code:
            code = int(willekeurig())
        elif x[i][1] == '-':
            x[i][1] = code
            lijst = x
            msg=messagebox.showinfo("Nieuwe code", "U heeft kluisje {} en uw code is {}.".format(i+1, code))
            schrijven_csv(bestand, lijst)
            break
        elif i == 11:
            msg=messagebox.showinfo("Error", "Alle kluisjes zitten vol.")

def keuze_2():

    global value
    global bestand
    x = lezen_csv(bestand)
    count = 0
    code = value

    for i in range(len(x)):
        if code in x[i][1]:
            msg=messagebox.showinfo("Info","Kluisje {} gaat open.\n".format(x[i][0]))
        elif code not in x[i][1] :
            count += 1
            if count >= len(x):
                msg=messagebox.showinfo("Info","Foute code, Probeer het opnieuw")

def keuze_3():

    global value
    global bestand
    x = lezen_csv(bestand)
    count = 0
    code = value

    for i in range(len(x)):
        if code in x[i][1]:
            msg=messagebox.showinfo("Info","Kluisje {} wordt terug gegeven.\n".format(i + 1))
            x[i][1] = '-'
            lijst = x
            schrijven_csv(bestand, lijst)
            break
        elif code not in x[i][1] :
            count += 1
            if count >= len(x):
                msg=messagebox.showinfo("Info","Foute code, Probeer het opnieuw")

def keuze_4():

    global bestand
    x = lezen_csv(bestand)

    count = 0
    for i in range(len(x)):
        if x[i][1] == '-':
            count += 1
    msg=messagebox.showinfo("Info", "Er zijn nog {} beschikbaar \n".format(count))

def keuze_5():

    #msg=messagebox.showinfo("Info","\nHet programma sluit af\n")
    root.destroy()

class GUI_2 (object):

    def __init__(self):

        top=self.top=Toplevel(root)
        self.entryl2=Label(top,text="Voer uw code in :")
        self.entryl2.pack()

        self.entry2=Entry(top)
        self.entry2.pack()

        self.entryb2=Button(top, text='Geef vrij', command=self.cleanup, fg='white', bg='#0079D3', activebackground='#003082', activeforeground='white', bd=0, font="calibri 13")
        self.entryb2.pack()

    def cleanup(self):

        global value
        value=self.entry2.get()
        self.top.destroy()
        keuze_2()

class GUI_3 (object):

    def __init__(self):

        top=self.top=Toplevel(root)
        self.entryl3=Label(top,text="Voer uw code in :")
        self.entryl3.pack()

        self.entry3=Entry(top)
        self.entry3.pack()

        self.entryb3=Button(top, text='Geef uw code', command=self.cleanup, fg='white', bg='#0079D3', activebackground='#003082', activeforeground='white', bd=0, font="calibri 13")
        self.entryb3.pack()

    def cleanup(self):

        global value
        value=self.entry3.get()
        self.top.destroy()
        keuze_3()

###############################################
#
# GUI menu
#
###############################################

root = Tk()
root.configure(background='white')
photo = PhotoImage(file="download.png")

root.wm_title("")
root.iconbitmap('favicon.ico')
root.resizable(width=False, height=False)
root.geometry('{}x{}'.format(800, 450))

logo=Label(image=photo, borderwidth=0, highlightthickness=0).place (x=0, y=0)

title=Label(text="Kluisjes", borderwidth=0, highlightthickness=0, bg='white', fg="#003082", font="calibri 20 bold")
title.place(x=330, y=0)

nemen = Button(root, text="Kluisje nemen", command=keuze_1, fg='white', bg='#0079D3', activebackground='#003082', activeforeground='white', bd=0, font="calibri 15 bold")
nemen.place(x=160,y=70, width=200, height=150)

openen = Button(root, text="Kluisje openen", command=GUI_2, fg='white', bg='#0079D3', activebackground='#003082', activeforeground='white', bd=0, font="calibri 15 bold")
openen.place(x=388,y=70, width=200, height=150)

teruggeven = Button(root, text="Kluisje teruggeven", command=GUI_3, fg='white', bg='#0079D3', activebackground='#003082', activeforeground='white', bd=0, font="calibri 15 bold")
teruggeven.place(x=160,y=250, width=200, height=150)

bekijken = Button(root, text="Kluisjes beschikbaar", command=keuze_4, fg='white', bg='#0079D3', activebackground='#003082', activeforeground='white', bd=0, font="calibri 15 bold")
bekijken.place(x=388,y=250, width=200, height=150)

afsluiten = Button(root, text="Menu", command=keuze_5, fg='white', bg='#0079D3', activebackground='#003082', activeforeground='white', bd=0, font="calibri 13")
afsluiten.place(x=680,y=10, width=100, height=40)

root.mainloop()

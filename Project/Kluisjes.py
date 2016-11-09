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
    kluis.destroy()

class GUI_2 (object):

    def __init__(self):

        vraag=self.vraag=Toplevel(kluis)
        self.entryl2=Label(vraag,text="Voer uw code in :")
        self.entryl2.pack()

        self.entry2=Entry(vraag, show="*")
        self.entry2.pack()

        self.entryb2=Button(vraag, text='Geef code uw code', command=self.cleanup)
        self.entryb2.pack()

    def cleanup(self):

        global value
        value=self.entry2.get()
        self.vraag.destroy()
        keuze_2()

class GUI_3 (object):

    def __init__(self):

        vraag=self.vraag=Toplevel(kluis)
        self.entryl3=Label(vraag,text="Voer uw code in :")
        self.entryl3.pack()

        self.entry3=Entry(vraag, show="*")
        self.entry3.pack()

        self.entryb3=Button(vraag, text='Geef uw code', command=self.cleanup)
        self.entryb3.pack()

    def cleanup(self):

        global value
        value=self.entry3.get()
        self.vraag.destroy()
        keuze_3()

###############################################
#
# GUI menu
#
###############################################
def GUI_kluisjes():

    global kluis
    global nemen
    global openen
    global teruggeven
    global bekijken
    global afsluiten

    kluis = Tk()
    kluis.configure(background='white')
    photo = PhotoImage(file="download.png")

    kluis.wm_title("")
    kluis.iconbitmap('favicon.ico')
    kluis.resizable(width=False, height=False)
    kluis.geometry('{}x{}'.format(800, 450))

    title2=Label(kluis, text="Kluisjes", borderwidth=0, highlightthickness=0, bg='white', fg="#003082", font="calibri 20 bold")
    title2.place(x=330, y=0)

    nemen = Button (kluis, text ="Kluisje nemen", command = keuze_1, fg='white', bg='#0079D3', activebackground='#003082', activeforeground='white', bd=0, font="calibri 15 bold")
    nemen.place(x=160,y=70, width=200, height=150)

    openen = Button (kluis, text ="Kluisje openen", command = GUI_2, fg='white', bg='#0079D3', activebackground='#003082', activeforeground='white', bd=0, font="calibri 15 bold")
    openen.place(x=388,y=70, width=200, height=150)

    teruggeven = Button (kluis, text ="Kluisje teruggeven", command = GUI_3, fg='white', bg='#0079D3', activebackground='#003082', activeforeground='white', bd=0, font="calibri 15 bold")
    teruggeven.place(x=160,y=250, width=200, height=150)

    bekijken = Button (kluis, text ="Kluisje bekijken", command = keuze_4, fg='white', bg='#0079D3', activebackground='#003082', activeforeground='white', bd=0, font="calibri 15 bold")
    bekijken.place(x=388,y=250, width=200, height=150)

    afsluiten = Button (kluis, text ="Menu", command = keuze_5, fg='white', bg='#0079D3', activebackground='#003082', activeforeground='white', bd=0, font="calibri 13 bold")
    afsluiten.place(x=680,y=10, width=100, height=40)

    kluis.mainloop()

# Bram Schenau - 1700154
#
###############################################
#
# imports
#
###############################################
import random
import csv
from tkinter import *
from tkinter import messagebox

bestand = "kluisjes.csv"

###############################################
#
# Functies
#
###############################################

# functie om een willekeurige code te maken van 4 cijfers voor de gebruiker
def willekeurig():

    nummer_1 = str(random.randrange(1,10))
    nummer_2 = str(random.randrange(1,10))
    nummer_3 = str(random.randrange(1,10))
    nummer_4 = str(random.randrange(1,10))

    code = nummer_1+nummer_2+nummer_3+nummer_4
    return code

# functie voor het inlezen van de CSV file waar de kluisjes met codes in staan.
def lezen_csv(x):

    lijst = []

    with open(x, 'r') as CSV:
        reader = csv.reader(CSV, delimiter=';')

        for rij in reader:
            lijst.append(rij)

    return lijst

# functie voor het wegschrijven van de CSV file waar de kluisjes met codes in staan.
def schrijven_csv(x, y):

    with open(x, 'w', newline='') as CSV:
        writer = csv.writer(CSV, delimiter=';')

        for i in range(len(y)):
            writer.writerow((y[i][0], y[i][1]))

# functie die een kluisje kiest en een code aan de gebruiker geeft.
# Zorgt er ook voor dat er niet 2 dezelfde codes in kunnen staan
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

# functie die om invoer van een code vraagt en vervolgens het kluisje opent met die code.
def keuze_2():

    global value
    global bestand
    x = lezen_csv(bestand)
    count = 0
    code = value

    for i in range(len(x)):
        if code is "-" or "":
            msg=messagebox.showinfo("Info","Foute code, Probeer het opnieuw")
            break
        else:
            if code in x[i][1]:
                msg=messagebox.showinfo("Info","Kluisje {} gaat open.\n".format(x[i][0]))
            elif code not in x[i][1] :
                count += 1
                if count >= len(x):
                    msg=messagebox.showinfo("Info","Foute code, Probeer het opnieuw")

# functie die om invoer van een code vraagt en
# vervolgens de code van het kluisje haalt en het mogelijk maakt om het kluisje opnieuw uit te delen
def keuze_3():

    global value
    global bestand
    x = lezen_csv(bestand)
    count = 0
    code = value

    for i in range(len(x)):
        if code is "-" or "":
            msg=messagebox.showinfo("Info","Foute code, Probeer het opnieuw")
            break
        else:
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

# Functie die telt hoeveel kluisjes er vrij zijn
def keuze_4():

    global bestand
    x = lezen_csv(bestand)

    count = 0
    for i in range(len(x)):
        if x[i][1] == '-':
            count += 1
    msg=messagebox.showinfo("Info", "Er zijn nog {} beschikbaar \n".format(count))

# functie die de GUI afsluit
def keuze_5():

    kluis.destroy()

# GUI die de oproepbox maakt waar je je code in moet voeren voor als je je kluisje wilt openen
class GUI_2 (object):

    def __init__(self):

        vraag=self.vraag=Toplevel(kluis)
        vraag.iconbitmap('favicon.ico')
        vraag.configure(background='white')
        vraag.resizable(width=False, height=False)
        vraag.geometry('{}x{}'.format(400, 225))

        self.entryl2=Label(vraag,text="Voer uw kluiscode in", borderwidth=0, highlightthickness=0, bg='white', fg="#003082", font="calibri 18 bold")
        self.entryl2.place(x=75,y=20, width=250, height=40)

        self.entry2=Entry(vraag, show="*", bd=1, font="calibri 13", fg='#0079D3')
        self.entry2.place(x=150,y=85, width=100, height=40)

        self.entryb2=Button(vraag, text='Open kluis', command=self.cleanup, fg='white', bg='#0079D3', activebackground='#003082', activeforeground='white', bd=0, font="calibri 13 bold")
        self.entryb2.place(x=100,y=145, width=200, height=40)

    def cleanup(self):

        global value
        value=self.entry2.get()
        self.vraag.destroy()
        keuze_2()

# GUI die de oproepbox maakt waar je je code in moet voeren voor als je je kluisje terug wil geven
class GUI_3 (object):

    def __init__(self):

        vraag=self.vraag=Toplevel(kluis)
        vraag.iconbitmap('favicon.ico')
        vraag.configure(background='white')
        vraag.resizable(width=False, height=False)
        vraag.geometry('{}x{}'.format(400, 225))

        self.entryl3=Label(vraag,text="Voer uw code in", borderwidth=0, highlightthickness=0, bg='white', fg="#003082", font="calibri 18 bold")
        self.entryl3.place(x=75,y=20, width=250, height=40)

        self.entry3=Entry(vraag, show="*", bd=1, font="calibri 13", fg='#0079D3')
        self.entry3.place(x=150,y=85, width=100, height=40)

        self.entryb3=Button(vraag, text='Geef kluisje terug', command=self.cleanup, fg='white', bg='#0079D3', activebackground='#003082', activeforeground='white', bd=0, font="calibri 13 bold")
        self.entryb3.place(x=100,y=145, width=200, height=40)

    def cleanup(self):

        global value
        value=self.entry3.get()
        self.vraag.destroy()
        keuze_3()

# Functie die het menu maakt van de kluisjes
def GUI_kluisjes():

    global kluis
    global nemen
    global openen
    global teruggeven
    global bekijken
    global afsluiten

    kluis = Tk()
    kluis.configure(background='white')

    kluis.wm_title("")
    kluis.iconbitmap('favicon.ico')
    kluis.resizable(width=False, height=False)
    kluis.geometry('{}x{}'.format(800, 450))

    title2=Label(kluis, text="Kluisjes", borderwidth=0, highlightthickness=0, bg='white', fg="#003082", font="calibri 20 bold")
    title2.place(x=20, y=10)

    listbox = Listbox(kluis, bg='#FFC917', bd=1, font="calibri 14")
    listbox.place(x=0, y=70, width=800, height=430)

    nemen = Button (kluis, text ="Kluisje nemen", command = keuze_1, fg='white', bg='#0079D3', activebackground='#003082', activeforeground='white', bd=0, font="calibri 15 bold")
    nemen.place(x=160,y=90, width=200, height=150)

    openen = Button (kluis, text ="Kluisje openen", command = GUI_2, fg='white', bg='#0079D3', activebackground='#003082', activeforeground='white', bd=0, font="calibri 15 bold")
    openen.place(x=388,y=90, width=200, height=150)

    teruggeven = Button (kluis, text ="Kluisje teruggeven", command = GUI_3, fg='white', bg='#0079D3', activebackground='#003082', activeforeground='white', bd=0, font="calibri 15 bold")
    teruggeven.place(x=160,y=270, width=200, height=150)

    bekijken = Button (kluis, text ="Kluisje bekijken", command = keuze_4, fg='white', bg='#0079D3', activebackground='#003082', activeforeground='white', bd=0, font="calibri 15 bold")
    bekijken.place(x=388,y=270, width=200, height=150)

    afsluiten = Button (kluis, text ="Menu", command = keuze_5, fg='white', bg='#0079D3', activebackground='#003082', activeforeground='white', bd=0, font="calibri 13 bold")
    afsluiten.place(x=680,y=10, width=100, height=40)


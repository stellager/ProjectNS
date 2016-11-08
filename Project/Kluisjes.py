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
            msg=messagebox.showinfo("Nieuwe code", "U heeft kluisje {} en uw code is {}.\n".format(i+1, code))
            schrijven_csv(bestand, lijst)
            break

def keuze_2():

    global entrycode
    global bestand
    x = lezen_csv(bestand)

    code = input("Voer kluis nummer en code in.")

    for i in range(len(x)):
        if code == x[i][1]:
            msg=messagebox.showinfo("Info","Kluisje {} gaat open.\n".format(x[i][0]))

def keuze_3():

    global bestand
    x = lezen_csv(bestand)

    code = input("Voer kluis nummer en code in.")

    for i in range(len(x)):
        if code in x[i][1]:
            msg=messagebox.showinfo("Info","Kluisje {} wordt terug gegeven.\n".format(i + 1))
            x[i][1] = '-'
            lijst = x
            schrijven_csv(bestand, lijst)
            break
        elif code not in x[i][1] :
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

    msg=messagebox.showinfo("Info","\nHet programma sluit af\n")

###############################################
#
# GUI
#
###############################################

root = Tk()
#root.configure(background='white')
#photo = PhotoImage(file="download.png")

#root.wm_title("Kluisjes")
#root.iconbitmap('favicon.ico')
#root.resizable(width=True, height=True)
root.geometry('{}x{}'.format(650, 500))

#logo=Label(image=photo).place (x=0, y=0)

nemen = Button (root, text ="Kluisje nemen", command = keuze_1)
nemen.place(x=50,y=50)

openen = Button (root, text ="Kluisje openen", command = keuze_2)
openen.place(x=150,y=50)

teruggeven = Button (root, text ="Kluisje teruggeven", command = keuze_3)
teruggeven.place(x=250,y=50)

bekijken = Button (root, text ="Kluisje bekijken", command = keuze_4)
bekijken.place(x=350,y=50)

afsluiten = Button (root, text ="Afsluiten", command = keuze_5)
afsluiten.place(x=450,y=50)

entrybutton = Button(root, text="get", command=callback)
entrybutton.pack()

root.mainloop()

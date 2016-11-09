#       Writer - Tim Hoogeland
#
##############################
from math import radians, cos, sin, asin, sqrt
import requests
import xmltodict
import datetime
from tkinter import *
from tkinter import ttk

weekdagen=['Maandag','Dinsdag','Woensdag','Donderdag','Vrijdag','Zaterdag','Zondag']
lang='en'
weekdag=0
def dagvdweek():
    global weekdag
    if datetime.datetime.today().weekday() in range(0,5):
        weekdag=1
    else:
        weekdag=0
class ComboBoxDemo(ttk.Frame):

    def __init__(self, isapp=True, name='combobox'):
        ttk.Frame.__init__(self, name=name)
        self.pack(expand=Y)
        self.master.title('')
        self.isapp = isapp
        global dag
        dag=Label(text='Dag van de week: '+weekdagen[datetime.datetime.today().weekday()], bg='#FFC917', activebackground='#003082', activeforeground='white', bd=0, font="calibri 13")
        dag.place(x=300, y=260, width=200, height=40)
        self._butone()
        self._create_demo_panel()



    def _create_demo_panel(self):
        global demoPanel
        demoPanel = Frame(self)
        demoPanel.pack(side=BOTTOM, fill=BOTH, expand=Y)

        global dag2
        dag2=Label(text='Leeftijd categorie', bg='#FFC917', activebackground='#003082', activeforeground='white', bd=0, font="calibri 13")
        dag2.place(x=300, y=160, width=200, height=40)

        global cb3
        opties = ('65+', '12 jaar of jonger', 'Volwassen')
        cb3 = ttk.Combobox(root, values=opties, state='readonly')
        cb3.current(0)  # set selection
        cb3.place(x=300, y=200, width=200, height=40)


    def _butone(self):
        global button1
        button1=Button(text='Volgende',command=self.leeftijdwaarde, fg='white', bg='#0079D3', activebackground='#003082', activeforeground='white', bd=0, font="calibri 13 bold")
        button1.place(x=350, y=300, width=100, height=40)
    def leeftijdwaarde(self):
        global leeftijd
        leeftijd=cb3.get()
        dag.destroy()
        dag2.destroy()
        cb3.destroy()
        dag.quit()
        button1.destroy()
        button1.quit()
        self.destroy()
        self.quit()











list=['JA','NEE']
ja= 'JA'
nee = 'NEE'

prijs=0
auth_details = ('t.hoogeland@live.com','3leOcnJcxNX8Hw3gJ7v5zn3EP2T_R_gEwcotJ-aQ0zzNz4ayWNO-tA')
stations_url = 'http://webservices.ns.nl/ns-api-stations-v2'
stations_response = requests.get(stations_url, auth=auth_details)
stationsXML = xmltodict.parse(stations_response.text)
stationslijst=[]
codes=[]
longlat=[]
kort=[]
middel=[]
lang=[]
syno=[]
onbekend=0
weekdag=0
def station_lijst_2():
    for station in stationsXML['Stations']['Station']:
        if station['Code']=='G':
            continue
        stationslijst.append(station['Code'])
        codes.append(station['Code'])
        stationslijst.append(station['Namen']['Kort'])
        kort.append(station['Namen']['Kort'])
        stationslijst.append(station['Namen']['Middel'])
        middel.append(station['Namen']['Middel'])
        stationslijst.append(station['Namen']['Lang'])
        lang.append(station['Namen']['Lang'])
        longlat.append([station['Lat'],station['Lon']])
        try:
            synoniemen=station['Synoniemen']
            if type(synoniemen['Synoniem'])==list:
                for synoniemen2 in synoniemen['Synoniem']:
                    stationslijst.append(synoniemen2)
                    syno.append(synoniemen2)
            else:
                stationslijst.append(synoniemen['Synoniem'])
                syno.append(synoniemen['Synoniem'])
        except TypeError:
            continue
    return stationslijst





def standaardprijs(afstandKM):
    global prijs
    if afstandKM>50:
        prijs=0.15*afstandKM+1
        if prijs>26.30:
            prijs=26.30
    elif afstandKM>0: prijs= 0.21*afstandKM+1
    else: prijs=0

def ritprijs():
    if weekdag == 0:
        if leeftijd== '65+' or leeftijd =='12 jaar of jonger': return prijs*0.65
        else: return prijs
    if weekdag == 1:
        if leeftijd=='Volwassen': return prijs*0.65
        else: return prijs


keuze2=''
keuze=''
keuze_2=''
stat_1=[]
stat_2=[]

def stationskeuze(x):
    global s

    while True:
        global onbekend
        onbekend=0
        global keuze
        global keuze3

        utrecht=['Utrecht', 'utrecht', 'Utrecht c.','utrecht c.', 'utrecht C.', 'Utrecht C.']
        if x in utrecht:
            return [52.0888900756836,5.11027765274048]
        elif x in stationslijst:
            keuze=x
            if keuze in codes:
                keuze3= stationslijst[stationslijst.index(keuze)+3]
                s=keuze3
                return longlat[(codes.index(keuze))]
            elif keuze in kort:
                keuze3= stationslijst[stationslijst.index(keuze)+2]
                s=keuze3
                return longlat[(kort.index(keuze))]
            elif keuze in middel:
                keuze3= stationslijst[stationslijst.index(keuze)+1]
                s=keuze3
                return longlat[(middel.index(keuze))]
            elif keuze in lang:
                keuze=keuze3
                s=keuze3
                return longlat[(lang.index(keuze))]
        elif x.title() in stationslijst:
            keuze=x.title()
            if keuze in codes:
                keuze3= stationslijst[stationslijst.index(keuze)+3]
                s=keuze3
                return longlat[(codes.index(keuze))]
            elif keuze in kort:
                keuze3= stationslijst[stationslijst.index(keuze)+2]
                s=keuze3
                return longlat[(kort.index(keuze))]
            elif keuze in middel:
                keuze3= stationslijst[stationslijst.index(keuze)+1]
                s=keuze3
                return longlat[middel.index(keuze)]
            elif keuze in lang:
                keuze=keuze3
                s=keuze3
                return longlat[lang.index(keuze)]

        elif x.upper() in stationslijst:
            keuze=x.upper()
            if keuze in codes:
                keuze3= stationslijst[(stationslijst.index(keuze)+3)]
                s=keuze3
                return longlat[(codes.index(keuze))]
        else:
            onbekend=2
            break
def longus():
    listbox.delete(0,END)

    if keuze=='':
        global keuze
        keuze=entry.get()
        global stat_1
        stat_1=stationskeuze(keuze)
        if onbekend==2:
            listbox.insert(0,'Station onbekend, probeer het opnieuw.')
            listbox.place(x=0, y=70, width=800, height=430)
            opnieuw()
        else:
            global stat1
            stat1=s
            listbox.insert(0,'Kies volgende station')
            listbox.place(x=0, y=70, width=800, height=430)
    elif keuze_2=='':
        global keuze_2
        keuze_2=entry.get()
        global stat_2
        stat_2=stationskeuze(keuze_2)
        if onbekend==2:
            listbox.insert(0,'Station onbekend, probeer het opnieuw.')
            listbox.place(x=0, y=70, width=800, height=430)
            keuze_2=''
        else:
            global stat2
            stat2=s
            lon1=float(stat_1[1])
            lat1=float(stat_1[0])
            lon2=float(stat_2[1])
            lat2=float(stat_2[0])
            haversine(lon1, lat1, lon2, lat2)
            main()
def opnieuw():
    global keuze
    global keuze_2
    global keuze2
    global stat_2
    global stat_1
    keuze2=''
    keuze=''
    keuze_2=''
    stat_1=[]
    stat_2=[]
def main():
    ComboBoxDemo().mainloop()
    standaardprijs(km2)
    a=round(ritprijs(),2)
    b='U valt in de leeftijdscategorie '+leeftijd+'.'
    c='Op een '+weekdagen[datetime.datetime.today().weekday()]+' bedraagt de prijs van uw rit van '+stat1+' naar '+stat2+': '+str(a)+' euro.'
    listbox.insert(0,(b))
    listbox.insert(1,(c))
    opnieuw()

def keuze_5():
    #msg=messagebox.showinfo("Info","\nHet programma sluit af\n")
    root.destroy()

def callback(event):
    g=event
    longus()

def GUI_Kaartjes():
    global root
    global entry
    global photo
    global listbox
    global button
    global afsluiten
    root = Tk()
    root.configure(background='white')
    photo = PhotoImage(file="download.png")

    root.wm_title("")
    root.iconbitmap('favicon.ico')
    root.resizable(width=False, height=False)
    root.geometry('{}x{}'.format(800, 450))

    title3=Label(master=root, text="Kaartjes", borderwidth=0, highlightthickness=0, bg='white', fg="#003082", font="calibri 20 bold")
    title3.place(x=20, y=10)

    entry=Entry(master=root, bd=0, font="calibri 13", fg='#0079D3')
    entry.place(x=345, y=10, width=235, height=40)
    entry.insert(0, 'Typ hier uw begin station...')

    listbox = Listbox(master=root, bg='#FFC917', bd=1, font="calibri 14")
    listbox.place(x=0, y=70, width=800, height=430)
    listbox.config()

    button=Button(master=root, text='Zoek',command=longus, fg='white', bg='#0079D3', activebackground='#003082', activeforeground='white', bd=0, font="calibri 13 bold")
    button.place(x=570, y=10, width=100, height=40)

    afsluiten = Button (master=root, text ="Menu", command = keuze_5, fg='white', bg='#0079D3', activebackground='#003082', activeforeground='white', bd=0, font="calibri 13 bold")
    afsluiten.place(x=680,y=10, width=100, height=40)

    entry.bind("<Return>",callback)


def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    km = 6367 * c
    global km2
    km2= round(km,2)


station_lijst_2()

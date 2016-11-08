#       WERKING
#       VUL STATION 1 IN
#       VUL STATION 2 IN
#       KIES LEEFTIJDSGROEP
#       ENTER GEEFT RITPRIJS
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

    def __init__(self, isapp=True, name='comboboxdemo'):
        ttk.Frame.__init__(self, name=name)
        self.pack(expand=Y)
        self.master.title('Combobox Demo')
        self.isapp = isapp
        global dag
        dag=ttk.Label(text='Dag van de week:'+weekdagen[datetime.datetime.today().weekday()])
        dag.pack(pady=5, padx=10)
        self._butone()
        self._create_demo_panel()



    def _create_demo_panel(self):
        global demoPanel
        demoPanel = Frame(self)
        demoPanel.pack(side=BOTTOM, fill=BOTH, expand=Y)


        global cb3
        opties = ('65+', '12 jaar of jonger', 'Volwassen')
        cbp3 = ttk.Labelframe(demoPanel, text='Leeftijd')
        cb3 = ttk.Combobox(cbp3, values=opties, state='readonly')
        cb3.current(0)  # set selection
        cb3.pack(side=BOTTOM,pady=5, padx=10)


        cbp3.pack(in_=demoPanel, side=BOTTOM, pady=5, padx=10)
    def _butone(self):
        global button1
        button1=Button(text='Volgende',command=self.leeftijdwaarde)
        button1.pack(side=BOTTOM,pady=5, padx=10)
    def leeftijdwaarde(self):
        global leeftijd
        leeftijd=cb3.get()
        dag.destroy()
        dag.quit()
        button1.destroy()
        button1.quit()
        self.destroy()
        self.quit()









root = Tk()
root.configure(background='white')
photo = PhotoImage(file="download.png")

root.wm_title("Kaartverkoop")
root.iconbitmap('favicon.ico')
root.resizable(width=False, height=False)
root.geometry('{}x{}'.format(640, 360))

logo=Label(image=photo).place(x=0, y=0)

entry=Entry(master=root)
entry.place(x=300, y=30, width=200, height=40)

listbox = Listbox(master=root, background='#FFC917')
listbox.place(x=20, y=100, width=600, height=240)
listbox.config()


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
    if afstandKM>50: prijs=15+0.6*afstandKM
    elif afstandKM>0: prijs= 0.8*afstandKM
    else: prijs=0

def ritprijs():
    if weekdag == 0:
        if leeftijd== '65+' or leeftijd =='12 jaar of jonger': return "De prijs van de rit is: " + str(prijs*0.65)+" euro."
        else: return "De prijs van de rit is: " + str(prijs)+" euro."
    if weekdag == 1:
        if leeftijd=='Volwassen': return "De prijs van de rit is: " +str(prijs*0.6)+" euro."
        else: return "De prijs van de rit is: " + str(prijs)+" euro."







keuze2=''
keuze=''
keuze_2=''
stat_1=[]
stat_2=[]

def stationskeuze(x):
    while True:
        global onbekend
        onbekend=0
        global keuze
        global keuze2

        if x in stationslijst:
            keuze=x
            if keuze in codes:
                keuze2= stationslijst[stationslijst.index(keuze)+3]
                return longlat[(codes.index(keuze))]
            elif keuze in kort:
                keuze2= stationslijst[stationslijst.index(keuze)+2]
                return longlat[(kort.index(keuze))]
            elif keuze in middel:
                keuze2= stationslijst[stationslijst.index(keuze)+1]
                return longlat[(middel.index(keuze))]
            elif keuze in lang:
                return longlat[(lang.index(keuze))]
        elif x.title() in stationslijst:
            keuze=x.title()
            if keuze in codes:
                keuze2= stationslijst[stationslijst.index(keuze)+3]
                return longlat[(codes.index(keuze))]
            elif keuze in kort:
                keuze2= stationslijst[stationslijst.index(keuze)+2]
                return longlat[(kort.index(keuze))]
            elif keuze in middel:
                keuze2= stationslijst[stationslijst.index(keuze)+1]
                return longlat[middel.index(keuze)]
            elif keuze in lang:
                return longlat[lang.index(keuze)]

        elif keuze.upper() in stationslijst:
            keuze=x.upper()
            if keuze in codes:
                keuze2= stationslijst[(stationslijst.index(keuze)+3)]
                return longlat[(codes.index(keuze))]
            else:
                onbekend=2
                break
def longus():
    listbox.delete(0,END)
    if onbekend==2:
        listbox.insert(0,'Station onbekend, probeer het opnieuw.')
        listbox.place(x=20, y=100, width=600, height=240)
    elif keuze=='':
        global keuze
        keuze=entry.get()
        global stat_1
        stat_1=stationskeuze(keuze)
        listbox.insert(0,'Kies volgende station')
        listbox.place(x=20, y=100, width=600, height=240)
    elif keuze_2=='':
        global keuze_2
        keuze_2=entry.get()
        global stat_2
        stat_2=stationskeuze(keuze_2)
        lon1=float(stat_1[1])
        lat1=float(stat_1[0])
        lon2=float(stat_2[1])
        lat2=float(stat_2[0])
        global km
        km=haversine(lon1, lat1, lon2, lat2)
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
    standaardprijs(km)
    a=str(ritprijs())
    listbox.insert(0,(a))
    opnieuw()



button=Button(master=root, text='Zoek',command=longus)
button.place(x=500, y=30, width=100, height=40)




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
    return km






station_lijst_2()
root.mainloop()



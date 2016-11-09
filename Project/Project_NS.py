#######################################################################################################
# writer - Tim Hoogeland
#
# imports-
#######################################################################################################
import requests
import xmltodict
from tkinter import *





auth_details = ('t.hoogeland@live.com','3leOcnJcxNX8Hw3gJ7v5zn3EP2T_R_gEwcotJ-aQ0zzNz4ayWNO-tA')
stations_url = 'http://webservices.ns.nl/ns-api-stations-v2'
stations_response = requests.get(stations_url, auth=auth_details)
stationsXML = xmltodict.parse(stations_response.text)
beginurl='http://webservices.ns.nl/ns-api-avt?station='

eindbestemming = ''
vertrektijd=''
ritnummer=''
treintype=''
traject=''
vertraging=''
spoor=int
stationslijst=[]
codes=[]

with open('stations.xml', 'w',encoding="utf8") as myXMLFile:
    myXMLFile.write(stations_response.text)
    myXMLFile.close()
def stationskeuze():
    while True:
        global onbekend
        onbekend=0
        global keuze

        if keuze in stationslijst:
            if keuze in codes:
                keuze= stationslijst[stationslijst.index(keuze)+3]
            keuze2=keuze.replace(" " ,"+")
            keuze3=keuze2.replace("'","%27")
            keuze4=keuze3.replace(".","%2E")
            global url2
            url2= beginurl+keuze4
            return url2
        elif keuze.title() in stationslijst:
            keuze=keuze.title()
            keuze2=keuze.replace(" " ,"+")
            keuze3=keuze2.replace("'","%27")
            keuze4=keuze3.replace(".","%2E")
            global url2
            url2= beginurl+keuze4
            return url2
        elif keuze.upper() in stationslijst:
            if keuze.upper() in codes:
                keuze= stationslijst[stationslijst.index((keuze.upper()))+3]
            keuze2=keuze.replace(" " ,"+")
            keuze3=keuze2.replace("'","%27")
            keuze4=keuze3.replace(".","%2E").replace("(","%28").replace(")","%29")
            global url2
            url2= beginurl+keuze4
            return url2

        else:
            onbekend=2
            break


def treininfo(x,y):
        response = requests.get(x, auth=auth_details)
        with open('vertrektijden.xml', 'w',encoding="utf8") as myXMLFile:
            myXMLFile.write(response.text)
            myXMLFile.close()
        vertrekXML = xmltodict.parse(response.text)



        listbox.insert(0,('    De volgende treinen vertrekken komend uur vanaf '+y+':'))

        for vertrek in vertrekXML['ActueleVertrekTijden']['VertrekkendeTrein']:
            eindbestemming = vertrek['EindBestemming']
            vertrektijd = vertrek['VertrekTijd']
            vertrektijd = vertrektijd[11:16]
            treintype = vertrek['TreinSoort']
            spoor = vertrek['VertrekSpoor']
            try:
                spoor2=spoor['#text']
            except KeyError:
                spoor2='onbekend'
            try:
                traject = vertrek['RouteTekst']
            except KeyError:
                traject = eindbestemming
            try:
                vertraging= vertrek['VertrekVertragingTekst']
                vertraging2=' '+vertraging
            except KeyError:
                vertraging2=''

            listbox.insert(END,("    " + vertrektijd + '' + vertraging2 + ' ' + treintype + ' naar '+ eindbestemming+' vanaf spoor: '+'{:2}'.format(spoor2)))

        listbox.place(x=0, y=70, width=800, height=430)

def station_lijst():
    for station in stationsXML['Stations']['Station']:
        if station['Code']=='G':
            continue
        stationslijst.append(station['Code'])
        codes.append(station['Code'])
        stationslijst.append(station['Namen']['Kort'])
        stationslijst.append(station['Namen']['Middel'])
        stationslijst.append(station['Namen']['Lang'])
        try:
            synoniemen=station['Synoniemen']
            if type(synoniemen['Synoniem'])==list:
                for synoniemen2 in synoniemen['Synoniem']:
                    stationslijst.append(synoniemen2)
            else:
                stationslijst.append(synoniemen['Synoniem'])
        except TypeError:
            continue
    return stationslijst




def invoer():
    global keuze
    listbox.delete(0,END)
    global keuze
    global url2
    keuze=''
    keuze=entry.get()
    keuzestring=keuze
    stationskeuze()
    if onbekend==2:
        listbox.insert(0,'Station onbekend, probeer het opnieuw.')
        listbox.place(x=0, y=70, width=800, height=430)
    else:
        treininfo(url2,keuze)

def callback(event):
    g=event
    invoer()

def GUI():
    global root
    global entry
    global logo
    global listbox
    global button

    root = Tk()
    root.configure(background='white')
    photo = PhotoImage(file="download.png")

    root.wm_title("")
    root.iconbitmap('favicon.ico')
    root.resizable(width=False, height=False)
    root.geometry('{}x{}'.format(800, 450))

    logo=Label(image=photo, borderwidth=0, highlightthickness=0).place(x=5, y=5)


    entry=Entry(master=root, bd=0, font="calibri 13", fg='#0079D3')
    entry.place(x=470, y=10, width=235, height=40)
    entry.insert(0, 'Typ hier uw bestemming...')

    listbox = Listbox(master=root, bg='#FFC917', bd=1, font="calibri 14")
    button=Button(master=root, text='Zoek',command=invoer, fg='white', bg='#0079D3', activebackground='#003082', activeforeground='white', bd=0, font="calibri 13")
    button.place(x=695, y=10, width=90, height=40)

    entry.bind("<Return>",callback)


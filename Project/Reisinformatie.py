#######################################################################################################
# writer - Tim Hoogeland
#############################
import requests
import xmltodict
import datetime
from tkinter import *
from tkinter import ttk

global url2
global url3
url2=''
tijd='Datum en tijd(24:00)'
auth_details = ('t.hoogeland@live.com','3leOcnJcxNX8Hw3gJ7v5zn3EP2T_R_gEwcotJ-aQ0zzNz4ayWNO-tA')
reisinfo_url = 'http://webservices.ns.nl/ns-api-treinplanner?fromStation=Utrecht+Centraal&toStation=Wierden&departure=true'
stations_url = 'http://webservices.ns.nl/ns-api-stations-v2'

stations_response = requests.get(stations_url, auth=auth_details)
stationsXML = xmltodict.parse(stations_response.text)

##

class ComboBoxDemo(ttk.Frame):

    def __init__(self, isapp=True, name='combobox'):
        ttk.Frame.__init__(self, name=name)
        self.pack(expand=Y)
        self.master.title('')
        self.isapp = isapp
        self._butone()
        self._create_demo_panel()



    def _create_demo_panel(self):
        global demoPanel
        demoPanel = Frame(self)
        demoPanel.pack(side=BOTTOM, fill=BOTH, expand=Y)

        global labelcb1
        labelcb1=Label(root, text='Reiswijze', bg='#FFC917', activebackground='#003082', activeforeground='white', bd=0, font="calibri 13")
        labelcb1.place(x=230, y=160, width=150, height=40)

        global entry1
        entry1=Entry(root, bd=0, font="calibri 9", fg='#0079D3')
        entry1.place(x=230, y=245, width=150, height=40)
        entry1.insert(0, 'Vul een tussenstation in...')
        global labelcb3
        labelcb3=Label(root, text='Moment', bg='#FFC917', activebackground='#003082', activeforeground='white', bd=0, font="calibri 13")
        labelcb3.place(x=610, y=160, width=150, height=40)
        global entry2
        entry2=Entry(root, bd=0, font="calibri 9", fg='#0079D3')
        entry2.place(x=610, y=245, width=150, height=40)
        entry2.insert(0, 'Disabled')
        global labelstat1
        labelstat1=Label(root, text='Vertrekstation', bg='#FFC917', activebackground='#003082', activeforeground='white', bd=0, font="calibri 13")
        labelstat1.place(x=40, y=160, width=150, height=40)
        global entry3
        entry3=Entry(root, bd=0, font="calibri 9", fg='#0079D3')
        entry3.place(x=40, y=245, width=150, height=40)
        entry3.insert(0,'Gewenst vertrekstation..')

        global labelstat2
        labelstat2=Label(root, text='Aankomststation', bg='#FFC917', activebackground='#003082', activeforeground='white', bd=0, font="calibri 13")
        labelstat2.place(x=420, y=160, width=150, height=40)
        global entry4
        entry4=Entry(root, bd=0, font="calibri 9", fg='#0079D3')
        entry4.place(x=420, y=245, width=150, height=40)
        entry4.insert(0,'Gewenst aankomststation..')
        global cb1
        opties = ('Via Station', 'Direct')
        cb1 = ttk.Combobox(root, values=opties, font="calibri 9",  state='readonly')
        cb1.current(1)  # set selection
        cb1.place(x=230, y=200, width=150, height=40)
        global cb2
        opties2=''
        global cb3
        opties3=('Tijd van aankomst','Tijd van vertrek','Nu')
        cb3 = ttk.Combobox(root, values=opties3, state='readonly')
        cb3.current(1)  # set selection
        cb3.place(x=610, y=200, width=150, height=40)

    def _butone(self):
        global button1
        button1=Button(root, text='Volgende',command=self.informatie, fg='white', bg='#0079D3', activebackground='#003082', activeforeground='white', bd=0, font="calibri 13 bold")
        button1.place(x=350, y=350, width=100, height=40)


    def informatie(self):
        global vertrekstation
        global reiswijze
        global aankomststation
        global tussenstation
        global moment
        global moment_url
        global reisinfoXML
        moment=cb3.get()
        vertrekstation=entry3.get()
        reiswijze=cb1.get()
        tussenstation=entry1.get()
        aankomststation=entry4.get()
        stationskeuze(vertrekstation)
        if onbekend==2:
            entry3.insert(0,'Onbekend vertrekstation..')
        global vertrek_url
        vertrek_url='http://webservices.ns.nl/ns-api-treinplanner?fromStation='+url2
        stationskeuze(aankomststation)
        if onbekend==2:
            entry4.insert(0,'Onbekend aankomststation..')
        global aankomst_url
        aankomst_url='&toStation='+url2
        if reiswijze =='Via Station':
            stationskeuze(tussenstation)
            if onbekend==2:
                entry1.insert(0,'Onbekend aankomststation..')
            else:
                global tussen_url
                tussen_url='&viaStation='+url2
        else :
            tussen_url=''
        if moment=='Tijd van vertrek':
            moment_url='&departure=true'
        elif moment=='Tijd van aankomst':
            moment_url='&departure=false'
        else:moment_url=''
        eind_url=vertrek_url+aankomst_url+tussen_url+moment_url
        reisinfo_response = requests.get(eind_url, auth=auth_details)

        with open('reisinfo.xml', 'w',encoding="utf8") as myXMLFile:
            myXMLFile.write(reisinfo_response.text)
            myXMLFile.close()
        reisinfoXML = xmltodict.parse(reisinfo_response.text)
        station_lijst_info()
        print(globale_info)
        print(eind_url)
        print(reiswijze)

        self.destroy()
        self.quit()



stationslijst=[]
codes=[]
beginurl=''
beginurl_begin='http://webservices.ns.nl/ns-api-treinplanner?fromStation='

beginurl_tussen='&viaStation='
beginurl_eind='&toStation='

keuze=''
keuze1=''
keuze2=''
reisinfolijst=[]
overstappen=[]
globale_info=[]
with open('stations.xml', 'w',encoding="utf8") as myXMLFile:
    myXMLFile.write(stations_response.text)
    myXMLFile.close()

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

def stationskeuze(keuze):
    global url2
    global url3
    while True:
        global onbekend
        onbekend=0



        if keuze in stationslijst:
            if keuze in codes:
                keuze= stationslijst[stationslijst.index(keuze)+3]
            keuze1=keuze
            keuze2=keuze1.replace(" " ,"+")
            keuze3=keuze2.replace("'","%27")
            keuze4=keuze3.replace(".","%2E")

            url2= beginurl+keuze4

            return url2
        elif keuze.title() in stationslijst:
            keuze1=keuze.title()
            keuze2=keuze1.replace(" " ,"+")
            keuze3=keuze2.replace("'","%27")
            keuze4=keuze3.replace(".","%2E")
            global url2
            url2= beginurl+keuze4

            return url2
        elif keuze.upper() in stationslijst:
            if keuze.upper() in codes:
                keuze= stationslijst[stationslijst.index((keuze.upper()))+3]
            keuze1=keuze
            keuze2=keuze1.replace(" " ,"+")
            keuze3=keuze2.replace("'","%27")
            keuze4=keuze3.replace(".","%2E").replace("(","%28").replace(")","%29")
            global url2
            url2= beginurl+keuze4

            return url2

        else:
            global onbekend
            onbekend=2
            break


def station_lijst_info():
    for mogelijkheden in reisinfoXML['ReisMogelijkheden']['ReisMogelijkheid']:
        globale_info.append(mogelijkheden['AantalOverstappen'])

        globale_info.append(mogelijkheden['GeplandeReisTijd'])
        globale_info.append(mogelijkheden['ActueleReisTijd'])
        for reisdelen in mogelijkheden['ReisDeel']:
            globale_info.append(reisdelen['Reisdeel'][0])
            globale_info.append(reisdelen['Reisdeel'][-1])

    return globale_info

def main():
    ComboBoxDemo().mainloop()


def callback(event):
    g=event
    main()



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

    title3=Label(master=root, text="Reisinformatie", borderwidth=0, highlightthickness=0, bg='white', fg="#003082", font="calibri 20 bold")
    title3.place(x=20, y=10)

    listbox = Listbox(master=root, bg='#FFC917', bd=1, font="calibri 14")
    listbox.place(x=0, y=70, width=800, height=430)
    listbox.config()

    button=Button(master=root, text='Zoek',command=main(), fg='white', bg='#0079D3', activebackground='#003082', activeforeground='white', bd=0, font="calibri 13 bold")
    button.place(x=570, y=10, width=100, height=40)

    afsluiten = Button (master=root, text ="Menu", command = main(), fg='white', bg='#0079D3', activebackground='#003082', activeforeground='white', bd=0, font="calibri 13 bold")
    afsluiten.place(x=680,y=10, width=100, height=40)

    entry.bind("<Return>",callback)
station_lijst()
GUI_Kaartjes()
root.mainloop()

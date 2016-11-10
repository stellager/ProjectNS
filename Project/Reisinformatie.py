#######################################################################################################
# writer - Tim Hoogeland
#############################
import requests
import xmltodict
import datetime
from tkinter import *
from tkinter import ttk


auth_details = ('t.hoogeland@live.com','3leOcnJcxNX8Hw3gJ7v5zn3EP2T_R_gEwcotJ-aQ0zzNz4ayWNO-tA')
reisinfo_url = 'http://webservices.ns.nl/ns-api-treinplanner?fromStation=Utrecht+Centraal&toStation=Wierden&departure=true'
stations_url = 'http://webservices.ns.nl/ns-api-stations-v2'
reisinfo_response = requests.get(reisinfo_url, auth=auth_details)
reisinfoXML = xmltodict.parse(reisinfo_response.text)
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
        entry1=Entry(root, font="calibri 13")
        entry1.place(x=230, y=245, width=150, height=40)

        global labelcb3
        labelcb3=Label(root, text='Moment', bg='#FFC917', activebackground='#003082', activeforeground='white', bd=0, font="calibri 13")
        labelcb3.place(x=610, y=160, width=150, height=40)
        global entry2
        entry2=Entry(root, font="calibri 13")
        entry2.place(x=610, y=245, width=150, height=40)
        global labelstat1
        labelstat1=Label(root, text='Vertrekstation', bg='#FFC917', activebackground='#003082', activeforeground='white', bd=0, font="calibri 13")
        labelstat1.place(x=40, y=160, width=150, height=40)
        global entry3
        entry3=Entry(root, font="calibri 13")
        entry3.place(x=40, y=245, width=150, height=40)

        global labelstat2
        labelstat2=Label(root, text='Aankomststation', bg='#FFC917', activebackground='#003082', activeforeground='white', bd=0, font="calibri 13")
        labelstat2.place(x=420, y=160, width=150, height=40)
        global entry4
        entry4=Entry(root, font="calibri 13")
        entry4.place(x=420, y=245, width=150, height=40)

        global cb1
        opties = ('Via Station', 'Direct')
        cb1 = ttk.Combobox(root, values=opties, state='readonly')
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
        vertrekstation=entry3.get()
        reiswijze=cb1.get()
        tussenstation=entry1.get()
        aankomststation=entry4.get()



        self.destroy()
        self.quit()



stationslijst=[]
codes=[]
beginurl='http://webservices.ns.nl/ns-api-avt?station='
keuze=''
keuze1=''
keuze2=''

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
    while True:
        global onbekend
        onbekend=0



        if keuze in stationslijst:
            if keuze in codes:
                keuze1= stationslijst[stationslijst.index(keuze)+3]
            keuze2=keuze1.replace(" " ,"+")
            keuze3=keuze2.replace("'","%27")
            keuze4=keuze3.replace(".","%2E")
            global url2
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
                keuze1= stationslijst[stationslijst.index((keuze.upper()))+3]
            keuze2=keuze1.replace(" " ,"+")
            keuze3=keuze2.replace("'","%27")
            keuze4=keuze3.replace(".","%2E").replace("(","%28").replace(")","%29")
            global url2
            url2= beginurl+keuze4
            return url2

        else:
            onbekend=2
            break

with open('reisinfo.xml', 'w',encoding="utf8") as myXMLFile:
    myXMLFile.write(reisinfo_response.text)
    myXMLFile.close()
def info_checker():
    stationskeuze(vertrekstation)
    stationskeuze(aankomststation)

    if reiswijze =='Via Station':
        stationskeuze(tussenstation)

def main():
    ComboBoxDemo().mainloop()
    info_checker()

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
GUI_Kaartjes()
root.mainloop()

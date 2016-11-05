#######################################################################################################
# writer - Tim Hoogeland
# imports-
#######################################################################################################
import requests
import xmltodict
#######################################################################################################
#API Variables
#######################################################################################################
auth_details = ('t.hoogeland@live.com','3leOcnJcxNX8Hw3gJ7v5zn3EP2T_R_gEwcotJ-aQ0zzNz4ayWNO-tA')
stations_url = 'http://webservices.ns.nl/ns-api-stations-v2'
stations_response = requests.get(stations_url, auth=auth_details)
stationsXML = xmltodict.parse(stations_response.text)
beginurl='http://webservices.ns.nl/ns-api-avt?station='
#######################################################################################################
#opslag variabelen
#######################################################################################################
eindbestemming = ''
vertrektijd=''
ritnummer=''
treintype=''
traject=''
vertraging=''
spoor=int
stationslijst=[]
codes=[]
afgekort=0
########################################################################################################
#writers to xml
########################################################################################################
with open('stations.xml', 'w',encoding="utf8") as myXMLFile:
    myXMLFile.write(stations_response.text)
########################################################################################################
#Maakt een lijst van alle stations met afkortingen en synoniemen
########################################################################################################
def station_lijst():
    for station in stationsXML['Stations']['Station']:
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
#########################################################################################################
#User input voor station+creatie van nieuwe url
#########################################################################################################
def stationskeuze():
    while True:
        global keuze
        keuze=input('Vul gewenste stationsnaam in ')
        if keuze in stationslijst:
            break
        else:
            print('Station onbekend, probeer het opnieuw.')
    if keuze in codes:
        keuze= stationslijst[stationslijst.index(keuze)+3]
        global afgekort
        afgekort=1
    keuze2=keuze.replace(" " ,"+")
    keuze3=keuze2.replace("'","%27")
    global url2
    url2= beginurl+keuze3
    return url2
##########################################################################################################
#Real time vertrekinfo voor gekozen station
##########################################################################################################


def treininfo():
    response = requests.get(url2, auth=auth_details)
    with open('vertrektijden.xml', 'w',encoding="utf8") as myXMLFile:
        myXMLFile.write(response.text)
    vertrekXML = xmltodict.parse(response.text)

    print('De volgende treinen vertrekken komend uur vanaf '+keuze+':\n')

    for vertrek in vertrekXML['ActueleVertrekTijden']['VertrekkendeTrein']:
        eindbestemming = vertrek['EindBestemming']
        vertrektijd = vertrek['VertrekTijd']
        vertrektijd = vertrektijd[11:16]
        ritnummer = vertrek['RitNummer']
        treintype = vertrek['TreinSoort']
        spoor = vertrek['VertrekSpoor']
        spoor2=spoor['#text']
        try:
            traject = vertrek['RouteTekst']
        except KeyError:
            traject = eindbestemming
        try:
            vertraging= vertrek['VertrekVertragingTekst']
            vertraging2='De vertraging bedraagt: '+vertraging
        except KeyError:
            vertraging2=''

        print('Om '+vertrektijd+' vertrekt een '+ '{:9}'.format(treintype)+' met ritnummer '+'{:6}'.format(ritnummer)+' naar '+ eindbestemming+' vanaf spoor: '+'{:2}'.format(spoor2)+' ,de stations op dit traject zijn: '+ traject+'.'+'\n'+vertraging2)
############################################################################################################
#Uit te voeren programma's
############################################################################################################
station_lijst()
stationskeuze()
treininfo()
print(url2)

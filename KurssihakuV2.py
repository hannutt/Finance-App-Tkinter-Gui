import webbrowser #Tuodaan nettiselaimen käyttömahdollisuus ohjelmaan
from tkinter import* #Tkinter
from tkinter import messagebox


osake = { #Luodaan sanakirja, jossa osakkeen nimi ja sitä vastaava
    #kaupankäyntitunnus. Haku tehdään nettisivulta kaupankäyntitunnuksella.
    
    'Afarak' : 'afagr',
    'Ahlstrom-Munksjö' : 'am1',
    'Aktia' : 'aktia',
    'Alma-Media' : 'alma',
    'Altia' : 'altia',
    'Apetit' : 'apetit',
    'Asiakastieto' : 'atg1v',
    'Aspo' : 'aspo',
    'Aspocomp' : 'acg1v',
    'Atria' : 'atrav',
    'Basware' : 'bas1v',
    'Biohit' : 'biobv',
    'Bittium' : 'bitti',
    'Capman' : 'capman',
    'Cargotec' : 'cgcbv',
    'Caverion' : 'cav1v',
    'Citycon' :  'cty1s',
    'Componenta' : 'cth1v',
    'Consti' : 'consti',
    'Cramo' : 'cra1v',
    'Digia' : 'digia',
    'Digitalist' : 'digigr',
    'Dna' : 'dna',
    'Dovre' : 'dov1v',
    'EAB' : 'eab',
    'Efore' : 'efo1v',
    'Elecster' : 'eleav',
    'Elisa' : 'elisa',
    'Endomines' : 'endom',
    'Eq' : 'eqv1v',
    'Ericsson' : 'eribr',
    'Etteplan' : 'ette',
    'Evli' : 'evli',
    'Exel' : 'exl1v',
    'F-Secure' : 'fsc1v',
    'Finnair' : 'fia1s',
    'Fiskars' : 'fskrs',
    'Fortum' : 'fortum',
    'Glaston' : 'gla1v',
    'Harvia' : 'harvia',
    'Hkscan' : 'hksav',
    'Hoivatilat' : 'hoiva',
    'Honkarakenne' : 'honbs',
    'Huhtamäki' : 'huh1v',
    'Ilkka-Yhtymä 1' : 'ilk1s',
    'Ilkka-Yhtymä 2' : 'ilk2s',
    'Incap' : 'icp1v',
    'Innofactor' : 'ifa1v',
    'Investors' : 'invest',
    'Kamux' : 'kamux',
    'Kemira' : 'kemira',
    'Keskisuomalainen' : 'kslav',
    'Kesko a' : 'keskoa',
    'Kesko b' : 'keskob',
    'Kesla' : 'kelas',
    'Kojamo' : 'kojamo',
    'Kone' : 'knebv',
    'Konecranes' : 'kcr',
    'Lassila & tikanoja' : 'lat1v',
    'Lehto' : 'lehto',
    'Marimekko' : 'mmo1v',
    'Martela' : 'maras',
    'Metso' : 'metso',
    'Metsä board a' : 'metsa',
    'Metsä board b' : 'metsb',
    'Neo' : 'neo1v',
    'Neste' : 'neste',
    'Nixu' : 'nixu',
    'Noho' : 'noho',
    'Nokia' : 'nokia',
    'Nokian renkaat' : 'tyres',
    'Nordea' : 'nda%20fi',
    'Nurminen' : 'nlg1v',
    'Olvi' : 'olvas',
    'Oma säästöpanki' : 'omasp',
    'Oriola a' : 'okdav',
    'Oriola b' : 'okdbv',
    'Orion a' : 'ornav',
    'Orion b' : 'ornbv',
    'Outokumpu' : 'out1v',
    'Outotec' : 'ote1v',
    'Ovaro' : 'ovaro',
    'Panostaja' : 'pna1v',
    'Pihlajalinna' : 'pihlis',
    'Ponsse' : 'pon1v',
    'Punamusta' : 'pumu',
    'Qpr' : 'qpr1v',
    'Qt' : 'qtcom',
    'Raisio k' : 'raikv',
    'Raisio v' : 'raivv',
    'Ramirent' : 'rami',
    'Rapala' : 'rap1v',
    'Raute' : 'raute',
    'Revenio' : 'reg1v',
    'Robit' : 'robit',
    'Rovio' : 'rovio',
    'Saga' : 'sagcv',
    'Sampo' : 'sampo',
    'Sanoma' : 'saa1v',
    'Scanfil' : 'scanfl',
    'Sievi' : 'sievi',
    'Siili solutions' : 'siili',
    'Silmäasema' : 'silma',
    'Solteq' : 'solteq',
    'Soprano' : 'sopra',
    'Sotkamo silver' : 'sosi1',
    'Srv' : 'srv1v',
    'Ssab a' : 'ssabah',
    'Ssab b' : 'ssabbh',
    'Ssh' : 'ssh1v',
    'Stockmann a' : 'stcas',
    'Stockmann b' : 'stcbv',
    'Stora enso a' : 'steav',
    'Stora enso r' : 'sterv',
    'Suominen' : 'suy1v',
    'Taaleri' : 'taala',
    'Talenom' : 'tnom', 
    'Tallink' : 'tallink',
    'Tecnotree' : 'tem1v',
    'Teleste' : 'tlt1v',
    'Telia' : 'telia1',
    'Terveystalo' : 'ttalo',
    'Tieto' : 'tieto',
    'Tikkurila' : 'tik1v',
    'Tokmanni' : 'tokman',
    'Trainers house' : 'trh1v',
    'Tulikivi' : 'tulav',
    'Upm-Kymmene' : 'upm',
    'Uponor' : 'uponor',
    'Uutechnic' : 'uutec',
    'Vaisala' : 'vaias',
    'Valmet' : 'valmt',
    'Valoe' : 'valoe',
    'Viking line' : 'vik1v',
    'Wulff' : 'wuf1v',
    'Wärtsilä' : 'wrt1v',
    'Yit' : 'yit',
    'Yleiselektroniikka' : 'yeint',
    'Ålandsbanken a' : 'albav',
    'Ålandsbanken b' : 'albbv'
    
    }

def hae():
    stock = (Entry.get(osakenimi))#muuttujaan stock tallennetaan osakenimi-kenttään
    #kirjoitettu merkkijono
    alkukirjain = stock.capitalize()#alkukirjain muuttujaan tallennetaan toiminto,
    #joka muuttaa stock-muuttujan tekstin ensimmäisen kirjaimen isoksi kirjaimeksi.
    stock = osake.get(stock)
    osakenimi.delete(0,END)
    Entry.insert(osakenimi,0,alkukirjain)
    
    if kurssitieto.get() == 1 and osinkotieto.get() == 0: #jos valittuna on kurssi
        #tieto valintaruutu, avataan selain allaolevaan osoitteeseen. stock-muutuja
        #linkin lopussa on haettu osake.
        webbrowser.open('https://www.kauppalehti.fi/porssi/porssikurssit/osake/'+stock)
    elif kurssitieto.get() == 0 and osinkotieto.get() == 1: #jos valittuna on
        #osinkotieto valintaruutu, avataan selain allaolevaan osoitteenseen.
          webbrowser.open('https://www.is.fi/taloussanomat/osinkokalenteri/'+stock)
    elif kurssitieto.get () == 1 and osinkotieto.get() == 1: # jos valittuna on
        #molemmat valintaruudut, avataan selain kahteen allaolevaan osoitteeseen.
        webbrowser.open('https://www.kauppalehti.fi/porssi/porssikurssit/osake/'+stock)
        webbrowser.open('https://www.is.fi/taloussanomat/osinkokalenteri/'+stock)

def kryptoHaku():
    crypto = (Entry.get(kryptohaku))
    webbrowser.open('https://fi.investing.com/crypto/'+crypto)

def kysymys():
    messagebox.showinfo('?','jos kirjoitat osakkeen nimen pienellä alkukirjaimella, niin ohjelmaa muuntaa sen ensin isoksi'
                        'koska osakkeiden nimet on kirjoitettu sanakirjaan isolla kirjaimella. Muunnon jälkeen paina uudestaan hakupainiketta')
    

    

ikkuna = Tk()
ikkuna.configure(background = 'azure4')

dollari = PhotoImage(file = 'KurssihakuDollari.png')
dollarimerkki = dollari.subsample(3,3)

kryptologo = PhotoImage(file = 'KurssihakuKrypto.png')
kryptokuva = kryptologo.subsample(3,3)

ikkuna.title('Kurssihaku 1.0')
frame1 = Frame(ikkuna, background = 'azure4')
frame2 = Frame(ikkuna, background = 'azure4')
ohjnimi = Label(ikkuna, text = 'Kurssi- ja osinkohaku', background = 'azure3', fg = 'white')
osakenimi = Entry(frame1, width = 15, relief = 'solid', background = 'gray94')
kirjnimi = Label (ikkuna, text = 'Kirjoita osakkeen nimi kenttään', background = 'azure4')
haetieto = Button(ikkuna, text = 'Hae kurssi/osinko', command = hae, image = dollarimerkki, compound = RIGHT, relief = 'groove')

kysymysmerkki = Button (frame1, text = '?', command = kysymys)
kurssitieto = IntVar()
kurssivalinta = Checkbutton(ikkuna, text = 'Kurssi', variable = kurssitieto, background = 'azure3')
osinkotieto = IntVar()
osinkovalinta = Checkbutton(ikkuna, text = 'Osinko', variable = osinkotieto, background = 'azure4')
tyhja = Label(ikkuna, background = 'azure4')
tyhja2 = Label(ikkuna, background = 'azure4')
tyhja3 = Label(ikkuna, background = 'azure4')
krypto = Label(ikkuna, text='Hae kryptovaluuttoja', background='azure3')
kryptohaku = Entry(frame2, background = 'gray94', relief = 'solid')
kryptonimi = Label(frame2, text = 'Valuutan nimi: ', background = 'azure3')
kryptopainike = Button(ikkuna, text = 'Hae kryptoja', command = kryptoHaku, image = kryptokuva, compound = RIGHT)
                    

ohjnimi.pack()
kirjnimi.pack()
frame1.pack()
osakenimi.pack(side=LEFT)
kysymysmerkki.pack(side=RIGHT)
kurssivalinta.pack()
osinkovalinta.pack()
haetieto.pack()
tyhja.pack()
krypto.pack()
tyhja2.pack()
frame2.pack()
kryptonimi.pack()                   
kryptohaku.pack()
tyhja3.pack()
kryptopainike.pack()
mainloop()







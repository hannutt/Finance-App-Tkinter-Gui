import webbrowser #Tuodaan nettiselaimen käyttömahdollisuus ohjelmaan
from tkinter import* #Tkinter
from tkinter import messagebox


osake = { #Luodaan sanakirja, jossa osakkeen nimi ja sitä vastaava
    #kaupankäyntitunnus. Haku tehdään nettisivulta kaupankäyntitunnuksella.
    
    'afarak' : 'afagr',
    'ahlstrom-Munksjö' : 'am1',
    'aktia' : 'aktia',
    'alma-Media' : 'alma',
    'altia' : 'altia',
    'apetit' : 'apetit',
    'asiakastieto' : 'atg1v',
    'aspo' : 'aspo',
    'aspocomp' : 'acg1v',
    'atria' : 'atrav',
    'basware' : 'bas1v',
    'biohit' : 'biobv',
    'bittium' : 'bitti',
    'capman' : 'capman',
    'cargotec' : 'cgcbv',
    'caverion' : 'cav1v',
    'citycon' :  'cty1s',
    'componenta' : 'cth1v',
    'consti' : 'consti',
    'cramo' : 'cra1v',
    'digia' : 'digia',
    'digitalist' : 'digigr',
    'dna' : 'dna',
    'dovre' : 'dov1v',
    'eab' : 'eab',
    'efore' : 'efo1v',
    'elecster' : 'eleav',
    'elisa' : 'elisa',
    'endomines' : 'endom',
    'eq' : 'eqv1v',
    'ericsson' : 'eribr',
    'etteplan' : 'ette',
    'evli' : 'evli',
    'exel' : 'exl1v',
    'f-secure' : 'fsc1v',
    'finnair' : 'fia1s',
    'fiskars' : 'fskrs',
    'fortum' : 'fortum',
    'glaston' : 'gla1v',
    'harvia' : 'harvia',
    'hkscan' : 'hksav',
    'hoivatilat' : 'hoiva',
    'honkarakenne' : 'honbs',
    'huhtamäki' : 'huh1v',
    'ilkka-Yhtymä 1' : 'ilk1s',
    'ilkka-Yhtymä 2' : 'ilk2s',
    'incap' : 'icp1v',
    'innofactor' : 'ifa1v',
    'investors' : 'invest',
    'kamux' : 'kamux',
    'kemira' : 'kemira',
    'keskisuomalainen' : 'kslav',
    'kesko a' : 'keskoa',
    'kesko b' : 'keskob',
    'kesla' : 'kelas',
    'kojamo' : 'kojamo',
    'kone' : 'knebv',
    'konecranes' : 'kcr',
    'lassila & tikanoja' : 'lat1v',
    'lehto' : 'lehto',
    'marimekko' : 'mmo1v',
    'martela' : 'maras',
    'metso' : 'metso',
    'metsä board a' : 'metsa',
    'metsä board b' : 'metsb',
    'neo' : 'neo1v',
    'neste' : 'neste',
    'nixu' : 'nixu',
    'noho' : 'noho',
    'nokia' : 'nokia',
    'nokian renkaat' : 'tyres',
    'nordea' : 'nda%20fi',
    'nurminen' : 'nlg1v',
    'olvi' : 'olvas',
    'oma säästöpanki' : 'omasp',
    'oriola a' : 'okdav',
    'oriola b' : 'okdbv',
    'orion a' : 'ornav',
    'orion b' : 'ornbv',
    'outokumpu' : 'out1v',
    'outotec' : 'ote1v',
    'ovaro' : 'ovaro',
    'panostaja' : 'pna1v',
    'pihlajalinna' : 'pihlis',
    'ponsse' : 'pon1v',
    'punamusta' : 'pumu',
    'qpr' : 'qpr1v',
    'qt' : 'qtcom',
    'raisio k' : 'raikv',
    'raisio v' : 'raivv',
    'ramirent' : 'rami',
    'rapala' : 'rap1v',
    'raute' : 'raute',
    'revenio' : 'reg1v',
    'robit' : 'robit',
    'rovio' : 'rovio',
    'saga' : 'sagcv',
    'sampo' : 'sampo',
    'sanoma' : 'saa1v',
    'scanfil' : 'scanfl',
    'sievi' : 'sievi',
    'siili solutions' : 'siili',
    'silmäasema' : 'silma',
    'solteq' : 'solteq',
    'soprano' : 'sopra',
    'sotkamo silver' : 'sosi1',
    'srv' : 'srv1v',
    'ssab a' : 'ssabah',
    'ssab b' : 'ssabbh',
    'ssh' : 'ssh1v',
    'stockmann a' : 'stcas',
    'stockmann b' : 'stcbv',
    'stora enso a' : 'steav',
    'stora enso r' : 'sterv',
    'suominen' : 'suy1v',
    'taaleri' : 'taala',
    'talenom' : 'tnom', 
    'tallink' : 'tallink',
    'tecnotree' : 'tem1v',
    'teleste' : 'tlt1v',
    'telia' : 'telia1',
    'terveystalo' : 'ttalo',
    'tieto' : 'tieto',
    'tikkurila' : 'tik1v',
    'tokmanni' : 'tokman',
    'trainers house' : 'trh1v',
    'tulikivi' : 'tulav',
    'upm-Kymmene' : 'upm',
    'uponor' : 'uponor',
    'uutechnic' : 'uutec',
    'vaisala' : 'vaias',
    'valmet' : 'valmt',
    'valoe' : 'valoe',
    'viking line' : 'vik1v',
    'wulff' : 'wuf1v',
    'wärtsilä' : 'wrt1v',
    'yit' : 'yit',
    'yleiselektroniikka' : 'yeint',
    'ålandsbanken a' : 'albav',
    'ålandsbanken b' : 'albbv'
    
    }

def hae():
    stock = (Entry.get(osakenimi))#muuttujaan stock tallennetaan osakenimi-kenttään
    #kirjoitettu merkkijono
    stock = osake.get(stock)
    osakenimi.delete(0,END)
    Entry.insert(osakenimi,0,stock)
    
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
    messagebox.showinfo('?','Use only small letters. Example: If you want to look Nokia company stock price or dividend,'
                        'write in the field just nokia. ')
    

    

ikkuna = Tk()
ikkuna.configure(background = 'azure4')

dollari = PhotoImage(file = 'KurssihakuDollari.png')
dollarimerkki = dollari.subsample(3,3)

kryptologo = PhotoImage(file = 'KurssihakuKrypto.png')
kryptokuva = kryptologo.subsample(3,3)

ikkuna.title('Kurssihaku 1.0')
frame1 = Frame(ikkuna, background = 'azure4')
frame2 = Frame(ikkuna, background = 'azure4')
ohjnimi = Label(ikkuna, text = 'Stock price and dividend search', background = 'azure4', fg = 'white')
osakenimi = Entry(frame1, width = 15, relief = 'solid', background = 'gray94')
kirjnimi = Label (ikkuna, text = 'Enter the stock name in the field', background = 'azure3')
haetieto = Button(ikkuna, text = 'Check price/dividend', command = hae, image = dollarimerkki, compound = RIGHT, relief = 'groove')

kysymysmerkki = Button (frame1, text = '?', command = kysymys)
kurssitieto = IntVar()
kurssivalinta = Checkbutton(ikkuna, text = 'Price', variable = kurssitieto, background = 'azure3')
osinkotieto = IntVar()
osinkovalinta = Checkbutton(ikkuna, text = 'Dividend', variable = osinkotieto, background = 'azure4')
tyhja = Label(ikkuna, background = 'azure4')
tyhja2 = Label(ikkuna, background = 'azure4')
tyhja3 = Label(ikkuna, background = 'azure4')
krypto = Label(ikkuna, text='Crypto currency', background='azure3')
kryptohaku = Entry(frame2, background = 'gray94', relief = 'solid')
kryptonimi = Label(frame2, text = 'Currency name: ', background = 'azure3')
kryptopainike = Button(ikkuna, text = 'Check value', command = kryptoHaku, image = kryptokuva, compound = RIGHT)
                    

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







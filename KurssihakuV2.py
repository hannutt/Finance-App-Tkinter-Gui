import webbrowser #Tuodaan webbrowser-moduuli, jolla avataan selain ohjelmassa määriteltyihin
#osoitteisiin.
from tkinter import* #Tuodaan tkinter kirjasto.
from tkinter import messagebox #Tuodaan messagebox-moduuli, jonka avulla avataan ohjetekstit uusiin ikkunoihin.


osake = { #Luodaan sanakirja, jossa on osakkeen nimi ja sitä vastaava
    #kaupankäyntitunnus. Haku tehdään nettisivulta kaupankäyntitunnuksella, käyttäjän
    #tarvitsee kirjoittaa vain osakkeen nimi.
    
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

def hae():#funktio kurssi- ja osinkohakuihin.
    stock = (Entry.get(osakenimi))#muuttujaan stock tallennetaan osakenimi-kenttään
                                  #kirjoitettu haettavan osakkeen nimi.
    
    stock = stock.lower()#muutetaan syötetty merkkijono pieniksi kirjaimiksi, koska ne ovat myös
                        #sanakirjaan tallennettu pieninä kirjaimina. Näin ne saadaan vastaamaan toisiaan,
                        #eikä käyttäjän tarvitse miettiä minkälaista kirjoitusasua käyttää.
    
    stock = osake.get(stock)#haetaan osaketta vastaava kaupankäyntitunnus sanakirjasta.
    osakenimi.delete(0,END) #tyhjennnetään syötekenttä.
    Entry.insert(osakenimi,0,stock)#lisätään osakkeen nimen tilalle sen kaupankäyntitunnus.
    
    if kurssitieto.get() == 1 and osinkotieto.get() == 0: #jos valittuna on kurssi
        #tieto valintaruutu, avataan selain allaolevaan osoitteeseen. stock-muutuja
        #linkin lopussa on haetun osakkeen kaupankäyntitunnus.
        webbrowser.open('https://www.kauppalehti.fi/porssi/porssikurssit/osake/'+stock)
        
    elif kurssitieto.get() == 0 and osinkotieto.get() == 1: #jos valittuna on
        #osinkotieto valintaruutu, avataan selain allaolevaan osoitteeseen.
          webbrowser.open('https://www.is.fi/taloussanomat/osinkokalenteri/'+stock)
          
    elif kurssitieto.get () == 1 and osinkotieto.get() == 1: # jos valittuna on
        #molemmat valintaruudut, avataan selain kahteen allaolevaan osoitteeseen.
        webbrowser.open('https://www.kauppalehti.fi/porssi/porssikurssit/osake/'+stock)
        webbrowser.open('https://www.is.fi/taloussanomat/osinkokalenteri/'+stock)

def kryptoHaku(): #funktio kryptovaluuttojen hakemiseen.
    crypto = (Entry.get(kryptohaku))
    crypto = crypto.lower() #muunnetaan käyttäjän syöttämä merkkijono pieniksi kirjaimiksi.
    webbrowser.open('https://fi.investing.com/crypto/'+crypto)

def kysymys(): #funktio, joka suoritetaan kysymysmerkkiä painettaessa.
                #funkto avaa ohjetekstin erilliseen ikkunaan.
    messagebox.showinfo('?','Write stock name here. Example: If you want to look Nokia company stock price or dividend,'
                        'write in the field just Nokia. Do not use oy,ab etc. Just a company name.')
    

    

ikkuna = Tk()#luodaan pohjakomponetti.
ikkuna.configure(background = 'azure4')#asetetaan pohjakomponentin taustaväri.

#tuodaan ohjelmaan png-kuvat, joita käytetään painikkeissa kuvakkeinna.
dollari = PhotoImage(file = 'KurssihakuDollari.png')
dollarimerkki = dollari.subsample(3,3)

kryptologo = PhotoImage(file = 'KurssihakuKrypto.png')
kryptokuva = kryptologo.subsample(3,3)

ikkuna.title('Kurssihaku')

#luodaan frame-komponentit, joiden avulla asemoidaan muita komponentteja.
frame1 = Frame(ikkuna, background = 'azure4')
frame2 = Frame(ikkuna, background = 'azure4')

#luodaan tekstikomponentit label-komennolla, text-komennolla annetaan näytettävä teksti, backgound-komennolla
#taustaväri ja fg-komennolla fontin väri.
ohjnimi = Label(ikkuna, text = 'Stock price and dividend search', background = 'azure4', fg = 'white')
kirjnimi = Label (ikkuna, text = 'Enter the stock name in the field', background = 'azure3')
kryptonimi = Label(frame2, text = 'Currency name: ', background = 'azure3')
krypto = Label(ikkuna, text='Crypto currencies', background='azure3')

#luodaan syötekentät entry-komennolla.
osakenimi = Entry(frame1, width = 15, relief = 'solid', background = 'gray94')
kryptohaku = Entry(frame2, background = 'gray94', relief = 'solid')

#luodaan painikkeet button-komennolla, command-komennolla annetaan painikkeelle funktio joka suoritetaan, kun
#painiketta on painettu. image-komennolla liitetään aiemmin tuotu png-kuva painikkeeseen
#compound-komennolla asemoidaan kuva painikkeen oikeaan reunaan.

haetieto = Button(ikkuna, text = 'Check price/dividend', command = hae, image = dollarimerkki, compound = RIGHT, relief = 'groove')
kysymysmerkki = Button (frame1, text = '?', command = kysymys)
kryptopainike = Button(ikkuna, text = 'Check value', command = kryptoHaku, image = kryptokuva, compound = RIGHT)


#luodaan valintaikkunat.
kurssitieto = IntVar()
kurssivalinta = Checkbutton(ikkuna, text = 'Price', variable = kurssitieto, background = 'azure3')
osinkotieto = IntVar()
osinkovalinta = Checkbutton(ikkuna, text = 'Dividend', variable = osinkotieto, background = 'azure4')

                    
#pakataan komponentit, jolloin ne näkyvät ohjelmassa, side komennoilla komponentteja voidaan
#asemoida. pady komennolla lisätään tyhjää tilaa komponenttien väliin.
ohjnimi.pack()
kirjnimi.pack()
frame1.pack()
osakenimi.pack(side=LEFT, pady = 4)
kysymysmerkki.pack(side=RIGHT, pady = 4)
kurssivalinta.pack()
osinkovalinta.pack()
haetieto.pack(pady = 10)
krypto.pack(pady = 8)
frame2.pack()
kryptonimi.pack()                   
kryptohaku.pack(pady = 4)
kryptopainike.pack()
mainloop()







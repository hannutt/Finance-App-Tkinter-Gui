# Stock-dividend and Crypto currency value search

Put the KurssiHaku.png and KryptoHaku.png -files in the same folder with KurssihakuV2.py file. the The png-files are used as an icons in the program.

With this program you can check stock prices & crypto currency values fast and also look how much companies
pay dividends. At this moment you can search only companies, which are listed in Helsinki stock market.
You can also scrape some stock indexs values and currency rates.

Program includes two checbox. If you type a stock name to the first input field and choose "price" -checkbox and click
"Check price/dividend" button, program open a webbrowser and takes you to the Kauppalehti.fi/porssi/porssikurssi/osake/(*stock name, which you writed*) website, where you can see a stock price information.

Choosing a "dividend" -checkbox, program open a webbrowser and takes you to the is.fi/taloussanomat/osinkokalenteri/ (*stock name, which you writed*) website,
where you can see dividends, if the company pays a dividend

How the Crypto currency method works?
Just type the currency name to the "currency name" -input field and click "check value" -button.
Program take you to the /fi.investing.com/crypto/ (*cryptocurrency name which you writed*) website, where you can see a currency value.

Stock indexes and currency rates:

Click "stock indexes and currency rates" -button and program scrapes OMXHPI, OMXH25, OMXS30, DAX30, SXXP, NDX,INX, HXI, EUR-USD AND JPY-USD
values and rates from Arvopaperi.fi -webpage. Scraping is made with BeautifulSoup 4.

# Tietokantakuvaus

Tietokanta on täysin normalisoitu, mikä ei oikein sovi laskutukseen. Nyt, jos asiakkaan tai tuotteen tietoja muokataan, niin muutokset vaikuttavat myös vanhoihin laskuihin: esimerkiksi hinta muuttuu. Oikeasti laskulle pitäisi kopioida senhetkiset tiedot asiakkaasta ja tuotteesta el denormalisoida. Nykyisessä ratkaisussa asiakasta tai tuotetta ei voi poistaa, jos se esiintyy jollain laskulla.

Indeksejä on aika paljon. Pääavaimet indeksoidaan automaattisesti, mutta myös kaikki viiteavaimet on indeksoitu. Lisäksi on indeksoitu käyttäjien nimet ja salasanat sisäänkirjautumista varten. Tuoteryhmät on indeksoitu raportointia varten. Jos raportteja ajetaan harvoin, niin tuoteryhmien indeksoinnin mielekkyyden voi kyseenalaistaa.

![Kaavio](https://github.com/riihikallio/tsoha/blob/master/documentation/kaavio.png)

## SQL-taulujen luonti

`CREATE TABLE customer (
	number INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	address VARCHAR(255), 
	PRIMARY KEY (number)
)

CREATE TABLE product (
	number INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	unit VARCHAR(10) NOT NULL, 
	price FLOAT NOT NULL, 
	category VARCHAR(144) NOT NULL, 
	PRIMARY KEY (number)
)

CREATE TABLE account (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	username VARCHAR(144) NOT NULL, 
	password VARCHAR(144) NOT NULL, 
	PRIMARY KEY (id)
)

CREATE TABLE invoice (
	number INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	customer_num INTEGER NOT NULL, 
	account_id INTEGER NOT NULL, 
	PRIMARY KEY (number), 
	FOREIGN KEY(customer_num) REFERENCES customer (number), 
	FOREIGN KEY(account_id) REFERENCES account (id)
)

CREATE TABLE "row" (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	product_num INTEGER NOT NULL, 
	qty INTEGER NOT NULL, 
	invoice_num INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(product_num) REFERENCES product (number), 
	FOREIGN KEY(invoice_num) REFERENCES invoice (number)
)`

## Käytetyt SQL-kyselyt

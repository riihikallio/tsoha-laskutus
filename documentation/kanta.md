# Tietokantakuvaus

Tietokanta on täysin normalisoitu, mikä ei todellisuudessa oikein sovi laskutukseen. Nyt, jos asiakkaan tai tuotteen tietoja muokataan, niin muutokset vaikuttavat myös vanhoihin laskuihin: esimerkiksi hinta muuttuu. Oikeasti laskulle pitäisi kopioida senhetkiset tiedot asiakkaasta ja tuotteesta eli denormalisoida. Nykyisessä ratkaisussa  viite-eheyden varmistamiseksi asiakasta tai tuotetta ei voi poistaa, jos se esiintyy jollain laskulla. Denormalisoinnin yhteydessä voisi laskea rivisumman (product.price*row.qty) ja tallentaa sen riville valmiiksi. Laskun loppusumman tallentamista voisi harkita.

Todelliseen laskutussovellukseen tarvittaisiin lisää kenttiä: viitenumeroita, yhteyshenkilöitä, maksuehto, eräpäivä jne. Niiden toteuttaminen on kuitenkin suoraviivaista tämän rakenteen päälle.

Indeksejä on aika paljon. Pääavaimet indeksoidaan automaattisesti, mutta myös kaikki muut viiteavaimet on indeksoitu. Lisäksi on indeksoitu käyttäjien nimet ja salasanat sisäänkirjautumista varten. Tuoteryhmät ja asiakkaiden nimet on indeksoitu raportointia varten. Jos raportteja ajetaan harvoin, niin niiden indeksoinnin mielekkyyden voi kyseenalaistaa.

![Kaavio](https://github.com/riihikallio/tsoha/blob/master/documentation/kaavio.png)

## SQL-taulujen luonti

```sql
CREATE TABLE customer (
	number INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	address VARCHAR(255), 
	PRIMARY KEY (number)
)
CREATE INDEX ix_customer_name ON customer (name)

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
CREATE INDEX ix_product_category ON product (category)

CREATE TABLE account (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	username VARCHAR(144) NOT NULL, 
	password VARCHAR(144) NOT NULL, 
	PRIMARY KEY (id)
)
CREATE UNIQUE INDEX ix_account_username ON account (username)
CREATE INDEX ix_account_password ON account (password)

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
CREATE INDEX ix_invoice_customer_num ON invoice (customer_num)
CREATE INDEX ix_invoice_account_id ON invoice (account_id)

CREATE TABLE row (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	product_num INTEGER NOT NULL, 
	qty INTEGER NOT NULL, 
	invoice_num INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(product_num) REFERENCES product (number), 
	FOREIGN KEY(invoice_num) REFERENCES invoice (number)
)
CREATE INDEX ix_row_invoice_num ON row (invoice_num)
CREATE INDEX ix_row_product_num ON row (product_num)
```

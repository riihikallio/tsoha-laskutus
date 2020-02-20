# Tietokantakuvaus

Tietokanta on täysin normalisoitu, mikä ei oikein sovi laskutukseen. Nyt, jos asiakkaan tai tuotteen tietoja muokataan, niin muutokset vaikuttavat myös vanhoihin laskuihin: esimerkiksi hinta muuttuu. Oikeasti laskulle pitäisi kopioida senhetkiset tiedot asiakkaasta ja tuotteesta el denormalisoida. Nykyisessä ratkaisussa asiakasta tai tuotetta ei voi poistaa, jos se esiintyy jollain laskulla.

Indeksejä on aika paljon. Pääavaimet indeksoidaan automaattisesti, mutta myös kaikki viiteavaimet on indeksoitu. Lisäksi on indeksoitu käyttäjien nimet ja salasanat sisäänkirjautumista varten. Tuoteryhmät on indeksoitu raportointia varten. Jos raportteja ajetaan harvoin, niin indeksoinnin mielekkyyden voi kyseenalaistaa.

![Kaavio](https://github.com/riihikallio/tsoha/blob/master/documentation/kaavio.png)

## SQL-taulujen luonti

## Käytetyt SQL-kyselyt
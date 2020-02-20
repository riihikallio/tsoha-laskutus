# Asennus

## Paikallisesti

1. Lataa ohjelma esimerkiksi komennolla `git clone https://github.com/riihikallio/tsoha-laskutus`
2. Luo hakemiston sisällä virtuaaliympäristö komennolla `python3 -m venv venv`
3. Käynnistä virtuaaliympäristö komennolla `source venv/bin/activate`
4. Lataa tarvittavat kirjastot komennolla `pip install -r requirements.txt`
5. Käynnistä sovellus komennolla `python3 run.py`
6. Avaa selaimessa osoite <http://localhost:5000>

## Herokuun

Herokun määrittelyt voi tehdä joko selaimessa tai komentoriviltä asentamalla Herokun CLI-paketin. Tässä komentorivikomennot, koska ne on helpompi selittää.

1. Lisää Herokuun PostgreSQL-kanta komennolla `heroku addons:add heroku-postgresql:hobby-dev`
2. Määrittele Herokuun ympäristömuuttujalle *HEROKU* arvoksi 1 komennolla `heroku config:set HEROKU=1`
3. Luo Herokuun uusi sovellus komennolla `heroku create uniikki-nimi`
4. Lisätään Heroku Git-repoon remoteksi komennolla `git remote add heroku https://git.heroku.com/uniikki-nimi.git`
5. Lataa sovellus Herokuun komennolla `git push heroku master`

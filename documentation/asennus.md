# Asennus

## Paikallisesti

1. Lataa ohjelma esimerkiksi komennolla `git clone https://github.com/riihikallio/tsoha-laskutus`
2. Luo virtuaaliympäristö komennolla `python3 -m venv venv`
3. Käynnistä virtuaaliympäristö komennolla `source venv/bin/activate`
4. Lataa tarvittavat kirjastot komennolla `pip install -r requirements.txt`
5. Käynnistä sovellus komennolla `python3 run.py`
6. Avaa selaimessa osoite <http://localhost:5000>

## Herokuun

1. Lisää Herokuun PostgreSQL-kanta joko selaimessa tai komennolla `heroku addons:add heroku-postgresql:hobby-dev`
2. Määrittele Herokuun ympäristömuuttujalle *HEROKU* arvo 1 joka selaimessa tai komennolla `heroku config:set HEROKU=1`
3. Lataa sovellus Herokuun

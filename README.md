Game engine + game (Game of Thrones)
====================================

Deze repo bevat python-code voor de casus-opdracht voor Modelleren 2015.


Inhoud
------

Bestand     | Omschrijving
----------- | ------------------------------------------------------------
engine.py   | De game engine
got.py      | De Game of Thrones game voor de engine. (of een eerste aanzet hiertoe)
sql.py      | SQLite-helpers
inout.py    | input/output-helpers
init_db.sql | Initiele database setup-script voor de Game of Thrones game.


Dependencies
------------
De code maakt gebruik van enkele dependencies. Als je IDE ondersteuning biedt voor *requirements.txt* dan wordt dit automatisch voor je geregeld. Zo niet, voer dan het volgende commando uit in je console: *pip install -r requirements.txt*

Package  | Omschrijving
-------- | -------------------------------------------------------------------------
future   | Zorgt dat de code zowel Python2 als Python3 compatible is.
termcolor| Maakt het mogelijk kleuren te gebruiken in de console.
colorama | Maakt het mogelijk termcolor werkend te krijgen in de Windows 10 console.


Werking van de engine
---------------------

Wanneer je *engine.py* runt, wordt *got.py* ingeladen. De engine-cycle is als volgt:

Stap     | Functie
-------- | -------------------------------------------------------------------------
1.	Creeer de database **got.db** met het sql-script **init_db.sql**, wanneer deze niet bestaat| 
2.	Initialiseer de game | **got.init_game()**
3.	Herhaal zolang het spel niet voorbij is | **got.is_game_over()**
    3.1 Toon wereld-informatie | **got.toon_wereld_informatie**
    3.2 Voor 'Fase' 1 en 2 |
        3.2.1 Set 'Fase' (speler/computer aan de beurt) | wordt gezet in **game_state**
        3.2.2 Speel fase | **got.speel_fase()**
        3.2.3 Bepaald 'Actie' |	Haal uit **game_state**
        3.2.4 Als 'Actie' niet leeg is, voor actie uit | **got.[actie_naam]**
    3.3 Verplaats speler |	**got.verplaats()**
4.	Toon afsluitende tekst | **got.toon_game_over()**

De game-logica van Game of Thrones wordt dus compleet bepaald door de invulling van de desbestreffende functies in **got.py**.


Hulp-functies
-------------

**sql.py** bevat hulpfuncties voor het uitvoeren van SQL-queries. **inout.py** bevat hulp-functies voor invoer van de gebruiker en uitvoer naar het scherm.

Functie  | Omschrijving
-------- | -------------------------------------------------------------------------
inout.show_list(lst)          | print ieder element in de lijst *lst* op een aparte regel, voorafgaand met een "-"-teken.
inout.ask(text)               | print de string *question* in het blauw.
inout.warn(text)              | print de string *text* in het geel.
inout.choose(lst)	          | geeft de gebruiker de optie een element te kiezen uit de lijst *lst*. De huidige selectie is in het rood. Retourneert de keuze (string).
sql.column(query, *params)    | Voert de SQL-query *query* uit de database **got.db**, met optionele parameters *params* en retourneert de eerste kolom als een lijst.

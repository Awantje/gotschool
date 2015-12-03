from __future__ import unicode_literals
from __future__ import print_function
import random
import inout
from inout import ask
import sql

# region SQL

SQL_SPEELBARE_KARAKTERS = "SELECT naam FROM personages WHERE speelbaar = 1"
SQL_VRIENDEN = "SELECT met FROM vriendschappen WHERE naam == ?"
SQL_VREEMDEN = "SELECT naam FROM personages WHERE naam != ?"
SQL_ROL_VAN_KARAKTER = "SELECT rol FROM personages WHERE naam == ?"  # LEERTAAK 21: Maak mij kloppend.

# endregion


# region Initialization
# De volgende functies zijn van belang bij het opzetten van het spel.


def init_game(game_state):
    kies_speler(game_state)
    plaats_speler_in_begin_locatie(game_state)


def kies_speler(game_state):
    print("Met wie ga je dit spel spelen?")
    speelbare_karakters = sql.column(SQL_SPEELBARE_KARAKTERS)
    speler = inout.choose(speelbare_karakters)
    game_state['HoofdSpeler'] = speler


def plaats_speler_in_begin_locatie(game_state):
    game_state['Locatie'] = "King's Landing"


# endregion


# region Round Information


def toon_wereld_informatie(game_state):
    toon_huidig_land(game_state)
    print("")  # lege regel


def toon_huidig_land(game_state):
    huidig_land = game_state['Locatie']
    print("Je bent momenteel in " + huidig_land)

# endregion


# region Phase


def speel_fase(game_state):
    speler = game_state['HoofdSpeler']

    if speler == 'Jon Snow':
        game_state['Actie'] = 'bevecht'
    else:
        game_state['Actie'] = 'overtuig'

# endregion


# region Helpers

# LEERTAAK 22: Implementeer mij.
# - Vraag de speler om een keuze te maken tussen "rock", "paper" of "scissors".
# - Laat de tegenstander een keuze maken tussen "paper", "rock" of "scissors".
#   (deze keuze maakt de computer, gebruik hiervoor random.randrange).
# - Herhaal totdat beide spelers verschillende keuzes hebben
# - Retouneer of de speler gewonnen heeft.
# Wees creatief, misschien heb je geen loop nodig ;)
def speel_rock_paper_scissors():
    opties = ["Wat", "Zijn", "De", "Opties"]
    keuze = inout.choose(opties)
    print("Je koos voor " + keuze)
    return False


# endregion


# region Move

# NOT IMPLEMENTED
def verplaats(game_state):
    pass

# endregion


# region Actions

# LEERTAAK 23: Voltooi mij zoals omschreven in de spelregels.
# - Gebruik de rol van de tegenstander
# - Ga ook eerst na of er geen andere krijger is tussen de vreemden,
#   deze zal immers de strijd opeisen.
# - Print de status van de RondeSpeler en de status van de tegenstander
#   aan het einde van de functie.
def bevecht(game_state):
    ronde_speler = game_state['HoofdSpeler']

    vreemden = sql.column(SQL_VREEMDEN, ronde_speler)
    print("Tegen wie ga je strijden?")
    tegenstander = inout.choose(vreemden)
    rol_van_tegenstander = sql.column(SQL_ROL_VAN_KARAKTER, ronde_speler)[0]      # We nemen de eerste uit de lijst

    print("We gaan strijden!")

    winst = speel_rock_paper_scissors()

    if winst:
        print("Victorious!! " + tegenstander + " is voor altijd beschaamd en is verbannen uit deze wereld!")
    else:
        print("Verslagen... Je zult met eeuwige schaamte moeten leven en wordt verbannen voor in de eeuwigheid!")

    print(ronde_speler + " huppelt nog steeds vrolijk rond.")
    print(tegenstander + " huppelt lekker mee.")


# LEERTAAK 23: Voltooi mij zoals omschreven in de spelregels.
# - Gebruik de rol van de tegenstander
# - Ga ook eerst na of de tegenstander geen vriend is,
#   want dan hoef je niet te vechten (gebruik hiervoor SQL_VRIENDSCHAP).
# - Print de status van de RondeSpeler en de status van de tegenstander
#   aan het einde van de functie.
def overtuig(game_state):
    print("We gaan onderhandelen!")
    inout.choose(["Als", "We", "Opties", "Hadden"])


# endregion


# region Termination and finalization


# NOT IMPLEMENTED
def is_game_over(game_state):
    return False


# NOT IMPLEMENTED
def toon_game_over(game_state):
    pass

# endregion

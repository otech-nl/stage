# language: nl

Functionaliteit: Tochtenbeheer
	Als gebruiker
	Wil ik tochten beheren

	Achtergrond:
	Stel ik ben ingelogd
	
@navigatie
Scenario: naar het tochtoverzicht gaan
Stel ik ben niet op de pagina Tochten
Als ik op de link Tochten druk
Dan kom ik op de pagina Tochten
En zie ik een tabel met 3 kolommen "naam, datum, plaats"

Scenario: tocht toevoegen 
Als ik op de knop Tocht toevoegen druk
Dan zie ik een pagina Tocht bewerken


Scenario: lege tocht toevoegen
Stel ik ben op de tocht toevoegen pagina
En het veld naam is leeg
Als ik op de knop verwerken druk
Dan krijg ik een vul-dit-veld-in-melding bij het naamveld
En wordt er geen tocht toegevoegd

@dontdo
Scenario: tocht toevoegen
Stel ik ben op de tocht toevoegen pagina
Als ik vul een naam in in het naamveld
En ik op de knop verwerken druk
Dan wordt de tocht toegevoegd

@tabel
Scenario: tabel sorteren
Als ik in de tabel op plaats druk
Dan wordt de tabel op plaatsnaam gesorteerd

@tocht_bewerken
Scenario: naar tocht bewerken
Als ik in de tabel op een tocht druk
Dan kom ik op een Tocht bewerken pagina van die tocht

@deelnemer_toevoegen
Scenario: knop deelnemers toevoegen aan tochten
Stel ik ben op de tocht bewerken pagina
Als ik druk op de knop Aanmelden deelnemers
Dan kom ik op een pagina waar ik deelnemers kan toevoegen

@deelnemer_afmelden
Scenario: knop deelnemers afmelden voor een tocht
Stel ik ben op de tocht bewerken pagina
Als ik druk op de knop Afmelden deelnemers
Dan kom ik op een pagina waar ik deelnemers kan verwijderen

@afstand_toevoegen
Scenario: knop afstand toevoegen aan een tocht
Stel ik ben op de tocht bewerken pagina
Als ik druk op de knop Afstand toevoegen
Dan kom ik op een pagina waar ik afstanden kan toevoegen

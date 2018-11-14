# language: nl

Functionaliteit: Verenigingbeheer
	Als gebruiker
	Wil ik verenigingen beheren

	Achtergrond:
	Stel ik ben ingelogd

@navigatie
Scenario: naar verenigingoverzicht gaan
Stel ik ben niet op de pagina verenigingen
Als ik op de link Verenigingen druk
Dan zie ik de pagina vereniging-overzicht
En zie ik een tabel met 2 kolommen "afkorting, naam"

@vereniging_toevoegen_knop
Scenario: naar de vereniging toevoegen pagina
Stel ik ben op de pagina vereniging-overzicht
Als ik op de knop voeg vereniging toe druk
Dan zie ik een pagina waar ik een vereniging kan toevoegen

@vereniging_toevoegen_zonderafk
Scenario: een vereniging toevoegen zonder afkorting in te vullen
Stel ik ben op de pagina waar ik een vereniging kan toevoegen
En het veld afkorting is leeg
Als ik op de knop verwerken druk
Dan wordt er geen vereniging toegevoegd

@vereniging_toevoegen
Scenario: een vereniging toevoegen
Stel ik ben op de pagina waar ik een vereniging kan toevoegen
Als ik vul het veld afkorting in
En ik vuld het veld naam in
En ik op de knop verwerken druk
Dan wordt de vereniging toegevoegd
En verwijdert behave de vereniging voor volgende tests


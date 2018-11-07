# language: nl

Functionaliteit: Tochtenbeheer
	Als gebruiker
	Wil ik tochten beheren

	Achtergrond:
	Stel ik ben ingelogd
	

Scenario: naar het tochtoverzicht gaan
Stel ik ben niet op de pagina Tochten
Als ik op de link Tochten druk
Dan kom ik op de pagina Tochten

Scenario: tocht toevoegen 
Als ik op de knop Tocht toevoegen druk
Dan zie ik een pagina Tocht bewerken

Scenario: lege tocht toevoegen
Stel ik ben op de tocht bewerken pagina
En het veld naam is leeg
Als ik op de knop verwerken druk
Dan krijg ik een vul-dit-veld-in-melding bij het naamveld
En wordt er geen tocht toegevoegd

@dontdo
Scenario: tocht toevoegen
Stel ik ben op de tocht bewerken pagina
Als ik vul een naam in in het naamveld
En ik op de knop verwerken druk
Dan wordt de tocht toegevoegd

@werknougewoon
Scenario: tabel sorteren
Als ik in de tabel op plaats druk
Dan wordt de tabel op plaatsnaam gesorteerd

Scenario: naar tocht bewerken
Als ik in de tabel op een tocht druk
Dan kom ik op een Tocht bewerken pagina van die tocht

Scenario: deelnemers toevoegen aan tochten
Stel ik ben op de toch bewerken pagina ----------------< dit is een andere pagina dan boven
En ik druk op de knop Aanmelden deelnemers
Dan kom ik op een pagina waar ik deelnemers kan toevoegen





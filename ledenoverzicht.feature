# language: nl

Functionaliteit: Ledenoverzicht
	Als gebruiker
	Wil ik leden beheren

	Achtergrond:
	Stel ik ben ingelogd
		

Scenario: Naar het ledenoverzicht gaan
Stel ik ben niet op de pagina ledenoverzicht
Als ik op de knop Leden druk
Dan kom ik op de pagina Lid-overzicht
En zie ik een tabel met kolommen "voornaam, tussenvoegsel, achternaam, geslacht, plaats, lidnummer"

@lid_zoeken
Scenario: Lid zoeken
Stel ik ben op de pagina ledenoverzicht
Als ik in het zoekveld een achternaam invul
Dan zie ik alle leden met die achternaam
En leegt behave het zoekveld voor volgende tests

@alfabetisch_sorteren
Scenario: Leden op achternaam sorteren
Stel ik ben op de pagina ledenoverzicht
Als ik in de tabel op achternaam druk
Dan wordt de tabel op achternaam gesorteerd

@10results
Scenario: 10 resultaten weergeven
Stel ik ben op de pagina ledenoverzicht
Als ik 10 selecteer in het aantal resultaten weergeven
Dan krijg maximaal 10 resultaten per pagina te zien

@100results
Scenario: 100 resultaten weergeven
Stel ik ben op de pagina ledenoverzicht
Als ik 100 selecteer in het aantal resultaten weergeven
Dan krijg maximaal 100 resultaten per pagina te zien

@volgende_ledenpagina
Scenario: door de ledenpagina's navigeren
Stel ik ben op de pagina ledenoverzicht
En behave heeft een lijst van de tweede set van 10 leden
En ik zie 10 leden per pagina
Als ik op pagina 2 druk
Dan zie ik de tweede set van 10 leden

@unieke_lidnummers
Scenario: zijn lidnummer uniek
Stel ik ben op de pagina ledenoverzicht
En ik zie een tabel met honderd leden
Dan zijn de lidnummers van deze leden uniek



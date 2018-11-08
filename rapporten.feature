# language: nl

Functionaliteit: Rapporten
	Als gebruiker
	Wil ik lijst van rapporten bekijken

	Achtergrond:
	Stel ik ben ingelogd


@rapporten
Scenario: Naar lijst met rapporten gaan
Als ik op de knop Rapporten druk
Dan kom ik op de pagina Rapporten
En zie ik een lijst met verscheidene rapporten

@rapportennaw
Scenario: Link naar NAW Overzicht
Stel ik ben op de Rapporten pagina
Als ik op de link klik naar NAW Overzicht
Dan kom ik op de pagina NAW Overzicht
En krijg ik een lijst met adresgegevens NAW te zien

@rapportenhoodbewoners
Scenario: Link naar Hoofdbewoners
Stel ik ben op de Rapporten pagina
Als ik op de link klik naar Hoofdbewoners
Dan kom ik op de pagina Hoofdbewoners
En krijg ik een lijst met adresgegevens Hoofdbewoners te zien

@rapportencsv
Scenario: Download link naar Hoofdbewoners
Stel ik ben op de Rapporten pagina
Als ik op de CSV link klik
Dan zie ik de voltooide download in de Downloads map
En verwijder ik deze voor toekomstige tests


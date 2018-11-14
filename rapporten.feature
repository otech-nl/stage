# language: nl

Functionaliteit: Rapporten
	Als gebruiker
<<<<<<< HEAD
	Wil ik een lijst van rapporten bekijken
=======
	Wil ik lijst van rapporten bekijken
>>>>>>> e9d3b664b3d15999a883b86d7d0d997dd99ff6e7

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

<<<<<<< HEAD
@rapportenhbcsv
=======
@rapportencsv
>>>>>>> e9d3b664b3d15999a883b86d7d0d997dd99ff6e7
Scenario: Download link naar Hoofdbewoners
Stel ik ben op de Rapporten pagina
Als ik op de CSV link klik
Dan zie ik de voltooide download in de Downloads map
En verwijder ik deze voor toekomstige tests

<<<<<<< HEAD
@rapportenhbprint
Scenario: Link naar printbare pagina Hoofdbewoners
Stel ik ben op de Rapporten pagina
Als ik op de 'etiketten op naam'-link klik
Dan kom ik op een pagina met adresgegevens in makkelijk printbaar formaat

@rapportenhbprintpc
Scenario: Link naar printbare pagina Postcodes
Stel ik ben op de Rapporten pagina
Als ik op de 'etiketten op postcodes'-link klik
Dan kom ik op een pagina met postcodes in makkelijk printbaar formaat

@rapportenopzeggingen
Scenario: Link naar pagina met opzeggingen
Stel ik ben op de rapporten pagina
Als ik op de link klik naar Opzeggingen
Dan kom ik op de pagina met Opzeggingen
En krijg ik een lijst met Opzeggingen te zien

@rapportenexleden
Scenario: Link naar pagina met ex-leden
Stel ik ben op de rapporten pagina
Als ik op de link klik naar Ex-leden
Dan kom ik op de pagina met Ex-leden
En krijg ik een lijst met Ex-leden te zien

@rapportencategorie
Scenario: Link naar pagina met leden per categorie
Stel ik ben op de rapporten pagina
Als ik op de link klik naar Categorie-overzicht
Dan kom ik op de pagina Categorie-overzicht
En kan ik alle categorieen bekijken door op de links te klikken

=======
>>>>>>> e9d3b664b3d15999a883b86d7d0d997dd99ff6e7

# language: nl

Functionaliteit: Rapporten
	Als gebruiker
	Wil ik een lijst van rapporten bekijken

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

@rapportenhbcsv
Scenario: Download link naar Hoofdbewoners
Stel ik ben op de Rapporten pagina
Als ik op de CSV link klik
Dan zie ik de voltooide download in de Downloads map
En verwijder ik deze voor toekomstige tests

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

@rapportenledenopafstand
Scenario: Link naar pagina leden op afstand
Stel ik ben op de rapporten pagina
Als ik op de link klik naar Afstanden-overzicht
Dan kom ik op de pagina met leden op afstand
En krijg ik een lijst van leden op afstand

@rapportenledenopafstand
Scenario: Lijst sorteren op ingevulde afstanden
Stel ik ben op de pagina leden op afstand
Als ik een minimum en maximum afstand invul en op verwerken klik
Dan krijg ik een lijst van leden die tussen die afstanden vallen

@rapportenledenprovincie
Scenario: Link naar pagina met leden per provincie
Stel ik ben op de rapporten pagina
Als ik op de link klik naar Herkomst-overzicht
Dan kom ik op de pagina Herkomst-overzicht
En kan ik alle provincies bekijken door op de links te klikken



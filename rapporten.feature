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

@rapporteninschrijving
#moet nog gemaakt worden

@rapportenleeftijd
Scenario: Link naar pagina leden op geboortedatum
Stel ik ben op de rapporten pagina
Als ik op de link klik naar leeftijd en geboortedatum
Dan kom ik op de pagina met leden op geboortedatum
En krijg ik een zoekfunctie te zien

@rapportenleeftijd
Scenario: Zoeken op leeftijd
Stel ik ben op de pagina leden op geboortedatum
Als ik een datum en leeftijden invul in de zoekvelden
Dan kan ik zoeken op geboortedatum en leeftijdsbereik
En krijg ik een lijst met de gespecificeerde zoekcriteria

@rapportenbekers
#moet nog gemaakt worden

@rapportenemailexport
Scenario: Download voor Outlook-CSV
Stel ik ben op de rapporten pagina
Als ik klik op de link naar Email export
Dan zal er een CSV bestand downloaden
En die verwijder ik voor toekomstige tests

@rapportentochten
#moet nog gemaakt worden

@rapportenbetalingen
Scenario: Link naar uitleg betalingen
Stel ik ben op de rapporten pagina
Als ik op de uitleg link klik
Dan kom ik op de pagina met betalingsuitleg
En kan ik de links op deze pagina bezoeken

@rapporteneersteincasso
Scenario: Link naar eerste incasso
Stel ik ben op de rapporten pagina
Als ik op de Eerste incasso link klik
Dan kom ik op de pagina met eerste incassos
En krijg ik een lijst met machtigingsdata te zien

@rapportenvolgendeincasso
Scenario: Link naar volgende incasso
Stel ik ben op de rapporten pagina
Als ik op de Volgende incasso link klik
Dan kom ik op de pagina met de volgende incassos
En krijg ik een lijst met machtigingsdata te zien

@rapportenxmldownload
#moet nog gemaakt worden. link op de website werkt niet.

@rapportenxmltoelichting
Scenario: Link naar toelichting over XML download
Stel ik ben op de rapporten pagina
Als ik de Toelichting link klik
Dan kom ik op de tweede helft van de pagina met betalingsuitleg

@rapportenkaslijst
Scenario: Link naar lijst met leden die betalen per kas
Stel ik ben op de rapporten pagina
Als ik op de lijst link klik
Dan kom ik de pagina met een lijst van leden die betalen per kas

@rapportenkasetiketten
Scenario: Link naar pagina met etiketten van leden die betalen per kas
Stel ik ben op de rapporten pagina
Als ik op etiketten link klik
Dan kom ik op de pagina met etiketten van leden die betalen per kas

@rapportenoninbaar
Scenario: Link naar pagina met leden met oninbare contributie
Stel ik ben op de rapporten pagina
Als ik op de link naar de pagina met leden waarvoor geen contributie kan worden geind
Dan kom ik op de pagina met leden met oninbare contributie
En zie ik hier een lijst van

@rapportenbondsnummers
Scenario: Link naar de lijst met leden met dubbele bondsnummers
Stel ik ben op de rapporten pagina
Als ik op de Dubbele bondsnummers link klik
Dan kom ik op de pagina met leden met dubbele bondsnummers
En zie ik hier een lijst van

@rapportenadressendubbel
Scenario: Link naar de lijst met leden met dubbele adressen
Stel ik ben op de rapporten pagina
Als ik op de Dubbele adressen link klik
Dan kom ik op de pagina met leden met dubbele adressen


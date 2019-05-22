# language: nl

Functionaliteit: Rapporten
        Als gebruiker
        Wil ik een lijst van rapporten bekijken

  Achtergrond:
    Stel ik ben ingelogd als "Bestuurslid (FLAL)"


  @rapporten
  Scenario: Naar lijst met rapporten gaan
    Als ik op de knop "rapport" druk
    Dan zie ik de pagina "rapport"
    En zie ik een lijst met verscheidene rapporten

  Abstract Scenario: Adresgegevens
    Stel ik ben op de pagina "rapport"
    Als ik op de link "<link>" druk
    Dan zie ik de pagina "<link>"
    En krijg ik een lijst met adresgegevens te zien

    Voorbeelden:
      | link                      |
      | rapport/naw               |
      | rapport/hoofdbewoners/naw |
      | rapport/opgezegd |
      | rapport/ex |

  Abstract Scenario: Etiketten
    Stel ik ben op de pagina "rapport"
    Als ik op de link "<link>" druk
    Dan zie ik de pagina "<link>"
    En kom ik op een pagina met etiketten

    Voorbeelden:
      | link                      |
      | rapport/hoofdbewoners/etiketten               |
      | rapport/hoofdbewoners/postcode |
      | rapport/kas/etiketten |

  @rapportencategorie
  Scenario: Link naar pagina met leden per categorie
    Stel ik ben op de pagina "rapport"
    Als ik op de link "rapport/categorie" druk
    Dan zie ik de pagina "rapport/categorie"
    En kan ik alle categorieen bekijken door op de links te klikken


  @rapportenledenopafstand
  Scenario: Lijst sorteren op ingevulde afstanden
    Stel ik ben op de pagina "rapport/afstanden"
    Als ik het formulier invul met "min: 10000, max: 17500"
    En ik op de knop "Verwerken" druk
    Dan zie ik de pagina "rapport/afstanden"
    En krijg ik een ledenlijst met tekst "Leden naar afstand"

  @rapportenledenprovincie
  Scenario: Link naar pagina met leden per provincie
    Stel ik ben op de pagina "rapport"
    Als ik op de link "rapport/herkomst" druk
    Dan zie ik de pagina "rapport/herkomst"
    En kan ik alle provincies bekijken door op de links te klikken

  @rapporteninschrijving
  #moet nog gemaakt worden

  @rapportenleeftijd
  Scenario: Link naar pagina leden op geboortedatum
    Stel ik ben op de pagina "rapport"
    Als ik op de link "rapport/leeftijd" druk
    Dan zie ik de pagina "rapport/leeftijd"
    En krijg ik een zoekfunctie te zien

  @rapportenleeftijd
  Scenario: Zoeken op leeftijd
    Stel ik ben op de pagina "rapport/leeftijd"
    Als ik het formulier invul met "minimum_leeftijd: 40, maximum_leeftijd: 50"
    Dan kan ik zoeken op geboortedatum en leeftijdsbereik
    En krijg ik een ledenlijst te zien

  @rapportenbekers
  #moet nog gemaakt worden

  @skip
  Abstract Scenario: Downloads
    Stel ik ben op de pagina "rapport"
    Als ik op de link "<link>" druk
    Dan zie ik de voltooide download "<filename>" in de Downloads map
    En verwijder ik "<filename>" voor toekomstige tests

    Voorbeelden:
      | link                      | filename         |
      | rapport/export            | outlook.csv      |
      | rapport/hoofdbewoners/csv | leden            |

  @rapportenxmldownload
  # moet nog gemaakt worden. link op de website werkt niet.


  @rapportentochten
  # moet nog gemaakt worden

  @rapportenbetalingen
  Scenario: Link naar uitleg betalingen
    Stel ik ben op de pagina "rapport"
    Als ik op de link "rapport/uitleg" druk
    Dan zie ik de pagina "rapport/uitleg"
    En kan ik de links op deze pagina bezoeken

  Abstract Scenario: Tekst
    Stel ik ben op de pagina "rapport"
    Als ik op de link "<link>" druk
    Dan zie ik de pagina "<link>"
    En zie ik de tekst "<tekst>"

    Voorbeelden:
      | link                            | tekst                     |
      | rapport/incasso/report/eerste   | Rapport: eerste incasso   |
      | rapport/incasso/report/volgende | Rapport: volgende incasso |
      | rapport/dubbel_adres            | dubbele adressen          |

  @skip
  Scenario: Link naar toelichting over XML download
    Stel ik ben op de pagina "rapport"
    Als ik de Toelichting link klik
    Dan kom ik op de tweede helft van de pagina met betalingsuitleg

  Abstract Scenario: Ledenlijst
    Stel ik ben op de pagina "rapport"
    Als ik op de link "<link>" druk
    Dan zie ik de pagina "<link>"
    En krijg ik een ledenlijst met tekst "<tekst>"

    Voorbeelden:
      | link                       | tekst                          |
      | rapport/afstanden          | Leden naar afstand             |
      | rapport/kas/list           | leden die betalen per kas      |
      | rapport/oninbaar           | Leden met oninbare contributie |
      | rapport/dubbel_bondsnummer | dubbele bondsnummers           |

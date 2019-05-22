# language: nl

Functionaliteit: Ledenoverzicht
        Als gebruiker
        Wil ik leden beheren

  Achtergrond:
    Stel ik ben ingelogd als "Bestuurslid (FLAL)"


  Scenario: Naar het ledenoverzicht gaan
    Stel ik ben niet op de pagina "lid"
    Als ik op de knop "lid" druk
    Dan kom ik op de pagina "lid"
    En zie ik een tabel met kolommen "voornaam, tussenvoegsel, achternaam, geslacht, plaats, lidnummer"

  @lid_zoeken
  Scenario: Lid zoeken
    Stel ik ben op de pagina "lid"
    Als ik in het zoekveld "Jong" invul
    Dan zie ik alle leden met "Jong"
    En leegt behave het zoekveld voor volgende tests

  @alfabetisch_sorteren
  Scenario: Leden op achternaam sorteren
    Stel ik ben op de pagina "lid"
    Als ik in de tabel op "achternaam" druk
    Dan wordt de tabel op "achternaam" gesorteerd

  @10results
  Scenario: 10 resultaten weergeven
    Stel ik ben op de pagina "lid"
    Als ik 10 resultaten per pagina selecteer
    Dan krijg maximaal 10 resultaten per pagina te zien

  @100results
  Scenario: 100 resultaten weergeven
    Stel ik ben op de pagina "lid"
    Als ik 100 resultaten per pagina selecteer
    Dan krijg maximaal 100 resultaten per pagina te zien

  @volgende_ledenpagina
  Scenario: door de ledenpagina's navigeren
    Stel ik ben op de pagina "lid"
    En behave heeft een lijst van de tweede set van 10 leden
    Als ik 10 resultaten per pagina selecteer
    En ik op pagina 2 druk
    Dan zie ik de tweede set van 10 leden

  @unieke_lidnummers
  Scenario: zijn lidnummer uniek
    Stel ik ben op de pagina "lid"
    Als ik 100 resultaten per pagina selecteer
    Dan zijn de lidnummers van deze leden uniek

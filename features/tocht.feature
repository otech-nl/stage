# language: nl

Functionaliteit: Tochtenbeheer
        Als gebruiker
        Wil ik tochten beheren

  Achtergrond:
    Stel ik ben ingelogd als "Bestuurslid (FLAL)"

  @navigatie
  Scenario: naar het tochtoverzicht gaan
    Stel ik ben niet op de pagina "tocht"
    Als ik op de link "tocht" druk
    Dan kom ik op de pagina "tocht"
    En zie ik een tabel met kolommen "naam, datum, plaats"

  @skip
  Scenario: lege tocht toevoegen
    Stel ik ben op de pagina "tocht/0"
    En het veld naam is leeg
    Als ik op de knop "verwerken" druk
    Dan krijg ik een vul-dit-veld-in-melding bij het veld "naam"
    En wordt er geen tocht toegevoegd

  @skip
  Scenario: tocht toevoegen
    Stel ik ben op de pagina "tocht/0"
    Als ik 1 sec wacht
    En ik het formulier invul met "naam: testtocht"
    En ik op de knop "verwerken" druk
    Dan wordt de tocht toegevoegd
    En verwijdert behave de tocht voor volgende tests

  @tabel
  Scenario: tabel sorteren
    Als ik in de tabel op plaats druk
    Dan wordt de tabel op plaatsnaam gesorteerd

  @tocht_bewerken
  Scenario: naar tocht bewerken
    Stel ik ben op de pagina "tocht"
    Als ik in de tabel op een tocht druk
    Dan kom ik op een Tocht bewerken pagina van die tocht

  @skip
  Abstract Scenario: Deelnemers
    Stel ik ben op de pagina "registratie/11"
    Als ik het formulier invul met "<veld>: <waarde>"
    En ik op de knop "Verwerken" druk
    Dan is deelnemer "<waarde>" aan de tocht toegevoegd
    En verwijdert behave de deelnemer voor volgende tests

    Voorbeelden:
      | veld       | waarde |
      | achternaam | Jong   |
      | lidnummer  | 1111   |

  Abstract Scenario: Paginas
    Stel ik ben op de pagina "<start>"
    Als ik op de knop "<link>" druk
    En ik 1 sec wacht
    Dan zie ik de pagina "<link>"

    Voorbeelden:
      | start    | link           |
      # | tocht    | tocht/0        |
      | tocht/11 | registratie/11 |
      | tocht/11 | afmelding/11   |

  @skip
  Scenario: knop afstand toevoegen aan een tocht
    Stel ik ben op de pagina "tocht/11"
    Als ik op de knop "Afstand toevoegen" druk
    Dan zie ik de tekst "Afstanden:"

  @skip
  Scenario: eerstvolgende tocht bekijken
    Stel ik ben op de pagina "tocht"
    Als ik de eerstvolgende tocht bekijk
    Dan ligt die tocht in de toekomst
    En is er geen tocht die eerder komt

# language: nl

Functionaliteit: Vereniging
        Als beheerder van een vereniging
        wil ik de verenigingsdetails, beloningen en categorieën kunnen beheren

  Achtergrond:
    Stel ik ben ingelogd als "admin"


  Scenario: Details vereniging aanpassen
    Stel ik ben op de pagina "instellingen"
    Als ik het veld postcode wijzig
    En ik op de knop "Verwerken" druk
    Dan verwacht ik dat de gegevens worden opgeslagen

  @skip
  Scenario: Categorie toevoegen
    Stel ik ben op de pagina "instellingen"
    Als ik op de knop "categorie/new/2" druk
    En ik vul het formulier in met "naam: Testcategorie, contributie: 12"
    En ik op de knop "Verwerken" druk
    Dan verwacht ik dat de gegevens worden opgeslagen

  @navigatie
  Scenario: naar verenigingoverzicht gaan
    Stel ik ben niet op de pagina "union"
    Als ik op de link "union" druk
    Dan zie ik de pagina "union/"
    En zie ik een tabel met kolommen "afkorting, naam"

  @vereniging_toevoegen_knop
  Scenario: naar de vereniging toevoegen pagina
    Stel ik ben op de pagina "union"
    Als ik op de knop "vereniging/0" druk
    Dan zie ik de pagina "vereniging/0"

  @vereniging_toevoegen_zonderafk
  Scenario: een vereniging toevoegen zonder afkorting in te vullen
    Stel ik ben op de pagina "vereniging/0"
    En het veld afkorting is leeg
    Als ik op de knop "Verwerken" druk
    Dan wordt er geen vereniging toegevoegd

  @skip
  Scenario: een vereniging toevoegen
    Stel ik ben op de pagina "vereniging/0"
    Als ik vul het formulier in met "afkorting: TV, naam: TestVereniging"
    En ik op de knop "Verwerken" druk
    Dan wordt de vereniging toegevoegd
    En verwijdert behave de vereniging voor volgende tests

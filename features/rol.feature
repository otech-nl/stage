# language: nl

Functionaliteit: Rollenbeheer
        Als gebruiker
        Wil ik rollen beheren

  Achtergrond:
    Stel ik ben ingelogd als "admin"

  Scenario: naar het rollenoverzicht gaan
    Stel ik ben niet op de pagina "role"
    Als ik op de link "role" druk
    Dan zie ik de pagina "role/"

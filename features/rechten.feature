# language: nl

Functionaliteit: Gebruikersrechten
        Als Gebruiker van een vereniging
        Wil ik alleen de rechten van mijn rol hebben
        En alleen toegang hebben tot pagina's van mijn eigen vereniging

  @rechten
  Abstract Scenario: Inloggen
        Stel ik ben uitgelogd
        Als ik de inloggegevens van een "<naam>" invul
        Dan ben ik ingelogd
        En zie ik alleen links die een <rol> mag zien
        En kan ik niet via de adresbalk bij voor een <rol> illegale links komen

  Voorbeelden:
    | naam                | rol          |
    | Vrijwilliger (FLAL) | vrijwilliger |
    | Bestuurslid (FLAL)  | bestuurslid  |
    | Beheerder (FLAL)    | beheerder    |


  @skip
  Scenario: toernooipagina ipv tochtenpagina
    Stel ik ben ingelogd als "Beheerder (ACV)"
    Als ik op de link "toernooi" klik
    Dan kom ik op de pagina "Toernooi-overzicht"
    En zie ik een tabel met 3 kolommen "naam, datum, plaats"


  @toegang
  Abstract Scenario: Geen toegang tot lid van een andere vereniging
    Stel ik ben ingelogd als "<naam>"
    En ik ben op de pagina "lid"
    Als ik lidnummer <nummer> invul
    Dan vind ik dat lid niet

    Voorbeelden:
      | naam             | nummer |
      | Beheerder (FLAL) |    497 |
      | Beheerder (ACV)  |   1450 |

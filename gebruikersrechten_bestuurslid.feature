# language: nl

Functionaliteit: Gebruikersrechten - bestuurslid
	Als Bestuurslid
	Wil ik alleen de rechten van een bestuurslid hebben

@rechten	
Scenario: inloggen(FLAL)
Stel ik ben uitgelogd
Als ik de inloggegevens van een Bestuurslid (FLAL) invul
Dan wordt ik ingelogd

@rechten
Scenario: rechten(FLAL)
Stel ik ben als Bestuurslid (FLAL) ingelogd
Dan zie ik alleen de links die een bestuurslid mag zien
En kan ik niet via de adresbalk bij voor bestuurslid illegale links komen

@rechten
Scenario: inloggen(ACV)
Stel ik ben uitgelogd
Als ik de inloggegevens van een Bestuurslid (ACV) invul
Dan wordt ik ingelogd

@rechten
Scenario: rechten(ACV)
Stel ik ben als Bestuurslid (ACV) ingelogd
Dan zie ik alleen de links die een bestuurslid mag zien
En kan ik niet via de adresbalk bij voor bestuurslid illegale links komen

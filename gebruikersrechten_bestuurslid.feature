# language: nl

Functionaliteit: Gebruikersrechten - bestuurslid
	Als Bestuurslid
	Wil ik alleen de rechten van een bestuurslid hebben

	
Scenario: inloggen(FLAL)
Stel ik ben uitgelogd
Als ik de inloggegevens van een Bestuurslid (FLAL) invul
Dan wordt ik ingelogd

Scenario: rechten(FLAL)
Stel ik ben als Bestuurslid (FLAL) ingelogd
Dan zie ik alleen de links die een bestuurslid mag zien

Scenario: inloggen(ACV)
Stel ik ben uitgelogd
Als ik de inloggegevens van een Bestuurslid (ACV) invul
Dan wordt ik ingelogd

Scenario: rechten(ACV)
Stel ik ben als Bestuurslid (ACV) ingelogd
Dan zie ik alleen de links die een bestuurslid mag zien

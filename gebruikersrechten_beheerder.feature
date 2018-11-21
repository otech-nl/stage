# language: nl

Functionaliteit: Gebruikersrechten - beheerder
	Als Beheerder
	Wil ik alleen rechten van een beheerder hebben

@inlogr		
Scenario: inloggen(FLAL)
Stel ik ben uitgelogd
Als ik de inloggegevens van een Beheerder (FLAL) invul
Dan wordt ik ingelogd

@rechten
Scenario: rechten(FLAL)
Stel ik ben als Beheerder (FLAL) ingelogd
Dan zie ik alleen de links die een beheerder mag zien
En kan ik niet via de adresbalk bij voor beheerder illegale links komen

@inlogr
Scenario: inloggen(ACV)
Stel ik ben uitgelogd
Als ik de inloggegevens van een Beheerder (ACV) invul
Dan wordt ik ingelogd

@rechten
Scenario: rechten(ACV)
Stel ik ben als Beheerder (ACV) ingelogd
Dan zie ik alleen de links die een beheerder mag zien
En kan ik niet via de adresbalk bij voor beheerder illegale links komen

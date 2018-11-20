# language: nl

Functionaliteit: Gebruikersrechten - beheerder
	Als Beheerder
	Wil ik alleen rechten van een beheerder hebben

		
Scenario: inloggen(FLAL)
Stel ik ben uitgelogd
Als ik de inloggegevens van een Beheerder (FLAL) invul
Dan wordt ik ingelogd

Scenario: rechten(FLAL)
Stel ik ben als Beheerder (FLAL) ingelogd
Dan zie ik alleen de links die een beheerder mag zien

Scenario: inloggen(ACV)
Stel ik ben uitgelogd
Als ik de inloggegevens van een Beheerder (ACV) invul
Dan wordt ik ingelogd

Scenario: rechten(ACV)
Stel ik ben als Beheerder (ACV) ingelogd
Dan zie ik alleen de links die een beheerder mag zien



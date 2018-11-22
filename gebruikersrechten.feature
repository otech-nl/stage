# language: nl

Functionaliteit: Gebruikersrechten
	Als Gebruiker van een vereniging
	Wil ik alleen de rechten van mijn rol hebben
	En alleen toegang hebben tot pagina's van mijn eigen vereniging

@rechten		
Scenario: inloggen(FLAL)
Stel ik ben uitgelogd
Als ik de inloggegevens van een Vrijwilliger (FLAL) invul
Dan wordt ik ingelogd

@rechten
Scenario: rechten(FLAL)
Stel ik ben als Vrijwilliger (FLAL) ingelogd
Dan zie ik alleen links die vrijwilligers mogen zien
En kan ik niet via de adresbalk bij voor vrijwilliger illegale links komen

@rechten
Scenario: inloggen(ACV)
Stel ik ben uitgelogd
Als ik de inloggegevens van een Vrijwilliger (ACV) invul
Dan wordt ik ingelogd

@rechten
Scenario: rechten(ACV)
Stel ik ben als Vrijwilliger (ACV) ingelogd
Dan zie ik alleen links die vrijwilligers mogen zien
En kan ik niet via de adresbalk bij voor vrijwilliger illegale links komen

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

@rechten		
Scenario: inloggen(FLAL)
Stel ik ben uitgelogd
Als ik de inloggegevens van een Beheerder (FLAL) invul
Dan wordt ik ingelogd

@rechten
Scenario: rechten(FLAL)
Stel ik ben als Beheerder (FLAL) ingelogd
Dan zie ik alleen de links die een beheerder mag zien
En kan ik niet via de adresbalk bij voor beheerder illegale links komen

@rechten
Scenario: inloggen(ACV)
Stel ik ben uitgelogd
Als ik de inloggegevens van een Beheerder (ACV) invul
Dan wordt ik ingelogd

@rechten
Scenario: rechten(ACV)
Stel ik ben als Beheerder (ACV) ingelogd
Dan zie ik alleen de links die een beheerder mag zien
En kan ik niet via de adresbalk bij voor beheerder illegale links komen

# language: nl

Functionaliteit: Gebruikersrechten - vrijwilliger
	Als Vrijwilliger
	Wil ik alleen de rechten van een vrijwilliger hebben

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

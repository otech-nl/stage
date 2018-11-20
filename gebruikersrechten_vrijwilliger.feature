# language: nl

Functionaliteit: Gebruikersrechten - vrijwilliger
	Als Vrijwilliger
	Wil ik alleen de rechten van een vrijwilliger hebben

		
Scenario: inloggen(FLAL)
Stel ik ben uitgelogd
Als ik de inloggegevens van een Vrijwilliger (FLAL) invul
Dan wordt ik ingelogd

Scenario: rechten(FLAL)
Stel ik ben als Vrijwilliger (FLAL) ingelogd
Dan zie ik alleen links die vrijwilligers mogen zien

Scenario: inloggen(ACV)
Stel ik ben uitgelogd
Als ik de inloggegevens van een Vrijwilliger (ACV) invul
Dan wordt ik ingelogd

Scenario: rechten(ACV)
Stel ik ben als Vrijwilliger (ACV) ingelogd
Dan zie ik alleen links die vrijwilligers mogen zien



Feature: Inlog
	Als gebruiker
	Wil ik inloggen


Scenario: inloggen
Given ik ben niet ingelogd
When ik een geldige gebruikersnaam invoer
And ik het goede wachtwoord invoer
And ik op de knop inloggen druk
Then kom ik op de pagina Tochten



Feature: Pytest-BDD
	Een alternatief voor Behave

Scenario: Pytest-BDD proberen
	Given Pytest-BDD is geinstalleerd
	When ik deze test run
	Then passed de test

Scenario: inloggen
	Given ik ben niet ingelogd
	When ik een geldige gebruikersnaam invoer
	And ik het goede wachtwoord invoer
	And ik op de knop inloggen druk
	Then kom ik op de pagina Tochten
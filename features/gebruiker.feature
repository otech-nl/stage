# language: nl

Functionaliteit: Gebruikersbeheer
	Als gebruiker
	Wil ik gebruikers beheren

	Achtergrond:
	Stel ik ben ingelogd als "Beheerder (FLAL)"


Scenario: naar het gebruikersoverzicht gaan
Stel ik ben niet op de pagina "user"
Als ik op de link "user" druk
Dan zie ik de pagina "user/"

Scenario: gebruiker toevoegen pagina openen
Stel ik ben op de pagina "user"
Als ik op de knop gebruiker toevoegen druk
Dan zie ik de pagina om een gebruiker toe te voegen

@bewerkgebruiker
Scenario: gebruiker bewerken pagina openen
Stel ik ben op de pagina "user"
Als ik op een gebruiker druk
Dan zie ik de pagina om de gebruiker te bewerken

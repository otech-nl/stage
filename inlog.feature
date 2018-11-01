# language: nl

Functionaliteit: Inlog
	Als gebruiker
	Wil ik inloggen

	Achtergrond:
	Stel ik ben niet ingelogd

Scenario: verkeerd wachtwoord
Als ik een geldige gebruikersnaam invoer
En ik een verkeerd wachtwoord invoer
En ik op de knop inloggen druk
Dan krijg ik een verkeerd-wachtwoord-melding
En word ik niet ingelogd

Scenario: verkeerde gebruikersnaam
Als ik een verkeerde gebruikersnaam invoer
En ik een verkeerd wachtwoord invoer
En ik op de knop inloggen druk
Dan krijg ik een verkeerde-gebruikersnaam-melding
En word ik niet ingelogd

Scenario: inloggen
Als ik een geldige gebruikersnaam invoer
En ik het goede wachtwoord invoer
En ik op de knop inloggen druk
Dan kom ik op de pagina Tochten



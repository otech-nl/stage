Feature: Ledenoverzicht
        Als gebruiker
        Wil ik leden beheren

        Background:
        Given ik ben ingelogd
                

Scenario Loop 10: Naar het ledenoverzicht gaan
Given ik ben niet op de pagina ledenoverzicht
When ik op de knop Leden druk
Then kom ik op de pagina Lid-overzicht
And zie ik een tabel met kolommen "voornaam, tussenvoegsel, achternaam, geslacht, plaats, lidnummer"

@lid_zoeken
Scenario: Lid zoeken
Given ik ben op de pagina ledenoverzicht
When ik in het zoekveld een achternaam invul
Then zie ik alle leden met die achternaam
And leegt behave het zoekveld voor volgende tests

@alfabetisch_sorteren
Scenario: Leden op achternaam sorteren
Given ik ben op de pagina ledenoverzicht
When ik in de tabel op achternaam druk
Then wordt de tabel op achternaam gesorteerd

@10results
Scenario: 10 resultaten weergeven
Given ik ben op de pagina ledenoverzicht
When ik 10 selecteer in het aantal resultaten weergeven
Then krijg maximaal 10 resultaten per pagina te zien

@100results
Scenario: 100 resultaten weergeven
Given ik ben op de pagina ledenoverzicht
When ik 100 selecteer in het aantal resultaten weergeven
Then krijg maximaal 100 resultaten per pagina te zien

@volgende_ledenpagina
Scenario: door de ledenpagina's navigeren
Given ik ben op de pagina ledenoverzicht
And behave heeft een lijst van de tweede set van 10 leden
And ik zie 10 leden per pagina
When ik op pagina 2 druk
Then zie ik de tweede set van 10 leden

@unieke_lidnummers
Scenario: zijn lidnummer uniek
Given ik ben op de pagina ledenoverzicht
And ik zie een tabel met honderd leden
Then zijn de lidnummers van deze leden uniek

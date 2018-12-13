from radish import given, when, then
from radish import world


@given('ik ben niet ingelogd')
def niet_ingelogd(step):
    world.browser.visit(world.base_url)

@when('ik een geldige gebruikersnaam invoer')
def gebruikersnaam_invoeren():
    pass

@when('ik het goede wachtwoord invoer')
def wachtwoord_invoeren():
    pass

@when('ik op de knop inloggen druk')
def klik_inloggen():
    pass

@then('kom ik op de pagina Tochten')
def step_assert():
    pass
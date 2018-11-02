


@given('ik ben niet ingelogd')
def step_logged_off(context):
    loggedoff_url = '%s/login?next=%%2F' % context.base_url
    context.browser.visit(loggedoff_url)

@when('ik een geldige gebruikersnaam invoer')
def vul_gebruikersnaam_in(context):
    context.browser.find_by_id('email').first.fill('admin')

@when('ik een verkeerde gebruikersnaam invoer')
def vul_verkeerde_gebruikersnaam_in(context):
    context.browser.find_by_id('email').first.fill('verkeerd')

@when('ik het goede wachtwoord invoer')
def vul_wachtwoord_in(context):
    context.browser.find_by_id('password').first.fill('nimda')

@when('ik een verkeerd wachtwoord invoer')
def vul_verkeerd_wachtwoord_in(context):
    context.browser.find_by_id('password').first.fill('verkeerd')

@when('ik geen wachtwoord invoer')
def vul_geen_wachtwoord_in(context):
    context.browser.find_by_id('password').first.fill('')

@when('ik op de knop inloggen druk')
def klik_inloggen(context):
    context.browser.find_by_id('submit').first.click()

@then('kom ik op de pagina Tochten')
def inlog_tochten_pagina(context):
    assert context.browser.url == '%s/tocht/' % context.base_url

@then('krijg ik een verkeerd-wachtwoord-melding')
def verkeerd_wachtwoord_melding(context):
    assert context.browser.is_text_present('Invalid password')

@then('krijg ik een wachtwoord-ontbrekend-melding')
def wachtwoord_ontbrekend_melding(context):
    pass
    #Moet nog een assert voor komen
    #assert context.browser.is_text_present('Vul dit veld in')

@then('word ik niet ingelogd')
def inlog_mislukt(context):
    assert context.browser.url != '%s/tocht/' % context.base_url

@then('krijg ik een verkeerde-gebruikersnaam-melding')
def verkeerde_gebruikersnaam_melding(context):
    assert context.browser.is_text_present('Specified user does not exist')
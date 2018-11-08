from behave import given, when, then

@given('ik ben niet ingelogd')
def step_logged_off(context):
    context.browser.visit(context.base_url)
    loggedoff_url = '%s/login?next=%%2F' % context.base_url
    if context.browser.url != loggedoff_url:
        context.browser.find_link_by_partial_href('/logout').first.click()
    
@when('ik een geldige gebruikersnaam invoer')
def vul_gebruikersnaam_in(context):
    context.browser.find_by_id('email').first.fill('admin')
    
@when('ik een verkeerd wachtwoord invoer')
def vul_verkeerd_wachtwoord_in(context):
    context.browser.find_by_id('password').first.fill('verkeerd')
    
@when('ik op de knop inloggen druk')
def klik_inloggen(context):
    context.browser.find_by_id('submit').first.click()

@when('ik geen wachtwoord invoer')
def vul_geen_wachtwoord_in(context):
    context.browser.find_by_id('password').first.fill('')
    
@when('ik een verkeerde gebruikersnaam invoer')
def vul_verkeerde_gebruikersnaam_in(context):
    context.browser.find_by_id('email').first.fill('verkeerd')
    
@when('ik het goede wachtwoord invoer')
def vul_wachtwoord_in(context):
    context.browser.find_by_id('password').first.fill('nimda')
    
@then('krijg ik een verkeerd-wachtwoord-melding')
def verkeerd_wachtwoord_melding(context):
    assert context.browser.is_text_present('Invalid password')
    
@then('word ik niet ingelogd')
def inlog_mislukt(context):
    assert context.browser.url != '%s/tocht/' % context.base_url
    
@then('krijg ik een wachtwoord-ontbrekend-melding')
def wachtwoord_ontbrekend_melding(context):
    try:
        alert = context.browser.get_alert()
        assert alert.text == 'Please fill out this field'
    except:
        pass
    
                                                                         #Moet nog een assert voor komen
    #assert context.browser.is_text_present('Vul dit veld in')
    
@then('krijg ik een verkeerde-gebruikersnaam-melding')
def verkeerde_gebruikersnaam_melding(context):
    assert context.browser.is_text_present('Specified user does not exist')
    
@then('kom ik op de pagina Tochten')
def inlog_tochten_pagina(context):
    assert context.browser.url == '%s/tocht/' % context.base_url
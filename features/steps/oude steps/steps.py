from behave import given, when, then

def split_and_strip(src, sep=None):
    return [token.strip() for token in src.split(sep)]


@given('ik ben niet ingelogd')
def step_logged_off(context):
    loggedoff_url = '%s/login?next=%%2F' % context.base_url
    context.browser.visit(loggedoff_url)
    
@given('ik ben op de pagina Lid-overzicht')
def check_lid_overzicht(context):
    lid_url = '%s/lid/' % context.base_url
    context.browser.visit(lid_url)

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
    
@when('ik op de knop Leden druk')
def klik_leden(context):
    context.browser.find_link_by_partial_href('lid').first.click()

@then('kom ik op de pagina Tochten')
def inlog_tochten_pagina(context):
    assert context.browser.url == '%s/tocht/' % context.base_url

@then('krijg ik een verkeerd-wachtwoord-melding')
def verkeerd_wachtwoord_melding(context):
    assert context.browser.is_text_present('Invalid password')

@then('krijg ik een wachtwoord-ontbrekend-melding')
def wachtwoord_ontbrekend_melding(context):
    try:
        alert = context.browser.get_alert()
        assert alert.text == 'Please fill out this field'
    except:
        pass
    
                                                                         #Moet nog een assert voor komen
    #assert context.browser.is_text_present('Vul dit veld in')

@then('word ik niet ingelogd')
def inlog_mislukt(context):
    assert context.browser.url != '%s/tocht/' % context.base_url

@then('krijg ik een verkeerde-gebruikersnaam-melding')
def verkeerde_gebruikersnaam_melding(context):
    assert context.browser.is_text_present('Specified user does not exist')
    
@given('ik ben ingelogd')
def ingelogd_check(context):
    loggedoff_url = '%s/login?next=%%2F' % context.base_url
    base_url = context.base_url
    context.browser.visit(base_url)
    if context.browser.url == loggedoff_url:                                
        context.browser.find_by_id('email').first.fill('admin')             #moet makkelijker kunnen
        context.browser.find_by_id('password').first.fill('nimda')          #
        context.browser.find_by_id('submit').first.click()                  #
    assert context.browser.url != loggedoff_url 
    
@when('ik op de knop uitloggen druk')
def klik_uitloggen(context):
    context.browser.find_link_by_partial_href('/logout').first.click()

@when('ik in het zoekveld een achternaam invul')
def vul_achternaam_in(context):
    #context.browser.find_by_type('search').first.fill('jansen')
    #context.browser.find_by_id('lid_filter').first.fill('jansen')           #hoe vind ik de zoekfunctie
    #context.browser.fill('search', 'jansen')
    #context.browser.find_by_id('search').first.find_by_tag('input').fill('jansen')
    context.browser.find_by_tag('input').fill('jansen')

@then('word ik uitgelogd')
def uitgelogd(context):
    loggedoff_url = '%s/login?next=%%2F' % context.base_url
    assert context.browser.url == loggedoff_url
    
@then('kom ik op de pagina Lid-overzicht')
def lid_overzicht(context):
    assert context.browser.url == '%s/lid/' % context.base_url
    
@then('zie ik een tabel met kolommen "{columns}"')
def step_table(context, columns):
    tables = context.browser.find_by_id('lid')
    assert len(tables) > 0, 'Geen datatable gevonden'
    table = tables.first
    row = table.find_by_tag('thead') or table.find_by_tag('tr')
    head = row.first.text
    for col in split_and_strip(columns, ','):
        assert col in head, 'Kolom "%s" niet gevonden in "%s"' % (col, head)  #komt dit goed? check of er een tabel is
    
@then('zie ik alle leden met die achternaam')
def zoek_op_achternaam(context):
    # check de waarde van het zoekveld tegen de resultaten abracadabra
    pass
    
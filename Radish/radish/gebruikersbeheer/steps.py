from behave import given, when, then
from time import sleep

@given('ik ben niet op de pagina gebruikers')
def check_pagina_is_niet(context):
    if context.browser.url == '%s/user/' % context.base_url:
        context.browser.find_link_by_partial_href('tocht').first.click()
    
@when('ik op de link Gebruikers druk')
def druk_op_gebruikers(context):
    context.browser.find_link_by_partial_href('user').first.click()
    
@then('zie ik de pagina gebruikersoverzicht')
def check_pagina(context):
    assert context.browser.url == '%s/user/' % context.base_url
    
@given('ik ben op de pagina gebruikers')
def check_pagina(context):
    if context.browser.url != '%s/user/' % context.base_url:
        context.browser.visit('%s/user/' % context.base_url)
        
@when('ik op de knop gebruiker toevoegen druk')
def druk_op_toevoegen(context):
    context.browser.find_link_by_partial_href('user/0').first.click()
    
@then('zie ik de pagina om een gebruiker toe te voegen')
def check_pagina(context):
    assert context.browser.url == '%s/user/0' % context.base_url

@when('ik op een gebruiker druk')
def druk_op_een_gebruiker(context):
    table = context.browser.find_by_css('table.table')
    assert len(table) > 0, 'geen table gevonden'
    tabel = context.browser.find_by_tag('tbody')                 
    rows = tabel.find_by_tag('tr')
    cell = rows[0].find_by_tag('td')
    context.naamGebruiker = cell.value
    cell.click() 

@then('zie ik de pagina om de gebruiker te bewerken')
def check_pagina(context):
    assert context.naamGebruiker == context.browser.find_by_id('email').value

    

from behave import given, when, then

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
    pass                                  #hoe behandel je een tabel???

@then('zie ik de pagina om de gebruiker te bewerken')
def check_pagina(context):
    pass
    #assert context.browser.url != '%s/user/0' % context.base_url
                                        #   |ligt eraan welke gebruiker je aanklikt
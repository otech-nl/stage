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
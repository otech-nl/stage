from behave import given, when, then

@given('ik ben niet op de pagina rollen')
def check_pagina_is_niet(context):
    if context.browser.url == '%s/role/' % context.base_url:
        context.browser.find_link_by_partial_href('tocht').first.click()
    
@when('ik op de link Rollen druk')
def druk_op_rollen(context):
    context.browser.find_link_by_partial_href('role').first.click()
    
@then('zie ik de pagina rollenoverzicht')
def check_pagina(context):
    assert context.browser.url == '%s/role/' % context.base_url
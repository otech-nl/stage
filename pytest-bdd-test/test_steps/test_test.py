from pytest_bdd import scenario, given, when, then, parsers
from splinter import Browser
import pytest
import os
import re
from time import sleep

#@scenario('features/test.feature', 'Pytest-BDD proberen')
#def test_proberen():
#    pass

#@given('Pytest-BDD is geinstalleerd')
#def pytest_bdd_installed():
#    pass

#@when('ik deze test run')
#def ren_test():
#    pass

#@then('passed de test')
#def test_succesvol():
#    pass

@scenario('features/test.feature', 'inloggen')
def test_inloggen():
    pass
    
@given('ik ben niet ingelogd')
def step_logged_off(context):
    context.browser.visit(context.base_url)
    loggedoff_url = '%s/login?next=%%2F' % context.base_url
    if context.browser.url != loggedoff_url:
        context.browser.find_link_by_partial_href('/logout').first.click()
        
@when('ik een geldige gebruikersnaam invoer')
def vul_gebruikersnaam_in(context):
    context.browser.find_by_id('email').first.fill('admin')
    
@when('ik het goede wachtwoord invoer')
def vul_wachtwoord_in(context):
    context.browser.find_by_id('password').first.fill('nimda')
    
@when('ik op de knop inloggen druk')
def klik_inloggen(context):
    context.browser.find_by_id('submit').first.click()
    
@then('kom ik op de pagina Tochten')
def inlog_tochten_pagina(context):
    assert context.browser.url == '%s/tocht/' % context.base_url
    
@scenario('features/test.feature', 'door de ledenpagina\'s navigeren')
def test_navigatie():
    pass

@given('ik ben op de pagina ledenoverzicht')
def ledenoverzicht(context):
    if context.browser.url != '%s/lid/' % context.base_url:
        context.browser.visit('%s/lid/' % context.base_url)

@given('behave heeft een lijst van de tweede set van 10 leden')
def stel_lijst_samen(context):
    context.browser.find_option_by_text('25').first.click()
    table = context.browser.find_by_tag('tbody')                  
    rows = table.find_by_tag('tr')                                
    lijst = [row.find_by_tag('td')[2].value for row in rows] 
    context.lijst2 = lijst[10:20]

@given('ik zie 10 leden per pagina')
def bekijk_10_leden(context):
    context.browser.find_option_by_text('10').first.click()

@when('ik op pagina 2 druk')
def klik_pagina(context):
    pad = context.browser.is_element_present_by_xpath('//ul/li/a[@data-dt-idx="2"]')
    if pad:
        context.browser.find_by_xpath('//ul/li/a[@data-dt-idx="2"]').click()
    else:
        try:
            sleep(10)
            context.browser.find_by_xpath('//ul/li/a[@data-dt-idx="2"]').click()
        except:
            assert 0, 'pagina niet correct geladen'
            
      
@then('zie ik de tweede set van 10 leden')
def check_lijst_tegen_lijst(context):
    if context.browser.is_element_present_by_tag('tbody'):
        sleep(0)
    else:
        sleep(5)
    table = context.browser.find_by_tag('tbody')                  
    rows = table.find_by_tag('tr')                                
    lijst = [row.find_by_tag('td')[2].value for row in rows] 
    assert lijst == context.lijst2, str(lijst) + ' is niet ' + str(context.lijst2)
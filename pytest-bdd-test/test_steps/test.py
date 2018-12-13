from pytest_bdd import scenario, given, when, then
from splinter import Browser
import pytest
import os
import re
from time import sleep

#HEADLESS = True
#HEADLESS = False


@scenario('features/test.feature', 'Pytest-BDD proberen')
def test_proberen():
    pass

@given('Pytest-BDD is geinstalleerd')
def pytest_bdd_installed():
    pass

@when('ik deze test run')
def ren_test():
    pass

@then('passed de test')
def test_succesvol():
    pass

@scenario('features/test.feature', 'inloggen')
def test_proberen():
    pass
    
@given('ik ben niet ingelogd')
def step_logged_off(context):
    context.browser.visit(context.base_url)
    loggedoff_url = '%s/login?next=%%2F' % context.base_url
    if context.browser.url != loggedoff_url:
        context.browser.find_link_by_partial_href('/logout').first.click()
        
@when('ik een geldige gebruikersnaam invoer')
def vul_gebruikersnaam_in(browser):
    browser.find_by_id('email').first.fill('admin')
    
@when('ik het goede wachtwoord invoer')
def vul_wachtwoord_in(browser):
    browser.find_by_id('password').first.fill('nimda')
    
@when('ik op de knop inloggen druk')
def klik_inloggen(browser):
    browser.find_by_id('submit').first.click()
    
@then('kom ik op de pagina Tochten')
def inlog_tochten_pagina(browser, base_url):
    assert browser.url == '%s/tocht/' % base_url
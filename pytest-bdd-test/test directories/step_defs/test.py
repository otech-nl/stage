from pytest_bdd import scenario, given, when, then
from splinter import Browser
import pytest
import os
import re
from time import sleep

HEADLESS = True
HEADLESS = False


def _mk_tmp(request, factory):
    name = request.node.name
    name = re.sub(r"[\W]", "_", name)
    MAXVAL = 30
    name = name[:MAXVAL]
    return factory.mktemp(name, numbered=True)

@pytest.fixture(scope='session')
def session_tmpdir(request, tmpdir_factory):
    """pytest tmpdir which is session-scoped."""
    return _mk_tmp(request, tmpdir_factory)

@pytest.fixture
def context():
    class Context(object):
        pass
    return Context

@pytest.fixture(autouse=True, scope='session')
def setup(request):
    os.environ['QT_QPA_PLATFORM'] = 'offscreen'
    #global base_url
    context.base_url = 'http://192.168.2.66' #testserver
    #request.session = None  # for requests
    #if os.name == 'posix':
    global browser
    browser = Browser('chrome',
                                  executable_path='/usr/lib/chromium-browser/chromedriver',
                                  headless=HEADLESS)
    def fin():
        browser.quit()
    request.addfinalizer(fin)

#browser = Browser


@scenario('features/test.feature', 'Pytest-BDD proberen')
def test_proberen():
    pass

@given('Pytest-BDD is geinstalleerd')
def pytest_bdd_installed(context):
    browser.visit(context.base_url)

@when('ik deze test run')
def ren_test():
    browser.find_by_id('email').first.fill('admin')
    sleep(3)

@then('passed de test')
def test_succesvol():
    assert browser.url == 'henk', browser.url

@scenario('features/test.feature', 'inloggen')
def test_proberen():
    pass
    
@given('ik ben niet ingelogd')
def step_logged_off():
    browser.visit(context.base_url)
    loggedoff_url = '%s/login?next=%%2F' % context.base_url
    if browser.url != loggedoff_url:
        browser.find_link_by_partial_href('/logout').first.click()
        
@when('ik een geldige gebruikersnaam invoer')
def vul_gebruikersnaam_in():
    browser.find_by_id('email').first.fill('admin')
    
@when('ik het goede wachtwoord invoer')
def vul_wachtwoord_in():
    browser.find_by_id('password').first.fill('nimda')
    
@when('ik op de knop inloggen druk')
def klik_inloggen():
    browser.find_by_id('submit').first.click()
    
@then('kom ik op de pagina Tochten')
def inlog_tochten_pagina():
    assert browser.url == '%s/tocht/' % context.base_url
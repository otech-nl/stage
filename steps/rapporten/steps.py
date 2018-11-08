from behave import given, when, then
from pathlib import Path
import os.path
import time
import os

@when('ik op de knop Rapporten druk')
def klik_rapporten(context):
    context.browser.find_link_by_partial_href('rapport').first.click()
    
@then('kom ik op de pagina Rapporten')
def pagina_rapporten(context):
    assert context.browser.url == '%s/rapport' % context.base_url
    
@then('zie ik een lijst met verscheidene rapporten')
def lijst_rapporten(context):
    assert context.browser.find_by_xpath('//*[@id="main"]/ul')
    
@given('ik ben op de Rapporten pagina')
def check_pagina_rapporten_naw(context):
    context.browser.find_link_by_partial_href('rapport').first.click()
    
@when('ik op de link klik naar NAW Overzicht')
def klik_link_naw(context):
    context.browser.find_link_by_partial_href('rapport/naw').first.click()
    
@then('kom ik op de pagina NAW Overzicht')
def check_pagina_naw(context):
    assert context.browser.url == '%s/rapport/naw' % context.base_url
    
@then('krijg ik een lijst met adresgegevens NAW te zien')
def check_adresgegevens_naw(context):
    assert context.browser.find_by_xpath('/html/body/div/table')
      
@when('ik op de link klik naar Hoofdbewoners')
def klik_link_naw(context):
    context.browser.find_link_by_partial_href('rapport/hoofdbewoners/naw').first.click()
    
@then('kom ik op de pagina Hoofdbewoners')
def check_pagina_naw(context):
    assert context.browser.url == '%s/rapport/hoofdbewoners/naw' % context.base_url
    
@then('krijg ik een lijst met adresgegevens Hoofdbewoners te zien')
def check_adresgegevens_naw(context):
    assert context.browser.find_by_xpath('/html/body/div/table')
    
@when('ik op de CSV link klik')
def click_csv(context):
    context.browser.find_link_by_partial_href('rapport/hoofdbewoners/csv').first.click()
    time.sleep(1)
    
@then('ik navigeer naar Chrome downloads')
def navigate_chromedownloads(context):
    chromedownloads_url = 'chrome://downloads/'
    context.browser.visit(chromedownloads_url) 
    
@then('zie ik de voltooide download in de Downloads map')
def check_download_complete(context):
    assert os.path.isfile(os.path.expanduser('~/Downloads/leden.csv'))
    
@then('verwijder ik deze voor toekomstige tests')
def delete_download(context):
    os.remove(os.path.expanduser('~/Downloads/leden.csv'))
    

from behave import given, when, then
#from selenium import webdriver
#driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')
#from selenium.webdriver.common.keys import Keys
import os.path
import time

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
def click_csvhb(context):
    context.browser.find_link_by_partial_href('rapport/hoofdbewoners/csv').first.click()
    time.sleep(1)
    
@then('zie ik de voltooide download in de Downloads map')
def check_download_complete(context):
    assert os.path.isfile(os.path.expanduser('~/Downloads/leden.csv'))
    
@then('verwijder ik deze voor toekomstige tests')
def delete_download(context):
    os.remove(os.path.expanduser('~/Downloads/leden.csv'))
    
@when("ik op de 'etiketten op naam'-link klik")
def click_etiketten(context):
    context.browser.find_link_by_partial_href('rapport/hoofdbewoners/etiketten').first.click()
    
@then('kom ik op een pagina met adresgegevens in makkelijk printbaar formaat')
def check_page_etiketten(context):
    assert context.browser.url == '%s/rapport/hoofdbewoners/etiketten' % context.base_url
    assert context.browser.find_by_css('.etiketten')
    
@when("ik op de 'etiketten op postcodes'-link klik")
def click_postcodes(context):
    context.browser.find_link_by_partial_href('rapport/hoofdbewoners/postcode').first.click()
    
@then('kom ik op een pagina met postcodes in makkelijk printbaar formaat')
def check_page_postcodes(context):
    assert context.browser.url == '%s/rapport/hoofdbewoners/postcode' % context.base_url
    assert context.browser.find_by_css('.etiketten')
    
@when('ik op de link klik naar Opzeggingen')
def click_opzeggingen(context):
    context.browser.find_link_by_partial_href('rapport/opgezegd').first.click()
    
@then('kom ik op de pagina met Opzeggingen')
def check_page_opzeggingen(context):
    assert context.browser.url == '%s/rapport/opgezegd' % context.base_url
    
@then('krijg ik een lijst met Opzeggingen te zien')
def check_list_opzeggingen(context):
    assert context.browser.find_by_css('.display')

@when('ik op de link klik naar Ex-leden')
def click_exleden(context):
    context.browser.find_link_by_partial_href('rapport/ex').first.click()

@then('kom ik op de pagina met Ex-leden')
def check_page_exleden(context):
    assert context.browser.url == '%s/rapport/ex' % context.base_url
    
@then('krijg ik een lijst met Ex-leden te zien')
def check_list_exleden(context):
    assert context.browser.find_by_css('.display')

@when('ik op de link klik naar Categorie-overzicht')
def click_categorie(context):
    context.browser.find_link_by_partial_href('rapport/categorie').first.click()

@then('kom ik op de pagina Categorie-overzicht')
def check_page_categorie(context):
    assert context.browser.url == '%s/rapport/categorie' % context.base_url

@then('kan ik alle categorieen bekijken door op de links te klikken')
def check_collapse_categorie(context):
    context.browser.find_by_css('div.panel:nth-child(1) > div:nth-child(1) > h3:nth-child(1) > a:nth-child(1)').click()
    assert context.browser.find_by_css('.collapse.in')
    context.browser.find_by_css('div.panel:nth-child(1) > div:nth-child(1) > h3:nth-child(1) > a:nth-child(1)').click()
    time.sleep(1)
    context.browser.find_by_css('div.panel:nth-child(2) > div:nth-child(1) > h3:nth-child(1) > a:nth-child(1)').click()
    assert context.browser.find_by_css('.collapse.in')
    context.browser.find_by_css('div.panel:nth-child(2) > div:nth-child(1) > h3:nth-child(1) > a:nth-child(1)').click()
    time.sleep(1)
    context.browser.find_by_css('div.panel:nth-child(3) > div:nth-child(1) > h3:nth-child(1) > a:nth-child(1)').click()
    assert context.browser.find_by_css('.collapse.in')
    context.browser.find_by_css('div.panel:nth-child(3) > div:nth-child(1) > h3:nth-child(1) > a:nth-child(1)').click()
    time.sleep(1)
    context.browser.find_by_css('div.panel:nth-child(4) > div:nth-child(1) > h3:nth-child(1) > a:nth-child(1)').click()
    assert context.browser.find_by_css('.collapse.in')
    context.browser.find_by_css('div.panel:nth-child(4) > div:nth-child(1) > h3:nth-child(1) > a:nth-child(1)').click()
    time.sleep(1)
    context.browser.find_by_css('div.panel:nth-child(5) > div:nth-child(1) > h3:nth-child(1) > a:nth-child(1)').click()
    assert context.browser.find_by_css('.collapse.in')
    context.browser.find_by_css('div.panel:nth-child(5) > div:nth-child(1) > h3:nth-child(1) > a:nth-child(1)').click()
    time.sleep(1)
    context.browser.find_by_css('div.panel:nth-child(6) > div:nth-child(1) > h3:nth-child(1) > a:nth-child(1)').click()
    assert context.browser.find_by_css('.collapse.in')
    context.browser.find_by_css('div.panel:nth-child(6) > div:nth-child(1) > h3:nth-child(1) > a:nth-child(1)').click()
    #assert context.browser.find_by_id('categorie_1')
    #assert context.browser.find_by_css('.collapse.in')

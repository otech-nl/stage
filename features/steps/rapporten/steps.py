from behave import given, when, then
from random import randint
#from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
import os.path
import time

#driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')

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
    assert not os.path.isfile(os.path.expanduser('~/Downloads/leden.csv'))
    
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

@when('ik op de link klik naar Afstanden-overzicht')
def click_link_afstanden(context):
    context.browser.find_link_by_partial_href('rapport/afstanden').first.click()

@then('kom ik op de pagina met leden op afstand')
def check_page_afstanden(context):
    assert context.browser.url == '%s/rapport/afstanden' % context.base_url
    assert context.browser.is_text_present('Leden naar afstand')

@then('krijg ik een lijst van leden op afstand')
def check_list_afstanden(context):
    assert context.browser.find_by_css('.display')
    assert context.browser.is_text_present('km)')

@given('ik ben op de pagina leden op afstand')
def check_page_afstanden(context):
    if context.browser.url == '%s/rapport/afstanden' % context.base_url:
        pass
    else:
        context.browser.visit('%s/rapport' % context.base_url)
        context.browser.find_link_by_partial_href('rapport/afstanden').first.click()
        assert context.browser.url == '%s/rapport/afstanden' % context.base_url
        assert context.browser.is_text_present('Leden naar afstand')

@when('ik een minimum en maximum afstand invul en op verwerken klik')
def fill_afstanden(context):
    randomminafstand = (randint(0,11000))
    randommaxafstand = (randint(11001, 25000))
    context.browser.find_by_id('min').first.fill(randomminafstand)
    context.browser.find_by_id('max').first.fill(randommaxafstand)
    context.browser.find_by_xpath('/html/body/div/div/form/div[2]/button/span').first.click()
    time.sleep(3)

@then('krijg ik een lijst van leden die tussen die afstanden vallen')
def check_results_afstanden(context):
    assert context.browser.find_by_css('.display')
    assert context.browser.is_text_present('km)')

@when('ik op de link klik naar Herkomst-overzicht')
def click_categorie(context):
    context.browser.find_link_by_partial_href('rapport/herkomst').first.click()

@then('kom ik op de pagina Herkomst-overzicht')
def check_page_categorie(context):
    assert context.browser.url == '%s/rapport/herkomst' % context.base_url

@then('kan ik alle provincies bekijken door op de links te klikken')
def check_collapse_categorie(context):
    #context.browser.find_link_by_partial_href('#categorie_', 'number').click() #voor later. uitvogelen hoe ik automatisch de getallen kan laten optellen.
    context.browser.find_link_by_partial_href('#categorie_1').click()
    assert context.browser.find_by_css('.collapse.in')
    context.browser.find_link_by_partial_href('#categorie_1').click()
    time.sleep(1)

    # context.browser.find_by_css('div.panel:nth-child(1) > div:nth-child(1) > h3:nth-child(1) > a:nth-child(1)').click()
    # assert context.browser.find_by_css('.collapse.in')
    # context.browser.find_by_css('div.panel:nth-child(1) > div:nth-child(1) > h3:nth-child(1) > a:nth-child(1)').click()
    # time.sleep(1)
    # context.browser.find_by_css('div.panel:nth-child(2) > div:nth-child(1) > h3:nth-child(1) > a:nth-child(1)').click()
    # assert context.browser.find_by_css('.collapse.in')
    # context.browser.find_by_css('div.panel:nth-child(2) > div:nth-child(1) > h3:nth-child(1) > a:nth-child(1)').click()
    # time.sleep(1)
    # context.browser.find_by_css('div.panel:nth-child(3) > div:nth-child(1) > h3:nth-child(1) > a:nth-child(1)').click()
    # assert context.browser.find_by_css('.collapse.in')
    # context.browser.find_by_css('div.panel:nth-child(3) > div:nth-child(1) > h3:nth-child(1) > a:nth-child(1)').click()
    # time.sleep(1)
    # context.browser.find_by_css('div.panel:nth-child(4) > div:nth-child(1) > h3:nth-child(1) > a:nth-child(1)').click()
    # assert context.browser.find_by_css('.collapse.in')
    # context.browser.find_by_css('div.panel:nth-child(4) > div:nth-child(1) > h3:nth-child(1) > a:nth-child(1)').click()
    # time.sleep(1)
    # context.browser.find_by_css('div.panel:nth-child(5) > div:nth-child(1) > h3:nth-child(1) > a:nth-child(1)').click()
    # assert context.browser.find_by_css('.collapse.in')
    # context.browser.find_by_css('div.panel:nth-child(5) > div:nth-child(1) > h3:nth-child(1) > a:nth-child(1)').click()
    # time.sleep(1)
    # context.browser.find_by_css('div.panel:nth-child(6) > div:nth-child(1) > h3:nth-child(1) > a:nth-child(1)').click()
    # assert context.browser.find_by_css('.collapse.in')
    # context.browser.find_by_css('div.panel:nth-child(6) > div:nth-child(1) > h3:nth-child(1) > a:nth-child(1)').click()
    # context.browser.find_by_css('div.panel:nth-child(7) > div:nth-child(1) > h3:nth-child(1) > a:nth-child(1)').click()
    # assert context.browser.find_by_css('.collapse.in')
    # context.browser.find_by_css('div.panel:nth-child(7) > div:nth-child(1) > h3:nth-child(1) > a:nth-child(1)').click()
    # time.sleep(1)
    # context.browser.find_by_css('div.panel:nth-child(8) > div:nth-child(1) > h3:nth-child(1) > a:nth-child(1)').click()
    # assert context.browser.find_by_css('.collapse.in')
    # context.browser.find_by_css('div.panel:nth-child(8) > div:nth-child(1) > h3:nth-child(1) > a:nth-child(1)').click()
    # time.sleep(1)
    # context.browser.find_by_css('div.panel:nth-child(9) > div:nth-child(1) > h3:nth-child(1) > a:nth-child(1)').click()
    # assert context.browser.find_by_css('.collapse.in')
    # context.browser.find_by_css('div.panel:nth-child(9) > div:nth-child(1) > h3:nth-child(1) > a:nth-child(1)').click()
    # time.sleep(1)
    # context.browser.find_by_css('div.panel:nth-child(10) > div:nth-child(1) > h3:nth-child(1) > a:nth-child(1)').click()
    # assert context.browser.find_by_css('.collapse.in')
    # context.browser.find_by_css('div.panel:nth-child(10) > div:nth-child(1) > h3:nth-child(1) > a:nth-child(1)').click()
    # time.sleep(1)
    # context.browser.find_by_css('div.panel:nth-child(11) > div:nth-child(1) > h3:nth-child(1) > a:nth-child(1)').click()
    # assert context.browser.find_by_css('.collapse.in')
    # context.browser.find_by_css('div.panel:nth-child(11) > div:nth-child(1) > h3:nth-child(1) > a:nth-child(1)').click()
    # time.sleep(1)
    # context.browser.find_by_css('div.panel:nth-child(12) > div:nth-child(1) > h3:nth-child(1) > a:nth-child(1)').click()
    # assert context.browser.find_by_css('.collapse.in')
    # context.browser.find_by_css('div.panel:nth-child(12) > div:nth-child(1) > h3:nth-child(1) > a:nth-child(1)').click()
    # time.sleep(1)
    # context.browser.find_by_css('div.panel:nth-child(13) > div:nth-child(1) > h3:nth-child(1) > a:nth-child(1)').click()
    # assert context.browser.find_by_css('.collapse.in')
    # context.browser.find_by_css('div.panel:nth-child(13) > div:nth-child(1) > h3:nth-child(1) > a:nth-child(1)').click()
    # time.sleep(1)

@when('ik op de link klik naar leeftijd en geboortedatum')
def click_link_geboortedatum(context):
    context.browser.find_link_by_partial_href('rapport/leeftijd').first.click()

@then('kom ik op de pagina met leden op geboortedatum')
def check_page_geboortedatum(context):
    assert context.browser.url == '%s/rapport/leeftijd' % context.base_url

@then('krijg ik een zoekfunctie te zien')
def check_search_geboortedatum(context):
    assert context.browser.find_by_css('#main > div:nth-child(6) > form:nth-child(1)')

@given('ik ben op de pagina leden op geboortedatum')
def check_page_afstanden(context):
    if context.browser.url == '%s/rapport/leeftijd' % context.base_url:
        pass
    else:
        context.browser.visit('%s/rapport' % context.base_url)
        context.browser.find_link_by_partial_href('rapport/leeftijd').first.click()
        assert context.browser.url == '%s/rapport/leeftijd' % context.base_url
        assert context.browser.is_text_present('Leden naar leeftijd/geboortedatum')

@when('ik een datum en leeftijden invul in de zoekvelden')
def fill_date_form_leeftijd(context):
    randomminleeftijd = (randint(0, 50))
    randommaxleeftijd = (randint(51, 100))
    #fillformdate = context.browser.find_by_id('peildatum')
    #fillformdate.click()
    #fillformdate.send_keys('12122012')
    # fillformdate = '12122012'
    # context.browser.find_by_id('peildatum').value == fillformdate
    # context.browser.find_by_id('peildatum').fill('11111950')      #"Element must be user-editable", moet nog opgelost worden
    context.browser.find_by_id('minimum_leeftijd').first.fill(randomminleeftijd)
    context.browser.find_by_id('maximum_leeftijd').first.fill(randommaxleeftijd)

@then('kan ik zoeken op geboortedatum en leeftijdsbereik')
def click_search_leeftijd(context):
    context.browser.find_by_css('.btn').first.click()

@then('krijg ik een lijst met de gespecificeerde zoekcriteria')
def check_results_leeftijd(context):
    assert context.browser.find_by_css('.display')


@when('ik klik op de link naar Email export')
def click_csvhb(context):
    context.browser.find_link_by_partial_href('rapport/export').first.click()
    time.sleep(1)


@then('zal er een CSV bestand downloaden')
def check_download_complete(context):
    assert os.path.isfile(os.path.expanduser('~/Downloads/outlook.csv'))


@then('die verwijder ik voor toekomstige tests')
def delete_download(context):
    os.remove(os.path.expanduser('~/Downloads/outlook.csv'))
    assert not os.path.isfile(os.path.expanduser('~/Downloads/outlook.csv'))

@when('ik op de uitleg link klik')
def click_link_uitleg(context):
    context.browser.find_link_by_partial_href('rapport/uitleg').first.click()

@then('kom ik op de pagina met betalingsuitleg')
def check_page_uitleg(context):
    assert context.browser.url == '%s/rapport/uitleg' % context.base_url
    assert context.browser.is_text_present('Uitleg betalingen')

@then('kan ik de links op deze pagina bezoeken')
def click_links_uitlegbetalingen(context):
    assert context.browser.find_link_by_partial_href('union.otech.nl/instellingen')
    assert context.browser.find_link_by_partial_href('union.otech.nl/rapport')

@when('ik op de Eerste incasso link klik')
def click_link_incasso(context):
    context.browser.find_link_by_partial_href('rapport/incasso/report/eerste').first.click()

@then('kom ik op de pagina met eerste incassos')
def check_link_incasso(context):
    assert context.browser.url == '%s/rapport/incasso/report/eerste' % context.base_url
    assert context.browser.is_text_present('Rapport: eerste incasso')

@then('krijg ik een lijst met machtigingsdata te zien')
def check_page_incasso(context):
    assert context.browser.find_by_css('.display')

@when('ik op de Volgende incasso link klik')
def click_link_incasso(context):
    context.browser.find_link_by_partial_href('rapport/incasso/report/volgende').first.click()

@then('kom ik op de pagina met de volgende incassos')
def check_link_incasso(context):
    assert context.browser.url == '%s/rapport/incasso/report/volgende' % context.base_url
    assert context.browser.is_text_present('Rapport: volgende incasso')

@when('ik de Toelichting link klik')
def click_link_toelichting(context):
    context.browser.find_link_by_partial_href('rapport/uitleg#upload').first.click()

@then('kom ik op de tweede helft van de pagina met betalingsuitleg')
def check_link_toelichting(context):
    assert context.browser.url == '%s/rapport/uitleg#upload' % context.base_url
    assert context.browser.is_text_present('Uploaden naar de bank')

@when('ik op de lijst link klik')
def click_link_lijst(context):
    context.browser.find_link_by_partial_href('rapport/kas/list').first.click()

@then('kom ik de pagina met een lijst van leden die betalen per kas')
def check_page_lijst(context):
    assert context.browser.url == '%s/rapport/kas/list' % context.base_url
    assert context.browser.is_text_present('leden die betalen per kas')
    assert context.browser.find_by_css('.display')

@when('ik op etiketten link klik')
def click_link_lijst(context):
    context.browser.find_link_by_partial_href('rapport/kas/etiketten').first.click()

@then('kom ik op de pagina met etiketten van leden die betalen per kas')
def check_page_lijst(context):
    assert context.browser.url == '%s/rapport/kas/etiketten' % context.base_url
    assert context.browser.find_by_css('.etiketten')

@when('ik op de link naar de pagina met leden waarvoor geen contributie kan worden geind')
def click_link_oninbaar(context):
    context.browser.find_link_by_partial_href('rapport/oninbaar').first.click()

@then('kom ik op de pagina met leden met oninbare contributie')
def check_page_oninbaar(context):
    assert context.browser.url == '%s/rapport/oninbaar' % context.base_url
    assert context.browser.is_text_present('Leden met oninbare contributie')

@then('zie ik hier een lijst van')
def check_list_oninbaar(context):
    assert context.browser.find_by_css('.display')

@when('ik op de Dubbele bondsnummers link klik')
def click_link_bondsnummers(context):
    context.browser.find_link_by_partial_href('rapport/dubbel_bondsnummer').first.click()

@then('kom ik op de pagina met leden met dubbele bondsnummers')
def check_page_bondsnummers(context):
    assert context.browser.url == '%s/rapport/dubbel_bondsnummer' % context.base_url
    assert context.browser.is_text_present('dubbele bondsnummers')

@when('ik op de Dubbele adressen link klik')
def click_link_bondsnummers(context):
    context.browser.find_link_by_partial_href('rapport/dubbel_adres').first.click()

@then('kom ik op de pagina met leden met dubbele adressen')
def check_page_bondsnummers(context):
    assert context.browser.url == '%s/rapport/dubbel_adres' % context.base_url
    assert context.browser.is_text_present('dubbele adressen')



from behave import given, when, then  # pylint: disable=no-name-in-module
from random import randint
import os.path
from time import sleep

from common import check_pagina


@then('zie ik een lijst met verscheidene rapporten')
def lijst_rapporten(context):
    assert context.browser.find_by_xpath('//*[@id="main"]/ul')
    
  
@then('krijg ik een lijst met adresgegevens te zien')
def check_adresgegevens_naw(context):
    assert context.browser.find_by_xpath('/html/body/div/table')
    assert context.browser.find_by_css('.display')
      
    
@then('zie ik de voltooide download "{filename}" in de Downloads map')
def check_download_complete(context, filename):
    sleep(2)
    try:
        filename = os.path.expanduser('~/Downloads/%s' % filename)
        assert os.path.isfile(filename), 'File "%s" not found' % filename
    except FileNotFoundError:
        assert False, 'File "%s" not found' % filename


@then('verwijder ik "{filename}" voor toekomstige tests')
def delete_download(context, filename):
    filename = os.path.expanduser('~/Downloads/%s' % filename)
    os.remove(filename)
    assert not os.path.isfile(os.path.expanduser(filename))
    
    
@then('kom ik op een pagina met etiketten')
def check_etiketten(context):
    assert context.browser.find_by_css('.etiketten')
    

@then('kan ik alle categorieen bekijken door op de links te klikken')
def check_collapse_categorie(context):
    for i in range(1, 7):
        selector = 'div.panel:nth-child(%s) > div:nth-child(1) > h3:nth-child(1) > a:nth-child(1)' % i
        context.browser.find_by_css(selector).click()
        assert context.browser.find_by_css('.collapse.in')
        context.browser.find_by_css(selector).click()
        sleep(1)


@then('krijg ik een ledenlijst met tekst "{txt}"')
def check_list(context, txt):
    assert context.browser.find_by_css('.display')
    assert context.browser.is_text_present(txt)


# @then('krijg ik een lijst van leden op afstand')
# def check_list_afstanden(context):
#     assert context.browser.find_by_css('.display')
#     assert context.browser.is_text_present('km)')


@given('ik ben op de pagina leden op afstand')
def check_page_afstanden2(context):
    if context.browser.url == '%s/rapport/afstanden' % context.base_url:
        pass
    else:
        context.browser.visit('%s/rapport' % context.base_url)
        context.browser.find_link_by_partial_href('rapport/afstanden').first.click()
        assert context.browser.url == '%s/rapport/afstanden' % context.base_url
        assert context.browser.is_text_present('Leden naar afstand')

# @when('ik een minimum en maximum afstand invul en op verwerken klik')
# def fill_afstanden(context):
#     randomminafstand = (randint(0,11000))
#     randommaxafstand = (randint(11001, 25000))
#     context.browser.find_by_id('min').first.fill(randomminafstand)
#     context.browser.find_by_id('max').first.fill(randommaxafstand)
#     context.browser.find_by_xpath('/html/body/div/div/form/div[2]/button/span').first.click()
#     sleep(3)


@then('kan ik alle provincies bekijken door op de links te klikken')
def check_collapse_categorie2(context):
    context.browser.find_link_by_partial_href('#categorie_1').click()
    assert context.browser.find_by_css('.collapse.in')
    context.browser.find_link_by_partial_href('#categorie_1').click()
    sleep(1)


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

# @when('ik een datum en leeftijden invul in de zoekvelden')
# def fill_date_form_leeftijd(context):
#     randomminleeftijd = (randint(0, 50))
#     randommaxleeftijd = (randint(51, 100))
#     context.browser.find_by_id('minimum_leeftijd').first.fill(randomminleeftijd)
#     context.browser.find_by_id('maximum_leeftijd').first.fill(randommaxleeftijd)

@then('kan ik zoeken op geboortedatum en leeftijdsbereik')
def click_search_leeftijd(context):
    context.browser.find_by_css('.btn').first.click()

# @then('krijg ik een lijst met de gespecificeerde zoekcriteria')
# def check_results_leeftijd(context):
#     assert context.browser.find_by_css('.display')

@then('kan ik de links op deze pagina bezoeken')
def click_links_uitlegbetalingen(context):
    assert context.browser.find_link_by_partial_href('union.otech.nl/instellingen')
    assert context.browser.find_link_by_partial_href('union.otech.nl/rapport')

# @when('ik op de Eerste incasso link klik')
# def click_link_incasso(context):
#     context.browser.find_link_by_partial_href('rapport/incasso/report/eerste').first.click()


@then('krijg ik een ledenlijst te zien')
def check_page_incasso(context):
    assert context.browser.find_by_css('.display')


@when('ik op de Volgende incasso link klik')
def click_link_incasso2(context):
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


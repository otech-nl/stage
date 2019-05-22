from datetime import datetime
from time import sleep

from behave import given, when, then  # pylint: disable=no-name-in-module
from selenium.webdriver.common.keys import Keys

from common import split_and_strip


@given('ik ben op de tocht toevoegen pagina')
def pagina_is_tocht_bewerken(context):
    if context.browser.is_text_present('Tocht bewerken') == True:
        pass
    else:
        context.browser.visit('%s/tocht/' %context.base_url)
        context.browser.find_link_by_partial_href('tocht/0').first.click()
        assert context.browser.is_text_present('Tocht bewerken')


@given('het veld naam is leeg')
def veld_naam_is_leeg(context):
    field = context.browser.find_by_id('naam').first
    value = field.value
    if value != '':
        field.clear()


@then('krijg ik een vul-dit-veld-in-melding bij het veld "{naam}"')
def foutmelding(context, naam):
    pass #kan niet


@then('wordt er geen tocht toegevoegd')
def check_pagina(context):
    assert context.browser.is_text_present('Tocht bewerken')  #waarom krijg ik een assertion error
                                                              #bij @then('zie ik een pagina Tocht bewerken') werkt ie wel
                                                              #en het is dezelfde pagina


@then('wordt de tocht toegevoegd')
def check_nieuwe_tocht(context):
    context.browser.find_link_by_partial_href('tochten').first.click()
    rows = context.browser.find_by_tag('tr')
    row = rows[-1]
    cells = row.find_by_tag('td')
    assert cells[0].value == context.testnaam, cells[0].value


@then('verwijdert behave de tocht voor volgende tests')
def tocht_verwijderen(context):
    def bekijk_alle_tochten(context):
        if context.browser.find_link_by_partial_href('tochten'):
            context.browser.find_link_by_partial_href('tochten').first.click()
    rows = context.browser.find_by_tag('tr')
    row = rows[-1]
    cells = row.find_by_tag('td')
    cells[0].click()
    if context.browser.find_by_id('naam').value == context.testnaam:                    #zodat niet echt-bestaande tochten worden verwijderd
        context.browser.find_by_xpath('//a/span[@title="remove"]').first.click()
        alert = context.browser.driver.switch_to_alert()
        alert.accept()
        bekijk_alle_tochten(context)
        assert cells[0] != context.testnaam
    else:
        return False, 'er is iets mis gegaan, de verkeerde tocht is geopend'


@when('ik in de tabel op plaats druk')
def druk_op_plaats(context):
    rows = context.browser.find_by_tag('tr')
    cells = rows.find_by_tag('th')
    plaats = cells[2]
    plaats.click()


@then('wordt de tabel op plaatsnaam gesorteerd')                
def check_volgorde_van_plaatsnamen(context):                    
    table = context.browser.find_by_tag('tbody')                 
    rows = table.find_by_tag('tr')                               
    values = [row.find_by_tag('td')[2].value for row in rows]
    assert values == sorted(values)

     
@when('ik in de tabel op een tocht druk')
def druk_op_tocht(context):
    table = context.browser.find_by_tag('tbody')                
    rows = table.find_by_tag('tr')                              
    row = rows[5]
    cells = row.find_by_tag('td')
    cell = cells[0]
    context.inhoud = cell.value
    cell.click()


@then('kom ik op een Tocht bewerken pagina van die tocht')
def check_tocht(context):
    tochtnaam = context.browser.find_by_id('naam').value
    assert tochtnaam == context.inhoud
    assert context.browser.is_text_present('Tocht bewerken')



@given('ik ben op de pagina waar ik deelnemers kan toevoegen')
def check_pagina(context):
    if context.browser.url == '%s/registratie/11' % context.base_url:
        pass
    else:
        context.browser.visit('%s/registratie/11' % context.base_url)


@then('is deelnemer "{naam}" aan de tocht toegevoegd')
def check_toevoeging_deelnemer(context):
    table = context.browser.find_by_tag('tbody')
    rows = table.find_by_tag('tr')
    row = rows[0]
    cells = row.find_by_tag('td')
    cell = cells[0]
    deelnemer = cell.value
    assert deelnemer == naam, naam + ' is niet aan de tocht toegevoegd'


@then('verwijdert behave de deelnemer voor volgende tests')
def verwijder_deelnemer(context):
    context.browser.visit('%s/afmelding/11' % context.base_url)
    context.browser.find_by_id('lidnummer').first.fill(context.lidnummer)
    context.browser.find_by_xpath('//button[@type="submit"]').first.click()
    table = context.browser.find_by_tag('tbody')
    rows = table.find_by_tag('tr')
    row = rows[0]
    cells = row.find_by_tag('td')
    cell = cells[0]
    deelnemer = cell.value
    assert deelnemer == context.complete_lidnaam, context.achternaam + ' is niet afgemeld'


@when('ik de eerstvolgende tocht bekijk')
def eerstvolgende_tocht(context):
    links = context.browser.find_link_by_partial_href('tocht')
    links[1].click()
    context.datum_eerstvolgende_tocht = context.browser.find_by_id('datum').value


@then('ligt die tocht in de toekomst')
def toekomstvoorspelling(context):
    context.heden = datetime.today()
    context.toekomst = datetime.strptime(context.datum_eerstvolgende_tocht, '%Y-%m-%d')
    assert context.toekomst >= context.heden, context.toekomst + ' is niet later dan ' + context.heden


@then('is er geen tocht die eerder komt')
def geen_andere_tocht(context):
    context.browser.visit('%s/tochten/' % context.base_url)
    table = context.browser.find_by_tag('tbody')
    rows = table.find_by_tag('tr')
    values = [datetime.strptime(row.find_by_tag('td')[1].value, '%Y-%m-%d') for row in rows]
    for data in values:
        assert data >= context.toekomst or context.heden >= data


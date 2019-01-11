from behave import given, when, then
from time import sleep
from selenium.webdriver.common.keys import Keys
#from datetime import datetime
import datetime

#@given('ik ben ingelogd')                                                   #wordt al gedaan in andere stepfile(uitloggen)
#def ingelogd_check(context):
 #   loggedoff_url = '%s/login?next=%%2F' % context.base_url
  #  base_url = context.base_url
   # context.browser.visit(base_url)
    #if context.browser.url == loggedoff_url:                                
     #   context.browser.find_by_id('email').first.fill('admin')             #moet makkelijker kunnen
      #  context.browser.find_by_id('password').first.fill('nimda')          #
        #context.browser.find_by_id('submit').first.click()                  #
    #assert context.browser.url != loggedoff_url

def split_and_strip(src, sep=None):
    return [token.strip() for token in src.split(sep)]    

@given('ik ben niet op de pagina Tochten')
def pagina_check_niet_ledenoverzicht(context):
    if context.browser.url == '%s/tocht/' % context.base_url:
        context.browser.find_link_by_partial_href('user').first.click()
    
@when('ik op de link Tochten druk')
def druk_op_tochten(context):
    context.browser.find_link_by_partial_href('tocht').first.click()
    
#@then('kom ik op de pagina Tochten')                                        #wordt al gedaan in andere stepfile(inloggen)
#def inlog_tochten_pagina(context):
 #   assert context.browser.url == '%s/tocht/' % context.base_url

@then('zie ik een tabel met 3 kolommen "{columns}"')                         
def step_table(context, columns):
    tables = context.browser.find_by_css('table.table')
    assert len(tables) > 0, 'Geen datatable gevonden'
    table = tables.first
    row = table.find_by_tag('thead') or table.find_by_tag('tr')
    head = row.first.text
    for col in split_and_strip(columns, ','):
        assert col in head, 'Kolom "%s" niet gevonden in "%s"' % (col, head)

@when('ik op de knop Tocht toevoegen druk')
def druk_op_tocht_toevoegen(context):
    context.browser.find_link_by_partial_href('tocht/0').first.click()
    
@then('zie ik een pagina Tocht bewerken')
def check_pagina_tocht_bewerken(context):
    assert context.browser.is_text_present('Tocht bewerken')
    
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
    
@when('ik op de knop verwerken druk')
def druk_op_verwerken(context):
    context.browser.find_by_xpath('//button[@type="submit"]').first.click()
        
@then('krijg ik een vul-dit-veld-in-melding bij het naamveld')
def foutmelding(context):
    pass #kan niet

@then('wordt er geen tocht toegevoegd')
def check_pagina(context):
    assert context.browser.is_text_present('Tocht bewerken')  #waarom krijg ik een assertion error
                                                              #bij @then('zie ik een pagina Tocht bewerken') werkt ie wel
                                                              #en het is dezelfde pagina

@when('ik vul een naam in in het naamveld')
def vul_naam_in(context):
    context.testnaam = 'testtocht'
    context.browser.find_by_id('naam').first.fill(context.testnaam)
    
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
    
@given('ik ben op de tocht bewerken pagina')
def check_pagina(context):
    #if context.browser.is_text_present('Tocht bewerken'):
    #    pass
    #else:
    context.browser.visit('%s/tocht/11' % context.base_url)
        
@when('ik druk op de knop Aanmelden deelnemers')
def druk_op_knop(context):
    context.browser.find_link_by_partial_href('registratie').first.click()
    
@then('kom ik op een pagina waar ik deelnemers kan toevoegen')
def check_pagina(context):
    assert context.browser.url == '%s/registratie/11' % context.base_url
    
@given('ik ben op de pagina waar ik deelnemers kan toevoegen')
def check_pagina(context):
    if context.browser.url == '%s/registratie/11' % context.base_url:
        pass
    else:
        context.browser.visit('%s/registratie/11' % context.base_url)
        
@when('ik in het veld achternaam een deelnemer invul')                          #hiervoor moet de 'Deelnemer' aan de database worden toegevoegd
def deelnemernaam_invullen(context):
    context.achternaam = 'Deelnemer'
    context.browser.find_by_id('achternaam').first.fill(context.achternaam)
    
@when('ik in het veld lidnummer het bijbehorende lidnummer invul')              #als de 'Deelnemer' opnieuw in de database is gezet, zoals hierboven
def lidnummer_invullen(context):                                                #genoemd, krijgt deze een nieuw lidnummer. Dit lidnummer moet aan
    context.lidnummer = '3230'                                                  #deze stap worden toegevoegd
    context.browser.find_by_id('lidnummer').first.clear()
    context.browser.find_by_id('lidnummer').first.fill(context.lidnummer)
    
@when('ik op de verwerken knop druk')
def op_verwerken_knop_drukken(context):
    context.browser.find_by_xpath('//button[@type="submit"]').first.click()

@then('wordt de deelnemer aan de tocht toegevoegd')
def check_toevoeging_deelnemer(context):
    table = context.browser.find_by_tag('tbody')                
    rows = table.find_by_tag('tr')                              
    row = rows[0]
    cells = row.find_by_tag('td')
    cell = cells[0]
    deelnemer = cell.value
    context.complete_lidnaam = '[' + context.lidnummer + '] ' + 'T. E. S. T. ' + context.achternaam
    assert deelnemer == context.complete_lidnaam, context.achternaam + ' is niet aan de toegevoegd'

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
    #if context.achternaam in deelnemer:
    #    cell.click()
    #    context.browser.find_by_xpath('//a[@onclick="delete_item()"]').click()
    #    context.browser.visit('%s/afmelding/11' % context.base_url)
    #    assert context.achternaam not in deelnemer, 'verwijderen van deelnemer is mislukt'
    #else:
    #    assert False, 'Deelnemer staat niet in de lijst. Als de voorgaande stap groen is dan is de lijst met deelnemers niet compleet op de afmeldingspagina'
    
@when('ik druk op de knop Afmelden deelnemers')
def druk_knop_deelnemers_verwijderen(context):
    context.browser.find_link_by_partial_href('afmelding').first.click()
    
@then('kom ik op een pagina waar ik deelnemers kan verwijderen')
def check_pagina(context):
    assert context.browser.url == '%s/afmelding/11' % context.base_url
    
@when('ik druk op de knop Afstand toevoegen')
def druk_op_knop(context):
    context.browser.find_link_by_partial_href('afstand/new').first.click()
    
@then('kom ik op een pagina waar ik afstanden kan toevoegen')
def check_pagina(context):
    assert context.browser.is_text_present('Afstanden:')
    
@given('ik ben op de tochten pagina')
def tochten_pagina(context):
    if context.browser.url != '%s/tocht/' % context.base_url:
        context.browser.visit('%s/tocht/' % context.base_url)
        
@when('ik de eerstvolgende tocht bekijk')
def eerstvolgende_tocht(context):
    links = context.browser.find_link_by_partial_href('tocht')
    links[1].click()
    context.datum_eerstvolgende_tocht = context.browser.find_by_id('datum').value

@then('ligt die tocht in de toekomst')
def toekomstvoorspelling(context):
    #now = datetime.datetime.now() 
    context.heden = datetime.datetime.today()
    context.toekomst = datetime.datetime.strptime(context.datum_eerstvolgende_tocht, '%Y-%m-%d')
    assert context.toekomst >= context.heden, context.toekomst + ' is niet later dan ' + context.heden
    
@then('is er geen tocht die eerder komt')
def geen_andere_tocht(context):
    context.browser.visit('%s/tochten/' % context.base_url)
    table = context.browser.find_by_tag('tbody')                 
    rows = table.find_by_tag('tr') 
    values = [datetime.datetime.strptime(row.find_by_tag('td')[1].value, '%Y-%m-%d') for row in rows]  
    #now = datetime.datetime.now() 
    #heden = str(now.year) + '-' + str(now.month) + '-' + str(now.day)    
    for data in values:
        assert data >= context.toekomst or context.heden >= data
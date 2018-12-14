from radish import given, when, then, world
from time import sleep

def split_and_strip(src, sep=None):
    return [token.strip() for token in src.split(sep)]

@given('ik ben ingelogd')                                                     
def ingelogd_check(step):
    loggedoff_url = '%s/login?next=%%2F' % world.base_url
    base_url = world.base_url
    world.browser.visit(base_url)
    if world.browser.url == loggedoff_url:                                
        world.browser.find_by_id('email').first.fill('admin')             #moet makkelijker kunnen
        world.browser.find_by_id('password').first.fill('nimda')          #
        world.browser.find_by_id('submit').first.click()                  #
    assert world.browser.url != loggedoff_url 
    
@given('ik ben op de pagina ledenoverzicht')
def check_pagina(step):
    if world.browser.url != '%s/lid/' % world.base_url:
        world.browser.visit('%s/lid/' % world.base_url)

@given('ik ben niet op de pagina ledenoverzicht')
def check_pagina_niet_ledenoverzicht(step):
    if world.browser.url == '%s/lid/' % world.base_url:
        world.browser.find_link_by_partial_href('user').first.click()    

@when('ik op de knop Leden druk')
def klik_leden(step):
    world.browser.find_link_by_partial_href('lid').first.click()
    
@then('kom ik op de pagina Lid-overzicht')
def lid_overzicht(step):
    assert world.browser.url == '%s/lid/' % world.base_url
    
@then('zie ik een tabel met kolommen "{columns}"')
def step_table(step, columns):
    tables = world.browser.find_by_id('lid')
    assert len(tables) > 0, 'Geen datatable gevonden'
    table = tables.first
    row = table.find_by_tag('thead') or table.find_by_tag('tr')
    head = row.first.text
    for col in split_and_strip(columns, ','):
        assert col in head, 'Kolom "%s" niet gevonden in "%s"' % (col, head)
        
@when('ik in het zoekveld een achternaam invul')
def zoek_achternaam(step):
    world.lidzoektocht = 'Deelnemer'
    world.browser.find_by_xpath('//input[@type="search"]').first.fill(world.lidzoektocht)
    #sleep(2)
    
@then('zie ik alle leden met die achternaam')
def check_tabel_results(step):
    sleep(2)
    table = world.browser.find_by_tag('tbody')                  
    rows = table.find_by_tag('tr')                                
    values = [row.find_by_tag('td')[2].value for row in rows] 
    assert all(world.lidzoektocht in values for values in values), values
    
@then('leegt behave het zoekveld voor volgende tests')
def leeg_zoekveld(step):
    world.browser.find_by_xpath('//input[@type="search"]').first.clear()   #cleart niks maar de boel wordt wel vrolijk groen?????????
    sleep(3)                                                                 #in ptpyhon komt deze melding: splinter.exceptions.ElementDoesNotExist:
                                                                             #no elements could be found with xpath "//input[@type="search"]"
                                                                             #terwijl @when('ik in het zoekveld een achternaam invul') het element
                                                                             #wel vindt en invult zoals opgedragen

    
@when('ik in de tabel op achternaam druk')
def druk_op_achternaam(step):
    rows = world.browser.find_by_tag('tr')
    cells = rows.find_by_tag('th')
    achternaam = cells[2]
    achternaam.click()
    
@then('wordt de tabel op achternaam gesorteerd')                
def check_volgorde_van_plaatsnamen(step):                    
    table = world.browser.find_by_tag('tbody')                 
    rows = table.find_by_tag('tr')                               
    values = [row.find_by_tag('td')[2].value for row in rows]
    assert values == sorted(values), 'niet gesorteerd:' + str(values)
    
@when('ik 10 selecteer in het aantal resultaten weergeven')
def selecteer_10(step):
    world.browser.find_option_by_text('10').first.click()
    
@then('krijg maximaal 10 resultaten per pagina te zien')
def check_tabel_lengte(step):
    tables = world.browser.find_by_css('table.table')
    assert len(tables) > 0, 'Geen datatable gevonden'
    tabel = world.browser.find_by_tag('tbody')
    rows = tabel.find_by_tag('tr')
    assert len(rows) <= 10, 'tabel is te lang:' + len(rows)
        
@when('ik 100 selecteer in het aantal resultaten weergeven')
def selecteer_100(step):
    world.browser.find_option_by_text('100').first.click()
    
@then('krijg maximaal 100 resultaten per pagina te zien')
def check_tabel_lengte(step):
    tables = world.browser.find_by_css('table.table')
    assert len(tables) > 0, 'Geen datatable gevonden'
    tabel = world.browser.find_by_tag('tbody')
    rows = tabel.find_by_tag('tr')
    assert len(rows) <= 100, 'tabel is te lang:' + len(rows)

@given('behave heeft een lijst van de tweede set van 10 leden')
def stel_lijst_samen(step):
    world.browser.find_option_by_text('25').first.click()
    table = world.browser.find_by_tag('tbody')                  
    rows = table.find_by_tag('tr')                                
    lijst = [row.find_by_tag('td')[2].value for row in rows] 
    world.lijst2 = lijst[10:20]
    
@given('ik zie 10 leden per pagina')
def bekijk_10_leden(step):
    world.browser.find_option_by_text('10').first.click()
        
@when('ik op pagina 2 druk')
def ga_naar_pagina_2(step):
    if world.browser.is_element_present_by_xpath('//ul/li/a[@data-dt-idx="2"]'):
        world.browser.find_by_xpath('//ul/li/a[@data-dt-idx="2"]').first.click()
        
@then('zie ik de tweede set van 10 leden')
def check_lijst_tegen_lijst(step):
    if world.browser.is_element_present_by_tag('tbody'):
        sleep(0)
    else:
        sleep(5)
    table = world.browser.find_by_tag('tbody')                  
    rows = table.find_by_tag('tr')                                
    lijst = [row.find_by_tag('td')[2].value for row in rows] 
    assert lijst == world.lijst2, str(lijst) + ' is niet ' + str(world.lijst2)
    
@given('ik zie een tabel met honderd leden')
def honderd_leden_tabel(step):
    world.browser.find_option_by_text('100').first.click()
    
@then('zijn de lidnummers van deze leden uniek')
def check_uniekheid(step):
    tabel = world.browser.find_by_tag('tbody') 
    rows = tabel.find_by_tag('tr') 
    uniekelijst = set(row.find_by_tag('td')[5].value for row in rows) 
    totalelijst = [row.find_by_tag('td')[5].value for row in rows] 
    assert len(uniekelijst) == len(totalelijst), 'Er zijn minder unieke lidnummers dan leden in deze lijst. Dus niet elk lidnummer is uniek'
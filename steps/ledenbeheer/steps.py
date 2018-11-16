from behave import given, when, then
from time import sleep

def split_and_strip(src, sep=None):
    return [token.strip() for token in src.split(sep)]

#@given('ik ben ingelogd')                                                     #wordt al gedaan in andere stepfile(uitloggen)
#def ingelogd_check(context):
 #   loggedoff_url = '%s/login?next=%%2F' % context.base_url
  #  base_url = context.base_url
   # context.browser.visit(base_url)
    #if context.browser.url == loggedoff_url:                                
     #   context.browser.find_by_id('email').first.fill('admin')             #moet makkelijker kunnen
      #  context.browser.find_by_id('password').first.fill('nimda')          #
       # context.browser.find_by_id('submit').first.click()                  #
    #assert context.browser.url != loggedoff_url 
    
@given('ik ben op de pagina ledenoverzicht')
def check_pagina(context):
    if context.browser.url != '%s/lid/' % context.base_url:
        context.browser.visit('%s/lid/' % context.base_url)

@given('ik ben niet op de pagina ledenoverzicht')
def check_pagina_niet_ledenoverzicht(context):
    if context.browser.url == '%s/lid/' % context.base_url:
        context.browser.find_link_by_partial_href('user').first.click()    

@when('ik op de knop Leden druk')
def klik_leden(context):
    context.browser.find_link_by_partial_href('lid').first.click()
    
@then('kom ik op de pagina Lid-overzicht')
def lid_overzicht(context):
    assert context.browser.url == '%s/lid/' % context.base_url
    
@then('zie ik een tabel met kolommen "{columns}"')
def step_table(context, columns):
    tables = context.browser.find_by_id('lid')
    assert len(tables) > 0, 'Geen datatable gevonden'
    table = tables.first
    row = table.find_by_tag('thead') or table.find_by_tag('tr')
    head = row.first.text
    for col in split_and_strip(columns, ','):
        assert col in head, 'Kolom "%s" niet gevonden in "%s"' % (col, head)
        
@when('ik in het zoekveld een achternaam invul')
def zoek_achternaam(context):
    context.lidzoektocht = 'Deelnemer'
    context.browser.find_by_xpath('//input[@type="search"]').first.fill(context.lidzoektocht)
    #sleep(2)
    
@then('zie ik alle leden met die achternaam')
def check_tabel_results(context):
    sleep(2)
    table = context.browser.find_by_tag('tbody')                  
    rows = table.find_by_tag('tr')                                
    values = [row.find_by_tag('td')[2].value for row in rows] 
    assert all(context.lidzoektocht in values for values in values), values
    
@then('leegt behave het zoekveld voor volgende tests')
def leeg_zoekveld(context):
    context.browser.find_by_xpath('//input[@type="search"]').first.clear()   #cleart niks maar de boel wordt wel vrolijk groen?????????
    sleep(3)                                                                 #in ptpyhon komt deze melding: splinter.exceptions.ElementDoesNotExist:
                                                                             #no elements could be found with xpath "//input[@type="search"]"
                                                                             #terwijl @when('ik in het zoekveld een achternaam invul') het element
                                                                             #wel vindt en invult zoals opgedragen

    
@when('ik in de tabel op achternaam druk')
def druk_op_achternaam(context):
    rows = context.browser.find_by_tag('tr')
    cells = rows.find_by_tag('th')
    achternaam = cells[2]
    achternaam.click()
    
@then('wordt de tabel op achternaam gesorteerd')                
def check_volgorde_van_plaatsnamen(context):                    
    table = context.browser.find_by_tag('tbody')                 
    rows = table.find_by_tag('tr')                               
    values = [row.find_by_tag('td')[2].value for row in rows]
    assert values == sorted(values), 'niet gesorteerd:' + str(values)
    
@when('ik 10 selecteer in het aantal resultaten weergeven')
def selecteer_10(context):
    context.browser.find_option_by_text('10').first.click()
    
@then('krijg maximaal 10 resultaten per pagina te zien')
def check_tabel_lengte(context):
    tables = context.browser.find_by_css('table.table')
    assert len(tables) > 0, 'Geen datatable gevonden'
    assert len(tables) <= 10, 'Tabel te lang'
    
@when('ik 100 selecteer in het aantal resultaten weergeven')
def selecteer_100(context):
    context.browser.find_option_by_text('100').first.click()
    
@then('krijg maximaal 100 resultaten per pagina te zien')
def check_tabel_lengte(context):
    tables = context.browser.find_by_css('table.table')
    assert len(tables) > 0, 'Geen datatable gevonden'
    assert len(tables) <= 100, 'Tabel te lang'    

@given('behave heeft een lijst van de tweede set van 10 leden')
def stel_lijst_samen(context):
    context.browser.find_option_by_text('25').first.click()
    table = context.browser.find_by_tag('tbody')                  
    rows = table.find_by_tag('tr')                                
    lijst = [row.find_by_tag('td')[2].value for row in rows] 
    context.lijst2 = [lijst[i] for i in (10,11,12,13,14,15,16,17,18,19)]  
    #Nog wel even een mooi loopje bouwen :
    #Deze lijkt oneindig te loopen:
    #i = 10
    #while i < 20:
    #    context.lijst2 = [lijst[i]]
    #    i + 1    
    
@given('ik zie 10 leden per pagina')
def bekijk_10_leden(context):
    context.browser.find_option_by_text('10').first.click()
        
@when('ik op pagina 2 druk')
def ga_naar_pagina_2(context):
    context.browser.find_by_xpath('//ul/li/a[@data-dt-idx="2"]').first.click()
    sleep(1)
    
@then('zie ik de tweede set van 10 leden')
def check_lijst_tegen_lijst(context):
    table = context.browser.find_by_tag('tbody')                  
    rows = table.find_by_tag('tr')                                
    lijst = [row.find_by_tag('td')[2].value for row in rows] 
    assert lijst == context.lijst2, str(lijst) + ' is niet ' + str(context.lijst2)
from behave import given, when, then
from time import sleep
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

@then('zie ik een tabel met 3 kolommen "{columns}"')                          #wordt al gedaan in andere stepfile(ledenbeheer)
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
    value = context.browser.find_by_id('naam').first.value
    if value == '':
        pass
    #else value.fill('')
    
    #else context.browser.find_by_id('naam').first.fill('')
    
@when('ik op de knop verwerken druk')
def druk_op_verwerken(context):
    context.browser.find_by_css('button').first.click() #selenium.common.exceptions.ElementNotVisibleException: Message: element not interactable
        
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
    context.browser.find_by_id('naam').first.fill('testtocht')
    
@then('wordt de tocht toegevoegd')
def check_nieuwe_tocht(context):
    pass
    #code
    
@when('ik in de tabel op plaats druk')
def druk_op_plaats(context):
    rows = context.browser.find_by_tag('tr')
    cells = rows.find_by_tag('th')
    plaats = cells[2]
    plaats.click()
    
@then('wordt de tabel op plaatsnaam gesorteerd')                # Deze gaat natuurlijk kapot
def check_volgorde_van_plaatsnamen(context):                    # als bijvoorbeeld de tocht in Appelscha verdwijnt
    table = context.browser.find_by_tag('tbody')                # of als een nieuwe tocht wordt gemaakt
    rows = table.find_by_tag('tr')                              # in een een plaats die hoger in het
    cells = rows.find_by_tag('td')                              # alfabet staat
    eerste_result = cells[2]
    laatsterow = rows[9]                                        # dit moet ook korter kunnen
    cells = laatsterow.find_by_tag('td')     
    laatste_result = cells[2]
    assert eerste_result.value == 'Appelscha'
    assert laatste_result.value == 'Zuidbroek'
    
#inhoud = ''  
@when('ik in de tabel op een tocht druk')
def druk_op_tocht(context):
    table = context.browser.find_by_tag('tbody')                
    rows = table.find_by_tag('tr')                              
    row = rows[5]
    cells = row.find_by_tag('td')
    cell = cells[0]
    global inhoud  #zodat de variabele in de @then('kom ik op een Tocht bewerken pagina van die tocht') opgevraagd kan worden
    inhoud = cell.value
    cell.click()
    
@then('kom ik op een Tocht bewerken pagina van die tocht')
def check_tocht(context):
    tochtnaam = context.browser.find_by_id('naam').value
    assert tochtnaam == inhoud
    assert context.browser.is_text_present('Tocht bewerken')
    
@given('ik ben op de tocht bewerken pagina')
def check_pagina(context):
    if context.browser.is_text_present('Tocht bewerken'):
        pass
    else:
        context.browser.visit('%s/tocht/11' % context.base_url)
        
@when('ik druk op de knop Aanmelden deelnemers')
def druk_op_knop(context):
    context.browser.find_link_by_partial_href('registratie').first.click()
    
@then('kom ik op een pagina waar ik deelnemers kan toevoegen')
def check_pagina(context):
    assert context.browser.url == '%s/registratie/11' % context.base_url

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
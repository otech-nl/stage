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
    
@given('ik ben niet op de pagina Tochten')
def pagina_check__niet_ledenoverzicht(context):
    if context.browser.url == '%s/tocht/' % context.base_url:
        context.browser.find_link_by_partial_href('user').first.click()
    
@when('ik op de link Tochten druk')
def druk_op_tochten(context):
    context.browser.find_link_by_partial_href('tocht').first.click()
    
#@then('kom ik op de pagina Tochten')                                        #wordt al gedaan in andere stepfile(inloggen)
#def inlog_tochten_pagina(context):
 #   assert context.browser.url == '%s/tocht/' % context.base_url

@when('ik op de knop Tocht toevoegen druk')
def druk_op_tocht_toevoegen(context):
    context.browser.find_link_by_partial_href('tocht/0').first.click()
    
@then('zie ik een pagina Tocht bewerken')
def check_pagina_tocht_bewerken(context):
    assert context.browser.is_text_present('Tocht bewerken')
    
@given('ik ben op de tocht bewerken pagina')
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
    #context.browser.find
    table = context.browser.find_by_tag('table')
    #assert len(table) > 0, 'Geen datatable gevonden'
    table.find_by_tag('tr').find_by_tag('th').find_by_name('plaats').first.click()
    sleep(10)
    
    #nu_dan = toenou.find_by_xpath('tr')
    #en_nu = nu_dan[2]
    #print(en_nu)
    #table.find_by_xpath('//td[. = "plaats"]/following-sibling::td/[2]').first.click()
    #row = table.find_by_tag('thead') or table.find_by_tag('tr')
    #head = row.first.text   
    
@when('ik in de tabel op een tocht druk')
def druk_op_tocht(context):
    #hoe werk je met tabellen?
    pass

@then('kom ik op een Tocht bewerken pagina van die tocht')
def check_tocht(context):
    assert context.browser.is_text_present('Tocht bewerken')
    # de value uit het naamveld halen en vergelijken met de tocht de je hebt aangeklikt
    
#@when('ik op de tocht bewerken pagina ben')

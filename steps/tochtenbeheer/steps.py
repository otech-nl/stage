from behave import given, when, then

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
    pass #moet nog gemaakt worden
    
#@then('kom ik op de pagina Tochten')                                        #wordt al gedaan in andere stepfile(inloggen)
#def inlog_tochten_pagina(context):
 #   assert context.browser.url == '%s/tocht/' % context.base_url
    

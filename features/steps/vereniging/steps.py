from behave import given, when, then


@given('ik ben op de vereniging pagina')
def check_pagina(context):
    if context.browser.url != '%s/instellingen/' % context.base_url:
        context.browser.visit('%s/instellingen/' % context.base_url)

@when(u'ik het veld postcode wijzig')
def change_postcode(context):
    postcodeField = context.browser.find_by_id('postcode')
    context.old_postcode = postcodeField.value;
    if postcodeField.value == "":
        context.new_postcode = 'AB 4321'         
    else:
        context.new_postcode = postcodeField.value[::-1] #postcode omdraaien, zinloos indien postcode een palindroom    
    context.browser.find_by_id('postcode').first.fill(context.new_postcode)    

#@when('ik op de knop verwerken druk')   
# Op de 'verwerken' knop drukken is al geimplementeerd in een andere step file, en hoeft daardoor hier niet opnieuw
    
@then(u'verwacht ik dat de gegevens worden opgeslagen')
def check_changed_postcode(context):
    context.browser.visit('%s/rapport/' % context.base_url)
    context.browser.visit('%s/instellingen/' % context.base_url)
    assert context.browser.find_by_id('postcode').value != context.old_postcode
    
#given('ik ben op de vereniging pagina')

@when('ik op de knop Voeg catagorie toe druk') 
def click_add_catagorie_btn(context):
    context.browser.find_link_by_partial_href('Voeg catagorie').first.click()
    assert True
    
@when(u'ik op de knop \'Voeg catagorie toe\' druk')
def step_impl(context):
    raise NotImplementedError(u'STEP: When ik op de knop \'Voeg catagorie toe\' druk')


@when(u'ik vul een naam in voor de nieuwe catagorie')
def step_impl(context):
    raise NotImplementedError(u'STEP: When ik vul een naam in voor de nieuwe catagorie')


@when(u'ik vul een prijs in voor de nieuwe catagorie')
def step_impl(context):
    raise NotImplementedError(u'STEP: When ik vul een prijs in voor de nieuwe catagorie')





#
#Scenario: Catagorie toevoegen
#Stel ik ben op de verenigingspagina
#Als ik op de knop 'Voeg catagorie toe' druk
#en ik vul een naam in voor de nieuwe catagorie #
#en ik vul een prijs in voor de nieuwe catagorie
#En ik op de knop verwerken druk
#Dan verwacht ik dat de gegevens worden opgeslagen
  


   

	

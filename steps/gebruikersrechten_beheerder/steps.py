from behave import given, when, then

@when('ik de inloggegevens van een Beheerder (FLAL) invul')
def inloggen_beheerder_FLAL(context):
    context.browser.find_by_id('email').first.fill('Beheerder FLAL')
    context.browser.find_by_id('password').first.fill('FLAL')
    context.browser.find_by_id('submit').first.click()
    
@when('ik de inloggegevens van een Beheerder (ACV) invul')
def inloggen_beheerder_FLAL(context):
    context.browser.find_by_id('email').first.fill('Beheerder ACV')
    context.browser.find_by_id('password').first.fill('ACV')
    context.browser.find_by_id('submit').first.click()
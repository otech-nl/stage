from behave import given, when, then

@when('ik de inloggegevens van een Bestuurslid (FLAL) invul')
def inlog_bestuurslid_FLAL(context):
    context.browser.find_by_id('email').first.fill('Bestuurslid FLAL')
    context.browser.find_by_id('password').first.fill('FLAL')
    context.browser.find_by_id('submit').first.click()
    
@when('ik de inloggegevens van een Bestuurslid (ACV) invul')
def inlog_bestuurslid_FLAL(context):
    context.browser.find_by_id('email').first.fill('Bestuurslid ACV')
    context.browser.find_by_id('password').first.fill('ACV')
    context.browser.find_by_id('submit').first.click()



@given('ik ben niet ingelogd')
def step_logged_off(context):
    
    loggedoff_url = '%s/login?next=%%2F' % context.base_url
    print(loggedoff_url)
    context.browser.visit(loggedoff_url)
    
@when('ik een geldige gebruikersnaam invoer')
def func(context):
    context.browser.find_by_id('email').first.fill('admin')

@when('ik het goede wachtwoord invoer')
def func1(context):
    context.browser.find_by_id('password').first.fill('nimda')
@when('ik op de knop inloggen druk')
def func2(context):
    context.browser.find_by_id('submit').click
@then('kom ik op de pagina Tochten')
def func3(context):
    pass

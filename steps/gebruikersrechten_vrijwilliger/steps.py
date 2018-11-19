from behave import given, when, then

@given('ik ben uitgelogd')
def uitgelogd(context):
    loggedoff_url = '%s/login?next=%%2F' % context.base_url
    if context.browser.url != loggedoff_url:
        try:
            context.browser.find_link_by_partial_href('/logout').first.click()
        except:
            context.browser.visit(loggedoff_url)
            
@when('ik de inloggegevens van een Vrijwilliger (FLAL) invul')
def inlog_vrijwilliger_FLAL(context):
    context.browser.find_by_id('email').first.fill('Vrijwilliger FLAL')
    context.browser.find_by_id('password').first.fill('FLAL')
    context.browser.find_by_id('submit').first.click() 

@then('wordt ik ingelogd')
def check_inlog(context):
    assert context.browser.url == '%s/tocht/' % context.base_url
    
@when('ik de inloggegevens van een Vrijwilliger (ACV) invul')
def inlog_vrijwilliger_ACV(context):
    context.browser.find_by_id('email').first.fill('Vrijwilliger ACV')
    context.browser.find_by_id('password').first.fill('ACV')
    context.browser.find_by_id('submit').first.click() 
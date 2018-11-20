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
    
@given('ik ben als Beheerder (FLAL) ingelogd')
def check_inlog(context):
    loggedoff_url = '%s/login?next=%%2F' % context.base_url
    base_url = context.base_url
    context.browser.visit(base_url)
    if context.browser.url == loggedoff_url:                                
        context.browser.find_by_id('email').first.fill('Beheerder FLAL')             
        context.browser.find_by_id('password').first.fill('FLAL')          
        context.browser.find_by_id('submit').first.click()                  
    assert context.browser.find_link_by_text('Beheerder FLAL')
    
@then('zie ik alleen de links die een beheerder mag zien')
def check_links(context):
    niet_links = ['role', 'union']
    for niet_link in niet_links:
        assert not context.browser.find_link_by_partial_href(niet_link)
    wel_links = ['instellingen', 'lid', 'rapport', 'tocht', 'logout', 'user']
    for wel_link in wel_links:
        assert context.browser.find_link_by_partial_href(wel_link)
        
@given('ik ben als Beheerder (ACV) ingelogd')
def check_inlog(context):
    loggedoff_url = '%s/login?next=%%2F' % context.base_url
    base_url = context.base_url
    context.browser.visit(base_url)
    if context.browser.url == loggedoff_url:                                
        context.browser.find_by_id('email').first.fill('Beheerder ACV')             
        context.browser.find_by_id('password').first.fill('ACV')          
        context.browser.find_by_id('submit').first.click()                  
    assert context.browser.find_link_by_text('Beheerder ACV')
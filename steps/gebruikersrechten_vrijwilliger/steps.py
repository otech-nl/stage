from behave import given, when, then
from time import sleep

def log_in(context, email, password):
    context.browser.find_by_id('email').first.fill(email)
    context.browser.find_by_id('password').first.fill(password)
    context.browser.find_by_id('submit').first.click()

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
    if context.browser.is_element_present_by_id('email'):                           #zodat er wordt gewacht op het invulveld
        log_in(context, 'Vrijwilliger FLAL', 'FLAL')
        #context.browser.find_by_id('email').first.fill('Vrijwilliger FLAL')
        #context.browser.find_by_id('password').first.fill('FLAL')
        #context.browser.find_by_id('submit').first.click() 

@then('wordt ik ingelogd')
def check_inlog(context):
    assert context.browser.url == '%s/tocht/' % context.base_url
    
@when('ik de inloggegevens van een Vrijwilliger (ACV) invul')
def inlog_vrijwilliger_ACV(context):
    if context.browser.is_element_present_by_id('email'):                           #zodat er wordt gewacht op het invulveld
        log_in(context, 'Vrijwilliger ACV', 'ACV')
    
@given('ik ben als Vrijwilliger (FLAL) ingelogd')
def check_inlog(context):
    loggedoff_url = '%s/login?next=%%2F' % context.base_url
    base_url = context.base_url
    context.browser.visit(base_url)
    if context.browser.url == loggedoff_url:                                
        log_in(context, 'Vrijwilliger FLAL', 'FLAL')               
    assert context.browser.find_link_by_text('Vrijwilliger FLAL')
    
@then('zie ik alleen links die vrijwilligers mogen zien')
def check_links(context):
    niet_links = ['instellingen', 'lid', 'rapport', 'user', 'role', 'union']
    for niet_link in niet_links:
        assert not context.browser.find_link_by_partial_href(niet_link)
    assert context.browser.find_link_by_partial_href('tocht')
    assert context.browser.find_link_by_partial_href('logout')
    
@given('ik ben als Vrijwilliger (ACV) ingelogd')
def check_inlog(context):
    loggedoff_url = '%s/login?next=%%2F' % context.base_url
    base_url = context.base_url
    context.browser.visit(base_url)
    if context.browser.url == loggedoff_url:                                
        log_in(context, 'Vrijwilliger ACV', 'ACV')                 
    assert context.browser.find_link_by_text('Vrijwilliger ACV')
    
@then('kan ik niet via de adresbalk bij voor vrijwilliger illegale links komen')
def check_adresbalk(context):
    niet_links = ['instellingen', 'lid', 'rapport', 'user', 'role', 'union']
    for niet_link in niet_links:
        context.browser.visit('%s/%s' % (context.base_url, niet_link))
        assert context.browser.url != '%s/%s' % (context.base_url, niet_link), context.browser.url

from behave import given, when, then
from time import sleep

def log_in(context, email, password):
    context.browser.find_by_id('email').first.fill(email)
    context.browser.find_by_id('password').first.fill(password)
    context.browser.find_by_id('submit').first.click()

@when('ik de inloggegevens van een Bestuurslid (FLAL) invul')
def inlog_bestuurslid_FLAL(context):
    if context.browser.is_element_present_by_id('email'):                           #zodat er wordt gewacht op het invulveld
        log_in(context, 'Bestuurslid FLAL', 'FLAL')
    
@when('ik de inloggegevens van een Bestuurslid (ACV) invul')
def inlog_bestuurslid_ACV(context):
    if context.browser.is_element_present_by_id('email'):                           #zodat er wordt gewacht op het invulveld
        log_in(context, 'Bestuurslid ACV', 'ACV')

@given('ik ben als Bestuurslid (FLAL) ingelogd')
def check_inlog(context):
    loggedoff_url = '%s/login?next=%%2F' % context.base_url
    base_url = context.base_url
    context.browser.visit(base_url)
    if context.browser.url == loggedoff_url:                                
        log_in(context, 'Bestuurslid FLAL', 'FLAL')
        assert context.browser.find_link_by_text('Bestuurslid FLAL'), context.browser.find_link_by_partial_href('profiel').value
    elif context.browser.find_link_by_partial_href('profiel').value != 'Bestuurslid FLAL':
        try:
            context.browser.find_link_by_partial_href('/logout').first.click()
            log_in(context, 'Bestuurslid FLAL', 'FLAL')
            assert context.browser.find_link_by_text('Bestuurslid FLAL'), context.browser.find_link_by_partial_href('profiel').value
        except:
            assert False
    
@then('zie ik alleen de links die een bestuurslid mag zien')
def check_links(context):
    niet_links = ['user', 'role', 'union']
    for niet_link in niet_links:
        assert not context.browser.find_link_by_partial_href(niet_link)
    wel_links = ['instellingen', 'lid', 'rapport', 'tocht', 'logout']
    for wel_link in wel_links:
        assert context.browser.find_link_by_partial_href(wel_link)
        
@given('ik ben als Bestuurslid (ACV) ingelogd')
def check_inlog(context):
    loggedoff_url = '%s/login?next=%%2F' % context.base_url
    base_url = context.base_url
    context.browser.visit(base_url)
    if context.browser.url == loggedoff_url:                                
        log_in(context, 'Bestuurslid ACV', 'ACV')
        assert context.browser.find_link_by_text('Bestuurslid ACV'), context.browser.find_link_by_partial_href('profiel').value
    elif context.browser.find_link_by_partial_href('profiel').value != 'Bestuurslid ACV':
        try:
            context.browser.find_link_by_partial_href('/logout').first.click()
            log_in(context, 'Bestuurslid ACV', 'ACV')
            assert context.browser.find_link_by_text('Bestuurslid ACV'), context.browser.find_link_by_partial_href('profiel').value
        except:
            assert False, 'wtf is going on'
    
@then('kan ik niet via de adresbalk bij voor bestuurslid illegale links komen')
def check_adresbalk(context):
    niet_links = ['role', 'union', 'user']
    for niet_link in niet_links:
        context.browser.visit('%s/%s' % (context.base_url, niet_link))
        assert context.browser.url != '%s/%s' % (context.base_url, niet_link), context.browser.url
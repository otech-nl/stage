from behave import given, when, then
from time import sleep

def log_in(context, email, password):
    context.browser.find_by_id('email').first.fill(email)
    context.browser.find_by_id('password').first.fill(password)
    context.browser.find_by_id('submit').first.click()

@when('ik de inloggegevens van een Beheerder (FLAL) invul')
def inloggen_beheerder_FLAL(context):
    if context.browser.is_element_present_by_id('email'):                       #zodat er wordt gewacht op het invulveld
        log_in(context, 'Beheerder FLAL', 'FLAL')
    
@when('ik de inloggegevens van een Beheerder (ACV) invul')
def inlog_bestuurslid_ACV(context):
    if context.browser.is_element_present_by_id('email'):                       #zodat er wordt gewacht op het invulveld
        log_in(context, 'Beheerder ACV', 'ACV')
    
@given('ik ben als Beheerder (FLAL) ingelogd')
def check_inlog(context):
    loggedoff_url = '%s/login?next=%%2F' % context.base_url
    base_url = context.base_url
    context.browser.visit(base_url)
    if context.browser.url == loggedoff_url:                                
        log_in(context, 'Beheerder FLAL', 'FLAL')
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
        log_in(context, 'Beheerder ACV', 'ACV')
        assert context.browser.find_link_by_text('Beheerder ACV'), context.browser.find_link_by_tekst('Beheerder ACV').value
    elif context.browser.find_link_by_partial_href('profiel').value != 'Beheerder ACV':
        try:
            context.browser.find_link_by_partial_href('/logout').first.click()
            log_in(context, 'Beheerder ACV', 'ACV')
            assert context.browser.find_link_by_text('Beheerder ACV'), context.browser.find_link_by_tekst('Beheerder ACV').value
        except:
            assert False, 'wtf is going on'
    
@then('kan ik niet via de adresbalk bij voor beheerder illegale links komen')
def check_adresbalk(context):
    niet_links = ['role', 'union']
    for niet_link in niet_links:
        context.browser.visit('%s/%s' % (context.base_url, niet_link))
        assert context.browser.url != '%s/%s' % (context.base_url, niet_link), context.browser.url
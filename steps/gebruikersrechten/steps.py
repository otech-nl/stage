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
            assert False
    
@then('kan ik niet via de adresbalk bij voor beheerder illegale links komen')
def check_adresbalk(context):
    niet_links = ['role', 'union']
    for niet_link in niet_links:
        context.browser.visit('%s/%s' % (context.base_url, niet_link))
        assert context.browser.url != '%s/%s' % (context.base_url, niet_link), context.browser.url

@when('ik een lidnummer invul van een lid van een andere vereniging')
def vul_lidnummer_in(context):
    context.lidnummerFLAL = '702'
    context.browser.find_by_xpath('//input[@type="search"]').first.fill(context.lidnummerFLAL)
    sleep(3)
    
@then('vind ik dat lid niet')
def check_tabel(context):
    table = context.browser.find_by_css('table.table')
    assert len(table) > 0, 'geen table gevonden'
    tabel = context.browser.find_by_tag('tbody')                 
    rows = tabel.find_by_tag('tr') 
    
    #if context.browser.is_element_not_present_by_tag('td'):
    #    assert True 
    #else:
    #    values = [row.find_by_tag('td')[5].value for row in rows]
    #    assert context.lidnummerFLAL not in values, 'gebruiker heeft toegang tot leden van andere vereniging'
        
    try:
        tabel = context.browser.find_by_tag('tbody')
        rows = tabel.find_by_tag('tr') 
        values = [row.find_by_tag('td')[5].value for row in rows]
        assert context.lidnummerFLAL not in values, 'gebruiker heeft toegang tot leden van andere vereniging'
    except IndexError:
        assert True
    
    #try:
    #    values = [row.find_by_tag('td')[5].value for row in rows]
    #    assert context.lidnummerFLAL not in values, 'gebruiker heeft toegang tot leden van andere vereniging'
    #except IndexError:
    #    assert True
    
@when('ik op de link Toernooien klik')
def klik_op_toernooien(context):
    context.browser.find_link_by_partial_href('toernooi').first.click()
    
@then('kom ik op de toernooienpagina')
def check_pagina(context):
    assert context.browser.url == '%s/toernooi/' %context.base_url, 'pagina niet bereikt'
    assert context.browser.is_text_present('Toernooi-overzicht'), 'geen toernooi-overzicht zichtbaar'
    

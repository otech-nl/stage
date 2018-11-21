from behave import given, when, then

def split_and_strip(src, sep=None):
    return [token.strip() for token in src.split(sep)]

def log_in(context, email, password):
    context.browser.find_by_id('email').first.fill(email)
    context.browser.find_by_id('password').first.fill(password)
    context.browser.find_by_id('submit').first.click()

@given('ik ben ingelogd')
def ingelogd_check(context):
    loggedoff_url = '%s/login?next=%%2F' % context.base_url
    base_url = context.base_url
    context.browser.visit(base_url)
    if context.browser.url == loggedoff_url:                                
        log_in(context, 'admin', 'nimda')
    assert context.browser.url != loggedoff_url 
    
@when('ik op de knop uitloggen druk')
def klik_uitloggen(context):
    context.browser.find_link_by_partial_href('/logout').first.click()
    
@then('word ik uitgelogd')
def uitgelogd(context):
    loggedoff_url = '%s/login?next=%%2F' % context.base_url
    assert context.browser.url == loggedoff_url
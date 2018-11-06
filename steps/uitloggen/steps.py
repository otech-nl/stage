from behave import given, when, then

def split_and_strip(src, sep=None):
    return [token.strip() for token in src.split(sep)]

@given('ik ben ingelogd')
def ingelogd_check(context):
    loggedoff_url = '%s/login?next=%%2F' % context.base_url
    base_url = context.base_url
    context.browser.visit(base_url)
    if context.browser.url == loggedoff_url:                                
        context.browser.find_by_id('email').first.fill('admin')             #moet makkelijker kunnen
        context.browser.find_by_id('password').first.fill('nimda')          #
        context.browser.find_by_id('submit').first.click()                  #
    assert context.browser.url != loggedoff_url 
    
@when('ik op de knop uitloggen druk')
def klik_uitloggen(context):
    context.browser.find_link_by_partial_href('/logout').first.click()
    
@then('word ik uitgelogd')
def uitgelogd(context):
    loggedoff_url = '%s/login?next=%%2F' % context.base_url
    assert context.browser.url == loggedoff_url
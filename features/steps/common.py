from pprint import pprint
from time import sleep
from urllib.parse import urljoin

from behave import given, when, then  # pylint: disable=no-name-in-module
from selenium.common.exceptions import WebDriverException
from splinter.exceptions import ElementDoesNotExist


class Credentials:

    def __init__(self, email, password):
        self.email = email
        self.password = password

credentials = {
    'admin': Credentials('admin', 'nimda'),
    'Vrijwilliger (FLAL)': Credentials('Vrijwilliger FLAL', 'FLAL'),
    'Vrijwilliger (ACV)': Credentials('Vrijwilliger ACV', 'ACV'),
    'Bestuurslid (FLAL)': Credentials('Bestuurslid FLAL', 'FLAL'),
    'Bestuurslid (ACV)': Credentials('Bestuurslid ACV', 'ACV'),
    'Beheerder (FLAL)': Credentials('Beheerder FLAL', 'FLAL'),
    'Beheerder (ACV)': Credentials('Beheerder ACV', 'ACV')
}


def split_and_strip(src, sep=None):
    return [token.strip() for token in src.split(sep)]

def full_url(context, path):
    return urljoin(context.base_url, path)

def visit(context, path):
    url = full_url(context, path)
    return context.browser.visit(url)

def cmp_url(context, path):
    return context.browser.url == full_url(context, path)

def click(context, link):
    try:
        link = context.browser.find_link_by_partial_href(link)
        link = link.first
        link.click()
        return link
    except ElementDoesNotExist:
        return None

def select(context, val):
    context.browser.find_option_by_text(val).first.click()

def fill_form(context, values):
    for key, val in values.items():
        element = context.browser.find_by_id(key).first
        element.clear()
        element.fill(val)


@given('ik ben ingelogd als "{role}"')
def inlog_role(context, role):
    uitgelogd(context)
    creds = credentials[role]
    fill_form(context, dict(
        email=creds.email,
        password=creds.password))
    context.browser.find_by_id('submit').first.click()
    assert context.browser.find_link_by_text(creds.email)


@given('ik ben uitgelogd')
def uitgelogd(context):
    visit(context, '/')   # avoid any modals
    click(context, '/logout')


@given('ik ben niet ingelogd')
def step_logged_off(context):
    visit(context, context.base_url)
    loggedoff_url = '%s/login?next=%%2F' % context.base_url
    if context.browser.url != loggedoff_url:
        context.browser.find_link_by_partial_href('/logout').first.click()


@given('ik ben op de pagina "{page}"')
def goto_pagina(context, page):
    if not cmp_url(context, page):
        visit(context, page)


@given('ik ben niet op de pagina "{page}"')
def check_pagina_is_niet(context, page):
    if cmp_url(context, page):
        click(context, 'user' if page == 'tocht' else 'tocht')


@when('ik op de link "{link}" druk')
def druk_op_link(context, link):
    click(context, link)


@when('ik op de knop "{knop}" druk')
def druk_op_knop(context, knop):
    click(context, knop)


@when('ik {aantal} sec wacht')
def step_wait(context, aantal):
    sleep(int(aantal))


@when('ik het formulier invul met "{values}"')
def step_form(context, values):
    pairs = {key: val for key, val in [split_and_strip(pair, ':') for pair in split_and_strip(values, ',')]}
    fill_form(context, pairs)


@then('ben ik ingelogd')
def check_inlog(context):
    check_pagina(context, 'tocht/')


@then('zie ik de pagina "{page}"')
def check_pagina(context, page):
    url = full_url(context, page)
    assert context.browser.url == url, '%s != %s' % (context.browser.url, url)


@then('zie ik de tekst "{txt}"')
def check_link_incasso(context, txt):
    assert context.browser.is_text_present(txt)


@then('zie ik een tabel met kolommen "{columns}"')
def step_table(context, columns):
    tables = context.browser.find_by_css('table.table')
    assert len(tables) > 0, 'Geen datatable gevonden'
    table = tables.first
    row = table.find_by_tag('thead') or table.find_by_tag('tr')
    head = row.first.text
    for col in split_and_strip(columns, ','):
        assert col in head, 'Kolom "%s" niet gevonden in "%s"' % (col, head)

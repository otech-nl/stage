from time import sleep

from behave import given, when, then  # pylint: disable=no-name-in-module
from splinter.exceptions import ElementDoesNotExist

from common import credentials, inlog_role, druk_op_link, cmp_url, visit


@when('ik de inloggegevens van een "{role}" invul')
def inloggegevens(context, role):
    inlog_role(context, role)


links = dict(
    vrijwilliger=dict(
        niet=['instellingen', 'lid', 'rapport', 'user', 'role', 'union'],
        wel=[]
    ),
    bestuurslid=dict(
        niet=['user', 'role', 'union'],
        wel=['instellingen', 'lid', 'rapport', 'logout']
    ),
    beheerder=dict(
        niet=['role', 'union'],
        wel=['instellingen', 'lid', 'rapport', 'user']
    )
)


@then('zie ik alleen links die een {role} mag zien')
def check_links(context, role):
    for link in links[role]['niet']:
        assert not context.browser.find_link_by_partial_href(link), '%s kan onterecht bij %s' % (role, link)
    for link in links[role]['wel'] + ['tocht', 'logout']:
        assert context.browser.find_link_by_partial_href(link), '%s kan niet bij %s' % (role, link)


@then('kan ik niet via de adresbalk bij voor een {role} illegale links komen')
def check_adresbalk(context, role):
    for link in links[role]['niet']:
        visit(context, link)
        sleep(1)
        assert not cmp_url(context, link + '/'), '%s kan onterecht bij %s' % (role, context.browser.url)


@when('ik lidnummer {nummer} invul')
def vul_lidnummer_in(context, nummer):
    context.lidnummer = nummer
    context.browser.find_by_xpath('//input[@type="search"]').first.fill(context.lidnummer)
    sleep(3)


@then('vind ik dat lid niet')
def check_tabel(context):
    table = context.browser.find_by_css('table.table')
    assert len(table) > 0, 'geen table gevonden'
    tabel = context.browser.find_by_tag('tbody')
    rows = tabel.find_by_tag('tr')
    resultaat = rows.find_by_tag('td').value
    if resultaat != 'Geen resultaten gevonden':
        values = [row.find_by_tag('td')[5].value for row in rows]
        assert context.lidnummer not in values, 'gebruiker heeft toegang tot leden van andere vereniging: ' + context.lidnummer


@then('kom ik op de pagina "{page}"')
def check_pagina(context, page):
    assert context.browser.is_text_present(page), '"%s" niet zichtbaar' % page

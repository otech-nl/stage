from time import sleep

from behave import given, when, then  # pylint: disable=no-name-in-module

from common import druk_op_link, check_pagina

@when('ik op de knop gebruiker toevoegen druk')
def druk_op_toevoegen(context):
    druk_op_link(context, 'user/0')


@then('zie ik de pagina om een gebruiker toe te voegen')
def check_user_pagina(context):
    check_pagina(context, 'user/0')


@when('ik op een gebruiker druk')
def druk_op_een_gebruiker(context):
    table = context.browser.find_by_css('table.table')
    assert len(table) > 0, 'geen table gevonden'
    tabel = context.browser.find_by_tag('tbody')
    rows = tabel.find_by_tag('tr')
    cell = rows[0].find_by_tag('td')
    context.naamGebruiker = cell.value
    cell.click()


@then('zie ik de pagina om de gebruiker te bewerken')
def check_edit_pagina(context):
    assert context.naamGebruiker == context.browser.find_by_id('email').value

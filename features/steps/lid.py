from time import sleep

from behave import given, when, then  # pylint: disable=no-name-in-module

from common import split_and_strip, select


@when('ik in het zoekveld "{waarde}" invul')
def zoek_achternaam(context, waarde):
    context.browser.find_by_xpath('//input[@type="search"]').first.fill(waarde)
    #sleep(2)


@then('zie ik alle leden met "{waarde}"')
def check_tabel_results(context, waarde):
    sleep(2)
    table = context.browser.find_by_tag('tbody')
    rows = table.find_by_tag('tr')
    values = [row.find_by_tag('td')[2].value for row in rows]
    assert all(waarde in values for values in values), values


@then('leegt behave het zoekveld voor volgende tests')
def leeg_zoekveld(context):
    context.browser.find_by_xpath('//input[@type="search"]').first.clear()
    # cleart niks maar de boel wordt wel vrolijk groen?????????
    # in ptpyhon komt deze melding: splinter.exceptions.ElementDoesNotExist:
    # no elements could be found with xpath "//input[@type="search"]"
    # terwijl @when('ik in het zoekveld een achternaam invul') het element
    # wel vindt en invult zoals opgedragen
    sleep(3)


@when('ik in de tabel op "{title}" druk')
def druk_op_achternaam(context, title):
    clicked = False
    for cell in context.browser.find_by_tag('th'):
        if cell.text == title:
            cell.click()
            clicked = True
    assert clicked, 'Column "%s" not in %s' % (title, context.browser.find_by_tag('th'))
    sleep(2)


@then('wordt de tabel op "{title}" gesorteerd')
def check_volgorde_van_plaatsnamen(context, title):
    headers = [cell.text for cell in context.browser.find_by_tag('th')]
    column = headers.index(title)
    table = context.browser.find_by_tag('tbody')
    values = [row.find_by_tag('td')[column].value for row in table.find_by_tag('tr')]
    assert values == sorted(values), 'niet gesorteerd:' + str(values)


@then('krijg maximaal {size} resultaten per pagina te zien')
def check_tabel_lengte(context, size):
    tables = context.browser.find_by_css('table.table')
    assert len(tables) > 0, 'Geen datatable gevonden'
    tabel = context.browser.find_by_tag('tbody')
    rows = tabel.find_by_tag('tr')
    assert len(rows) <= int(size), 'tabel is te lang:' + len(rows)


@given('behave heeft een lijst van de tweede set van 10 leden')
def stel_lijst_samen(context):
    select(context, '25')
    sleep(1)
    table = context.browser.find_by_tag('tbody')
    rows = table.find_by_tag('tr')
    column = [row.find_by_tag('td') for row in rows]
    lijst = [cell[2].value for cell in column]
    context.lijst2 = lijst[10:20]


@when(u'ik {size} resultaten per pagina selecteer')
def selecteer_aantal_resultaten(context, size):
    select(context, size)
    sleep(1)


@when('ik op pagina {nr} druk')
def ga_naar_pagina_nr(context, nr):
    selector = '//ul/li/a[@data-dt-idx="%s"]' % nr
    context.browser.find_by_xpath(selector).first.click()
    sleep(1)


@then('zie ik de tweede set van 10 leden')
def check_lijst_tegen_lijst(context):
    table = context.browser.find_by_tag('tbody')
    rows = table.find_by_tag('tr')
    lijst = [row.find_by_tag('td')[2].value for row in rows]
    assert lijst == context.lijst2, '%s is niet %s' % (lijst, context.lijst2)


@then('zijn de lidnummers van deze leden uniek')
def check_uniekheid(context):
    tabel = context.browser.find_by_tag('tbody')
    rows = tabel.find_by_tag('tr')
    totalelijst = [row.find_by_tag('td')[5].value for row in rows]
    uniekelijst = list(set(totalelijst))
    if len(totalelijst) != len(uniekelijst):
        counts = [(e, totalelijst.count(e)) for e in uniekelijst if totalelijst.count(e) > 1]
        assert False, 'Er zijn minder unieke lidnummers dan leden in deze lijst. Dus niet elk lidnummer is uniek:\n   %s' % counts

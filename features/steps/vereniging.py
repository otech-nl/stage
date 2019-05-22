from time import sleep

from behave import given, when, then  # pylint: disable=no-name-in-module

from common import split_and_strip, check_pagina


@when(u'ik het veld postcode wijzig')
def change_postcode(context):
    postcodeField = context.browser.find_by_id('postcode')
    context.old_postcode = postcodeField.value;
    if postcodeField.value == "":
        context.new_postcode = 'AB 4321'
    else:
        context.new_postcode = postcodeField.value[::-1] #postcode omdraaien, zinloos indien postcode een palindroom
    context.browser.find_by_id('postcode').first.fill(context.new_postcode)


@then(u'verwacht ik dat de gegevens worden opgeslagen')
def check_changed_postcode(context):
    context.browser.visit('%s/rapport/' % context.base_url)
    context.browser.visit('%s/instellingen/' % context.base_url)
    assert context.browser.find_by_id('postcode').value != context.old_postcode


@given('het veld afkorting is leeg')
def check_veld_afkorting(context):
    value = context.browser.find_by_id('afkorting').first.value
    if value == '':
        pass


@then('wordt er geen vereniging toegevoegd')
def check_vereniging(context):
    check_pagina(context, 'vereniging/0')


@then('wordt de vereniging toegevoegd')
def check_toevoeging(context):
    rows = context.browser.find_by_tag('tr')
    row = rows[-1]
    cells = row.find_by_tag('td')
    assert cells[0].value == context.afkorting_vereniging, cells[0].value
    assert cells[1].value == context.naam_vereniging, cells[1].value


@then('verwijdert behave de vereniging voor volgende tests')
def verwijder_toegevoegde_vereniging(context):
    rows = context.browser.find_by_tag('tr')
    row = rows[-1]
    cells = row.find_by_tag('td')
    if cells[0].value == context.afkorting_vereniging:
        try:
            cell[0].click()
            context.browser.find_by_xpath('//a[@onclick="delete_item()"]').click()
        except:
            assert False, 'verwijderknop niet aanwezig'
# verenigingen kunnen niet verwijderd worden

from splinter import Browser
import pytest
import os
import re
from time import sleep

def _mk_tmp(request, factory):
    name = request.node.name
    name = re.sub(r"[\W]", "_", name)
    MAXVAL = 30
    name = name[:MAXVAL]
    return factory.mktemp(name, numbered=True)

@pytest.fixture(autouse=True, scope='session')
def context():
    class Context(object):
        pass
    return Context()
    

@pytest.fixture(scope='session')
def session_tmpdir(request, tmpdir_factory):
    """pytest tmpdir which is session-scoped."""
    return _mk_tmp(request, tmpdir_factory)

@pytest.fixture(autouse=True, scope='session')
def setup(context, request):
    HEADLESS = False
    os.environ['QT_QPA_PLATFORM'] = 'offscreen'

    context.base_url = 'http://192.168.2.66'
    context.browser = Browser('chrome',
                                  executable_path='/usr/lib/chromium-browser/chromedriver',
                                  headless=HEADLESS)

    request.addfinalizer(context.browser.quit)


#def fin(context):
#    if context.browser:
#        context.browser.quit()
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

@pytest.fixture(scope='session')
def session_tmpdir(request, tmpdir_factory):
    """pytest tmpdir which is session-scoped."""
    return _mk_tmp(request, tmpdir_factory)

@pytest.fixture(autouse=True, scope='session')
def context(request):
    HEADLESS = False
    os.environ['QT_QPA_PLATFORM'] = 'offscreen'

    class Context:
        def __init__(self):
            self.base_url = 'http://192.168.2.66'
            self.browser = Browser('chrome',
                                  executable_path='/usr/lib/chromium-browser/chromedriver',
                                  headless=HEADLESS)
    def fin():
        browser.quit()
    request.addfinalizer(fin)

    return Context()
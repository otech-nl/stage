import os
from splinter import Browser


HEADLESS = True
HEADLESS = False


def before_all(context):
    os.environ['QT_QPA_PLATFORM'] = 'offscreen'
    context.base_url = 'http://192.168.2.66' #testserver
    context.session = None  # for requests

    if os.name == 'posix':
        context.browser = Browser('chrome',
                                  executable_path='/usr/lib/chromium-browser/chromedriver',
                                  headless=HEADLESS)
    elif os.name == 'nt':
        context.browser = Browser('chrome',
            executable_path='C:/Program Files (x86)/chromedriver.exe',
            headless=HEADLESS)
        # context.browser = Browser('Edge',
        #     executable_path='C:/Program Files (x86)/MicrosoftWebDriver.exe',
        #     headless=HEADLESS)



# def after_all(context):
#     if context.session:
#         context.session.close()

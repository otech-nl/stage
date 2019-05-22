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


def enable_download_in_headless_chrome(self, browser, download_dir):
    #add missing support for chrome "send_command"  to selenium webdriver
    browser.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
    params = {'cmd': 'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': download_dir}}
    browser.execute("send_command", params)
    
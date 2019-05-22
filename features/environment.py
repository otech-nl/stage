import os

from splinter import Browser


HEADLESS = True
HEADLESS = False

BASE_URL = 'http://0.0.0.0:5000/'

def before_all(context):
    os.environ['QT_QPA_PLATFORM'] = 'offscreen'
    context.session = None  # for requests
    context.base_url = BASE_URL

    if os.name == 'posix':
        context.browser = Browser('chrome',
                                  executable_path='/usr/lib/chromium-browser/chromedriver',
                                  headless=HEADLESS)
    elif os.name == 'nt':
        context.browser = Browser('chrome',
                                  executable_path='C:/Program Files (x86)/chromedriver.exe',
                                  headless=HEADLESS)

        # self.browser = Browser('Edge',
        #     executable_path='C:/Program Files (x86)/MicrosoftWebDriver.exe',
        #     headless=HEADLESS)


def before_scenario(context, scenario):
    if "skip" in scenario.effective_tags:
        scenario.skip("Marked with @skip")
        return


def enable_download_in_headless_chrome(self, browser, download_dir):
    #add missing support for chrome "send_command"  to selenium webdriver
    browser.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
    params = {'cmd': 'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': download_dir}}
    browser.execute("send_command", params)

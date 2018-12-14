import os
from splinter import Browser
from radish import before, world, after
import radish


HEADLESS = True
HEADLESS = False


@before.all
def before_all(features, marker):
    start_browser()
    
@after.all
def after_all(features, marker):
    close_browser()
    
def start_browser():
    world.browser = chrome_driver()
    world.base_url = 'http://192.168.2.66' #testserver
    world.session = None  # for requests
        
def chrome_driver():
    os.environ['QT_QPA_PLATFORM'] = 'offscreen'
    if os.name == 'posix':
        browser = Browser('chrome',
                                  executable_path='/usr/lib/chromium-browser/chromedriver',
                                  headless=HEADLESS)
            
    elif os.name == 'nt':
        browser = Browser('chrome',
            executable_path='C:/Program Files (x86)/chromedriver.exe',
            headless=HEADLESS)
    
    return browser

def close_browser():
    if world.browser:
        world.browser.quit()
# features/environment.py
from utils.browser_utils import open_url, close_browser

def before_all(context):
    context.browser = open_browser()

def after_all(context):
    close_browser(context.browser)
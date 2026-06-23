from playwright.sync_api import Page
from utils.logger import setup_logger
logger = setup_logger()

class BasePage:

    def __init__(self, page: Page):
        self.page = page

    def navigate(self, url):
        # logger.info(f"Clicking in the {url}")
        self.page.goto(url)

    def click(self, locator):
        # logger.info(f"Clicking on the {locator}")
        locator.click()

    def fill(self, locator, text):
        # logger.info(f"enter the info of {text}")
        locator.fill(text)

    def get_title(self):
        return self.page.title()

    def current_url(self):
        return self.page.url
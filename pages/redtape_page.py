from playwright.sync_api import Page, expect
from pages.base_page import BasePage
from utils.logger import setup_logger
from test_data.test_data import URL

logger = setup_logger()


class RedTapePage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

        # Locators
        self.search_box = page.get_by_placeholder("What are you looking for?" )
        self.product = page.get_by_role("link",name = "Round Neck T-Shirt for Men").first
        self.add_to_cart_button = page.get_by_role("button",name="add")
        self.view_cart_link = page.get_by_role("link",name="View cart")

# Perform actions on the RedTape page
    def open_website(self):
        logger.info("Opening RedTape Website")
        self.navigate(URL)

    def search_product(self, product_name):
        logger.info(f"Searching product: {product_name}")
        self.fill(self.search_box,product_name)

    def select_product(self):
        logger.info("Selecting product")
        self.product.click(timeout=10000)

    def add_product_to_cart(self):
        logger.info("Adding product to cart")
        self.click(self.add_to_cart_button)

    def verify_cart_visible(self):
        logger.info("Verifying cart visibility")
        expect(self.view_cart_link).to_be_visible(timeout =10000)

    def open_cart(self):
        logger.info("Opening cart page")
        self.click(self.view_cart_link)

    def get_page_title(self):
        return self.get_title()
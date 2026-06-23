from playwright.sync_api import expect
from pages.base_page import BasePage
from utils.logger import setup_logger
from test_data.test_login_data import URL
logger = setup_logger()

class SaucePage(BasePage):

    def __init__(self, page):
        super().__init__(page)

        # Locators
        self.username_input = page.get_by_placeholder("Username")
        self.password_input = page.get_by_placeholder("Password")
        self.login_button = page.get_by_role("button", name="Login")
        self.product_add_cart_button = page.locator("#add-to-cart-sauce-labs-backpack")
        self.cart_view_button = page.locator("#shopping_cart_container")
        self.checkout_button = page.get_by_role("button", name ="checkout")
        self.first_name_input = page.get_by_placeholder("First Name")
        self.last_name_input = page.get_by_placeholder("Last Name")
        self.postal_code_input = page.get_by_placeholder("Zip/Postal Code")
        self.continue_button = page.locator("#continue")
        self.finish_button = page.get_by_role("button", name="finish")
        self.back_to_home_button = page.get_by_role("button", name="back-to-products")

#Actions Performed on Sauce Demo page

    def open_website(self):
        logger.info("Opening Sauce Demo Website")
        self.navigate(URL)

    def login(self, username, password):
        logger.info(f"Logging in with username: {username}")
        self.fill(self.username_input, username)
        self.fill(self.password_input, password)
        self.click(self.login_button)

    def verify_login_successful(self):
        logger.info("Verifying login was successful")
        expect(self.page.get_by_text("Products")).to_be_visible()

    def add_product_to_cart(self):
        logger.info("Adding product to cart")
        self.click(self.product_add_cart_button)
        logger.info("Product added to cart successfully")
        logger.info("Navigating to cart view")
        self.click(self.cart_view_button)
        logger.info("Cart view opened successfully")

    def checkout(self, first_name, last_name, postal_code):
        logger.info("Initiating checkout process")
        self.click(self.checkout_button)
        self.fill(self.first_name_input, first_name)
        self.fill(self.last_name_input, last_name)
        self.fill(self.postal_code_input, postal_code)
        self.click(self.continue_button)
        logger.info("Checkout information submitted successfully")

    def finish_checkout(self):
        logger.info("Finishing checkout process")
        self.click(self.finish_button)
        logger.info("Checkout process completed successfully")


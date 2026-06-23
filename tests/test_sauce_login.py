from pages.sauce_page import SaucePage
from test_data.test_login_data import URL, USERNAME, PASSWORD
from utils.logger import setup_logger
logger = setup_logger()

def test_sauce_login(page):
    logger.info("Starting Sauce Demo Login Test :")
    sauce_page = SaucePage(page)
    sauce_page.open_website()
    sauce_page.login(USERNAME, PASSWORD)
    sauce_page.verify_login_successful()
    logger.info("Login test completed successfully")
    sauce_page.add_product_to_cart()
    sauce_page.checkout("John", "Doe", "12345")
    sauce_page.finish_checkout()
    
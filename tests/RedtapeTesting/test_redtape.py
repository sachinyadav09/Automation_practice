from pages.redtape_page import RedTapePage
from test_data.test_data import PRODUCT_NAME
from utils.logger import setup_logger

logger = setup_logger()

def test_redtape_cart(page):

    logger.info("Starting RedTape Cart Test")

    redtape = RedTapePage(page)
    redtape.open_website()
    redtape.search_product(PRODUCT_NAME)
    redtape.select_product()
    redtape.add_product_to_cart()
    redtape.verify_cart_visible()
    redtape.open_cart()

    logger.info(f"Page Title: {redtape.get_page_title()}")
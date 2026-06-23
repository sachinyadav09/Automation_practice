from playwright.sync_api import expect, sync_playwright
from utils.logger import setup_logger
logger = setup_logger()
def test_oracle(page):
    
    logger.info("Starting test: test_oracle")
    page.goto("https://www.netsuite.com/portal/in/home.shtml")
    with page.expect_popup() as obj:
        page.get_by_role("link", name="Discover More").click()
        nw = obj.value
        logger.info("Clicked on Discover More link")
        roll= nw.locator("ul.story-specs__list--sub.list-unstyled").get_by_role("link", name="NetSuite OneWorld")
        logger.info("Located the link")
        roll.scroll_into_view_if_needed()
        logger.info("Scrolled into view")
        expect(roll).to_be_visible(timeout=10000)
        logger.info("Link is visible")
        roll.click()
        logger.info("Clicked on NetSuite OneWorld link")
        nw.wait_for_timeout(5000)
        nw.locator("#customers-tab").click()
        logger.info("Clicked on Customers tab")
        nw.locator("ul.list-unstyled").get_by_role("link", name="Brex, the Fintech Star, Looks Back on Its Switch from QuickBooks to NetSuite").click()
        nw.wait_for_timeout(2000)
        logger.info("Clicked on the specific customer story link")
        logger.info("Taking screenshot of the customer story page")
        nw.screenshot(path="screen_shots/customer_story.png")
        logger.info("Testing is completed")



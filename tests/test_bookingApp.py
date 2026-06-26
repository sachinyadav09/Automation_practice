from pages.booking_app_page import BookingAppPage
from utils.logger import setup_logger

logger = setup_logger()

logger.info("Starting of BookingApp Application")

def test_BookApp_web(page):
    booking_app_page = BookingAppPage(page)
    logger.info("Login in the Application")
    booking_app_page.visit_site()

# def test_click_action_btn(page):
#     booking_app_page = BookingAppPage(page)
#     booking_app_page.visit_site()
#     logger.info("Click on the action btn")
#     booking_app_page.click_action_btn()

# def test_login(page):
#     logger.info("Staring Login testing")
#     booking_app_page = BookingAppPage(page)
#     booking_app_page.visit_site()
#     booking_app_page.click_action_btn()
#     booking_app_page.login("Sachinyadav121", "password@11")
#     logger.info("Login testing Done..")
#     booking_app_page.backTohome()
    
def test_BookAvailability(page):
    logger.info("Starting testing for Reserve Room")
    booking_app_page = BookingAppPage(page)
    booking_app_page.visit_site()
    booking_app_page.BookingBtn()
    booking_app_page.to_checIN()
    booking_app_page.to_checOUT()
    booking_app_page.click_checkAvailability_btn()
    booking_app_page.roomBook_btn()
    booking_app_page.reserveRoom_btn("Sachin","yadav","ss@gmail.com","987654321234")
    logger.info("Done with the Testing it Working..")


      


    



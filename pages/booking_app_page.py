from playwright.sync_api import Page ,expect 
from pages.base_page import BasePage
from test_data.booking_app_data import URL
from utils.logger import setup_logger

logger = setup_logger()

class BookingAppPage(BasePage):
    def __init__(self, page:Page):
        super().__init__(page)

    # locators
        self.action_btn= page.get_by_role("link", name = "Admin").first
        self.username_btn = page.locator("#username")
        self.password_btn = page.locator("#password")
        self.login_btn = page.get_by_role("button", name ="Login")
        self.back_home_page = page.locator("#frontPageLink")
        self.booking_btn = page.get_by_role("link" , name = "Booking").first
        self.checkIn = page.locator("label[for = 'checkin'] + div input ")
        self.checkOut = page.locator("label[for = 'checkout'] + div input ")
        self.checkAvailability_btn= page.get_by_role("button" , name = "Check Availability")
        self.bookRoom_btn = page.get_by_role( "link",name="Book now").nth(1)
        self.reserve_btn = page.locator("#doReservation")
        self.reserve_fN = page.get_by_placeholder("Firstname")
        self.reserve_LN = page.get_by_placeholder("Lastname")
        self.reserve_email = page.get_by_placeholder("Email")
        self.reserve_phoneNum = page.get_by_placeholder("Phone")
        self.confirmReserve_btn= page.get_by_role("button", name = "Reserve Now")
        expect 
        self.return_to_home = page.locator('a[type="button"]' ).filter(has_text="Return home") 
        


    def visit_site(self):
        logger.info("Visit the application ")
        self.navigate(URL)

    def click_action_btn(self):
        self.click(self.action_btn)
        logger.info(" Action btn clicked ")
    
    def login(self,username,password):
        logger.info("Typing Username")
        self.fill(self.username_btn,username)
        logger.info("Typing Password")
        self.fill(self.password_btn,password)
        logger.info("Click on Login btn ")
        self.click(self.login_btn)
        expect(self.page.get_by_text ("Invalid credentials")).to_be_visible()
        logger.info("get the text of Invalid credentials")
        
    def backTohome(self):
        logger.info("Click On Front page btn")
        self.click(self.back_home_page)

    def BookingBtn(self):
        logger.info("Clicking on the Booking button/link")
        self.click(self.booking_btn)

    def to_checIN(self):
        logger.info("Go to checkIn ")
        self.checkIn.click()
        logger.info("press ctrl +A")
        self.checkIn.press("Control+A")
        logger.info("press Backspace")
        self.checkIn.press("Backspace")
        logger.info("enter date")
        self.checkIn.type("24/06/2026")
        logger.info("press enter ")
        self.checkIn.press("Enter")

    def to_checOUT(self):
        logger.info("Go to checkOut ")
        self.checkOut.click()
        logger.info("press ctrl +A")
        self.checkOut.press("Control+A")
        logger.info("press Backspace")
        self.checkOut.press("Backspace")
        logger.info("enter date")
        self.checkOut.type("27/06/2026")
        logger.info("press enter ")
        self.checkOut.press("Enter")

    def click_checkAvailability_btn(self):
        logger.info("Click on the check Availability Button")
        self.checkAvailability_btn.click()
        # self.page.wait_for_timeout(2000)

    def roomBook_btn(self):
        logger.info("waiting to book now button  ")
        expect(self.bookRoom_btn).to_be_visible(timeout=10000)
        logger.info("Clicking Book Now button")
        self.bookRoom_btn.click()    
    
    def reserveRoom_btn(self,firstname,lastname, email ,phone):
        logger.info("Clicking on the ReserveButton")
        self.reserve_btn.click()
        logger.info("typing first_name")
        self.reserve_fN.fill(firstname)
        logger.info("typing last_name")
        self.reserve_LN.fill(lastname)
        logger.info("typing email")
        self.reserve_email.fill(email)
        logger.info("typing phone_number")
        self.reserve_phoneNum.fill(phone)
        logger.info("Clicking on Confirn Reserve Now button")
        self.confirmReserve_btn.click()
        expect(self.page.get_by_text ("Booking Confirmed")).to_be_visible()
        logger.info("Text is shown")
        self.page.wait_for_timeout(2000)
        logger.info("Return to Home Page")
        self.return_to_home.click()
        self.page.wait_for_timeout(2000)

    






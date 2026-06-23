from pages.automation_page import AutomationPage
from test_data.test_data import USERNAME
from utils.logger import setup_logger

logger = setup_logger()
logger.info("Starting Automation Practice Test")

def test_automation_practice(page):
    automation_page = AutomationPage(page)
    logger.info("Button Testing is Starting..")
    automation_page.opening_website()
    automation_page.click_button("Primary Action")
    automation_page.click_button("Toggle Button")
    automation_page.click_button("Div With button role")
    automation_page.click_button("START")
    automation_page.click_button("STOP")
    logger.info("Button Testing  Done..")


def test_mouse_features(page):
    automation_page =AutomationPage(page)
    logger.info("Mouse & Slider Testing Starting..")
    automation_page.opening_website()
    automation_page.hover_button()
    automation_page.move_slider()
    automation_page.drop_down("Item 98")
    logger.info("Mouse & Slider Testing Done..")


def test_new_tab(page):
    automation_page = AutomationPage(page)
    automation_page.opening_website()
    logger.info("Tab changing & USERNAME typing  functionality Started")
    automation_page.enter_username(USERNAME)
    automation_page.check_checkbox()
    automation_page.search_input("Youtube")
    logger.info("Tab changing & USERNAME typing  functionality Ended..")
    
def test_file_upload(page):
    logger.info("File Upload Testing Started")
    automation_page =AutomationPage(page)
    automation_page.opening_website()
    automation_page.upload_files()
    logger.info("File Upload testng is Done....")


def test_table_pagination(page):
    logger.info("Pagination Testing Starting..")
    automation_page =AutomationPage(page)
    automation_page.opening_website()
    automation_page.pagination_table()
    logger.info("Pagination Testing Starting..")

def test_check_alert(page):
    logger.info("Testing Alert funtionality ")
    automation_page = AutomationPage(page)
    automation_page.opening_website()
    automation_page.alert_button()
    logger.info("Testing alerts Done..")

def test_input_alert_box(page):
    logger.info("Staring testing Input Alert functionality ")
    automation_page = AutomationPage(page)
    automation_page.opening_website()
    automation_page.input_alert_button()
    logger.info("done with the Input alert functionality ")


def test_popup_box(page):
    logger.info("Staring testing Pop-Up functionality ")
    automation_page = AutomationPage(page)
    automation_page.opening_website()
    automation_page.popup_click()
    logger.info("done with the Pop-up  functionality ")  

logger.info("OverAll Testing  is completed..")

    



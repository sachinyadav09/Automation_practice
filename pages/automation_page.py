from playwright.sync_api import Page, expect
from pages.base_page import BasePage
from utils.logger import setup_logger
from test_data.test_data import URL1
logger = setup_logger()

class AutomationPage(BasePage):

    def __init__ (self, page:Page):
        super().__init__(page)

        #define locators there
        self.Primary_button = page.get_by_role("button", name= "Primary Action")
        self.Toggle_button = page.get_by_role("button", name = "Toggle Button")
        self.div_button = page.get_by_role("button", name ="Div with button role")
        self.username_input = page.get_by_role("textbox", name = "Username")
        self.checkbox = page.get_by_role("checkbox", name = " Accept terms")
        self.search_box = page.locator("#Wikipedia1_wikipedia-search-input")
        self.click_search_icon = page.locator(".wikipedia-search-button")
        self.result_click = page.get_by_role("link" , name ="YouTube").first
        self.start_button = page.get_by_role("button" , name = "START")
        self.stop_button = page.get_by_role("button" , name = "STOP")
        self.slider_button = page.locator("#slider-range")
        self.mouse_button = page.get_by_role("button", name = "Point Me")
        self.mouse_slider_button= page.locator(".ui-slider-range")
        self.dropdown_button = page.locator("#comboBox")
        self.upload_multiple_file = page.locator("#multipleFilesInput")
        self.upload_button = page.get_by_role("button", name  = "Upload Multiple Files")
        self.navigate_to_table = page.locator("#pagination")
        self.navigate_pagination = self.navigate_to_table.locator("li").filter(has_text= "3")
        self.Alert_button = page.locator("#alertBtn")
        self.input_Alert_button = page.locator("#promptBtn")
        self.pop_up_button = page.locator("#PopUp")
        self.navigate_home_button = page.get_by_role("link", name="Home").first
        self.product_link = page.get_by_role("link",name = "Products" )
        self.contact_link = page.get_by_role("link", name = "Contact")

# Opening  the Website 
    def opening_website(self):
            logger.info("Opening Automation Practice Website")
            self.navigate(URL1)
# Clicking on the Buttons 
    def click_button(self,button_name):
            # logger.info(f"Clicking on button: {button_name}")
            if button_name == "Primary Action":
                self.click(self.Primary_button)
            elif button_name == "Toggle Button":
                self.click(self.Toggle_button)
            elif button_name == "Div with button role":
                self.click(self.div_button)
            elif button_name == "START":
                   self.click(self.start_button)
            elif button_name == "STOP":
                   self.click(self.stop_button)

# User Login 
    def enter_username(self, username):
                logger.info(f"Entering username: {username}")
                self.fill(self.username_input , username)

# Click on the check_Boxes
    def check_checkbox(self):
                logger.info("checking the checkbox is mark or not ")
                self.click(self.checkbox)

# Searching Functionality 
    def search_input(self, search):
           logger.info("Typing something")
           self.fill(self.search_box , search)
           self.click(self.click_search_icon)
           expect(self.result_click).to_be_visible(timeout=15000)
           try:
               with self.page.expect_popup(timeout=15000) as obj:
                       self.click(self.result_click)
                       nw = obj.value
                       nw.wait_for_timeout(2000)
           except Exception as exc:
               logger.warning("Popup did not open, continuing on current page: %s", exc)
               self.click(self.result_click)
               self.page.wait_for_load_state("load", timeout=15000)
               nw = self.page
               nw.wait_for_timeout(2000)
               
# Hover  on the button 
    def hover_button(self):
           logger.info("Hover on the Point me Button")
           self.mouse_button.scroll_into_view_if_needed()
           expect(self.mouse_button).to_be_visible(timeout=10000)
           self.mouse_button.hover()

# Slider the price range(Use of mouse slider)
    def move_slider(self):
        logger.info("Starting of slider functionality")
        self.pointer = self.mouse_slider_button  
        self.boxer=self.pointer.bounding_box()
        logger.info("pointer move ")
        self.page.mouse.move(self.boxer["x"],self.boxer["y"])
        logger.info("pointer catch ")
        self.page.mouse.down()
        logger.info("move pointer to the d/f value")
        self.page.mouse.move(self.boxer["x"]+ 150 ,self.boxer["y"])
        logger.info("Mouse up ")
        self.page.mouse.up()

#Drop-Down Functionality 
    def drop_down(self,value):
           logger.info("Moving on the dropdown values")
           self.click(self.dropdown_button) 
           self.page.locator("#dropdown .option" , has_text = value)
           logger.info("get the value ")
           self.page.wait_for_timeout(5000)

# Uplaod files functionality 
    def upload_files(self):
           logger.info("strating uplaoding the files ")
           from pathlib import Path
           root = Path(__file__).resolve().parents[1]
           files = [
               root / "screen_shots" / "customer_story.png",
               root / "screen_shots" / "home_page.png",
           ]
           existing = [str(path) for path in files if path.exists()]
           if not existing:
               logger.error("Upload files not found: %s", files)
               return
           self.upload_multiple_file.set_input_files(existing)
           self.click(self.upload_button)
           logger.info("uplaoding of file is Completed ..")

# Pagination in the table 
    def pagination_table(self):
           logger.info("Going the 3 page")
           self.navigate_pagination.click()
           logger.info("INSIDE the 3 page")
           self.row = self.page.locator("#productTable tbody tr" ).filter(has_text="12")
           self.row.locator("input[type='checkbox']").check()

# Checking the alerts Functionality 
    def alert_button(self):
           self.page.on("dialog", lambda dialog: dialog.accept())
           logger.info("clicking on alert button ")
           self.click(self.Alert_button)

# Checking the alerts Functionality with input 
    def input_alert_button(self):
           logger.info("Input the name in the alert box")
           self.page.on("dialog", lambda dialog: dialog.accept("Sachin yadav"))
           self.click(self.input_Alert_button)
           
       
# checking the Pop-up functionality 
    def popup_click(self):
           logger.info("Detect & click the pop-up button")
           with self.page.expect_popup() as obj:
                   self.pop_up_button.click()
                   nP = obj.value
                   nP.wait_for_timeout(1000)

    # def click_link(self):
    #        logger.info("Clicking on the Home Link")
    #        self.click(self.navigate_home_button)
    #        self.page.wait_for_timeout(5000)
    #        self.page.screenshot(path="screen_shots/home_page.png")
                # logger.info(f"Clicking on link: {link_name}")
                # if link_name == "Home":
                #     self.click(self.navigate_home_button)
                # elif link_name == "Products":
                #     self.click(self.product_link)
                # elif link_name == "Contact":
                #     self.click(self.contact_link)
            

    
        
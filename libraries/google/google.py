from libraries.common import act_on_element, capture_page_screenshot, log_message
from config import OUTPUT_FOLDER
import random
import time

class Google():

    def __init__(self, rpa_selenium_instance, credentials: dict):
        self.browser = rpa_selenium_instance
        self.google_url = credentials["url"]


    def access_google(self):
        """
        Access Google from the browser.
        """
        self.browser.go_to(self.google_url)

    def search_movie(self):
        self.browser.input_text_when_element_is_visible('//input[@title="Search"]', "Spider-Man")
        act_on_element('//div[@class="CqAVzb lJ9FBc"]//input[@value="Google Search"]', "click_element")
        time.sleep(5)

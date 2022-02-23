from libraries.common import act_on_element, capture_page_screenshot, log_message
from config import OUTPUT_FOLDER, tabs_dict
import random
import time
from selenium.webdriver.common.keys import Keys

class Google():

    def __init__(self, rpa_selenium_instance, credentials: dict):
        self.browser = rpa_selenium_instance
        self.google_url = credentials["url"]


    def access_google(self):
        """
        Access Google from the browser.
        """
        log_message("Start - Access Google")
        self.browser.go_to(self.google_url)
        log_message("End - Access Google")


    def search_movie(self):
        """
        Searches for the lord of the rings the return of the king.
        """
        log_message("Start - Search Movie")
        search_bar = act_on_element('//input[@title="Search"]', "find_element")
        self.browser.input_text_when_element_is_visible('//input[@title="Search"]', "the lord of the rings the return of the king itunes movie us")
        search_bar.send_keys(Keys.ENTER)
        matched_link = act_on_element('//a[contains(@href, "itunes.apple.com") and not(contains(@href, "translate"))]', "find_elements")[0].get_attribute("href")
        log_message("End - Search Movie")
        return matched_link

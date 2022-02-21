from libraries.common import act_on_element, capture_page_screenshot, log_message
from config import OUTPUT_FOLDER, tabs_dict
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
        # print(self.browser.get_source())
        try:
            act_on_element('//button[child::div[text()="Customise"]]', "click_element", 2)
            act_on_element('//button[@aria-label="Turn on Search customization"]', "click_element")
            act_on_element('//button[@aria-label="Turn on YouTube History"]', "click_element")
            act_on_element('//button[@aria-label="Turn on Ad personalization"]', "click_element")
            act_on_element('//button[child::span[text()="Confirm"]]', "click_element")
            # act_on_element('//button[child::div[text()="I agree"]]', "click_element", 2)
        except Exception as e:
            pass

    def search_movie(self):
        log_message("Start - Search Movie")
        # self.browser.go_to("https://www.google.com/search?q=spiderman%20itunes%20movie%20us")
        self.browser.input_text_when_element_is_visible('//input[@title="Search"]', "Spider-Man")
        act_on_element('//div[@class="CqAVzb lJ9FBc"]//input[@value="Google Search"]', "click_element")
        time.sleep(5)
        capture_page_screenshot(OUTPUT_FOLDER, "SEARCH_MOVIE_FINISHED")
        log_message("End - Search Movie")

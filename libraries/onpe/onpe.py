from libraries.common import act_on_element, capture_page_screenshot, log_message, check_file_download_complete
from config import OUTPUT_FOLDER
import random
import time

class ONPE():

    def __init__(self, rpa_selenium_instance, credentials: dict):
        self.browser = rpa_selenium_instance
        self.onpe_url = credentials["url"]


    def access_onpe(self):
        """
        Access ONPE from the browser.
        """
        self.browser.go_to(self.onpe_url)

    def download_files(self):
        act_on_element('//header[@class="main-header"]//a[text()="Resoluciones"]', "click_element")
        pdf_elements = act_on_element('//div[@class="pdf"]//a', "find_elements")
        for pdf_element in pdf_elements:
            act_on_element(pdf_element, "click_element")
            check_file_download_complete("pdf", 20)


        # time.sleep(10)

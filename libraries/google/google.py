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
        capture_page_screenshot(OUTPUT_FOLDER, "ACCESS_TO_GOOGLE_BEGAN")
        print("ABOUT TO RELOAD")
        self.browser.reload_page()
        print("RELOADED")
        # print(self.browser.get_source())
        try:
            # frame = act_on_element('//*[@id="cnsw"]/iframe', "find_element", 10)
            # frame = act_on_element('tag:iframe', "find_element")
            # print(dir(self.browser))
            # self.browser.find_element_by_class_name('tHlp8d').click()


            capture_page_screenshot(OUTPUT_FOLDER, "1")
            print(self.browser.get_source())
            dropdown = act_on_element('//*[@class="tHlp8d"]', "find_element")
            act_on_element(dropdown, "click_element")

            capture_page_screenshot(OUTPUT_FOLDER, "2")
            # print(self.browser.get_source())

            on_elements = act_on_element('//button[descendant::span[text()="On"]]', "find_elements")
            on_elements = on_elements[:3]
            for index, on_element in enumerate(on_elements):
                act_on_element(on_element, "click_element")
                capture_page_screenshot(OUTPUT_FOLDER, "option_{}".format(index))

            # agree_button = act_on_element('//*[@class="L2AGLb"]', "find_element")
            # agree_button = act_on_element('//button[text()="I agree"]', "find_element")
            agree_button = act_on_element('//button[descendant::span[text()="Confirm"]]', "find_element")

            act_on_element(agree_button, "click_element")

            capture_page_screenshot(OUTPUT_FOLDER, "3")




            # <button class="VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-INsAgc VfPpkd-LgbsSe-OWXEXe-dgl2Hf Rj2Mlf OLiIxf PDpWxe P62QJc S82sre" jscontroller="soHxf" jsaction="click:cOuCgd; mousedown:UX7yZ; mouseup:lbsD7e; mouseenter:tfO1Yc; mouseleave:JywGue; touchstart:p6p2H; touchmove:FwuNnf; touchend:yfqBxc; touchcancel:JMtRjd; focus:AHmuwe; blur:O22p3e; contextmenu:mg9Pef;mlnRJb:fLiPzd;" jsname="vaX9ac" data-disable-idom="true" aria-label="Turn on Search customization">
            # <div class="VfPpkd-Jh9lGc"></div>
            # <div class="VfPpkd-J1Ukfc-LhBDec"></div>
            # <div class="VfPpkd-RLmnJb"></div>
            # <span jsname="V67aGc" class="VfPpkd-vQzf8d" aria-hidden="true">On</span>
            # </button>




             # driver.find_element_by_id('L2AGLb').click()


            frames = act_on_element('//iframe', "find_elements")
            print("IFRAME FOUND")
            # self.browser.switch_to.frame(frame[0])
            print("FRAMES:", frames)
            self.browser.select_frame(frames[0])
            try:
                # act_on_element('//*[@id="introAgreeButton"]', "click_element")
                act_on_element('//button[text()="I agree"]', "click_element", 5)
            except Exception as e:
                self.browser.unselect_frame()
                raise Exception(str(e))
        except Exception as e:
            print(e)
            pass
        # self.browser.switch_window(locator = self.browser.get_window_handles()[tabs_dict["Google"]])
        capture_page_screenshot(OUTPUT_FOLDER, "ACCESS_TO_GOOGLE_FINISHED")

    def search_movie(self):
        log_message("Start - Search Movie")
        # self.browser.go_to("https://www.google.com/search?q=spiderman%20itunes%20movie%20us")
        self.browser.input_text_when_element_is_visible('//input[@title="Search"]', "Spider-Man")
        act_on_element('//div[@class="CqAVzb lJ9FBc"]//input[@value="Google Search"]', "click_element")
        time.sleep(5)
        capture_page_screenshot(OUTPUT_FOLDER, "SEARCH_MOVIE_FINISHED")
        log_message("End - Search Movie")

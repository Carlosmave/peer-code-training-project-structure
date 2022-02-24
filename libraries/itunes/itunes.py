from libraries.common import act_on_element, capture_page_screenshot, log_message, check_file_download_complete, files
from config import OUTPUT_FOLDER, tabs_dict
import random
import time

class Itunes():

    def __init__(self, rpa_selenium_instance, credentials: dict):
        self.browser = rpa_selenium_instance
        self.itunes_url = credentials["url"]
        self.artists_data_dict_list = []


    def access_itunes(self):
        """
        Access Itunes from the browser.
        """
        log_message("Start - Access Itunes")
        self.browser.go_to(self.itunes_url)
        log_message("End - Access Itunes")

    def extract_artists_information(self):
        """
        Extracts the movie information for each artist on Itunes.
        """
        log_message("Start - Extract Artists Information")
        artist_elements = act_on_element('//dd[@class="cast-list__detail"]/a', "find_elements")[:5]
        self.browser.execute_javascript("window.open()")
        self.browser.switch_window(locator = "NEW")
        tabs_dict["Artist Page"] = len(tabs_dict)
        for artist_element in artist_elements:
            artist_data_dict = {}
            self.browser.switch_window(locator = self.browser.get_window_handles()[tabs_dict["Itunes"]])
            link = artist_element.get_attribute('href')
            artist_name = artist_element.text
            match = next((artist_data_dict for artist_data_dict in self.artists_data_dict_list if artist_name in artist_data_dict.keys()), None)
            if not match:
                self.browser.switch_window(locator = self.browser.get_window_handles()[tabs_dict["Artist Page"]])
                self.browser.go_to(link)
                try:
                    data_elements = act_on_element('//section[descendant::h2[@class="section__headline" and text()="Movies"]]//div[@class="we-lockup__text"]', "find_elements")
                    movies_list = []
                    for data_element in data_elements:
                        movie_name = data_element.find_element_by_xpath('./div[contains(@class, "we-lockup__title")]/div').text
                        movie_genre = data_element.find_element_by_xpath('./div[contains(@class, "we-lockup__subtitle")]').text
                        movie_dict = {"Name": movie_name, "Genre": movie_genre}
                        movies_list.append(movie_dict)
                    artist_data_dict[artist_name] = movies_list
                    self.artists_data_dict_list.append(artist_data_dict)
                except Exception as e:
                    capture_page_screenshot(OUTPUT_FOLDER, "Exception_Page_With_Different_Format")
                    log_message("Error: {}".format(str(e)))
        log_message("End - Extract Artists Information")


    def create_report(self):
        """
        Writes the data extracted to an excel file
        """
        log_message("Start - Create Report")
        files.create_workbook(path = "{}/Itunes_Data.xlsx".format(OUTPUT_FOLDER))
        for artists_data_dict in self.artists_data_dict_list:
            for key, value in artists_data_dict.items():
                files.create_worksheet(name = key, content = None, exist_ok = False, header = False)
                files.append_rows_to_worksheet(value, name = key, header = True, start = None)
        files.remove_worksheet(name = "Sheet")
        files.save_workbook(path = None)
        files.close_workbook()
        log_message("End - Create Report")

from libraries.common import log_message, capture_page_screenshot, browser
from libraries.mundialitis.mundialitis import Mundialitis
from libraries.google.google import Google
from libraries.onpe.onpe import ONPE
from libraries.infogob.infogob import Infogob
from libraries.itunes.itunes import Itunes
from libraries.gob.gob import Gob
from config import OUTPUT_FOLDER, tabs_dict
import time



class Process:
    def __init__(self, credentials: dict):
        log_message("Initialization")
        prefs = {
            "profile.default_content_setting_values.notifications": 2,
            "profile.default_content_settings.popups": 0,
            "directory_upgrade": True,
            "download.default_directory": OUTPUT_FOLDER,
            "plugins.always_open_pdf_externally": True,
            "download.prompt_for_download": False
        }
        browser.open_available_browser(preferences = prefs)#browser_selection=["firefox"]
        browser.set_window_size(1920, 1080)
        browser.maximize_browser_window()

        gob = Gob(browser, {"url": "https://www.gob.pe/"})
        self.gob = gob

        # infogob = Infogob(browser, {"url": "https://infogob.jne.gob.pe/Eleccion/FichaEleccion/segunda-vuelta-de-elecci%C3%B3n-presidencial-2016-presidencial_candidatos-y-resultados_7p675u8oH7Q=6u"})
        # infogob.access_infogob()
        # infogob.extract_information()
        # infogob.write_data_to_excel()
        # infogob.read_sample_excel()

        # google = Google(browser, {"url": "https://www.google.com/ncr"})
        # tabs_dict["Google"] = len(tabs_dict)
        # google.access_google()
        # self.google = google
        # browser.execute_javascript("window.open()")
        # browser.switch_window(locator="NEW")
        #
        #
        #
        # onpe = ONPE(browser, {"url": "https://www.onpe.gob.pe/"})
        # tabs_dict["ONPE"] = len(tabs_dict)
        # onpe.access_onpe()
        # self.onpe = onpe
        #
        # browser.switch_window(locator = browser.get_window_handles()[tabs_dict["Google"]])
        # time.sleep(3)
        # browser.switch_window(locator = browser.get_window_handles()[tabs_dict["ONPE"]])
        # time.sleep(3)
        # browser.execute_javascript("window.close()")
        # browser.switch_window(locator = browser.get_window_handles()[tabs_dict["Google"]])

        # mundialitis = Mundialitis(browser, credentials["Mundialitis"])
        # mundialitis.login()
        # self.mundialitis = mundialitis



    def start(self):

        self.gob.access_gob()
        self.gob.move_to_onpe()
        self.gob.select_category()
        self.gob.filter_dates()
        self.gob.download_files()
        self.gob.generate_reports()
        # pass
        # self.onpe.download_files()
        # self.onpe.extract_information()
        # matched_link = self.google.search_movie()
        # itunes = Itunes(browser, {"url": matched_link})
        # self.itunes = itunes
        # self.itunes.access_itunes()
        # tabs_dict["Itunes"] = len(tabs_dict)
        # self.itunes.extract_artists_information()
        # self.itunes.create_report()
        # log_message("Start - Create Lobby")
        # self.mundialitis.create_lobby()
        # log_message("End - Create Lobby")
        # log_message("Start - Register New User")
        # self.mundialitis.register_new_user()
        # log_message("Finish - Register New User")
        # log_message("Start - Join Lobby")
        # self.mundialitis.join_lobby("user")
        # log_message("Finish - Join Lobby")
        # log_message("Start - Login with First User")
        # self.mundialitis.login()
        # log_message("Finish - Login with First User")
        # log_message("Start - Join Lobby with First User")
        # self.mundialitis.join_lobby("creator")
        # log_message("Finish - Join Lobby with First User")
        # log_message("Start - Start Game")
        # self.mundialitis.start_game()
        # log_message("Finish - Start Game")
        # log_message("Start - Play Game")
        # self.mundialitis.play_game()
        # log_message("Finish - Play Game")

    def finish(self):
        log_message("DW Process Finished")
        browser.close_browser()

from libraries.common import act_on_element, capture_page_screenshot, log_message, check_file_download_complete, file_system, pdf
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
        log_message("Start - Access ONPE")
        self.browser.go_to(self.onpe_url)
        log_message("Finish - Access ONPE")

    def download_files(self):
        """
        Downloads files from ONPE.
        """
        log_message("Start - Download Files")
        act_on_element('//header[@class="main-header"]//a[text()="Resoluciones"]', "click_element")
        tab_elements = act_on_element('//div[@class="menu-interna"]//li[position()<4]', "find_elements")
        for tab_element in tab_elements[:-1]:
            act_on_element(tab_element, "click_element")
            check_file_download_complete("pdf", 20)
        act_on_element(tab_elements[-1], "click_element")
        self.browser.switch_window(locator = "NEW")
        download_button_elements = act_on_element('//div[@class="col-md-8"][child::h2[text()="Más vistos en los últimos 7 días"]]//a[child::span[text()="Descargar"]]', "find_elements")
        for download_button_element in download_button_elements:
            act_on_element(download_button_element, "click_element")
            check_file_download_complete("pdf", 20)
        self.browser.execute_javascript("window.close()")
        self.browser.switch_window(locator = self.browser.get_window_handles()[0])
        pdf_elements = act_on_element('//div[@class="pdf"]//a', "find_elements")
        for pdf_element in pdf_elements:
            act_on_element(pdf_element, "click_element")
            check_file_download_complete("pdf", 20)
        log_message("Finish - Download Files")

    def extract_information(self):
        """
        Extracts information from the PDF's downloaded from ONPE.
        """
        log_message("Start - Extract Information")
        result_data = ""
        files_downloaded = file_system.find_files("{}/Ley-*.{}".format(OUTPUT_FOLDER, "pdf"))
        for file_downloaded in files_downloaded:
            text_dict = pdf.get_text_from_pdf(file_downloaded)
            pages_amount = len(text_dict)
            last_page_text = text_dict[pages_amount]
            try:
                first_disposition_name = last_page_text.split("rimera Disposición Final.-")[1].split("Reglamento de Organización  y Funciones")[0][:-3].strip()
                # print(first_disposition_name)
            except IndexError:
                continue
            result_data = result_data + "First Disposition Name: " + first_disposition_name + "\n"
            if "Diario Oficial El Peruano" in last_page_text:
                result_data = result_data + "Includes El Peruano: Yes" + "\n"
            else:
                result_data = result_data + "Includes El Peruano: No" + "\n"
            result_data = result_data + "------------------------------------" + "\n"
        file_system.create_file("{}/Result.txt".format(OUTPUT_FOLDER), content = result_data, encoding = 'utf-8', overwrite = True)
        log_message("Finish - Extract Information")

    def read_text_file(self):
        file_content = file_system.read_file("sample_file.txt", encoding = 'utf-8')
        


        # time.sleep(10)

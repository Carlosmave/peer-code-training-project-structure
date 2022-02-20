from libraries.common import act_on_element, capture_page_screenshot, log_message, check_file_download_complete, files
from config import OUTPUT_FOLDER
import random
import time

class Infogob():

    def __init__(self, rpa_selenium_instance, credentials: dict):
        self.browser = rpa_selenium_instance
        self.infogob_url = credentials["url"]
        self.data_dict_list = []


    def access_infogob(self):
        """
        Access Infogob from the browser.
        """
        self.browser.go_to(self.infogob_url)

    def extract_information(self):
        """
        Extract information from the infogob website.
        """
        data_rows = act_on_element('//table[@id="gridEleccionResultadosElectorales"]/tbody/tr[position()<3]', "find_elements")
        for data_row in data_rows:
            data_dict = {"ORGANIZACIÓN POLÍTICA": data_row.find_element_by_xpath('./td[1]/a').text,
            "TOTAL VOTOS": data_row.find_element_by_xpath('./td[4]').text,
            "PORCENTAJE DE VOTOS VÁLIDOS": data_row.find_element_by_xpath('./td[5]').text}
            self.data_dict_list.append(data_dict)
        print(self.data_dict_list)

    def write_data_to_excel(self):
        """
        Writes the data extracted to an excel file
        """
        files.create_workbook(path = "{}/Infogob_Data.xlsx".format(OUTPUT_FOLDER))
        files.create_worksheet(name = "SEGUNDA VUELTA DE ELECCIÓN PRESIDENCIAL 2016", content = None, exist_ok = False, header = False)
        files.append_rows_to_worksheet(self.data_dict_list, name = "SEGUNDA VUELTA DE ELECCIÓN PRESIDENCIAL 2016", header = True, start=None)
        files.remove_worksheet(name = "Sheet")
        files.save_workbook(path = None)
        files.close_workbook()

    def read_sample_excel(self):
        files.open_workbook("RLTEST.xlsx")
        excel_data_dict_list = files.read_worksheet(name = "Sheet1", header = True)
        files.close_workbook()
        print("LIST OF DICTIONARIES: ", excel_data_dict_list)

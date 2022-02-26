from libraries.common import act_on_element, capture_page_screenshot, log_message, check_file_download_complete, file_system, pdf, files
from config import OUTPUT_FOLDER
import random
import time
from datetime import datetime

class Gob():

    def __init__(self, rpa_selenium_instance, credentials: dict):
        self.browser = rpa_selenium_instance
        self.gob_url = credentials["url"]


    def access_gob(self):
        """
        Access Gob from the browser.
        """
        log_message("Start - Access Gob")
        self.browser.go_to(self.gob_url)
        log_message("Finish - Access Gob")

    def move_to_onpe(self):
        """
        Goes to the ONPE page section.
        """
        log_message("Start - Move to ONPE")
        act_on_element('//a[child::span[text()="El Estado Peruano"]]', "click_element")
        act_on_element('//a[child::div[text()="Organismos Autónomos"]]', "click_element")
        act_on_element('//a[text()="Oficina Nacional de Procesos Electorales (ONPE)"]', "click_element")
        log_message("End - Move to ONPE")

    def select_category(self):
        """
        Gets the category from the text file and clicks it in the page.
        """
        log_message("Start - Select Category")
        category = file_system.read_file("Category.txt", encoding = 'utf-8')
        act_on_element('//a[text()="{}"]'.format(category), "click_element")
        act_on_element('//a[text()="Buscar informes y publicaciones"]', "click_element")
        act_on_element('//h1[text()="Buscador"]', "find_element", 10)
        log_message("End - Select Category")

    def filter_dates(self):
        """
        Filters the documents with the dates indicated.
        """
        log_message("Start - Filter Dates")
        base_link = self.browser.get_location()
        full_link = "{}&desde=28-10-2021&hasta={}".format(base_link, datetime.now().strftime("%d-%m-%Y"))
        self.browser.go_to(full_link)
        log_message("End - Filter Dates")

    def download_files(self):
        """
        Downloads the files specified in the Excel file received as input.
        """
        log_message("Start - Download Files")
        files.open_workbook("Files_To_Download.xlsx")
        excel_data_dict_list = files.read_worksheet(name="Sheet1", header=True)
        files.close_workbook()
        for excel_data_dict in excel_data_dict_list:
            if excel_data_dict["Download Required"].upper() == "YES":
                act_on_element('//article[descendant::a[text()="{}"]]//a[text()="Descargar"]'.format(excel_data_dict["Name"]), "click_element")
                check_file_download_complete("pdf", 20)
        log_message("End - Download Files")

    def generate_reports(self):
        """
        Generates both the Excel and text file reports based on the data retrieved from the pdfs downloaded.
        """
        log_message("Start - Generate Reports")
        report_dict_list = []
        result_data = ""
        downloaded_files = file_system.find_files("{}/*.pdf".format(OUTPUT_FOLDER))
        for downloaded_file in downloaded_files:
            file_name = file_system.get_file_name(downloaded_file)
            text_dict = pdf.get_text_from_pdf(downloaded_file)
            pages_amount = len(text_dict)
            report_dict_list.append({"File Name": file_name, "Amount of Pages": pages_amount})
            if pages_amount > 50:
                result_data = result_data + "File Name: " + file_name + "\n"
                result_data = result_data + "-----------------------------------" + "\n"
        excel_report_path = "{}/Results.xlsx".format(OUTPUT_FOLDER)
        text_report_path = "{}/Results.txt".format(OUTPUT_FOLDER)
        files.create_workbook(path=excel_report_path)
        files.rename_worksheet("Sheet", "Report Data")
        files.append_rows_to_worksheet(report_dict_list, name = "Report Data", header = True, start = None)
        files.save_workbook(path = None)
        files.close_workbook()
        file_system.create_file(text_report_path, content = result_data, encoding = 'utf-8', overwrite = True)
        log_message("End - Generate Reports")

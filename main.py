import unittest
from selenium import webdriver
import page


class PythonOrgSearch(unittest.TestCase):
    # we are inheriting from unittest to access methods and properties needed

    def setUp(self):
        # runs at the beginning
        self.driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
        self.driver.get("http://www.python.org")


    def test_search_python(self):
        main_page = page.MainPage(self.driver)
        assert main_page.is_title_matches()
        main_page.search_text_element = "pycon"
        main_page.click_go_button()
        search_results_page = page.SearchResultPage(self.driver)
        assert search_results_page.is_results_found()


    def tearDown(self):
        # runs at the end
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import page


# requirements: googledriver, selenium package, unittest package

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        print("setup")
        ser = Service('C:\Program Files\chromedriver.exe')
        self.driver = webdriver.Chrome(service=ser)
        self.driver.get("https://www.wallashops.co.il/")

    # for testing:
    # def test_example(self):
    #     print("Test")
    #     assert False
    # def test_example2(self):
    #     print("Test2")
    #     assert True
    # def test_title(self):
    #     mainPage = page.MainPage(self.driver)
    #     assert mainPage.is_title_matches()

    def test_search_walla_shops(self):
        mainPage = page.MainPage(self.driver)
        #assert mainPage.is_title_matches()   #TODO: Unicode the hebrew string וואלה!שופס - אתר הקניות הגדול בישראל"
        mainPage.search_text_element = "ninja"
        mainPage.click_go_button()
        search_result_page = page.SearchResultPage(self.driver)
        assert search_result_page.is_results_found()

    def test_cart_page(self):
        mainPage = page.MainPage(self.driver)
        mainPage.click_cart_button()
        search_result_page = page.SearchResultPage(self.driver)
        assert search_result_page.is_results_found()
        print(f'Cart page is: {search_result_page.is_results_found()}')

    def test_favorites_page(self):
        mainPage = page.MainPage(self.driver)
        mainPage.click_favorites_button()
        search_result_page = page.SearchResultPage(self.driver)
        search_result_page.click_google_button()
        assert search_result_page.is_results_found()
        print(f'Google page is: {search_result_page.is_results_found()}')

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()

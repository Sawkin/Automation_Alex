from locator import *
from element import BasePageElement
from encodings import utf_8

class SearchTextElement(BasePageElement):
    locator = "q"
# class GoButton(BasePageElement):
#     locator = "go"


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):

    search_text_element = SearchTextElement()

    def is_title_matches(self):
        utf8 = "וואלה!שופס - אתר הקניות הגדול בישראל".encode()
        # print(utf8)
        # print(utf8.decode())
        return utf8.decode() in self.driver.title

    def click_go_button(self):
        element = self.driver.find_element(*MainPageLocations.GO_BUTTON)
        element.click()

    def click_cart_button(self):
        element = self.driver.find_element(*MainPageLocations.CART_BUTTON)  # "*" for unpacking the tuple)
        element.click()

    def click_favorites_button(self):
        element = self.driver.find_element(*MainPageLocations.FAVORITES_BUTTON)
        element.click()




class SearchResultPage(BasePage):
    def is_results_found(self):
        return "No results found." not in self.driver.page_source

    def click_google_button(self):
        element = self.driver.find_element(*SearchResultsPageLocators.GOOGLE_BUTTON)
        element.click()
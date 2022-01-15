from selenium.webdriver.common.by import By


class MainPageLocations(object):

    GO_BUTTON = (By.XPATH, "/html/body/div[2]/header/div[1]/div[3]/div[3]/div[2]/form/button[2]")
    CART_BUTTON = (By.CLASS_NAME, "b-header-minicart")
    FAVORITES_BUTTON = (By.CLASS_NAME, "b-header-saved-products-link")


class SearchResultsPageLocators(object):
    GOOGLE_BUTTON = (By.CLASS_NAME, "b-auth-button")

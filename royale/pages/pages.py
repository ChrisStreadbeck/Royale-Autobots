from selenium.webdriver.remote.webdriver import WebDriver

from royale.pages.cards_page import CardsPage
from royale.pages.card_details_page import CardDetailsPage


class Pages:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.cards = CardsPage(driver)
        self.card_details = CardDetailsPage(driver)

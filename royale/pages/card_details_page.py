from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from royale.models.card import Card


class CardDetailsPage:
    def __init__(self, driver: WebDriver):
        self.map = CardDetailsPageMap(driver)
        self.wait = WebDriverWait(driver, 10)

    def get_base_card(self) -> Card:
        card_name = self.map.card_name.text
        card_details = self.map.card_details.text.split(', ')
        card_type = card_details[0]
        card_arena = int(card_details[1].split()[-1])
        card_rarity = self.map.card_rarity.text

        card = {
            'id': 0,
            'name': card_name,
            'icon': None,
            'cost': 0,
            'rarity': card_rarity,
            'type': card_type,
            'arena': card_arena
        }

        return Card(**card)

    def wait_for_page_load(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[text()='Statistics']")))


class CardDetailsPageMap:
    def __init__(self, driver: WebDriver):
        self._driver = driver

    @property  # not necessary, can put when not passing arguments
    def card_name(self):
        return self._driver.find_element(By.CSS_SELECTOR, "[class*=\"cardName\"]")

    @property
    def card_details(self):
        return self._driver.find_element(By.XPATH, "//div[@class=\"card__rarity\"]")

    @property
    def card_rarity(self):
        return self._driver.find_element(By.XPATH, "//span[@class=\"card__common\"]")

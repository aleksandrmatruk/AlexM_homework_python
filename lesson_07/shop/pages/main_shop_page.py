from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class MainShopPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_backpack_to_cart(self):
        self.wait.until(EC.element_to_be_clickable(
            (By.ID, "add-to-cart-sauce-labs-backpack")
        )).click()

    def add_bolt_t_shirt_to_cart(self):
        self.wait.until(EC.element_to_be_clickable(
            (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
        )).click()

    def add_onesie_to_cart(self):
        self.wait.until(EC.element_to_be_clickable(
            (By.ID, "add-to-cart-sauce-labs-onesie")
        )).click()

    def go_to_cart(self):
        self.wait.until(EC.element_to_be_clickable(
            (By.CLASS_NAME, "shopping_cart_link")
        )).click()

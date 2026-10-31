from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_checkout(self):
        self.wait.until(EC.element_to_be_clickable(
            (By.ID, "checkout")
        )).click()

    def get_cart_items(self):
        items = self.wait.until(EC.presence_of_all_elements_located(
            (By.CLASS_NAME, "inventory_item_name")
        ))
        return [item.text for item in items]

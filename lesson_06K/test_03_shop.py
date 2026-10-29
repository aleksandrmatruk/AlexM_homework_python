from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_shop():
    driver = webdriver.Firefox()
    wait = WebDriverWait(driver, 10)

    driver.get("https://www.saucedemo.com/")

    wait.until(EC.element_to_be_clickable(
        (By.ID, "user-name"))).send_keys("standard_user")
    wait.until(EC.element_to_be_clickable(
        (By.ID, "password"))).send_keys("secret_sauce")
    wait.until(EC.element_to_be_clickable(
        (By.ID, "login-button"))).click()

    wait.until(EC.element_to_be_clickable(
        (By.ID, "add-to-cart-sauce-labs-backpack"))).click()
    wait.until(EC.element_to_be_clickable(
        (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"))).click()
    wait.until(EC.element_to_be_clickable(
        (By.ID, "add-to-cart-sauce-labs-onesie"))).click()

    wait.until(EC.element_to_be_clickable(
        (By.CLASS_NAME, "shopping_cart_link"))).click()

    wait.until(EC.element_to_be_clickable(
        (By.ID, "checkout"))).click()

    wait.until(EC.element_to_be_clickable(
        (By.ID, "first-name"))).send_keys("Иван")
    wait.until(EC.element_to_be_clickable(
        (By.ID, "last-name"))).send_keys("Петров")
    wait.until(EC.element_to_be_clickable(
        (By.ID, "postal-code"))).send_keys("123456")
    wait.until(EC.element_to_be_clickable(
        (By.ID, "continue"))).click()

    total = wait.until(EC.presence_of_element_located(
        (By.CLASS_NAME, "summary_total_label"))).text

    assert "$58.29" in total, f"Ожидалось $58.29, получено: {total}"

    driver.quit()

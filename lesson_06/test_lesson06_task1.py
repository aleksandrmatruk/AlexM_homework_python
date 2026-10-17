from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_dynamic_loading():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 15)

    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")

    start_button = driver.find_element(By.CSS_SELECTOR, "#start button")
    start_button.click()

    hello_element = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//h4[text()='Hello World!']")
        )
    )

    driver.save_screenshot("screenshots/lesson06_task1.png")

    assert hello_element.text == "Hello World!", (
        f"Ожидался текст 'Hello World!', а получен '{hello_element.text}'"
    )

    driver.quit()

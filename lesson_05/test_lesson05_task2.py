from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form_submission():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/forms/post")

    name_input = driver.find_element(By.NAME, "custname")
    name_input.send_keys("Александр")

    submit_button = driver.find_element(
        By.XPATH, "//button[contains(text(), 'Submit')]"
    )
    submit_button.click()

    assert "/post" in driver.current_url

    driver.quit()

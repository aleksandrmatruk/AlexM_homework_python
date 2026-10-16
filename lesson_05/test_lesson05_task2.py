from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form_submission():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/forms/post")

    name_input = driver.find_element(By.NAME, "custname")
    name_input.send_keys("Александр")

    old_url = driver.current_url

    submit_button = driver.find_element(
        By.XPATH, "//button[contains(text(), 'Submit')]"
    )
    submit_button.click()

    assert driver.current_url != old_url

    driver.quit()

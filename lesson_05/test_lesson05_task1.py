from selenium import webdriver
from selenium.webdriver.common.by import By


def test_navigation():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online")

    html_form_link = driver.find_element(By.LINK_TEXT, "HTML Form")
    html_form_link.click()

    assert "/forms/post" in driver.current_url
    driver.back()
    assert "httpbin.qa-territory.online" in driver.current_url

    driver.quit()

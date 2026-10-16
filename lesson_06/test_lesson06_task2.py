from selenium import webdriver
from secret import COOKIE_USER_1, COOKIE_USER_2


def test_session_storage_auth():
    driver = webdriver.Chrome()

    driver.get("https://gitflic.ru/")

    driver.add_cookie({
        "name": "SESSION",
        "value": COOKIE_USER_1,
        "domain": "gitflic.ru"
    })

    driver.refresh()

    driver.get("https://gitflic.ru/user/airsworld")

    url_user_1 = driver.current_url

    driver.delete_all_cookies()

    driver.add_cookie({
        "name": "SESSION",
        "value": COOKIE_USER_2,
        "domain": "gitflic.ru"
    })

    driver.refresh()

    driver.get("https://gitflic.ru/user/matrukaleksandr")

    url_user_2 = driver.current_url

    assert url_user_1 != url_user_2, (
        f"URL пользователей должны различаться, "
        f"но оба равны: {url_user_1}"
    )

    driver.quit()

from selenium import webdriver

from lesson_07.shop.pages.cart_page import CartPage
from lesson_07.shop.pages.checkout_page import CheckoutPage
from lesson_07.shop.pages.login_page import LoginPage
from lesson_07.shop.pages.main_shop_page import MainShopPage


def test_shop():
    driver = webdriver.Firefox()

    try:
        # 1. Логин
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        # 2. Добавляем товары в корзину
        shop_page = MainShopPage(driver)
        shop_page.add_backpack_to_cart()
        shop_page.add_bolt_t_shirt_to_cart()
        shop_page.add_onesie_to_cart()

        # 3. Переходим в корзину
        shop_page.go_to_cart()

        # 3.1 Проверяем, что в корзине 3 товара
        cart_page = CartPage(driver)
        items = cart_page.get_cart_items()
        assert len(items) == 3, f"Ожидалось 3, найдено: {len(items)}"

        # 4. Нажимаем Checkout
        cart_page.click_checkout()

        # 5. Заполняем форму
        checkout_page = CheckoutPage(driver)
        checkout_page.fill_form("Иван", "Петров", "123456")
        checkout_page.click_continue()

        # 6. Получаем сумму
        total = checkout_page.get_total()
    finally:
        driver.quit()

    # 7. Проверяем итог
    assert "$58.29" in total, f"Ожидалось $58.29, получено: {total}"

import allure
from selenium import webdriver

from lesson_10.calculator.pages.calculator_page import CalculatorPage


@allure.feature("Калькулятор")
@allure.title("Проверка калькулятора")
@allure.description("Вычисление 7 + 8 с задержкой")
@allure.severity(allure.severity_level.NORMAL)
def test_calculator():
    driver = webdriver.Chrome()

    with allure.step("Открыть калькулятор и установить задержку"):
        calc_page = CalculatorPage(driver)
        calc_page.open()
        calc_page.set_delay("45")

    with allure.step("Выполнить вычисления: 7 + 8 ="):
        calc_page.click_button("7")
        calc_page.click_button("+")
        calc_page.click_button("8")
        calc_page.click_button("=")

    with allure.step("Проверить, что результат равен 15"):
        result = calc_page.get_result("15")
        assert result == "15", f"Ожидалось 15, получено: {result}"

    driver.quit()

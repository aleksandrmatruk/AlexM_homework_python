from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 46)

    def open(self) -> None:
        """
        Открывает страницу калькулятора.

        :return: None
        """
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "slow-calculator.html"
        )

    def set_delay(self, seconds: str) -> None:
        """
        Устанавливает задержку.

        :param seconds: Время задержки в секундах.
        :type seconds: str
        :return: None
        """
        delay_input = self.driver.find_element(By.ID, "delay")
        delay_input.clear()
        delay_input.send_keys(seconds)

    def click_button(self, button_text: str) -> None:
        """
        Нажимает на кнопку калькулятора по её тексту.

        :param button_text: Текст на кнопке (например, '7', '+', '=').
        :type button_text: str
        :return: None
        """
        self.driver.find_element(
            By.XPATH, f"//span[text()='{button_text}']"
        ).click()

    def get_result(self, expected_text: str) -> str:
        """
        Ожидает результата и возвращает итог текстом.

        :param expected_text: Ожидаемый результат.
        :type expected_text: str
        :return: Итоговое значение.
        :rtype: str
        """
        self.wait.until(EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, ".screen"), expected_text
        ))
        return self.driver.find_element(By.CSS_SELECTOR, ".screen").text

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def fill_form(
            self,
            first_name: str,
            last_name: str,
            postal_code: str
    ) -> None:
        """
        Заполняет форму заказа.

        :param first_name: Имя.
        :type first_name: str
        :param last_name: Фамилия.
        :type last_name: str
        :param postal_code: Почтовый индекс.
        :type postal_code: str
        :return: None
        """
        self.wait.until(EC.element_to_be_clickable(
            (By.ID, "first-name")
        )).send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)

    def click_continue(self) -> None:
        """
        Нажимает кнопку продолжения заказа.

        :return: None
        """
        self.wait.until(EC.element_to_be_clickable(
            (By.ID, "continue")
        )).click()

    def get_total(self) -> str:
        """
        Возвращает итоговую сумму заказа.

        :return: Итоговая сумма.
        :rtype: str
        """
        total_element = self.wait.until(EC.presence_of_element_located(
            (By.CLASS_NAME, "summary_total_label")
        ))
        return total_element.text

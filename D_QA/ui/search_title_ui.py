from selenium import webdriver
from selenium.webdriver.common.by import By
import allure


@allure.description("Тестирование поля поиска по автору на сайте Читай-город.")
class SearchByTitle:
    """Класс для выполнения поиска книг по автору на сайте Читай-город."""

    def __init__(self, driver):
        self.driver = driver
        self.search_field = (
            By.XPATH, '//input[@class="header-search__input"]'
            )

    def search_by_title(self, title: str) -> None:
        search_button = self.driver.find_element(
            By.CSS_SELECTOR, "button[aria-label='Искать']"
            )
        with allure.step("Выбор поисковой строки и ввод названия книги."):
            webdriver(self.driver, 2).until(
                EC.presence_of_element_located(self.search_field)
            ).send_keys(title)
        with allure.step("Клик по кнопке поиска."):
            search_button.click()

    def search_by_genre(self, genre: str) -> None:
        search_button = self.driver.find_element(
            By.CSS_SELECTOR, "button[aria-label='Искать']"
            )
        with allure.step("Выбор поисковой строки и ввод жанра книги."):
            webdriver(self.driver, 2).until(
                EC.presence_of_element_located(self.search_field)
            ).send_keys(genre)
        with allure.step("Клик по кнопке поиска."):
            search_button.click()
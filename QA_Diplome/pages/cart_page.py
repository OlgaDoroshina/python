from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import allure
from selenium import webdriver

class CartPage:
    URL = "https://www.chitai-gorod.ru/cart"
    SEARCH_INPUT = (By.CLASS_NAME, "header-search__input")

    def __init__(self, driver):
        self._driver = driver
        self._driver.maximize_window()
        self._driver.get(self.URL)

          
    @allure.step("Проверка пустой корзины")
    def get_empty_cart(self):
        cart_icon = webdriver(self._driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "header-cart__icon--desktop"))
        )
        cart_icon.click()
        txt = webdriver(self._driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "empty-title"))
        ).text
        return txt
    
    @allure.step("Поиск книги по названию и удаление из корзины")
    def delete_from_cart(self, driver: webdriver.Chrome) -> None:
            
            # Поиск книги по названию
        driver.find_element(By.NAME, "phrase").send_keys(self.book_title)

            # Клик по кнопке поиска
        search_button_find = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Искать']")
        search_button_find.click()

            # Клик по кнопке "Купить"
        search_button_buy = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Купить']")
        search_button_buy.click()

            # Открытие корзины
        cart_icon = driver.find_element(By.CSS_SELECTOR, '.header-cart__icon')
        cart_icon.click()

            # Клик по кнопке "Очистить корзину"
        delete_button = driver.find_element(By.CSS_SELECTOR, 'span.clear-cart')
        delete_button.click()


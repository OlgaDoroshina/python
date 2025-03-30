import pytest
import allure
from pages.config import SEARCH_TERMS
from pages.main_pages import MainPage
from pages.CartPage import CartPage
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def main_page(driver):
    page = MainPage(driver)
    page.open()
    return page

@pytest.fixture
def cart_page(driver):
    page = CartPage(driver)
    page.open()
    return page

@allure.step("Тест: Поле принимает кириллицу")
def test_search_cyrillic(main_page):
    entered_text = main_page.enter_search_text(SEARCH_TERMS['cyrillic'])
    assert entered_text == SEARCH_TERMS['cyrillic'], f"Ожидали '{
        SEARCH_TERMS['cyrillic']}', но получили '{entered_text}'"


@allure.step("Тест: Поле принимает латиницу")
def test_search_latin(main_page):
    entered_text = main_page.enter_search_text(SEARCH_TERMS['latin'])
    assert entered_text == SEARCH_TERMS['latin'], f"Ожидали '{
        SEARCH_TERMS['latin']}', но получили '{entered_text}'"


@allure.step("Тест: Поле принимает цифры")
def test_search_numbers(main_page):
    entered_text = main_page.enter_search_text(SEARCH_TERMS['numbers'])
    assert entered_text == SEARCH_TERMS['numbers'], f"Ожидали '{
        SEARCH_TERMS['numbers']}', но получили '{entered_text}'"


@allure.step("Тест: Поле принимает дефис")
def test_search_dash(main_page):
    entered_text = main_page.enter_search_text(SEARCH_TERMS['dash'])
    assert entered_text == SEARCH_TERMS['dash'], f"Ожидали '{
        SEARCH_TERMS['dash']}', но получили '{entered_text}'"


@allure.step("Тест: Поле принимает восклицательный знак")
def test_search_exclamation(main_page):
    entered_text = main_page.enter_search_text(SEARCH_TERMS['exclamation'])
    assert entered_text == SEARCH_TERMS['exclamation'], f"Ожидали '{
        SEARCH_TERMS['exclamation']}', но получили '{entered_text}'"


@allure.step("Тест: Поле принимает вопросительный знак")
def test_search_question(main_page):
    entered_text = main_page.enter_search_text(SEARCH_TERMS['question'])
    assert entered_text == SEARCH_TERMS['question'], f"Ожидали '{
        SEARCH_TERMS['question']}', но получили '{entered_text}'"
    
@allure.title("Пустая корзина")
@allure.description("Проверка пустой корзины")
@allure.feature("READ")
@allure.severity("blocker")
@pytest.mark.ui_test
@pytest.mark.negative_test
def test_get_empty_cart(browser):
    with allure.step("Открытие веб-страницы в Chrome, заходим в корзину"):
        cart_page = CartPage(browser)
        cart_page.set_cookie_policy()
        text = cart_page.get_empty_cart()
        assert text.startswith("В корзине ничего нет")

@allure.title("Тест удаления товара из корзины. POSITIVE")
@allure.description("Этот тест проверяет, что товар из корзины удаляется корректно.")
@allure.feature("DELETE")
@allure.severity("BLOCKER")
def test_delete_from_card():
        
        with allure.step ("Запустить браузер Chrome"):
            driver = webdriver.Chrome() 
        
        with allure.step ("Перейти на сайт Читай-город"):
           cart_page=driver.get(self.URL)  

        with allure.step ("Удалить книгу из корзины"):
            book_title = "Ветреный"
            cart_page.delete_from_cart(book_title)
            results_del = cart_page.driver.find_elements(By.CSS_SELECTOR, 'div.product-title__head')

        with allure.step ("Проверить, что товар больше не существует в списке"):
            assert all(book_title not in element.text for element in results_del), f"Книга '{book_title}' все еще в корзине."
        
        with allure.step("Закрыть браузер"):
            driver.quit()
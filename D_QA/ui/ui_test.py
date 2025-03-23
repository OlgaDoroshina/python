from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import allure
from ui.search_author_ui import SearchByAuthor
from ui.search_title_ui import SearchByTitle
from const import UI_url

@pytest.fixture
def driver(browser, UI_url):
    browser.get(UI_url)
    yield browser

search_by_author = SearchByAuthor
search_by_title = SearchByTitle

@allure.feature("Поиск")
@allure.title("Тест поиска книг на сайте Читай-город по автору. POSITIVE")
@allure.suite("UI тесты")
@allure.severity(allure.severity_level.BLOCKER)
@allure.description("Проверка поиска книг по автору.")
def test_search_by_author(driver):
    search_ui = UI_url(driver)
    search_ui.search_by_author('Гивакс Джей')
    with allure.step("Проверка успешного поиска по автору книги."):
        result_find = webdriver(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[@class='product-title']/div[@class='product-title__author']")
                )
        )
        result_text = result_find.text
        assert result_text == "Джей Гивакс"


@allure.feature("Поиск")
@allure.title("Тест поиска книг на сайте Читай-город по названию. POSITIVE")
@allure.suite("UI тесты")
@allure.severity(allure.severity_level.BLOCKER)
@allure.description("Проверка поиска книг по названию.")
def test_search_by_title(driver):
    search_ui = UI_url(driver)
    search_ui.search_by_title('Паттерны проектирования API')
    with allure.step("Проверка успешного поиска по названию книги."):
        result_find = webdriver(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[@class='product-title']/div[@class='product-title__head']")
                )
        )
        result_text = result_find.text
        assert result_text == 'Паттерны проектирования API'


@allure.feature("Поиск")
@allure.title("Тест поиска книг на сайте Читай-город по жанру. POSITIVE")
@allure.suite("UI тесты")
@allure.severity(allure.severity_level.BLOCKER)
@allure.description("Проверка проводится на наличие элемента 'Товары'. Если данного элемента нет - поиск неудачный.")
def test_search_by_genre(driver):
    search_ui = UI_url(driver)
    search_ui.search_by_genre('Роман')
    with allure.step("Проверка успешного поиска по жанру книги."):
        result_find = webdriver(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[@class='app-tabs__btn app-tabs__btn--active']")
                )
        )
        result_text = result_find.text
        assert result_text == "Товары"


@allure.feature("Поиск")
@allure.title("Тест поиска книг на сайте Читай-город по автору. NEGATIVE")
@allure.suite("UI тесты")
@allure.severity(allure.severity_level.BLOCKER)
@allure.description("Проверка поиска по автору которого нет.")
def test_search_by_author_negative(driver):
    search_ui = UI_url(driver)
    with allure.step("Поиск книг c отправкой пустого поля."):
        search_ui.search_by_author('Уфуфуфуфуфуфуф')
    with allure.step("Проверка наличия сообщения о неудачном поиске."):
        result_find =webdriver(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//h4[@class='catalog-empty-result__header']"))
        )
        result_text = result_find.text
        assert result_text == "Похоже, у нас такого нет"


@allure.feature("Поиск")
@allure.title("Тест поиска книг на сайте Читай-город по названию. NEGATIVE")
@allure.suite("UI тесты")
@allure.severity(allure.severity_level.BLOCKER)
@allure.description("Проверка поиска по названию в котором присутствуют спецсимволы.")
def test_search_by_title_symb_negative(driver):
    search_ui = UI_url(driver)
    with allure.step("Поиск книг c отправкой названия в котором есть спецсимволы."):
        search_ui.search_by_title('!!"Паттерны проектирования API')
    with allure.step("Проверка наличия сообщения о поиске."):
        result_find = webdriver(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[@class='product-title']/div[@class='product-title__head']"))
        )
        result_text = result_find.text
        assert result_text == "Паттерны проектирования API"


@allure.feature("Поиск")
@allure.title("Тест поиска книг на сайте Читай-город по названию. NEGATIVE")
@allure.suite("UI тесты")
@allure.severity(allure.severity_level.BLOCKER)
@allure.description("Проверка поиска по названию которое в верхнем регистре.")
def test_search_by_title_upper_negative(driver):
    search_ui = UI_url(driver)
    with allure.step("Поиск книг c отправкой названия в верхнем регистре."):
        search_ui.search_by_title('!!"ПАТТЕРНЫ ПРОЕКТИРОВАНИЯ API')
    with allure.step("Проверка наличия сообщения о поиске."):
        result_find = webdriver(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[@class='product-title']/div[@class='product-title__head']"))
        )
        result_text = result_find.text
        assert result_text == 'Паттерны проектирования API'
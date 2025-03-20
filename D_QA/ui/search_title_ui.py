from selenium import webdriver
from selenium.webdriver.common.by import By
import allure


@allure.description("Тест поля поиска по названию на сайте Читай-город")
class SearchByTitle:
    """Класс для выполнения поиска книг по названию на сайте Читай-город."""

    def __init__(self, book_title: str):
        """
                    Инициализация класса SearchByTitle.
                    :param book_title: Название книги, которую необходимо найти
        """
        self.book_title = book_title

    @allure.step("Поиск книги по названию")
    def search_by_title(self, driver: webdriver.Chrome):
        """Поиск книг по названию на сайте Читай-город.
            :param driver: Экземпляр драйвера Selenium (в данном случае Chrome)
            :raises Exception: если не удается найти элементы поиска
        """
        # Ввод названия в строку поиска
       
        def __init__(self, browser):
        self.browser = browser
        self.search_button = (By.CSS_SELECTOR, "input[value='поиск']")
        
        

            # Клик по кнопке поиска
            
    def click_search_button(self):
        self.browser.find_element(*self.search_button).click()
       
        except Exception as e:
            allure.attach(str(e), name="error",
                          attachment_type=allure.attachment_type.TEXT)
            raise
    
    

    # Метод для ввода текста в указанное поле
    def vvod_text(self, by, identifier, text):
        element = webdriver(self.browser, 10).until(
             EC.presence_of_element_located((by, identifier)))
        element.clear()
        element.send_keys(text)

    # Метод для нажатия на кнопку поиска
    def click_search_button(self):
        self.browser.find_element(*self.search_button).click()

    # Метод выпадающего списка
    def select_count_list(self, by, dropdown_id, option_xpath):
        dropdown = self.browser.find_element(by, dropdown_id)
        dropdown.click()
        option = self.browser.find_element(By.XPATH, option_xpath)
        option.click()

    # Метод ожидания элемента на странице
    def wait_elem(self, by, value, timeout=8):
        return WebDriverWait(self.browser, timeout).until(
            EC.visibility_of_element_located((by, value)))

    # Метод ожидания появления текста в поле ввода на странице
    def wait_text(self, by, value, text, timeout=15):
        try:
            return webdriver(self.browser, timeout).until(
                EC.text_to_be_present_in_element((by, value), text))
        except TimeoutException:
            # Сообщение об ошибке при отсутствии текста
            # в течение заданного времени
            print(f"Элемент с локатором {by} и значением {value},"
                  "содержащий текст '{text}', "
                  "не найден после {timeout} секунд.")
            return False

    # Поиск по жанру
    def search_kind(self, kind):
        kind_find = self.browser.find_element(
            By.XPATH,
            f"//input[@value='{kind}'] | //option[text()='{kind}']")
        kind_find.click()
        self.click_search_button()

    # Поиск по стране производства
    def search_country(self, country):
        # Выбор страны из выпадающего списка
        text_l = ("//option[@value='"+country+"' or text()='"+country+"']")
        print(text_l)
        self.select_count_list(By.ID, "country", text_l)
        self.click_search_button()


    # Поиск по году выпуска
    def search_year(self, year):
        self.vvod_text(By.ID, "year", str(year))
        self.click_search_button()

# Запуск случайного поиска по ранее заполненным параметрам
    
    def random_poisk(self):
        with allure.step("Нажитие кнопки поиска на главной странице"):
            self.browser.find_element(By.CSS_SELECTOR,
                                      "button[type='submit']"
                                      ).click()
        with allure.step('Нажитие кнопки "Случайный поиск"'):
            self.browser.find_element(By.ID, "search"
                                      ).click()
        with allure.step('Сайт отобразил случайный фильм'):
            res = self.browser.find_element(By.CLASS_NAME,
                                            "filmName")
    # Получено названия фильма
        return (res.find_element(By.CSS_SELECTOR, 'a'
                                 ).get_attribute('text'))
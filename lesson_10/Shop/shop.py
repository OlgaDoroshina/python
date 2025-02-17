from selenium.webdriver.common.by import By


class Registration:
    """
        Страница для регистрации на сайте
    """

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(4)
        self.driver.maximize_window()

    def open(self, browser : str) -> None:
        self.driver.get(browser)

    def put_username(self, username : str) -> None:
        self.driver.find_element(
            By.CSS_SELECTOR, '[data-test="username"]').send_keys(username)

    def put_password(self, password : str) -> None:
        self.driver.find_element(
            By.CSS_SELECTOR, '#password').send_keys(password)

    def click_login(self) -> None:
        self.driver.find_element(
            By.CSS_SELECTOR, '[data-test="login-button"]').click()

    def quit(self) -> None:
        self.driver.quit()

class Cart:
    """
        Страница для ввода информации о покупателя и номера карты
    """
    def __init__(self, driver):
        self.driver = driver

    def click_checkout(self) -> None:
        self.driver.find_element(By.CSS_SELECTOR, '#checkout').click()

    def put_firt_name(self, first_name : str) -> None:
        self.driver.find_element(
            By.CSS_SELECTOR, '#first-name').send_keys(first_name)

    def put_last_name(self, last_name : str) -> None:
        self.driver.find_element(
            By.CSS_SELECTOR, '#last-name').send_keys(last_name)

    def put_zip(self, zip : str) -> None:
        self.driver.find_element(
            By.CSS_SELECTOR, '#postal-code').send_keys(zip)

    def click_continue(self) -> None:
        self.driver.find_element(
            By.CSS_SELECTOR, '#continue').click()

    def quit(self) -> None:
        self.driver.quit()

class Checkout:
    """
        Методы работы с корзиной в магазине
    """
    def __init__(self, driver):
        self.driver = driver

    def watch_total(self) -> str:
        total = self.driver.find_element(
            By.CSS_SELECTOR, '.summary_total_label').text
        return total

    def quit(self) -> None:
        self.driver.quit()

class PageShop:
    """
        Страница для выбора товаров для покупки в магазине
    """
    def __init__(self, driver):
        self.driver = driver

    def add_backpack(self) -> None:
        self.driver.find_element(
            By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack').click()

    def add_bolt_t_shirt(self) -> None:
        self.driver.find_element(
            By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt').click()

    def add_onesie(self) -> None:
        self.driver.find_element(
            By.CSS_SELECTOR, '#add-to-cart-sauce-labs-onesie').click()

    def get_cart(self) -> None:
        self.driver.find_element(
            By.CSS_SELECTOR, '.shopping_cart_link').click()

    def quit(self) -> None:
        self.driver.quit()
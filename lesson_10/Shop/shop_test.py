from shop import Registration
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import allure

@allure.title("Тестирование магазина в интернете")
@allure.description("Smoke тест")
@allure.feature("Мазагин")
@allure.severity("Critical")
def test_shop():
    """
    Покупка товаров в магазине
    """
    with allure.step("Подключиться к браузеру"):
        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install())
            )
        reg = Registration(driver)
    with allure.step("Открыть страницу магазина"):
        reg.open("https://www.saucedemo.com/")
    with allure.step("Ввести логин"):
        reg.put_username("standard_user")
    with allure.step("Ввести пароль"):
        reg.put_password("secret_sauce")
    with allure.step("Нажать на кнопку подтверждения"):
        reg.click_login()
    with allure.step("Подключиться к драйверу страницы магазина"):
        page_shop = Registration(driver)
    with allure.step("Выбрать элемент backpack"):
        page_shop.add_backpack()
    with allure.step("Выбрать t-shirt"):
        page_shop.add_bolt_t_shirt()
    with allure.step("Выбрать onesie"):
        page_shop.add_onesie()
    with allure.step("Кликнуть на значек карзины(Перейти в карзину)"):
        page_shop.get_cart()
    cart = Registration(driver)
    with allure.step("Нажать на checkout"):
        cart.click_checkout()
    with allure.step("Ввести имя покупателя"):
        cart.put_firt_name("Olga")
    with allure.step("Вести фамилию покупателя"):
        cart.put_last_name("Dor")
    with allure.step("Ввести номер карты"):
        cart.put_zip("1144567")
    with allure.step("Нажать на кнопку Продолжить"):
        cart.click_continue()
    checkout = Registration(driver)
    with allure.step("Считать с сайта полную сумму"):
        total = checkout.watch_total()
    to_is = ("Total: $58.29")
    with allure.step("Проверить полную сумму в чеке с суммой покупки товаров"):
        assert total == to_is
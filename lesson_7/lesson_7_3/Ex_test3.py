import pytest
from PageObject_7_3 import Shop_MainPage
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def browser():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver

    # Закройте браузер.
    driver.quit()
    
@pytest.mark.parametrize("url, login, password, f_name, l_name, zip_code", [
    ("https://www.saucedemo.com/", "standard_user", "secret_sauce", "Ольга", "Дорошина", "440000")
    ])
def test_total(browser, url, login, password, f_name, l_name, zip_code):
    # 1. Откройте сайт магазина
    shp = Shop_MainPage(browser, url)
    # 2. Авторизуйтесь как пользователь `standard_user`.
    shp.authorization(login, password)
    # 3. Добавьте в корзину товары:
    shp.add_to()
    # 4. Перейдите в корзину.
    shp.go_to()
    crd = Shop_MainPage(browser)
    # 5. Нажмите Checkout.
    crd.clk_check()
    # 6. Заполните форму своими данными:
    crd.input_form(f_name, l_name, zip_code)
    # 7. Нажмите кнопк у Continue.
    crd.clk_cnt()
    # 8. Прочитайте со страницы итоговую стоимость (`Total`).
    total_coast = crd.rd_total()
    # 10. Проверьте, что итоговая сумма равна **$58.29.**
    assert "$58.29" in total_coast

    
    
    
    
    
    
    
    


    
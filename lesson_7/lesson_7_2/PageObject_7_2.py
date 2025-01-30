from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

url = ""

class СalculatorPage():
    def __init__(self, browser, url):
        self.driver = browser
        self.driver.get(url)
    
    def finder_CSS(self, select, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, select))
        )
        
    # def finder_Name(self, select, timeout=10):
    #     return WebDriverWait(self.driver, timeout).until(
    #         EC.visibility_of_element_located((By.NAME, select))
    #     )
    
    def finder_Xpath(self, select, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((By.XPATH, select))
        )
    
    # Поле Delay
    def type_Delay(self, delay):
        delay_field = self.finder_CSS("#delay")
        delay_field.clear()
        delay_field.send_keys(delay)
    
    # Кнопка Плюс
    def btn_plus(self):
        self.finder_Xpath('//*[@id="calculator"]/div[2]/span[4]').click()
    
    # Кнопка Равно
    def btn_equally(self):
        self.finder_Xpath('//*[@id="calculator"]/div[2]/span[15]').click()
     
    # Кнопка 7
    def btn_seven(self):
        self.finder_Xpath('//*[@id="calculator"]/div[2]/span[1]').click()
    
    # Кнопка 8
    def btn_eight(self):
        self.finder_Xpath('//*[@id="calculator"]/div[2]/span[2]').click()
    
    # Окно с результатом
    def btn_screen(self, delay):
        return self.finder_Xpath('//*[@id="calculator"]/div[1]/div', delay)
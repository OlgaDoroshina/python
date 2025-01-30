from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

url = ""

class DatatypesPage():
    def __init__(self, browser, url):
        self.driver = browser
        self.driver.get(url)
        
    # def finder(self, select):
    #     fnd = self.driver.find_element(By.CSS_SELECTOR, select)
    #     return fnd
    
    def finder_CSS(self, select, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, select))
        )
        
    def finder_Name(self, select, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((By.NAME, select))
        )
    
    # Поля формы
    ## First Name       
    def type_First_name(self, First_name):
        self.finder_Name("first-name").send_keys(First_name)
    
    def bkgr_First_name(self):
        return self.finder_CSS("#first-name").value_of_css_property("background-color")
    
    ## Last Name
    def type_Last_name(self, Last_name):
        self.finder_Name("last-name").send_keys(Last_name)
        
    def bkgr_Last_name(self):
        return self.finder_CSS("#last-name").value_of_css_property("background-color")
     
    ## Address
    def type_Address(self, Address):
        self.finder_Name("address").send_keys(Address)
    
    def bkgr_Address(self):
        return self.finder_CSS("#address").value_of_css_property("background-color")
    
    ## Zip code
    def type_Zip_code(self, Zip_code):
        self.finder_Name("zip-code").send_keys(Zip_code)
    
    def bkgr_Zip_code(self):
        return self.finder_CSS("#zip-code").value_of_css_property("background-color")
    
    ## City
    def type_City(self, City):
        self.finder_Name("city").send_keys(City)
    
    def bkgr_City(self):
        return self.finder_CSS("#city").value_of_css_property("background-color")
    
    ## Country
    def type_Country(self, Country):
        self.finder_Name("country").send_keys(Country)
    
    def bkgr_Country(self):
        return self.finder_CSS("#country").value_of_css_property("background-color")
    
    ## Email
    def type_Email(self, Email):
        self.finder_Name("e-mail").send_keys(Email)   

    def bkgr_Email(self):
        return self.finder_CSS("#e-mail").value_of_css_property("background-color")
    
    ## Phone number
    def type_Phone_number(self, Phone_number):
        self.finder_Name("phone").send_keys(Phone_number)
    
    def bkgr_Phone_number(self):
        return self.finder_CSS("#phone").value_of_css_property("background-color")
      
    ## Job position
    def type_Job_position(self, Job_position):
        self.finder_Name("job-position").send_keys(Job_position)
    
    def bkgr_Job_position(self):
        return self.finder_CSS("#job-position").value_of_css_property("background-color")
    
    ## Company
    def type_Company(self, Company):
        self.finder_Name("company").send_keys(Company)
        
    def bkgr_Company(self):
        return self.finder_CSS("#company").value_of_css_property("background-color")
    
    # кнопка       
    def clk_Submit(self):
        self.finder_CSS(".btn.btn-outline-primary.mt-3").click()
UI_url = 'https://www.chitai-gorod.ru'
API1_url = "https://web-gate.chitai-gorod.ru/api/v1/cart/product"
API2_url = "https://web-gate.chitai-gorod.ru/api/v1/cart"
bearer_token = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3VzZXItcmlnaHQiLCJzdWIiOjIxMDk0OTM1LCJpYXQiOjE3MjY0ODQyNTUsImV4cCI6MTcyNjQ4Nzg1NSwidHlwZSI6MjB9.f90FiXjhwmDTgPqBQ4KZFPptlMLZwwWwIU0Y5OT9QS4"

@pytest.fixture(scope="session")
def browser():
    s = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def api_url():
    return "https://web-gate.chitai-gorod.ru/api"


@pytest.fixture(scope="session")
def ui_url():
    return 'https://www.chitai-gorod.ru'
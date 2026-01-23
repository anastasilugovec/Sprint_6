import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions

@pytest.fixture(scope="session")
def driver():
    options = ChromeOptions()
    options.add_argument("--headless=new")  # можно убрать, если нужен GUI
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    service = ChromeService(ChromeDriverManager().install())
    drv = webdriver.Chrome(service=service, options=options)
    drv.implicitly_wait(10)
    yield drv
    drv.quit()



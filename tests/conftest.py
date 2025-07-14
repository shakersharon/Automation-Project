import pytest
from selenium import webdriver
import yaml
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

def get_config():
    with open("config/config.yaml") as f:
        return yaml.safe_load(f)

@pytest.fixture
def browser():
    config = get_config()
    options = Options()
    options.add_argument("--start-maximized")
    # options.add_argument("--headless")  # Uncomment if running in CI or no-GUI env
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.implicitly_wait(config["implicit_wait"])
    driver.get(config["base_url"])
    yield driver
    driver.quit()

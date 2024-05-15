import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# To allow running tests in headless mode from the terminal
# pytest --headless
def pytest_addoption(parser):
    parser.addoption(
        "--headless", action="store_true", help="Run tests in headless mode"
    )

@pytest.fixture(scope="session")
def driver(request):
    headless = request.config.getoption("--headless")
    options = Options()
    if headless:
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)  # Adjust path if necessary
    driver.maximize_window()
    yield driver
    driver.quit()

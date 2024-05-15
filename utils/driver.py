from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Driver:
    def __init__(self, headless=False):
        self.driver = None
        self.headless = headless

    def start_browser(self, browser_name='chrome'):
        options = Options()
        if self.headless:
            options.add_argument("--headless")
            options.add_argument("--disable-gpu")
            options.add_argument("--window-size=1920,1080")

        if browser_name.lower() == 'chrome':
            self.driver = webdriver.Chrome(options=options)
        elif browser_name.lower() == 'firefox':
            from selenium.webdriver.firefox.options import Options as FirefoxOptions
            options = FirefoxOptions()
            if self.headless:
                options.add_argument("--headless")
                options.add_argument("--disable-gpu")
                options.add_argument("--window-size=1920,1080")
            self.driver = webdriver.Firefox(options=options)
        else:
            raise ValueError(f"Browser {browser_name} is not supported.")

        self.driver.maximize_window()
        return self.driver

    def quit_browser(self):
        if self.driver:
            self.driver.quit()

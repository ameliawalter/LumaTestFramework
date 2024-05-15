# Test Automation Framework for LUMA, a Magento practice website

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Selenium](https://img.shields.io/badge/-selenium-%43B02A?style=for-the-badge&logo=selenium&logoColor=white)

This is a demo of a simple TAF skeleton created with: Python, pytest, Selenium, Page Object Model.

Clone the repository and run the tests with: 
pytest
pytest --headless

Feel free to clone or fork it, play with the code, develop the framework to practise.

### Hints on Continuing the Framework

* Expand Page Objects: Add more pages such as ProductPage, CartPage, CheckoutPage, etc. Each page should have its own class and methods corresponding to the elements and actions on that page.

* Selectors and Methods: For each page, identify the key elements and actions. For example, for the HomePage, you might add methods to interact with the search bar, navigation menus, etc.

* Test Cases: Add more test cases under the tests directory. Each test case should instantiate the necessary page objects and call their methods to perform actions and assertions.

* Parameterization: Use pytest's parameterization to run tests with multiple sets of data. This is useful for testing different user credentials, product searches, etc.

* Assertions: Add assertions to verify the outcomes of your tests. This could include checking for specific text on a page, verifying that a user is logged in, ensuring items are added to the cart, etc.

* Utility Functions: Add utility functions as needed for tasks like taking screenshots, handling waits, and reading from configuration files.

* CI/CD Integration: Integrate the framework with a CI/CD tool like Jenkins, GitHub Actions, or GitLab CI to run the tests automatically on every commit.

This playground framework was created with support from ChatGPT 4o LLM.
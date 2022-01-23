# Import Bibliotek
from faker import Faker
from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

LOCALE = 'pl_PL'
PASSWORD = "123890"

class EObuwie(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get("https://www.eobuwie.com.pl/")
        self.fake = Faker(LOCALE)

    def tearDown(self):
        self.driver.quit()

    def testinvalidEmail(self):
        driver = self.driver
        fake = self.fake
        wait = WebDriverWait(driver, 15)
        close_cookie_modal = wait.until(
            EC.visibility_of_element_located((By.XPATH, '//button[@data-testid="permission-popup-accept"]')))
        close_cookie_modal.click()

        # 1. Kliknij ZAREJESTRUJ
        driver.find_element_by_xpath('//a[@data-testid="header-register-link"]').click()
        # 2. Wpisz imię
        name_field = driver.find_element_by_id('firstname')
        name_field.send_keys(fake.first_name())
        # 3. Wpisz nazwisko
        surname_field = driver.find_element_by_id('lastname')
        surname_field.send_keys(fake.last_name())
        # 4. Wpisz bledny e-mail
        email_input = driver.find_element_by_xpath('//*[@id="email_address"]')
        email_input.send_keys(fake.email().replace("@",""))
        # 5. Wpisz haslo
        password_input = driver.find_element_by_xpath('//*[@id="password"]')
        password_input.send_keys(PASSWORD)
        # 6. Potwierdz haslo
        confirm_password = driver.find_element_by_id('confirmation')
        confirm_password.send_keys(PASSWORD)
        # 7. Zatwierdz regulamin
        terms_tick_box = driver.find_element_by_xpath('//label[@class="checkbox-wrapper__label"]')
        terms_tick_box.click()
        # 8. Kliknij "Zaloz Nowe konto"
        create_account = driver.find_element_by_xpath('//button[@id="create-account"]')
        create_account.click()



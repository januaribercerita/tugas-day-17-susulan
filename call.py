from selenium import webdriver
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager



driver = webdriver.Chrome()

class TestLogin(unittest.TestCase): 
        def setUp(self): 
                self.browser = webdriver.Chrome(ChromeDriverManager().install())
        def test_login_success(self): 
                # steps
                browser = self.browser #buka web browser
                browser.get("https://itera-qa.azurewebsites.net/Login") # buka situs
                driver.maximize_window 
                time.sleep(2)
                browser.find_element(By.ID,"Username").send_keys("SectumSempra") # isi usernam
                time.sleep(2)
                browser.find_element(By.ID,"Password").send_keys("KeRen0601") # isi password
                time.sleep(2)
                browser.find_element(By.NAME,"login" ).click()
                time.sleep(2)

                response = browser.find_element(By.CSS_SELECTOR,"div[class='container body-content'] div h3").text
                self.assertEqual(response,"Welcome")

unittest.main()
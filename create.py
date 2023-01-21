from selenium import webdriver
import unittest
import time
import call
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager



class TestLogin(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        
    def test_logout(self): 
        browser = self.browser
        driver.maximize_window 
        call.test_login_success(self) # ini manggil method login 
        time.sleep(2)

        

if __name__ == "__main__": 
    unittest.main()          
          


    

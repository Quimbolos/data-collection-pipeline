# %% 

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import time


class Scraper():

    def __init__(self, url):

        self.main_url = url
        self.driver = webdriver.Chrome() 
        self.delay = 20


    def load_and_accept_manual_and_cookies_promts(self):

        '''
        Open Main URL (CoinMarket) and accept the manual and cookies prompt
        
        '''
        URL = self.main_url
        self.driver.get(URL)
        try:

            # Buttons

            Button1 = WebDriverWait(self.driver, self.delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[2]/div[4]/button')))
            Button1.click()
           
            Button2 = WebDriverWait(self.driver, self.delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[2]/div[4]/button')))
            Button2.click()

            Button3 = WebDriverWait(self.driver, self.delay).until(EC.presence_of_element_located((By.XPATH, '//*[@id="cmc-cookie-policy-banner"]/div[2]')))
            Button3.click()
            

            time.sleep(1)

        except TimeoutException:
            print("Loading took too much time!")

        return self.driver 


    def scroll_down(self):

        '''
        Scroll down Main URL (Ikea) 
        
        '''

        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        print("Scroll down executed!")

        return self.driver 

    def insert_postcode(self):
        '''
        Enter the postcode in the Main URL (Ikea) 
        
        '''
        try:
            WebDriverWait(self.driver, self.delay).until(EC.presence_of_element_located((By.XPATH, '//*[@class="sc-a4a6801b-0 glxMF"]')))
            enter_postcode_button = self.driver.find_element(by=By.XPATH, value='//*[@class="sc-a4a6801b-0 glxMF"]')
            print("Postcode Button Ready!")
            enter_postcode_button.click()
            time.sleep(1)
        except TimeoutException:
            print("Loading took too much time!")

        self.driver.find_element(by=By.XPATH, value='//*[@id="hnf-txt-postalcodepicker-postcode"]').send_keys('SW1V 2NE').send_keys(Keys.ENTER)

        return self.driver
         



    def run(self):

        self.load_and_accept_manual_and_cookies_promts()
        #self.scroll_down()
        #self.insert_postcode()



URL = 'https://coinmarketcap.com/'

game = Scraper(URL)

game.run()
# %%

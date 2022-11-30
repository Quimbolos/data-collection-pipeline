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

    def get_links(self):
        '''
        Returns a list with all the links in the current page
        Parameters
        ----------
        driver: webdriver.Chrome
            The driver that contains information about the current page
        
        Returns
        -------
        link_list: list
            A list with all the links in the page
        '''

        prop_container = self.driver.find_element(by=By.XPATH, value='//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[4]/table')
        prop_container2 = prop_container.find_element(by=By.XPATH, value='./tbody')
        prop_list = prop_container2.find_elements(by=By.XPATH, value='./tr')
        print(prop_list)
        
        link_list = []

        for crypto in prop_list:
            a_tag = crypto.find_element(by=By.TAG_NAME, value='a')
            link = a_tag.get_attribute('href')
            link_list.append(link)
            print(link)

        return link_list

    # big_list = []
    # driver = load_and_accept_cookies()

    # for i in range(5): # The first 5 pages only
    #     big_list.extend(get_links(driver)) # Call the function we just created and extend the big list with the returned list
    #     ## TODO: Click the next button. Don't forget to use sleeps, so the website doesn't suspect
    #     pass # This pass should be removed once the code is complete


    # for link in big_list:
    #     ## TODO: Visit all the links, and extract the data. Don't forget to use sleeps, so the website doesn't suspect
    #     pass # This pass should be removed once the code is complete

# driver.quit() # Close the browser when you finish
         



    def run(self):

        self.load_and_accept_manual_and_cookies_promts()
        self.get_links()
        #self.insert_postcode()



URL = 'https://coinmarketcap.com/'

game = Scraper(URL)

game.run()
# %%


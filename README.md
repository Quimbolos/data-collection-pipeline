# Data Collection Pipeline

> This project implements an industry-grade data collection pipeline that runs scalably in the cloud. It uses Python code to automatically control your browser, extract information from a website, and store it on the cloud in a data warehouse and data lake. The system conforms to industry best practices, such as being containerised in Docker and running automated.

## Milestone 1: Set up the environment

Create a new GitHub repo to upload the code and allow version control throughout the project.


## Milestone 2: Decide which website you are going to collect data from

A website is chosen based on the data you are interested in to collect and build a dataset from. In this case, the selected website is [CoinMarket](https://coinmarketcap.com/). This financial webpage contains data from all the current cryptocurrencies, and scraping data from it could mainly allow for the following:

- Overall Monitoring of Cryptocurrency panorama.
- Price Monitoring of Cryptocurrency.
- Analysis of Major Cryptocurrency Rates.
- Keeping Record of Government Decisions on Cryptocurrency.
- Monitor Companies that Accept Payments in Cryptocurrency.

## Milestone 3: Prototype finding the individual page for each entry

Find the links within the main page to the many pages containing the data you want to collect. A Scraper class is created containing all the methods used to scrape the data. Using Selenium, three methods, aside from the constructor, are defined:

 - The load_and_accept_manual_and_cookies_promts() method waits for the manual and cookies prompts to appear and then accepts them.

 - The scroll_down() method scrolls down the whole webpage.

 - The get_links() method navigates to the container where links are stored in a tabular format and then gets the 'href' from each row and stores it in link_list

 In addition, an extra method is created:

 - The run_scraper() method runs all the methods within the class

Finally, the class is initialised within an  if __name__ == "__main__" block, so that it only runs if this file is run directly rather than on any import. For each TASK, changes in the code are committed and pushed to the GitHub repo.

```python

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

            manual_button1 = WebDriverWait(self.driver, self.delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[2]/div[4]/button')))
            manual_button1.click()
           
            manual_button2 = WebDriverWait(self.driver, self.delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[2]/div[4]/button')))
            manual_button2.click()

            cookies_button = WebDriverWait(self.driver, self.delay).until(EC.presence_of_element_located((By.XPATH, '//*[@id="cmc-cookie-policy-banner"]/div[2]')))
            cookies_button.click()
            
            time.sleep(1)

        except TimeoutException:
            print("Loading took too much time!")

        return self.driver 


    def scroll_down(self):
        '''
        Scroll down Main URL (CoinMarket) 
        
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
        
        link_list = []

        for crypto in prop_list:
            a_tag = crypto.find_element(by=By.TAG_NAME, value='a')
            link = a_tag.get_attribute('href')
            link_list.append(link)

        return print(link_list)


    def run_scraper(self):

        self.load_and_accept_manual_and_cookies_promts()
        self.get_links()
        #self.scroll_down()



if __name__ == '__main__':
    url = 'https://coinmarketcap.com/'
    game = Scraper(url)
    game.run_scraper()


```

# %% 

import datetime
import json
import os
import re
import requests
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys

class Scraper():

    def __init__(self):
        self.main_url = 'https://coinmarketcap.com/'
        # self.options = webdriver.ChromeOptions()
        # self.options.addArguments("--no-sandbox")
        # self.options.add_argument('--headless')
        # self.options.addArguments("start-maximized")
        # self.options.addArguments("disable-infobars")
        # self.options.addArguments("--disable-extensions")
        # self.options.addArguments("--disable-dev-shm-usage")
        # self.options.add_argument('window-size=800x841')
        # self.driver = webdriver.Chrome(chrome_options=self.options) 
        
        self.driver = webdriver.Chrome() 

        self.delay = 20

     

    def load_and_accept_manual_and_cookies_promts(self):
        '''
        Open Main URL (CoinMarket) and accept the manual and cookies prompt

        Parameters
        ----------
        None

        Returns
        -------
        self.driver: webdriver.Chrome
            The driver after the manual and cookies prompts are accepted
        '''

        URL = self.main_url
        self.driver.get(URL)
        try:

            # Click Buttons from Prompts
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

        Parameters
        ----------
        None

        Returns
        -------
        self.driver: webdriver.Chrome
            The driver after the window has been scrolled down
        '''

        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        return self.driver 


    def get_links(self):
        '''
        Returns a list with all the links on the current page

        Parameters
        ----------
        None
        
        Returns
        -------
        link_list: list
            A list with all the links of interest on the page
        '''

        self.driver = self.load_and_accept_manual_and_cookies_promts()

        prop_container = self.driver.find_element(by=By.XPATH, value='//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[4]/table')
        prop_container2 = prop_container.find_element(by=By.XPATH, value='./tbody')
        prop_list = prop_container2.find_elements(by=By.XPATH, value='./tr')
        
        link_list = []

        for crypto in prop_list:
            a_tag = crypto.find_element(by=By.TAG_NAME, value='a')
            link = a_tag.get_attribute('href')
            link_list.append(link)

        return link_list


    def get_data(self, links):
        '''
        Returns a dictionary with all the data of interest from the links from get_links()

        Parameters
        ----------
        links: links
            The list with all the links of interest on the page
        
        Returns
        -------
        data_dict: dict
            A dictionary with all the data of interest from the links
        '''
 
        # Extract all the links
        link_list = links

        # Variables to extract:
        name = []
        price = []
        price_change_24_hours = []
        low_price_24_hours = []
        high_price_24_hours = []
        trading_volume_24_hours = []
        volume_market_cap = []
        market_dominance = []
        market_rank = []
        timestamp = []

        # Iterate through the list, and for each iteration, visit the corresponding URL
        for i in range(5): # The first 5 pages only
            # Load url
            self.driver.get(link_list[i])

            # click prompt button if it appears
            # if i == 0:
            #     prompt_button1 = WebDriverWait(self.driver, self.delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div/div/div/button[2]')))
            #     prompt_button1.click()

            # Wait Until Container with data appears
            WebDriverWait(self.driver, self.delay).until(EC.presence_of_element_located((By.XPATH, '//div[@class="sc-aef7b723-0 jfPVkR container"]')))
            # Extract the information of the link
            name_container = self.driver.find_element(by=By.XPATH, value='//div[@class="sc-aef7b723-0 jfPVkR container"]')
            name.append(name_container.find_element(by=By.XPATH, value='//h2/span/span').text)

            price_statistics_container = self.driver.find_element(by=By.XPATH, value='//div[@class="sc-aef7b723-0 RdAHw"]')
            tbody_tag = price_statistics_container.find_element(by=By.XPATH, value='//tbody')
            tr_tag = tbody_tag.find_elements(by=By.XPATH, value='.//td')

            price.append((tr_tag[0].get_attribute('innerHTML'))[1:10])
            price_change_24_hours.append(((tr_tag[1].find_element(by=By.XPATH, value='.//span/span').get_attribute('innerHTML'))[0]+(tr_tag[1].find_element(by=By.XPATH, value='.//span/span').get_attribute('innerHTML'))[10:16]))
            low_price_24_hours.append(re.sub('[^a-zA-Z0-9\n\.]', '',(tr_tag[2].find_element(by=By.XPATH, value='.//div').get_attribute('innerHTML'))[1:10]))
            high_price_24_hours.append((tr_tag[2].find_element(by=By.XPATH, value='.//div[2]').get_attribute('innerHTML'))[1:10])
            trading_volume_24_hours.append((tr_tag[3].find_element(by=By.XPATH, value='.//span').get_attribute('innerHTML'))[1:-1])
            volume_market_cap.append(tr_tag[4].get_attribute('innerHTML'))
            market_dominance.append(re.sub('[^a-zA-Z0-9\n\.]', '',(tr_tag[5].find_element(by=By.XPATH, value='.//span').get_attribute('innerHTML'))[0:5]))
            market_rank.append((tr_tag[6].get_attribute('innerHTML'))[1:4])
            timestamp.append(datetime.datetime.fromtimestamp(time.time()).strftime("%m/%d/%Y %H:%M:%S"))
            
            # Sleep
            time.sleep(1)


        data_dict = {

            'Name' : name,
            'Price ($)' : price,
            'Price Change 24h ($)' : price_change_24_hours,
            'Lowest Price 24h ($)' : low_price_24_hours,
            'Highest Price 24h ($)' : high_price_24_hours,
            'Trading Volume 24h ($)' : trading_volume_24_hours,
            'Volume / Market Cap' : volume_market_cap,
            'Market Dominance' : market_dominance,
            'Market Rank' : market_rank,
            'TimeStamp' : timestamp

        }


        return data_dict


    def get_images(self, links):
        '''
        Returns a dictionary with all the images from the links from get_links()

        Parameters
        ----------
        links: links
            The list with all the links of interest in the page
        
        Returns
        -------
        images_dict: dict
            A dictionary with all the images of interest from the links
        '''

        # Extract all the links
        link_list = links

        # Allocate space for the images
        images = []

        # Iterate through the link list, and for each iteration, visit the corresponding URL
        for i in range(5): # The first 5 pages only
            # Load url
            self.driver.get(link_list[i])

            # Wait Until Container with image appears
            WebDriverWait(self.driver, self.delay).until(EC.presence_of_element_located((By.XPATH, '//div[@class="sc-aef7b723-0 jPJwrb nameHeader"]')))
            image_container  = self.driver.find_element(by=By.XPATH, value='//div[@class="sc-aef7b723-0 jPJwrb nameHeader"]')
            images.append(image_container.find_element(by=By.XPATH, value='.//img').get_attribute('src'))

            # Sleep
            time.sleep(1)

        images_dict = {

            'Images - src' : images
        }

        return images_dict


    def merge_dict(self, data, images):
        '''
        Returns a dictionary with all the images from the links from get_links()

        Parameters
        ----------
        data: dict
            The dictionary containing all the price statistics data
        images: dict
            The dictionary containing all the images for each crypto

        Returns
        -------
        dictionary: dict
            A dictionary with all the images of interest and data from the links
        '''

        dictionary = {}
        dictionary.update(images)
        dictionary.update(data)

        return dictionary


    def create_raw_data_folder(self, dictionary):
        '''
        Creates the raw_data folder, creates the dictionary folder within the raw_data folder,
        and saves the dictionary in the dictionary folder

        Parameters
        ----------
        dictionary: dict
            The dictionary containing all the price statistics data
        
        Returns
        -------
        None
        '''

        dictionary_dir = 'raw_data'
        parent_dir = "/Users/joaquimbolosfernandez/Desktop/AICore/Data Collection Project/data-collection-pipeline"
        path = os.path.join(parent_dir, dictionary_dir)
        if os.path.exists(path) == False:
            os.mkdir(path)

        # Create the dictionary folder within the raw_data folder
        dictionary_dir = 'dictionary'
        parent_dir = "/Users/joaquimbolosfernandez/Desktop/AICore/Data Collection Project/data-collection-pipeline/raw_data/"
        path = os.path.join(parent_dir, dictionary_dir)
        if os.path.exists(path) == False:
            os.mkdir(path)

         # Save the dictionary in the dictionary folder
        with open(os.path.join(path, 'data.json'), 'w') as fp:
            json.dump(dictionary, fp)


    def create_crypto_folders(self, dictionary):
        '''
        Creates a folder for each cryptocurrency within the raw_data folder

        Parameters
        ----------
        dictionary: dict
            The dictionary containing all the price statistics data
        
        Returns
        -------
        None
        '''

        for name in dictionary['Name']:
            dictionary_dir = f'{name}'
            images_dir = 'images'
            parent_dir = "/Users/joaquimbolosfernandez/Desktop/AICore/Data Collection Project/data-collection-pipeline/raw_data/"
            images_parent_dir = "/Users/joaquimbolosfernandez/Desktop/AICore/Data Collection Project/data-collection-pipeline/raw_data/"+f"{name}"+"/"
            path = os.path.join(parent_dir, dictionary_dir)
            path_images = os.path.join(images_parent_dir,images_dir)
            if os.path.exists(path) == False:
                os.mkdir(path)
            if os.path.exists(path_images) == False:
                os.mkdir(path_images)  
            
               


    def download_and_store_images(self, dictionary):
        '''
        Downloads and saves the images within each crypto/images folder

        Parameters
        ----------
        dictionary: dict
            The dictionary containing all the price statistics data
        
        Returns
        -------
        None
        '''

        for i in range(len(dictionary['Images - src'])):
            img_data = requests.get(dictionary['Images - src'][i]).content
            image_name = ((((dictionary['TimeStamp'][i]).replace("/","")).replace(" ","_")).replace(":",""))+'_'+ dictionary['Name'][i] +".jpg"
            path_name = "/Users/joaquimbolosfernandez/Desktop/AICore/Data Collection Project/data-collection-pipeline/raw_data/"+dictionary['Name'][i]+"/"+"images"
            with open(os.path.join(path_name, image_name), 'wb') as handler:
                handler.write(img_data)


# %%


# Data Collection Pipeline

> This project implements an industry-grade data collection pipeline that runs scalably in the cloud. It uses Python code to automatically control your browser, extract information from a website, and store it on the cloud in a data warehouse and data lake. The system conforms to industry best practices, such as being containerised in Docker and running automated.

## Language and tools

<p align="left"> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> <a href="https://www.selenium.dev" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/detain/svg-logos/780f25886640cef088af994181646db2f6b1a3f8/svg/selenium-logo.svg" alt="selenium" width="40" height="40"/> </a> <a href="https://www.w3.org/html/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original-wordmark.svg" alt="html5" width="40" height="40"/> </a> <a href="https://git-scm.com/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/git-scm/git-scm-icon.svg" alt="git" width="40" height="40"/> </a> </p>

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

The aim is to find the links within the main page to the many pages containing the data you want to collect. A Scraper class is created containing all the methods used to scrape the data. Using Selenium, three methods, aside from the constructor, are defined:

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


## Milestone 4: Retrieve data from details page

All the data for each cryptocurrency is obtained from its corresponding webpage. Within the Scraper class, in Task 1, two methods are defined:

 - The get_data() method navigates to the price statistics container, scrapes all the statistics, and stores them in the data_dict dictionary.

 - The get_images() method retrieves the src links for each cryptocurrency logo

 In task 2:

 - The get_data() method is modified to include the timestamp of when the data was scraped in the data_dict dictionary

 - The merge_dict() method is created to merge the images_dict and the data_dict into a single dictionary

In task 3:

 - The create_raw_data_folder() method creates a raw_data folder in the root of your project if it doesn't yet exist. Then, within the raw_data folder, another folder (dictionary) is created. Within the dictionary folder, the dictionary containing all the data is saved in a file called data.json.

In task 4, all the images are to be downloaded and stored in their corresponding directories:

 - The create_crypto_folders() method creates a folder within raw_data for each cryptocurrency. In each folder, an images folder is created to store the downloaded images

 - The download_and_store_images() method downloads the cryptocurrencies logo and stores them within its corresponding images folder. The naming convention for each image must be:

```
<date>_<time>_<order of image>.<image file extension>
```

For each TASK, changes in the code are committed and pushed to the GitHub repo.

```python

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import time
import re
import datetime
import os
import json
import requests


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
        driver: webdriver.Chrome
            The driver that contains information about the current page
        
        Returns
        -------
        data: dict
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
            name.append(name_container.find_element(by=By.XPATH, value='//h2/span').text)

            price_statistics_container = self.driver.find_element(by=By.XPATH, value='//div[@class="sc-aef7b723-0 sc-7bd0ce10-0 dkDCAO"]')
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

        dictionary = {}
        dictionary.update(images)
        dictionary.update(data)

        return dictionary


    def create_raw_data_folder(self, dictionary):

        dictionary_dir = 'raw_data'
        parent_dir = "/Users/joaquimbolosfernandez/Desktop/AICore/Data Collection Project/"
        path = os.path.join(parent_dir, dictionary_dir)
        if os.path.exists(path) == False:
            os.mkdir(path)

        # Create the dictionary folder within the raw_data folder
        dictionary_dir = 'dictionary'
        parent_dir = "/Users/joaquimbolosfernandez/Desktop/AICore/Data Collection Project/raw_data/"
        path = os.path.join(parent_dir, dictionary_dir)
        if os.path.exists(path) == False:
            os.mkdir(path)

         # Save the dictionary in the dictionary folder
        with open(os.path.join(path, 'data.json'), 'w') as fp:
            json.dump(dictionary, fp)


    def create_crypto_folders(self, dictionary):

        # Create a folder for each crypto
        for id in dictionary['Name']:
            dictionary_dir = f'{id}'
            images_dir = 'images'
            parent_dir = "/Users/joaquimbolosfernandez/Desktop/AICore/Data Collection Project/raw_data/"
            images_parent_dir = "/Users/joaquimbolosfernandez/Desktop/AICore/Data Collection Project/raw_data/"+f"{id}"+"/"
            path = os.path.join(parent_dir, dictionary_dir)
            path_images = os.path.join(images_parent_dir,images_dir)
            if os.path.exists(path) == False:
                os.mkdir(path)
            if os.path.exists(path_images) == False:
                os.mkdir(path_images)     


    def download_and_store_images(self, dictionary):

        for i in range(len(dictionary['Images - src'])):
            img_data = requests.get(dictionary['Images - src'][i]).content
            image_name = ((((dictionary['TimeStamp'][i]).replace("/","")).replace(" ","_")).replace(":",""))+'_'+ dictionary['Name'][i] +".jpg"
            path_name = "/Users/joaquimbolosfernandez/Desktop/AICore/Data Collection Project/raw_data/"+dictionary['Name'][i]+"/"+"images"
            with open(os.path.join(path_name, image_name), 'wb') as handler:
                handler.write(img_data)


    def run_scraper(self):


        # Get the links to scrape data from
        link_list = self.get_links()

        # Scrape the Price statistics for each cryprocurrency
        data_dict = self.get_data(link_list)

        # Scrape the Image/Logo for each cryprocurrency
        images_dict = self.get_images(link_list)

        # Merge both data and image dictionaries
        dictionary = self.merge_dict(data_dict, images_dict)

        # Create the raw_data folder, 
        # Create the dictionary folder within the raw_data folder 
        # Save the dictionary in the dictionary folder
        self.create_raw_data_folder(dictionary)

        # Create a folder for each cryptocurrency within the raw_data folder
        self.create_crypto_folders(dictionary)

        # Save the downloaded images in each crypto folder
        self.download_and_store_images(dictionary)

        # self.scroll_down()

        # Close the browser when you finish
        self.driver.quit() 

        return dictionary
    

if __name__ == '__main__':
    url = 'https://coinmarketcap.com/'
    game = Scraper(url)
    dictionary = game.run_scraper()


```


## Milestone 5: Documentation and testing

Using docstrings and unittest documentation and testing are included in the project. 

In Task 1, the current code is optimised and refactored. All the classes, methods and variables are to be named appropriately using conventions. The main goal is to have clean code and be as concise as possible.

In Task 2, docstrings are included in all the functions used in the project. The format chosen follows the NumPy convention.

```python

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

```

In Task 3, using unittest, a ScraperTestCase() class is created to test all the methods from the Scraper() class. The implemented tests check trivial aspects of the methods, such as the output type, length, and overall, whether the output is what we expect. 

```python

import unittest
import sys
import os
sys.path.append("..")
from scraper.main import run_scraper

# Run the Scraper
scraper_outputs = run_scraper()
get_links_ouput = scraper_outputs[0]
get_data_ouput = scraper_outputs[1]
get_images_ouput = scraper_outputs[2]
merge_dict_ouput = scraper_outputs[3]

class ScraperTestCase(unittest.TestCase):

    # Test Basic methods of the Scraper

    # def test_load_and_accept_manual_and_cookies_promts(self):
    #     output = Scraper().load_and_accept_manual_and_cookies_promts()
    #     self.assertEqual(str(type(output)),"<class 'selenium.webdriver.chrome.webdriver.WebDriver'>")

    # def test_scroll_down(self):
    #     output = Scraper().scroll_down()
    #     self.assertEqual(str(type(output)),"<class 'selenium.webdriver.chrome.webdriver.WebDriver'>")

    # Test the Essential methods of the Scraper

    def test_get_links(self):
        output = get_links_ouput
        self.assertEqual(type(output),list)
        self.assertEqual(len(output), 100)

    def test_get_data(self):
        output = get_data_ouput
        self.assertEqual(type(output),dict)
        self.assertEqual(len(output), 10)
        self.assertEqual(len(output['Name']), 5)

    def test_get_images(self):
        output = get_images_ouput
        self.assertEqual(type(output),dict)
        self.assertEqual(len(output), 1)
        self.assertEqual(len(output["Images - src"]), 5)

    def test_merge_dict(self):
        output = merge_dict_ouput
        self.assertEqual(type(output),dict)
        self.assertEqual(len(output), 11)
        self.assertEqual(len(output["Images - src"]), 5)

    def test_create_raw_data_folder(self):
        root_path = "/Users/joaquimbolosfernandez/Desktop/AICore/Data Collection Project/"
        raw_data_path = root_path+"raw_data"
        dictionary_path = raw_data_path+"/dictionary"
        data_json_path = dictionary_path+"/data.json"
        self.assertTrue(os.path.exists(raw_data_path))
        self.assertTrue(os.path.exists(dictionary_path))
        self.assertTrue(os.path.exists(data_json_path))

    def test_create_crypto_folders(self):
        output_1 = merge_dict_ouput
        root_path = "/Users/joaquimbolosfernandez/Desktop/AICore/Data Collection Project/raw_data/"
        for i in range(len(output_1['Name'])):
            crypto_path = root_path + output_1['Name'][i]
            self.assertTrue(os.path.exists(crypto_path))
            crypto_images_path = crypto_path + "/images"
            self.assertTrue(os.path.exists(crypto_images_path))

    def download_and_store_images(self):
        output_1 = merge_dict_ouput
        for i in range(len(output_1['Name'])):
            image_name = ((((output_1['TimeStamp'][i]).replace("/","")).replace(" ","_")).replace(":",""))+'_'+ output_1['Name'][i] +".jpg"
            image_path = "/Users/joaquimbolosfernandez/Desktop/AICore/Data Collection Project/raw_data/"+output_1['Name'][i]+"/"+"images/"+image_name
            self.assertTrue(os.path.exists(image_path))

# Test the Scraper
if __name__ == '__main__':
    test_suite = unittest.TestLoader().loadTestsFromTestCase(ScraperTestCase)
    unittest.TextTestRunner().run(test_suite)
```

In Task 4, The ScraperTestCase() is implemented into a different file named test.py. Following the project structure convention, the project structure is created as follows:

```pyhton
data-collection-pipeline
│
├── scraper
│   ├── __init__.py
│   ├── main.py
│   └── scraper_coinmarket.py
│
├── test
│   ├── __init__.py
│   └── test.py
│
├── raw_data
│   ├── dictionary
│   │   └── data.json
│   ├── Bitcoin
│   │   └── images
│   ├── Ethereum
│   │   └── images
│   ├── Tether
│   │   └── images
│   ├── BNB
│   │   └── images
│   └── USD Coin
│       └── images
│
└── README.md
```
 - ```scraper```: The folder containing the main script.
 - ```scraper/__init__.py```: This file tells python that the folder scraper is not simply a directory but a package.
 - ```scraper/main.py```: This file contains the run_scraper() function, and imports the Scraper() class from the scraper_coinmarket.py in order to be able to run the scraper.
 - ```test```: The folder containing the test script
 - ```test/__init__.py```: Again, this file tells python that the folder test is not simply a directory but a package.
 - ```test/test.py``` : This file executes the run_scraper() function and then runs the tests on all the methods from the Scraper() class.
 - ```raw_data```: The folder containing the scraped data obtained
 - ```raw_data/dictionary/data.json```: This file contains the dictionary obtained by the scraper
 - ```raw_data/Crypto/images```: This directory contains the downloaded image from the src link obtained in the scraper

Finally, in Task 5 all unit tests are checked to pass all the public methods from the scraper.

For each TASK, changes in the code are committed and pushed to the GitHub repo.
# %% 
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Scraper():

    def __init__(self, url):

        self.main_url = url


    def load_and_accept_cookies(self) -> webdriver.Chrome:
        '''
        Open Main URL (CoinMarket) and accept the cookies
        
        Returns
        -------
        driver: webdriver.Chrome
            This driver is already in the CoinMarket webpage
        '''
        driver = webdriver.Chrome() 
        URL = self.main_url
        driver.get(URL)
        time.sleep(3) 
        try:
            # driver.switch_to_frame('frame id') # This is the id of the frame / For CoinMarket there's no iframe tag
            accept_cookies_button = driver.find_element(by=By.XPATH, value='//*[@class="cmc-cookie-policy-banner__close" ]') # *** MODIFY THIS 
            accept_cookies_button.click()
            time.sleep(1)
        except AttributeError: # If you have the latest version of Selenium, the code above won't run because the "switch_to_frame" is deprecated
            driver.switch_to.frame('gdpr-consent-notice') # This is the id of the frame *** MODIFY THIS 
            accept_cookies_button = driver.find_element(by=By.XPATH, value='//*[@class="cmc-cookie-policy-banner__close" ]') # *** MODIFY THIS 
            accept_cookies_button.click()
            time.sleep(1)

        except:
            pass

        return driver 

    def get_links(self, driver: webdriver.Chrome) -> list:
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

        prop_container = driver.find_element(by=By.XPATH, value='//div[@class="css-1itfubx e5pbze00"]')
        prop_list = prop_container.find_elements(by=By.XPATH, value='./div')
        link_list = []

        for house_property in prop_list:
            a_tag = house_property.find_element(by=By.TAG_NAME, value='a')
            link = a_tag.get_attribute('href')
            link_list.append(link)

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


URL = 'https://coinmarketcap.com/'
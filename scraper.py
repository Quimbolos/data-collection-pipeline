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


    def load_and_accept_cookies(self):

        '''
        Open Main URL (Ikea) and accept the cookies prompt
        
        '''
        URL = self.main_url
        self.driver.get(URL)
        try:
            WebDriverWait(self.driver, self.delay).until(EC.presence_of_element_located((By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')))
            accept_cookies_button = WebDriverWait(self.driver, self.delay).until(EC.presence_of_element_located((By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')))
            print("Accept Cookies Button Ready!")
            accept_cookies_button.click()
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
            WebDriverWait(self.driver, self.delay).until(EC.presence_of_element_located((By.XPATH, '//*[@class="hnf-location__postalcode hnf-btn hnf-btn--tertiary hnf-leading-icon"]')))
            enter_postcode_button = self.driver.find_element(by=By.XPATH, value='//*[@class="hnf-location__postalcode hnf-btn hnf-btn--tertiary hnf-leading-icon"]')
            print("Postcode Button Ready!")
            enter_postcode_button.click()
            time.sleep(1)
        except TimeoutException:
            print("Loading took too much time!")

        self.driver.find_element(by=By.XPATH, value='//*[@id="hnf-txt-postalcodepicker-postcode"]').send_keys('SW1V 2NE').send_keys(Keys.ENTER)

        return self.driver
         



    def run(self):

        self.load_and_accept_cookies()
        self.scroll_down()
        self.insert_postcode()



#     def get_links(self, driver: webdriver.Chrome) -> list:
#         '''
#         Returns a list with all the links in the current page
#         Parameters
#         ----------
#         driver: webdriver.Chrome
#             The driver that contains information about the current page
        
#         Returns
#         -------
#         link_list: list
#             A list with all the links in the page
#         '''

#         prop_container = driver.find_element(by=By.XPATH, value='//div[@class="css-1itfubx e5pbze00"]')
#         prop_list = prop_container.find_elements(by=By.XPATH, value='./div')
#         link_list = []

#         for house_property in prop_list:
#             a_tag = house_property.find_element(by=By.TAG_NAME, value='a')
#             link = a_tag.get_attribute('href')
#             link_list.append(link)

#         return link_list

    



# # big_list = []
# # driver = load_and_accept_cookies()

# # for i in range(5): # The first 5 pages only
# #     big_list.extend(get_links(driver)) # Call the function we just created and extend the big list with the returned list
# #     ## TODO: Click the next button. Don't forget to use sleeps, so the website doesn't suspect
# #     pass # This pass should be removed once the code is complete


# # for link in big_list:
# #     ## TODO: Visit all the links, and extract the data. Don't forget to use sleeps, so the website doesn't suspect
# #     pass # This pass should be removed once the code is complete

# # driver.quit() # Close the browser when you finish


URL = 'https://www.ikea.com/gb/en/'

game = Scraper(URL)

game.run()
# %%

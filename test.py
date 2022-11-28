# %%

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import time

def accept_cookies(url) -> webdriver.Chrome:

    driver = webdriver.Chrome() 
    URL = url
    driver.get(URL)
    delay = 10
    try:
        accept_cookies_button = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')))
        print("Accept Manual Button Ready!")
        accept_cookies_button.click()
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
    except TimeoutException:
        print("Loading took too much time!")

    return driver

def scroll_down(url) -> webdriver.Chrome:

    driver = webdriver.Chrome() 
    URL = url
    driver.get(URL)

    driver.execute_script("window.scrollTo(0, Y)") 

    return driver

def click_and_input(url):

    driver = webdriver.Chrome() 
    URL = url
    driver.get(URL)
    test = driver.find_element(by=By.XPATH, value='//*[@class="hnf-location__postalcode hnf-btn hnf-btn--tertiary hnf-leading-icon"]')
    test.click()
    print("Postcode Button Ready!")
    driver.find_element(by=By.XPATH, value='//*[@id="hnf-txt-postalcodepicker-postcode"]').send_keys('SW1V 2NE').send_keys(Keys.ENTER)



    return driver


url = 'https://www.ikea.com/gb/en/'

click_and_input(url)
# scroll_down(url)
# %%

# %%
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import time
import datetime

driver = webdriver.Chrome()

driver.get('https://coinmarketcap.com/currencies/bitcoin/')
delay = 20

# name = driver.find_element(by=By.XPATH, value='//*[class="sc-1d5226ca-0 gNMZTD tooltip"]').text()
# print(name)
WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '//div[@class="sc-aef7b723-0 jfPVkR container"]')))

price_statistics_container  = driver.find_element(by=By.XPATH, value='//div[@class="sc-aef7b723-0 sc-7bd0ce10-0 dkDCAO"]')
tbody_tag = price_statistics_container.find_element(by=By.XPATH, value='//tbody')
tr_tag = tbody_tag.find_elements(by=By.XPATH, value='.//td')
# th_tag = tr_tag.find_element(by=By.XPATH, value='//td')

print(price_statistics_container.get_attribute('innerHTML'))
print('break')
print(tbody_tag.get_attribute('innerHTML'))
print('break')
for i in range(len(tr_tag)):
    print(tr_tag[i].get_attribute('innerHTML'))
    print('')
# print('break')

# print(th_tag.get_attribute('innerHTML'))
price = tr_tag[0].get_attribute('innerHTML')
price

# # %%

# test = price.get_attribute('innerHTML')
# test_ = price
# # %%
# test2 = test_.find_element(by=By.XPATH, value='//h2/span').text
# test2


# %%
# Price change
((tr_tag[1].find_element(by=By.XPATH, value='.//span/span').get_attribute('innerHTML'))[0]+(tr_tag[1].find_element(by=By.XPATH, value='.//span/span').get_attribute('innerHTML'))[10:16])

# %%
(tr_tag[2].find_element(by=By.XPATH, value='.//div').get_attribute('innerHTML'))[1:10]
# %%
tr_tag[2].find_element(by=By.XPATH, value='.//div[2]').get_attribute('innerHTML')[1:10]
# %%
(tr_tag[3].find_element(by=By.XPATH, value='.//span').get_attribute('innerHTML'))[1:-1]
# %%
tr_tag[4].get_attribute('innerHTML')
# %%
tr_tag[5].find_element(by=By.XPATH, value='.//span').get_attribute('innerHTML')[0:5]
# %%
tr_tag[6].get_attribute('innerHTML')[-1]
# %%
tr_tag[0].get_attribute('innerHTML')[1:10]
# %%
price
# %%
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get('https://coinmarketcap.com/currencies/bitcoin/')
delay = 20

# name = driver.find_element(by=By.XPATH, value='//*[class="sc-1d5226ca-0 gNMZTD tooltip"]').text()
# print(name)
WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '//div[@class="sc-aef7b723-0 jPJwrb nameHeader"]')))

image_container  = driver.find_element(by=By.XPATH, value='//div[@class="sc-aef7b723-0 jPJwrb nameHeader"]')


# %%
image_container.find_element(by=By.XPATH, value='.//img').get_attribute('src')

# %%
time.time()
# %%
import datetime 
timetest = time.time()
datetime.datetime.fromtimestamp(timetest).strftime('%c')
# %%

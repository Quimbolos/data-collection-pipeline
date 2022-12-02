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
WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '//div[@class="sc-aef7b723-0 jfPVkR container"]')))

price_statistics_container  = driver.find_element(by=By.XPATH, value='//div[@class="sc-aef7b723-0 sc-7bd0ce10-0 dkDCAO"]')
tbody_tag = price_statistics_container.find_element(by=By.XPATH, value='//tbody')
tr_tag = tbody_tag.find_element(by=By.XPATH, value='//*[@scope="row"]')
th_tag = tr_tag.find_element(by=By.XPATH, value='//th')

print(price_statistics_container.get_attribute('innerHTML'))
print('break')
print(tbody_tag.get_attribute('innerHTML'))
print('break')
print(tr_tag.get_attribute('innerHTML'))
print('break')

print(th_tag.get_attribute('innerHTML'))



# # %%

# test = price.get_attribute('innerHTML')
# test_ = price
# # %%
# test2 = test_.find_element(by=By.XPATH, value='//h2/span').text
# test2


# %%
len(name2)
# %%

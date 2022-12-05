# %%
import unittest
import scraper_coinmarket
import time
import os

class ScraperTestCase(unittest.TestCase):

    def test_load_and_accept_manual_and_cookies_promts(self):
        scraper = scraper_coinmarket.Scraper()
        output = scraper.load_and_accept_manual_and_cookies_promts()
        self.assertEqual(str(type(output),"<class 'selenium.webdriver.chrome.webdriver.WebDriver'>"))

    def test_scroll_down(self):
        scraper = scraper_coinmarket.Scraper()
        output = scraper.scroll_down()
        self.assertEqual(str(type(output),"<class 'selenium.webdriver.chrome.webdriver.WebDriver'>"))

    def test_get_links(self):
        scraper = scraper_coinmarket.Scraper()
        output = scraper.get_links()
        self.assertEqual(type(output),list)
        self.assertEqual(len(output), 100)

    def test_get_data(self):
        scraper = scraper_coinmarket.Scraper()
        output = scraper.get_data(scraper.get_links())
        self.assertEqual(type(output),dict)
        self.assertEqual(len(output), 10)
        self.assertEqual(len(output['Name']), 5)

    def test_get_images(self):
        scraper = scraper_coinmarket.Scraper()
        output = scraper.get_images(scraper.get_links())
        self.assertEqual(type(output),dict)
        self.assertEqual(len(output), 1)
        self.assertEqual(len(output["Images - src"]), 5)

    def test_merge_dict(self):
        scraper = scraper_coinmarket.Scraper()
        output = scraper.merge_dict(scraper.get_data(),scraper.get_images())
        self.assertEqual(type(output),dict)
        self.assertEqual(len(output), 11)
        self.assertEqual(len(output["Images - src"]), 5)

    def test_create_raw_data_folder(self):
        scraper = scraper_coinmarket.Scraper()
        output = scraper.create_raw_data_folder(scraper.merge_dict())
        root_path = "/Users/joaquimbolosfernandez/Desktop/AICore/Data Collection Project/"
        raw_data_path = root_path+"raw_data"
        dictionary_path = raw_data_path+"/dictionary"
        data_json_path = dictionary_path+"/data.json"
        self.assertTrue(os.path.exists(raw_data_path))
        self.assertTrue(os.path.exists(dictionary_path))
        self.assertTrue(os.path.exists(data_json_path))

    def test_create_crypto_folders(self):
        scraper = scraper_coinmarket.Scraper()
        output_1 = scraper.merge_dict()
        output_2 = scraper.create_crypto_folders(scraper.merge_dict())
        root_path = "/Users/joaquimbolosfernandez/Desktop/AICore/Data Collection Project/raw_data/"
        for i in range(len(output_1['Name'])):
            crypto_path = root_path + output_1['Name'][i]
            self.assertTrue(os.path.exists(crypto_path))
            crypto_images_path = crypto_path + "/images"
            self.assertTrue(os.path.exists(crypto_images_path))

    def download_and_store_images(self):
        scraper = scraper_coinmarket.Scraper()
        output_1 = scraper.merge_dict()
        output_2 = scraper.download_and_store_images(scraper.merge_dict())
        for i in range(len(output_1['Name'])):
            image_name = ((((output_1['TimeStamp'][i]).replace("/","")).replace(" ","_")).replace(":",""))+'_'+ output_1['Name'][i] +".jpg"
            image_path = "/Users/joaquimbolosfernandez/Desktop/AICore/Data Collection Project/raw_data/"+output_1['Name'][i]+"/"+"images/"+image_name
            self.assertTrue(os.path.exists(image_path))

if __name__ == '__main__':
    unittest.main()
# %%

scraper = scraper_coinmarket.Scraper()
output = scraper.load_and_accept_manual_and_cookies_promts()
str(type(output))
# %%
dict
# %%
a = {

    'Key1' : 1
}
type(a)
# %%
len(a)
# %%
dict = {"Images - src": ["https://s2.coinmarketcap.com/static/img/coins/64x64/1.png", "https://s2.coinmarketcap.com/static/img/coins/64x64/1027.png", "https://s2.coinmarketcap.com/static/img/coins/64x64/825.png", "https://s2.coinmarketcap.com/static/img/coins/64x64/1839.png", "https://s2.coinmarketcap.com/static/img/coins/64x64/3408.png"], "Name": ["Bitcoin", "Ethereum", "Tether", "BNB", "USD Coin"], "Price ($)": ["17,084.21", "1,268.17", "1.00", "290.71", "0.9999"], "Price Change 24h ($)": ["+56.49", "+9.12", "-0.0000", "+0.9958", "-0.0001"], "Lowest Price 24h ($)": ["16994.70", "1258.73", "1.00", "289.32", "0.9997"], "Highest Price 24h ($)": ["17,378.15", "1,302.24", "1.00", "296.91", "1.00"], "Trading Volume 24h ($)": ["21,645,921,616.8", "6,087,192,200.2", "27,333,349,718.7", "685,536,571.2", "2,300,323,077.4"], "Volume / Market Cap": ["0.0659", "0.03922", "0.4173", "0.01474", "0.05307"], "Market Dominance": ["38.28", "18.09", "7.64", "5.42", "5.05"], "Market Rank": ["1", "2", "3", "4", "5"], "TimeStamp": ["12/05/2022 15:36:30", "12/05/2022 15:36:34", "12/05/2022 15:36:38", "12/05/2022 15:36:43", "12/05/2022 15:36:49"]}
# %%
dict
# %%
len(dict)
len(dict['Name'])# %%

# %%
output = dict
# %%
len(output['Name'])
# %%

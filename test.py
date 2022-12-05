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

# %%
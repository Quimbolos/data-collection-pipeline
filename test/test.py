# %%
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

# %%
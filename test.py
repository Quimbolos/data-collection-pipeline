# %%
import unittest
import scraper_coinmarket
from selenium import webdriver


class ScraperTestCase(unittest.TestCase):

    def test_load_and_accept_manual_and_cookies_promts(self):
        scraper = scraper_coinmarket.Scraper()
        output = scraper_coinmarket.Scraper.load_and_accept_manual_and_cookies_promts()
        self.assertEqual(type(output),selenium.webdriver.chrome.webdriver.WebDriver)

    def test_scroll_down(self):
        output = scraper

if __name__ == '__main__':
    unittest.main()
# %%
scraper = scraper_coinmarket.Scraper()
output = scraper.load_and_accept_manual_and_cookies_promts()
# %%
scraper = scraper_coinmarket.Scraper()
output = scraper.load_and_accept_manual_and_cookies_promts()
# %%

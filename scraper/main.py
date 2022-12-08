# %% 
import sys
sys.path.append("..")
from scraper.scraper_coinmarket import Scraper

def run_scraper():
        '''
        Runs the Scraper methods

        Parameters
        ----------
        None
        
        Returns
        -------
        dictionary: dict
            The dictionary containing all the price statistics data
        '''

        # Get the links to scrape data from
        link_list = Scraper().get_links()

        # Scrape the Price statistics for each cryprocurrency
        data_dict = Scraper().get_data(link_list)

        # Scrape the Image/Logo for each cryprocurrency
        images_dict = Scraper().get_images(link_list)

        # Merge both data and image dictionaries
        dictionary = Scraper().merge_dict(data_dict, images_dict)

        # Create the raw_data folder, 
        # Create the dictionary folder within the raw_data folder 
        # Save the dictionary in the dictionary folder
        Scraper().create_raw_data_folder(dictionary)

        # Create a folder for each cryptocurrency within the raw_data folder
        Scraper().create_crypto_folders(dictionary)

        # Save the downloaded images in each crypto folder
        Scraper().download_and_store_images(dictionary)

        # Scraper.scroll_down()

        # Close the browser when you finish
        Scraper().driver.quit() 

        return link_list, data_dict, images_dict, dictionary

if __name__ == '__main__':
    run_scraper()
    
# %%

# %%

import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

# define functions to extract data
def extract(url, user_agent):
    headers = {'User-Agent': user_agent}
    r = requests.get(url, headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup

def transform(soup, selector_name, class_name, selector_price, class_price):
    find_name = soup.find(selector_name, class_ = class_name)
    product_name = find_name.text

    find_price = soup.find(selector_price, class_ = class_price)
    price_str = find_price.text
    product_price = float(price_str.replace('$', ''))

    return product_name, product_price

# define selectors for each of the sites and turn them into a dataframe
parameters = {
    'sfw': {
        'selector_name': 'h1', 
        'class_name': 'heading__Base-sc-1vuwqc7-0-h1', 
        'selector_price': 'div',
        'class_price': 'spacing__Spacing-sc-ngu0v9-0 lbarHM'}, 
    'sof': {
        'selector_name': 'h2', 
        'class_name': 'PdpInfoTitle--1qi97uk', 
        'selector_price': 'span',
        'class_price': 'PdpMainPrice--4c0ljm'}
}
parameters_df = pd.DataFrame.from_dict(parameters)

# define user agent variable to access data in site
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'

# read into a dataframe list of products
webscraping_list = pd.read_csv('./webscraping_product_list.csv')

# define list of supermarkets to be scraped
supermarket_list = ['sfw', 'sof']

product_list = []

# iterate over each supermarket name to assign corresponding selectors
for supermarket in supermarket_list:
    selector_name = parameters_df[supermarket]['selector_name']
    class_name = parameters_df[supermarket]['class_name']
    selector_price = parameters_df[supermarket]['selector_price']
    class_price = parameters_df[supermarket]['class_price']
    store_products = webscraping_list[webscraping_list['Store'] == supermarket]

    # iterate over list of products for the specific supermarket to extract data 
    for row in store_products.itertuples():
        product = row[2]
        url = row[3]
        soup = extract(url, user_agent)
        product_name_price = transform(soup, selector_name, class_name, selector_price, class_price)
        product_name = product_name_price[0]
        product_price = product_name_price[1]

        timestamp = datetime.now()

        product = {
            'datetime': timestamp, 
            'supermarket': supermarket, 
            'product' : product, 
            'product_name': product_name, 
            'product_price': product_price
        }

        product_list.append(product)

webscraping_results = pd.DataFrame(product_list)
print(webscraping_results)

# get timestamp to include in filename when saving to csv
timestamp = datetime.now().strftime('%Y%m%d-%H%M')
print(timestamp)

# save data to csv file
webscraping_results.to_csv('./webscraping_results/webscraping_results_' + timestamp + '.csv', index=False)
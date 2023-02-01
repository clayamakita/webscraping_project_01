import requests
from bs4 import BeautifulSoup
import pandas as pd

def extract(url, user_agent):
    headers = {'User-Agent': user_agent}
    url = url
    r = requests.get(url, headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup

def transform(soup, class_name, class_price):
    find_name = soup.find('h1', class_ = class_name)
    product_name = find_name.text

    find_price = soup.find('div', class_ = class_price)
    price_str = find_price.text
    product_price = float(price_str.replace('$', ''))

    return product_name, product_price

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
class_product = 'heading__Base-sc-1vuwqc7-0-h1 sc-jgrIVw oOzLa iCeTLf'
class_price = 'spacing__Spacing-sc-ngu0v9-0 lbarHM'

url_list = [
    'https://voila.ca/products/627001EA/details', 
    'https://voila.ca/products/217703EA/details',
    'https://voila.ca/products/862810EA/details'
    ]

list_products = []

for url in url_list:
    soup = extract(url, user_agent)
    list_products.append(transform(soup, class_product, class_price))

df_products = pd.DataFrame(list_products, columns=['Product Name', 'Product Price'])

print(df_products)
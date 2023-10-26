import json
from datetime import datetime
from tabulate import tabulate
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
# options.add_argument('--headless')
def get_current_date():
    current_date = datetime.now().strftime('%Y-%m-%d')
    return current_date

def get_product_info(browser, url, wine, attribute):
    try:
        wait = WebDriverWait(browser, 1)
        elements = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, attribute)))
        if elements:
            for element in elements:
                product_info = element.text
                if product_info:
                    return product_info
    except Exception as e:
        return "No information"

def scrape_store_products(browser,store, wine):
    product_data = []
    
    for url in store["urls"]:
        browser.get(url + wine)
        name = get_product_info(browser, url, wine, store["attribute_name"])
        price = get_product_info(browser, url, wine, store["attribute_price"])
        product_data.append({"store": store["name"], "name": name, "price": price, "currency": "EUR", "date": get_current_date(), "location": "Portugal", "ean": wine})

    return product_data

def main():
    stores = [
        {
            "name": "El Corte Ingles",
            "urls": [
                'https://www.elcorteingles.pt/supermercado/pesquisar/?term=',
            ],
            "attribute_name": "js-product-link",
            "attribute_price": "prices-price",
        },
        {
            "name": "Garrafeira Soares",
            "urls": [
                'https://www.garrafeirasoares.pt/pt/resultado-da-pesquisa_36.html?term=',
            ],
            "attribute_name": "name",
            "attribute_price": "current",
        },
        {
            "name": "Continente",
            "urls": [
                'https://www.continente.pt/pesquisa/?q=',
            ],
            "attribute_name": "pwc-tile--description",
            "attribute_price": "ct-price-formatted",
        }
    ]

    wines = ["5601012011500", "5601012001310", "5601012004427", "5601012011920"]
    all_product_data = []

    for wine in wines:
        browser = webdriver.Firefox(options=options)
        for store in stores:
            product_data = scrape_store_products(browser,store, wine)
            all_product_data.extend(product_data)
        browser.quit()

    output_file = '../hack_dashboard/srcs/requirements/nginx/www/html/product_data.json'

    with open(output_file, 'w') as json_file:
        json.dump(all_product_data, json_file, indent=4)

if __name__ == "__main__":
    main()

import requests
from bs4 import BeautifulSoup
import csv
import time
import random

# Set headers to mimic a real browser
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# Send request to Jumia website
url = "https://www.jumia.co.ke/"
try:
    response = requests.get(url, headers=headers, timeout=10)
    
    # Check status code
    if response.status_code == 200:
        # Parse HTML content
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find Deals of the Week section - updated selector
        deals_section = soup.find('section', {'class': 'card -oh _fw -rad4'})
        if not deals_section:
            deals_section = soup.find('div', {'class': '-fh'})  # Alternative class
        
        if not deals_section:
            print("Could not find deals section on the page")
            # exit()
        
        # Extract product data - updated selectors
        products = soup.find_all('article', {'class': 'prd _box _hvr'})
        if not products:
            products = soup.find_all('div', {'class': 'info'})  # Alternative selector
        
        if not products:
            print("No products found in the deals section")
            # exit()
            
        # Create CSV file
        with open('jumia_products.csv', 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['Product Name', 'Brand Name', 'Price', 'Discount', 'Total Reviews', 'Product Rating']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            
            product_count = 0
            
            for product in products:
                try:
                    # Extract product name
                    name_elem = product.find('h3', {'class': 'name'}) or product.find('div', {'class': 'name'})
                    product_name = name_elem.text.strip() if name_elem else "N/A"
                    
                    # Extract brand name (often part of product name on Jumia)
                    brand_name = product_name.split()[0] if product_name != "N/A" else "N/A"
                    
                    # Extract price
                    price_elem = product.find('div', {'class': 'prc'}) or product.find('span', {'class': 'price'})
                    price = price_elem.text.strip() if price_elem else "N/A"
                    
                    # Extract discount
                    discount_elem = product.find('div', {'class': 'bdg'}) or product.find('div', {'class': 'discount'})
                    discount = discount_elem.text.strip() if discount_elem else "N/A"
                    
                    # Extract reviews
                    reviews_elem = product.find('h2', {'class': ' -fs14 -m -upp -ptm'}) or product.find('span', {'class': 'total-reviews'})
                    total_reviews = reviews_elem.text.strip() if reviews_elem else "N/A"
                    
                    # Extract rating
                    rating_elem = product.find('div', {'class': '-fs29 -yl5 -pvxs'}) or product.find('span', {'class': 'rating'})
                    product_rating = rating_elem.text.strip() if rating_elem else "N/A"
                    
                    writer.writerow({
                        'Product Name': product_name,
                        'Brand Name': brand_name,
                        'Price': price,
                        'Discount': discount,
                        'Total Reviews': total_reviews,
                        'Product Rating': product_rating
                    })
                    
                    product_count += 1
                    
                    # Add a small delay to be respectful to the server
                    time.sleep(random.uniform(0.1, 0.3))
                    
                except Exception as e:
                    print(f"Error processing a product: {e}")
                    continue
            
            print(f"Successfully scraped {product_count} products and saved to jumia_products.csv")
    
    else:
        print(f"Failed to retrieve webpage. Status code: {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"Request error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
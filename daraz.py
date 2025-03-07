

import requests
from bs4 import BeautifulSoup

def search_daraz(product_name):
    # Prepare the search URL for Daraz
    base_url = "https://www.daraz.com.np/catalog/?q="
    search_url = base_url + "+".join(product_name.split())

    # Headers to mimic a browser request (necessary for Daraz)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
    }

    # Send a request to Daraz
    response = requests.get(search_url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")

        # Find all product containers (class names may vary; inspect the site for current structure)
        product_containers = soup.find_all("div", class_="c1_t2i")

        for product in product_containers:
            # Extract product title
            title_tag = product.find("a", class_="c16H9d")
            title = title_tag.text.strip() if title_tag else "No title found"

            # Extract product link
            link = "https:" + title_tag["href"] if title_tag else None

            # Print product details
            if link and product_name.lower() in title.lower():
                return f"Product found: {title}\nBuy here: {link}"

        return "No matching product found on Daraz."
    else:
        return f"Failed to fetch Daraz page. Status code: {response.status_code}"

# Example usage
user_product = "gaming laptops"
result = search_daraz(user_product)
print(result)

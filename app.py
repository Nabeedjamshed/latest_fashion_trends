import requests
from bs4 import BeautifulSoup
import json
import time
import random

urls = [
    "https://www.flipkart.com/search?q=men%27s+trousers",
    "https://www.flipkart.com/clothing-and-accessories/topwear/tshirt/men-tshirt/pr?sid=clo,ash,ank,edy&otracker=categorytree&otracker=nmenu_sub_Men_0_T-Shirts",
    "https://www.flipkart.com/clothing-and-accessories/topwear/shirt/men-shirt/formal-shirt/pr?sid=clo,ash,axc,mmk,bk1&otracker=categorytree&otracker=nmenu_sub_Men_0_Formal%20Shirts",
    "https://www.flipkart.com/clothing-and-accessories/topwear/shirt/men-shirt/casual-shirt/pr?sid=clo,ash,axc,mmk,kp7&otracker=categorytree&otracker=nmenu_sub_Men_0_Casual%20Shirts",
    "https://www.flipkart.com/clothing-and-accessories/bottomwear/jeans/men-jeans/pr?sid=clo,vua,k58,i51&otracker=categorytree&otracker=nmenu_sub_Men_0_Jeans",
    "https://www.flipkart.com/mens-clothing/trousers/pr?sid=2oq,s9b,9uj&otracker=nmenu_sub_Men_0_Casual%20Trousers",
    "https://www.flipkart.com/clothing-and-accessories/bottomwear/trouser/men-trouser/pr?sid=clo%2Cvua%2Cmle%2Clhk&otracker=categorytree&p%5B%5D=facets.occasion%255B%255D%3DFormal&otracker=nmenu_sub_Men_0_Formal%20Trousers"
]

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/109.0"
]

session = requests.Session()

products = []

for url in urls:
    headers = {"User-Agent": random.choice(user_agents)}
    
    try:
        response = session.get(url, headers=headers, timeout=10)
        
        if response.status_code != 200:
            print(f"Failed to fetch {url} (Status: {response.status_code})")
            continue

        soup = BeautifulSoup(response.text, "html.parser")

        for div in soup.find_all("div", {"data-id": True}):
            product_id = div["data-id"]
            img_tag = div.find("img", {"src": True})
            if img_tag:
                image_url = img_tag["src"]
                products.append({"image_url": image_url, "product_id": product_id})

        time.sleep(random.uniform(2, 5)) 

    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        continue

output = {"products": products}
with open("latest_fashion.json", "w") as file:
    json.dump(output, file, indent=4)

print("Latest fashion trends saved!")





# import requests
# from bs4 import BeautifulSoup
# import json

# # Flipkart URLs
# urls = [
#     "https://www.flipkart.com/search?q=men%27s+trousers",
#     "https://www.flipkart.com/clothing-and-accessories/topwear/tshirt/men-tshirt/pr?sid=clo,ash,ank,edy&otracker=categorytree&otracker=nmenu_sub_Men_0_T-Shirts",
#     "https://www.flipkart.com/clothing-and-accessories/topwear/shirt/men-shirt/formal-shirt/pr?sid=clo,ash,axc,mmk,bk1&otracker=categorytree&otracker=nmenu_sub_Men_0_Formal%20Shirts",
#     "https://www.flipkart.com/clothing-and-accessories/topwear/shirt/men-shirt/casual-shirt/pr?sid=clo,ash,axc,mmk,kp7&otracker=categorytree&otracker=nmenu_sub_Men_0_Casual%20Shirts",
#     "https://www.flipkart.com/clothing-and-accessories/bottomwear/jeans/men-jeans/pr?sid=clo,vua,k58,i51&otracker=categorytree&otracker=nmenu_sub_Men_0_Jeans",
#     "https://www.flipkart.com/mens-clothing/trousers/pr?sid=2oq,s9b,9uj&otracker=nmenu_sub_Men_0_Casual%20Trousers",
#     "https://www.flipkart.com/clothing-and-accessories/bottomwear/trouser/men-trouser/pr?sid=clo%2Cvua%2Cmle%2Clhk&otracker=categorytree&p%5B%5D=facets.occasion%255B%255D%3DFormal&otracker=nmenu_sub_Men_0_Formal%20Trousers"
# ]

# # Headers to mimic a real browser request
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
# }

# products = []

# # Loop through each URL and scrape images
# for url in urls:
#     response = requests.get(url, headers=headers)
    
#     # Check if request was successful
#     if response.status_code != 200:
#         print(f"Failed to fetch {url}")
#         continue

#     soup = BeautifulSoup(response.text, "html.parser")

#     # Extract product image URLs and product IDs
#     for div in soup.find_all("div", {"data-id": True}):
#         product_id = div["data-id"]
#         img_tag = div.find("img", {"src": True})
#         if img_tag:
#             image_url = img_tag["src"]
#             products.append({"image_url": image_url, "product_id": product_id})

# # Convert to JSON format
# output = {"products": products}

# # Print JSON output
# print(json.dumps(output, indent=4))




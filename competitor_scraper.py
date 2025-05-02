import requests
from bs4 import BeautifulSoup

def fetch_competitor_data():
    url = "https://naivas.info/locations/naivas-supercentre-nakuru/"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        # Dynamically fetch store name
        store_element = soup.find("h1")
        store_name = store_element.get_text(strip=True) if store_element else "Unknown Store"

        # Address and promotion scraping
        address_element = soup.select_one("div.elementor-widget-container p")
        address = address_element.get_text(strip=True) if address_element else None

        promo_element = soup.find(lambda tag: tag.name in ['h2', 'p'] and 'offer' in tag.text.lower())
        promotion = promo_element.get_text(strip=True) if promo_element else None

        return {
            "store_name": store_name,
            "address": address,
            "promotion": promotion,
            "source": url
        }

    except Exception as e:
        print(f"❌ Error scraping competitor: {e}")
        return {
            "store_name": "Unknown Store",
            "address": None,
            "promotion": None,
            "source": url
        }



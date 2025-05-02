import requests
from bs4 import BeautifulSoup

def fetch_competitor_data():
    url = "https://naivas.info/locations/naivas-nakuru-midtown/"
    store_name = "Naivas Supermarket Nakuru Midtown"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract Address
        address_element = soup.find(lambda tag: tag.name in ['h2', 'h3', 'p'] and 'located in' in tag.text.lower())
        address = address_element.get_text(strip=True).replace('\n', ' ') if address_element else "Unavailable"

        # Extract Promotion Text
        promo_element = soup.find(lambda tag: tag.name in ['h2', 'p'] and 'offer' in tag.text.lower())
        if not promo_element:
            # Fallback to any paragraph with promotional tone
            promo_element = soup.find(lambda tag: tag.name == 'p' and 'selection' in tag.text.lower())
        promotion = promo_element.get_text(strip=True).replace('\n', ' ') if promo_element else "Unavailable"

        return {
            "store_name": store_name,
            "address": address,
            "promotion": promotion,
            "source": url
        }

    except Exception as e:
        print(f"❌ Error scraping competitor: {e}")
        return {
            "store_name": store_name,
            "address": "Unavailable",
            "promotion": "Unavailable",
            "source": url
        }

